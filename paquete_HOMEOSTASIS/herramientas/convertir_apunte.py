#!/usr/bin/env python3
"""Convierte un apunte en Word (.docx) al formato de contenido/ y figuras/.

Uso:
    python3 herramientas/convertir_apunte.py APUNTE.docx LETRA "Título corto" \
        [--fotos 1,16,20] [--descripciones desc.json]

- LETRA es el identificador del apunte (A, B, C...). Las figuras quedan como
  LETRA-figNN.jpg.
- --fotos: números de figura que son fotos reales (histología, micrografías,
  animales, estructuras 3D). Van a figuras/fotos/ y se usan en el juego. El resto
  va a figuras/esquemas/, solo como referencia para redibujarlas en SVG.
- --descripciones: JSON {"1": "texto", ...} con la descripción detallada de cada
  figura. Las que falten quedan marcadas como PENDIENTE para que Claude las
  escriba mirando la imagen una sola vez.

Requiere pandoc y Pillow (pip install pillow).
"""
import argparse
import json
import re
import subprocess
import tempfile
import unicodedata
from pathlib import Path

from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
PATRON_FIGURA = re.compile(
    r'<img src="\./media/([^"]+)"[^>]*/>\*\s*\n(Figura (\d+)\..*?)\*\n', re.S
)


def slug(texto):
    texto = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    return re.sub(r"[^A-Za-z0-9]+", "_", texto).strip("_")


def guardar_imagen(origen, destino, lado_max, calidad):
    imagen = Image.open(origen)
    if imagen.mode in ("RGBA", "LA", "P"):
        fondo = Image.new("RGB", imagen.size, "white")
        imagen = imagen.convert("RGBA")
        fondo.paste(imagen, mask=imagen.split()[-1])
        imagen = fondo
    else:
        imagen = imagen.convert("RGB")
    imagen.thumbnail((lado_max, lado_max))
    destino.parent.mkdir(parents=True, exist_ok=True)
    imagen.save(destino, "JPEG", quality=calidad, optimize=True)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("docx")
    p.add_argument("letra")
    p.add_argument("titulo")
    p.add_argument("--fotos", default="")
    p.add_argument("--descripciones")
    a = p.parse_args()

    letra = a.letra.upper()
    fotos = {int(n) for n in a.fotos.split(",") if n.strip()}
    descripciones = {}
    if a.descripciones:
        descripciones = json.loads(Path(a.descripciones).read_text(encoding="utf-8"))

    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(
            ["pandoc", str(Path(a.docx).resolve()), "-t", "gfm", "--wrap=none",
             "--extract-media=.", "-o", "apunte.md"],
            cwd=tmp, check=True,
        )
        texto = (Path(tmp) / "apunte.md").read_text(encoding="utf-8")

        def reemplazar(m):
            archivo, leyenda, num = m.group(1), m.group(2), int(m.group(3))
            es_foto = num in fotos
            carpeta = "fotos" if es_foto else "esquemas"
            nombre = f"{letra}-fig{num:02d}.jpg"
            guardar_imagen(Path(tmp) / "media" / archivo,
                           RAIZ / "figuras" / carpeta / nombre,
                           1200 if es_foto else 1400, 82 if es_foto else 85)
            leyenda = re.sub(r"^Figura \d+\.\s*", "", leyenda.strip())
            desc = descripciones.get(str(num), "PENDIENTE: describir mirando la imagen.")
            tipo = "foto (va en el juego)" if es_foto else "esquema (redibujar en SVG)"
            return (f"> **Figura {letra}-{num:02d}** · {tipo} · `figuras/{carpeta}/{nombre}`  \n"
                    f"> **Leyenda:** {leyenda}  \n"
                    f"> **Qué muestra:** {desc}\n")

        texto = PATRON_FIGURA.sub(reemplazar, texto)

    # Quita la negrita sobrante de los títulos que deja pandoc.
    texto = re.sub(r"^(#+) \*\*(.+?)\*\*[ \t]*$", r"\1 \2", texto, flags=re.M)
    salida = RAIZ / "contenido" / f"{letra}_{slug(a.titulo)}.md"
    salida.parent.mkdir(parents=True, exist_ok=True)
    salida.write_text(texto, encoding="utf-8")
    pendientes = texto.count("PENDIENTE: describir")
    print(f"{salida.relative_to(RAIZ)} listo. Figuras sin descripción: {pendientes}")


if __name__ == "__main__":
    main()

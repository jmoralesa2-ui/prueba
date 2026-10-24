# Resumen para continuar: proyecto HOMEOSTASIS

## 1. Quién soy y qué busco
- Estudiante de Medicina en la UFT. El ramo es Bioquímica (Bioquímica II / Bioquímica y Biofísica). Uso skills propias para estudiar: apunte-magistral, generadores de controles y solemnes, esqueletos de blurting, etc.
- Quiero un videojuego para aprender bioquímica, en el que la parte de "juego" se note mucho, pero donde **aprender es la prioridad**: todo el contenido, sin omitir ningún detalle, en el menor tiempo posible.
- Necesito empezar a estudiar ya. Me importa el **tiempo**: que todo el proyecto quepa en unos **3 límites de uso de 5 horas** de Claude Code, trabajando de la forma más rápida, ahorrativa y eficiente posible, sin perder calidad.
- Cada etapa del trabajo tiene que dejar algo que ya pueda usar para estudiar.
- Solo 2D (nada de 3D, porque es caro y complicado de programar).
- Escríbeme en español; mi español es chileno.

## 2. El concepto del juego: HOMEOSTASIS, "Mantén vivo a tu humano"
- **La idea:** Factorio dentro de una célula + jefes de roguelite al estilo Hades. Las vías metabólicas se construyen como líneas de producción, las enzimas son máquinas o cartas y el ATP es el dinero. El mapa metabólico (el póster de Roche) es el mapa del mundo, tapado por niebla de guerra.
- **Regla de oro:** la bioquímica ES la mecánica. Nada de "responde esta pregunta para continuar". La prueba es: si le quitas la bioquímica al juego, se rompe.
- **Cómo cada concepto se vuelve mecánica:**
  - Km = afinidad; Vmax = velocidad.
  - Paso irreversible = válvula de un solo sentido.
  - Enzima reguladora = nodo con interruptores.
  - Coenzimas = munición.
  - ATP, NADH y NADPH = tres monedas; el balance neto es la economía.
  - Lanzaderas = puertos con distinto peaje.
  - Inhibidores competitivos y no competitivos = enemigos.
  - Tejidos = mundos.
  - Estados metabólicos = clima.
  - Enfermedades genéticas = maldiciones.
- **Mascota:** Mito, una mitocondria sarcástica con forma de frijol, naranja-rosada, con crestas en zigzag.
- **Modos inspirados en juegos:**
  - Aduana Mitocondrial (Papers, Please);
  - puzzles de optimización (Opus Magnum);
  - microjuegos (WarioWare);
  - cooperativo (Overcooked) y duelos de cartas (Slay the Spire) — se descartaron para esta versión;
  - Detective (Dr. House).
- **Game feel:** monedas de ATP con sonido, combos, música adaptativa, y la pantalla "¿Por qué moriste?" con la cadena causal.
- **Qué evitar:** el "brócoli bañado en chocolate" (quiz + puntos), muros de texto, errores científicos y meter todo el contenido de golpe.

## 3. Decisiones de diseño y tecnología (finales)
- **Arte:** 2D vectorial (SVG) dibujado en código, estilo plano Kurzgesagt / Cells at Work, con toques retro solo en la interfaz: tipografía pixel (Press Start 2P o VT323) en títulos y HUD, marcos gruesos y efectos chiptune con Web Audio API.
  - No pixel art puro: a baja resolución se pierde el detalle químico (cis/trans, Δ9, anillos).
  - No imágenes de IA: no se animan por partes y pesan mucho.
  - No vista isométrica.
- **Código:** HTML + CSS + JavaScript sin frameworks y sin instalar nada, en varios archivos chicos, con scripts clásicos (no módulos ES) para que index.html se abra con doble clic. React, TypeScript y los motores de juego se descartaron porque gastan más uso y obligan a compilar.
- **Todo se genera desde datos:**
  - videos = lista de pasos que el motor dibuja con una biblioteca de piezas SVG reutilizables;
  - mecánicas = motores genéricos, con niveles en archivos de datos chicos;
  - preguntas = datos;
  - un diccionario único de metabolitos con ID compartidos.
- **Validador** (Node o Python, sin dependencias) y revisión de errores de consola, en vez de capturas de pantalla (máximo 2 por etapa).
- **Script de unión:** junta todo en HOMEOSTASIS.html, un solo archivo para el celular, con las fotos incrustadas.
- **Voces con Kokoro** (modelo de voz gratuito que corre en el computador), como en mi app "Solemne de Biofísica":
  - Mito narra cada paso de los videos, y también hay voz en los jefes, logros y errores graves;
  - el script herramientas/generar_voces.py las genera en lote al final de cada etapa y regenera solo lo que cambia;
  - si falta un audio, se usa la voz del navegador (Web Speech API);
  - si Kokoro no se puede instalar, se usa la voz del navegador y Claude Code avisa;
  - si con las voces el archivo único pasa de unos 40 MB, ese archivo usa la voz del navegador, y la versión con Kokoro es la carpeta completa.
- **Modelos:** Opus para el motor + el capítulo I-1 (el modelo de calidad) y para los motores de las mecánicas de la etapa 3; Sonnet para todo lo demás. El prompt tiene puntos de control donde Claude Code se detiene y avisa que es momento de cambiar de modelo.

## 4. El paquete final: HOMEOSTASIS.zip
Está en el repo jmoralesa2-ui/prueba, rama `claude/practical-lovelace-wd8egb`, carpeta `paquete_HOMEOSTASIS/`. También me lo entregaron como zip.

```
HOMEOSTASIS/
├── PROMPT.md       ← el prompt para Claude Code (~7.800 palabras)
├── base/           ← aquí van: mi HTML base, el HTML de "Solemne de Biofísica" (sin sus audios),
│                     el script de Kokoro si lo tengo, y la imagen conceptual (opcional)
├── contenido/
│   ├── CONTENIDO.md  ← índice, formato y datos que están solo en las figuras
│   ├── A_Oxidacion_acidos_grasos_cuerpos_cetonicos.md
│   └── B_Biosintesis_AG_eicosanoides_colesterol.md
├── figuras/fotos/     ← 6 fotos que van en el juego: A-01, A-16, A-20, B-01, B-07, B-10
├── figuras/esquemas/  ← 76 esquemas, solo como referencia (se redibujan en SVG)
└── herramientas/convertir_apunte.py
```

- **Los apuntes en texto** salieron de los Word que subí ("Oxidación de ácidos grasos y cuerpos cetónicos" y "Clase 8: Biosíntesis de AG, eicosanoides y colesterol"), convertidos con pandoc. Quedó el texto completo, las tablas y los recuadros.
  - A: 24 secciones, 34 figuras; recuadros: Clave 17, Ojo 25, Clínica 9, Mnemotecnia 3, Diferencia 3, Síntesis 4.
  - B: 24 secciones, 48 figuras; recuadros: Clave 13, Ojo 11, Clínica 4, Mnemotecnia 1, Diferencia 5, Síntesis 4.
  - Cada figura quedó como un bloque `> **Figura A-10** · tipo · archivo / Leyenda / Qué muestra`, con una descripción detallada escrita a partir de la figura.
- **Datos que están solo en las figuras** (anotados en CONTENIDO.md):
  - B-09: los glucocorticoides activan la ácido graso sintasa; ↑AMP y palmitato inhiben la ACC.
  - B-23: receptor de LDL, Apo B-100, LCAT plasmática e IDL; la HDL va a las glándulas endocrinas; sales biliares y colesterol fecal.
  - B-30: a mano: araquidonato → 2TX, 2PG, 4LT y lipoxinas; EPA → 3TX, 3PG, 5LT y resolvinas; DHA → maresinas, protectinas y resolvinas.
  - B-32: los AINEs inhiben las dos actividades de la PGH sintasa; la peroxidasa usa 2 GSH → GSSG.
  - B-33: la PLA2 se activa con angiotensina II, bradicinina, adrenalina y trombina; series completas de los grupos 1, 2 y 3.
  - B-18: la carga energética alta inhibe el ciclo del citrato.
  - A-14 y A-28: "12 ATP" es el valor antiguo; hoy son 10 por acetil-CoA.
  - A-19: el reciclaje del malato por la enzima málica.
  - A-33 y A-34: los valores de los gráficos del ayuno.
- **convertir_apunte.py**, para apuntes futuros. Necesita pandoc y Pillow.
  - Uso: `python3 herramientas/convertir_apunte.py APUNTE.docx C "Titulo corto" --fotos 1,5 --descripciones desc.json`
  - Las figuras sin descripción quedan como "PENDIENTE", para que Claude las describa mirando cada imagen una sola vez.

## 5. Qué dice PROMPT.md (sección por sección)
- **Reglas de ahorro:**
  1. 3 etapas, no amarradas a los límites de 5 horas: al terminar una se hace /clear y se sigue de inmediato.
  2. CLAUDE.md corto (máximo 40 líneas) + PROGRESO.md actualizado después de cada capítulo, para retomar si se corta el límite.
  3. El contenido ya está listo; se lee por secciones, nunca completo.
  4. Todo desde datos y piezas SVG.
  5. Escribir cada archivo una vez, sin releerlo; editar solo lo necesario.
  6. Validar con scripts.
  7. Sin subagentes ni dependencias (salvo Kokoro para las voces).
  8. Respuestas cortas.
- **0.** Qué hay en la carpeta.
- **1.** Objetivo y prioridades: aprender todo, que se sienta juego, conservar el HTML base y dejarlo listo para más apuntes.
- **2.** Antes de programar:
  - leer los HTML de base/ sin el base64 (copia temporal con marcadores, sin abrir audios);
  - INVENTARIO.md del HTML base;
  - análisis de los videos y voces de Solemne de Biofísica;
  - COBERTURA.md armada desde el índice.
- **3.** Reglas que no se negocian: no perder nada del HTML base (con tabla "original → dónde quedó"); su paleta como identidad; cero omisiones; la bioquímica es la mecánica; los valores del apunte mandan (2,5 ATP por NADH; 1,5 por FADH2; 10 por acetil-CoA; palmitato 108 brutos / 106 netos); los "Ojo" se enseñan como trampas; funciona sin internet.
- **4.** Dirección de arte: lo del punto 3 de este resumen, la voz y la skill frontend-design (ya instalada).
- **5.** Mapa unificado (la pieza más importante):
  - acetil-CoA al centro;
  - compartimentos como regiones y tejidos como mundos;
  - zoom, arrastre y buscador;
  - niebla de guerra;
  - interruptor Alimentado / Ayuno / Ejercicio, con las enzimas reguladas mostrando su estado;
  - capas activables;
  - mapa de calor de dominio.
- **6.** Modo Historia. Cada capítulo tiene:
  1. un video narrado por Mito;
  2. práctica dentro del video;
  3. los recuadros como objetos (Clave = Gema; Ojo = Trampa que vuelve en los jefes; Clínica = paciente del Modo Detective; Mnemotecnia = Hechizo del Grimorio; Diferencia = Duelo; Síntesis = Pergamino);
  4. un nivel jugable;
  5. un mini-jefe con estrellas;
  6. un Modo Exprés de 2–3 minutos.

  Acto I "El Tesoro del Ayuno" (I-1 a I-24, apunte A) y Acto II "La Fábrica del Banquete" (II-1 a II-26, apunte B), con el contenido de cada capítulo detallado.
- **7.** Mecánicas:
  1. Fábrica;
  2. Aduana Mitocondrial;
  3. Sala de Control Hormonal;
  4. Laboratorio de Carbonos;
  5. Contador de ATP;
  6. Detector de Mentiras (V/F con justificación, el formato de los controles);
  7. Modo Detective (casos clínicos);
  8. Microjuegos;
  9. Duelos.
- **8.** Jefes: Ayuno de 40 días, Cetoacidosis Diabética, Bebé Prematuro (CPT I), El Muffin, La Torcedura (eicosanoides y fármacos), Hipercolesterolemia, Aceite de Lorenzo, El Camello y, al final, El Señor de las Trampas.
- **9.** Colecciones y repaso:
  - Enzimodex, Arsenal, Bestiario, Grimorio, Gemas y Pergaminos;
  - XP, rangos, logros y racha;
  - repaso espaciado y "Repaso de hoy";
  - Modo Examen: Control (V/F) y Solemne (a–d), con pauta razonada;
  - guardado con exportar e importar.
- **10.** Matriz de cobertura: cada sección, tabla, figura y recuadro con su capítulo, video, nivel y preguntas; al menos una V/F + otro formato por ítem, más preguntas inversas y de cálculo.
- **11.** Tecnología: lo del punto 3 de este resumen, más COMO_AGREGAR_APUNTES.md.
- **12.** Las 3 etapas:
  - **Etapa 1 "Ya puedo estudiar el Acto I":** inventario, motor completo de estudio (preguntas, Detector, repaso, Modo Examen), Acto I completo (el nivel jugable es provisionalmente un desafío de preguntas con tiempo y vidas), mapa del Acto I, voces del Acto I y HOMEOSTASIS.html. **Punto de control** después del motor + el capítulo I-1, para cambiar de Opus a Sonnet.
  - **Etapa 2 "Ya puedo estudiar todo":** Acto II, mapa completo, colecciones, voces del Acto II.
  - **Etapa 3 "El juego completo":** mecánicas (con punto de control para volver a Opus y luego Sonnet), jefes, progresión, sonido, voces, COMO_AGREGAR_APUNTES.md, verificación final y entrega.

## 6. Mis pasos para usarlo
1. Descomprimir el zip y poner en `base/` el HTML base, el HTML de Solemne de Biofísica (sin audios), el script de Kokoro si lo tengo y la imagen si quiero. No poner los PDF ni los Word en la carpeta.
2. Abrir Claude Code en la carpeta HOMEOSTASIS → `/model` → Opus → escribir "Lee PROMPT.md y empieza."
3. En el punto de control: revisar index.html y pedir cambios con Opus si hace falta → `/model` → Sonnet → "sigue".
4. Al terminar cada etapa: `/clear` → "Lee CLAUDE.md y PROGRESO.md y sigue con la siguiente etapa." En la etapa 3, empezar con Opus y cambiar a Sonnet en su punto de control.
5. Si se corta el límite: "Lee CLAUDE.md y PROGRESO.md y sigue donde quedaste."
6. Para estudiar: abrir HOMEOSTASIS.html con doble clic.
7. Si necesito el apunte B primero: agregar "haz el Acto II antes que el Acto I".
8. Si un capítulo hecho con Sonnet queda peor que el I-1: cambiar a Opus y pedir "rehaz el capítulo X siguiendo el modelo del I-1".
- Si uso Claude Code en la web, la carpeta tiene que estar en GitHub: ya está en mi repo, y solo falta subir mis archivos a base/.

## 7. Cómo ahorrar uso en Claude Code (consejos que me dieron)
- **Qué gasta más:** la conversación larga (se reprocesa en cada mensaje), los PDF leídos como imagen, reescribir archivos grandes, Opus, las capturas de pantalla y los subagentes.
- **Qué hacer:**
  - Sonnet para construir y Opus solo para lo clave (`/model`);
  - una etapa a la vez, con `/clear` entre etapas y `/compact` si una sesión se alarga;
  - pedidos concretos;
  - `/usage` (uso del plan) y `/context` (qué ocupa la conversación);
  - CLAUDE.md es la memoria (`/memory`), y tiene que ser corto.
- **Plugins:** frontend-design (Anthropic) ya está instalado. Para ver cuánto gasta cada respuesta me sugirieron Turn Usage y Usage Line. Ningún plugin hace gastar menos por sí solo.
- **Límites:** se reinician cada 5 horas, y además hay un límite semanal. No hay garantía de que todo quepa en 3 límites: depende del plan.

## 8. Prompt de imagen (para ver cómo se vería el juego)
Es para una IA de imágenes (ChatGPT, Ideogram o Gemini escriben bien el texto en la imagen; Midjourney no). Son 4 recuadros en 2×2:
1. el mapa unificado con ACETIL-CoA al centro, el interruptor ALIMENTADO / AYUNO / EJERCICIO y la niebla de guerra;
2. el video del "CAP. 9: LANZADERA DE CARNITINA" (CPT I, CACT, CPT II, con MALONIL-CoA bloqueando);
3. la Fábrica con la espiral de β-oxidación y el HUD "ATP 106, NADH 7, FADH2 7, ACETIL-CoA 8";
4. el jefe "AYUNO DE 40 DÍAS", en FASE IV, DÍA 24.

Opcionales:
5. la Aduana: ACETIL-CoA RECHAZADO, ácido graso muy largo → PEROXISOMA, cadena corta → DIFUSIÓN, CITRATO ACEPTADO;
6. el Detector de Mentiras: "EL MALONIL-CoA INHIBE LA CPT II" → FALSO, "x5 COMBO".

Estilo: vector plano tipo SVG, contornos gruesos, fondo azul marino, brillos neón, personajes tiernos, Mito en cada recuadro, y tipografía pixel solo en la interfaz; nada de 3D. Prompt negativo: "3D render, isometric 3D, realistic, photorealistic, perspective camera, depth of field, pixelated characters, blurry, gibberish text, long sentences, watermark, low resolution". Si conozco los colores de mi HTML base, agregar "Main color palette: #..." al final.

## 9. Estado actual y pendientes
- Todo lo pedido está hecho y subido. Último commit: "Agrega al prompt las voces con Kokoro y cómo leer base/ sin los audios".
- **Pendiente de mi parte:** poner mis archivos en base/ y lanzar Claude Code.
- **Para apuntes futuros:** convertirlos con convertir_apunte.py (o pedirle a Claude que lo haga), describir sus figuras y agregar sus capítulos como datos, siguiendo COMO_AGREGAR_APUNTES.md, que Claude Code crea en la etapa 3.

# HOMEOSTASIS: juego para aprender Bioquímica (módulo Lípidos)

Este archivo es PROMPT.md y está en la carpeta del proyecto. Léelo completo en la primera sesión; en las siguientes, abre solo la sección que necesites.

## Reglas para trabajar rápido y ahorrar uso (aplícalas siempre)
Necesito empezar a estudiar ya. Mis límites de uso se reinician cada 5 horas, y la meta es que todo el proyecto quepa en unos 3 de esos límites. Trabaja lo más rápido, ahorrativo y eficiente posible, sin perder calidad.
1. El trabajo está dividido en 3 etapas (sección 12), y cada una termina con una versión que ya puedo usar para estudiar. Las etapas no van amarradas a los límites de uso: cuando termines una, detente para que yo limpie la conversación con /clear, y sigue de inmediato con la siguiente.
2. Al empezar, crea un CLAUDE.md corto (máximo 40 líneas) con estas reglas, la estructura de carpetas y la etapa en que vamos. Actualiza PROGRESO.md (qué está hecho, qué falta y qué decisiones tomaste) cada vez que termines un capítulo o un bloque de trabajo, para que, si se acaba el límite de uso a mitad de una etapa, se pueda retomar exactamente donde quedó.
3. El contenido de los apuntes ya está listo en contenido/ (sección 0). No hay PDF. No leas los archivos de contenido completos de una vez: busca el título de la sección que necesitas y abre solo esa parte.
4. Todo se genera desde datos: los videos, los niveles y las preguntas se escriben como datos, y el motor los dibuja con piezas SVG reutilizables (sección 11). Nunca dibujes SVG a mano para cada escena.
5. Escribe cada archivo completo de una vez y no lo vuelvas a leer después de escribirlo. Para cambiar algo, edita solo la parte necesaria.
6. Verifica con scripts, no con capturas: un validador de los datos y una revisión de errores de consola con un navegador sin ventana. Usa como máximo 2 capturas de pantalla por etapa.
7. No uses subagentes ni tareas en paralelo, y no instales frameworks ni dependencias.
8. Respuestas cortas: no me expliques el código ni repitas lo que hiciste. Al final de cada etapa, un resumen de 5 líneas como máximo y qué puedo usar ya.

## 0. Qué hay en la carpeta
- PROMPT.md: este archivo.
- base/: mi HTML actual (la referencia de pestañas, funciones, colores y recursos) y el archivo "Solemne de Biofísica" (la referencia del estilo de las explicaciones animadas, los "videos": ese es el estilo que quiero, pero todavía mejor). Puede haber también una imagen conceptual del juego; úsala solo como referencia de estilo visual.
- contenido/CONTENIDO.md: índice de los apuntes, formato de los archivos y datos que aparecen solo en las figuras. Léelo primero.
- contenido/A_Oxidacion_acidos_grasos_cuerpos_cetonicos.md: Apunte A, "Oxidación de ácidos grasos y cuerpos cetónicos" (24 secciones, 34 figuras).
- contenido/B_Biosintesis_AG_eicosanoides_colesterol.md: Apunte B, "Biosíntesis y almacenamiento de ácidos grasos, eicosanoides y colesterol" (24 secciones, 48 figuras).
  Los dos tienen el texto completo, las tablas, los recuadros (Clave, Ojo, Clínica, Mnemotecnia, Diferencia y Síntesis) y cada figura descrita en detalle donde aparece.
- figuras/fotos/: las 6 fotos reales que sí van en el juego.
- figuras/esquemas/: los demás esquemas, solo como referencia (ver CONTENIDO.md).
- herramientas/convertir_apunte.py: script para pasar apuntes nuevos en Word al mismo formato.

## 1. Objetivo y prioridades
Analiza el HTML base y hazme uno como ese, pero con la información de los dos apuntes y convertido en un videojuego muy bien diseñado llamado HOMEOSTASIS. Mis prioridades, de mayor a menor:
1. Aprender TODO el contenido de los dos apuntes, sin omitir ningún detalle, en el menor tiempo posible.
2. Que se sienta un videojuego de verdad, no una página de estudio con puntos.
3. Conservar todo lo que tiene el HTML base.
4. Dejar el código listo para agregar más apuntes después, porque faltan temas.

Si aprender y jugar chocan, gana aprender, pero busca la forma de que siga sintiéndose juego.

## 2. Antes de programar (al inicio de la etapa 1)
1. Inventario del HTML base: todas las pestañas, funciones, botones, recursos, paleta de colores exacta (con códigos), tipografías, sonidos, animaciones, sistema de guardado y cualquier otro detalle. Guárdalo en INVENTARIO.md. Después no vuelvas a leer el HTML base completo: consulta INVENTARIO.md y abre solo la parte que necesites.
2. Análisis de los videos de "Solemne de Biofísica": cómo están construidos, su ritmo, sus transiciones, sus controles y cómo presentan cada paso. Anótalo en INVENTARIO.md. Ese es el estándar mínimo para todas las explicaciones nuevas.
3. Lee contenido/CONTENIDO.md. Arma COBERTURA.md (sección 10) a partir del índice y de los títulos, tablas, figuras y recuadros de los apuntes, buscándolos: para esto no necesitas leer todo el texto. Cada etapa completa las filas de lo que construye.

No esperes mi confirmación: haz esto y sigue directo con la etapa 1.

## 3. Reglas que no se negocian
- Nada del HTML base se pierde. Las pestañas y funciones pueden cambiar de nombre o de lugar para encajar en el juego, pero todas siguen existiendo y funcionando. Al final, entrega una tabla "pestaña o función original → dónde quedó".
- Colores: la paleta del HTML base se mantiene como identidad, y el aspecto de juego (brillos, sombras, partículas, marcos de HUD) se construye encima de ella.
- Cero omisiones: cada sección, tabla, figura y recuadro de los apuntes aparece en al menos una explicación y en al menos una pregunta o mecánica.
- La bioquímica es la mecánica: cada nivel exige saber algo del apunte para ganar. Está prohibido el "responde esta pregunta para desbloquear".
- Los valores del apunte mandan: 2,5 ATP por NADH, 1,5 por FADH2, 10 ATP por acetil-CoA, y el palmitato rinde 108 ATP brutos y 106 netos. Cuando el apunte corrige una diapositiva (recuadros "Ojo"), usa la versión corregida y enséñala como trampa de examen.
- Tiene que funcionar abriendo el archivo en el navegador, en celular y en PC, sin instalar nada y sin internet (las fuentes web son opcionales y deben tener respaldo).
- La tecnología y la forma de los archivos están en la sección 11.

## 4. Dirección de arte (2D, nada de 3D)
- Todo se dibuja en código con SVG (canvas solo para partículas si hace falta). Estilo plano, contornos gruesos, colores saturados y personajes redondos con ojos grandes, al estilo de Kurzgesagt y Cells at Work. Sin 3D, sin WebGL y sin imágenes de internet: las únicas imágenes son las fotos reales de los apuntes (sección 10).
- Toques retro de videojuego: tipografía pixel en títulos y HUD (por ejemplo Press Start 2P o VT323, con fuente de respaldo), marcos de HUD gruesos y efectos de sonido chiptune generados con Web Audio API (sin archivos de audio), con botón para silenciar.
- Moléculas precisas: cadenas con los carbonos numerados (C1 del carboxilo, α, β, ω), dobles enlaces cis o trans en su posición real (Δ2, Δ3, Δ9, Δ12...), los anillos A-B-C-D del colesterol y el enlace tioéster con la CoA.
- Mascota guía: "Mito", una mitocondria sarcástica (con forma de frijol, color naranja-rosado y crestas en zigzag) que narra las explicaciones y reacciona a los aciertos y errores.
- Que se sienta juego: cada ATP producido suena y salta como una moneda. Contadores animados, combos, partículas, temblor de pantalla en errores graves, transiciones suaves y sonido que cambia según el estado (alimentado, ayuno, ejercicio).
- Si tienes disponible la skill frontend-design, úsala.

## 5. Mapa unificado = mapa del mundo (la pieza más importante)
Un solo mapa metabólico interactivo que integra todo el contenido de los dos apuntes, con el acetil-CoA al centro (como la Figura 2 del Apunte A).
- Compartimentos dibujados como regiones: lumen intestinal y enterocito, linfa y sangre, citosol, membrana mitocondrial externa, espacio intermembrana, membrana interna, matriz, retículo endoplasmático liso y peroxisoma.
- Tejidos como "mundos": intestino, hígado, tejido adiposo, músculo esquelético, corazón, cerebro, riñón, glóbulo rojo, glándula mamaria, plaquetas y endotelio, y leucocitos.
- Vías: todas las de la sección 6, conectadas entre sí por sus metabolitos compartidos (acetil-CoA, malonil-CoA, citrato, oxalacetato, malato, piruvato, HMG-CoA, glicerol-3-fosfato, DHAP, NADPH, etc.).
- Zoom y arrastre fluidos con el dedo y con el mouse, y un buscador de enzimas y metabolitos.
- Niebla de guerra: cada tramo se revela al completar su capítulo del Modo Historia. Debe haber una opción "mostrar todo" para repasar.
- Interruptor hormonal global con tres estados: Alimentado (insulina), Ayuno (glucagón) y Ejercicio (adrenalina, AMPK). Al cambiarlo, el mapa se reconfigura en vivo:
  - las vías activas brillan y tienen partículas fluyendo;
  - las inactivas se apagan;
  - cada enzima regulada muestra su estado (fosforilada o desfosforilada, activa o inactiva, polímero o protómeros) y quién la regula.
- Capas que se pueden activar: enzimas; coenzimas y energía (ATP, NADH, FADH2, NADPH); regulación; fármacos; enfermedades.
- Al tocar cualquier nodo se abren su ficha en la Enzimodex, su explicación animada y un botón "jugar este nivel".
- Mapa de calor de dominio: cada tramo se pinta según cuánto lo domina el jugador.

## 6. Modo Historia (aprender): el centro del juego
Una campaña en dos actos, uno por apunte, con los capítulos en el orden lógico del apunte. Todos los capítulos siguen esta estructura:
1. Explicación animada ("video") narrada por Mito, al nivel de las de "Solemne de Biofísica" o mejor. Va paso a paso, con controles de reproducir, pausa, anterior, siguiente y velocidad. El texto va sincronizado, las moléculas se mueven y se transforman, las enzimas actúan en pantalla y cada concepto clave queda resaltado.
2. Práctica dentro del video, cada uno o dos pasos: una acción corta y jugable (arrastrar la enzima correcta, elegir la coenzima, predecir qué se acumula, ordenar reacciones, contar carbonos). Si el jugador falla, el video vuelve al paso que explica eso.
3. Los recuadros del apunte convertidos en objetos del juego:
   - Clave → Gema de conocimiento (coleccionable).
   - Ojo → Trampa: se guarda y reaparece como enemigo en los jefes.
   - Clínica → Caso clínico: desbloquea un paciente en el Modo Detective.
   - Mnemotecnia → Hechizo: se guarda en el Grimorio.
   - Diferencia → Duelo: minijuego de comparar dos cosas parecidas.
   - Síntesis → Pergamino con el resumen del capítulo.
4. Nivel jugable del capítulo, con una de las mecánicas de la sección 7. En las etapas 1 y 2 es un desafío de preguntas provisional (sección 12).
5. Mini-jefe que da de 1 a 3 estrellas según la precisión. Al ganarlo se revela ese tramo del mapa y se desbloquean sus cartas.

Además, cada capítulo tiene un "Modo Exprés" (un resumen animado de 2 a 3 minutos para repasar rápido) y muestra su tiempo estimado.

Los capítulos mínimos son los siguientes. Cada uno debe cubrir todo lo que se lista y todo lo demás que diga esa parte del apunte.

### Acto I: "El Tesoro del Ayuno" (Apunte A)
- I-1 Los lípidos como reserva:
  - los triglicéridos son la principal reserva de energía (9 kcal/g frente a 4 kcal/g);
  - sirven para sobrevivir al ayuno, pero se movilizan lento;
  - el adipocito tiene el núcleo en la periferia y una gran gota de grasa; el tejido adiposo infiltrado en el músculo explica el lomo vetado; el tejido adiposo es un tejido vivo;
  - grasa blanca frente a grasa parda;
  - panorama centrado en el acetil-CoA: la doble flecha, el colesterol, las hormonas esteroidales, los ácidos biliares, los cuerpos cetónicos (solo los produce el hígado, que no puede gastarlos) y los aminoácidos cetogénicos.
- I-2 Digestión y absorción:
  - en el estómago casi no pasa nada (la lipasa gástrica tiene acción mínima);
  - la bilis y las sales biliares emulsionan, no digieren; micelas y superficie expuesta;
  - lipasas y colipasa liberan monoglicéridos, diglicéridos y ácidos grasos libres;
  - los triglicéridos se rearman en el enterocito (retículo liso);
  - estructura del quilomicrón: monocapa de fosfolípidos, núcleo de triglicéridos y ésteres de colesterol, colesterol, apo B-48, C-III y C-II;
  - recorrido: sistema linfático, quilífero central, conducto torácico y vena subclavia izquierda.
- I-3 Lipoproteína lipasa:
  - sus 6 pasos (la apoC-II activa la LPL del endotelio, se liberan ácidos grasos y glicerol, los ácidos grasos pasan a las células o viajan con la albúmina);
  - el glicerol va al hígado, y los remanentes también, donde se forma la VLDL;
  - la LPL es extracelular y no hay que confundirla con las lipasas intracelulares.
- I-4 Movilización en el adipocito:
  - hormonas: glucagón, adrenalina y noradrenalina;
  - receptores α (α1, α2) y β (β1, β2, β3), proteína Gs, adenilato ciclasa, AMPc y PKA;
  - perilipinas (la mandarina) y lipasa sensible a hormona;
  - los 11 pasos de la Figura 6 (CGI-58, ATGL, HSL, MGL, albúmina, transportador y β-oxidación en el miocito);
  - la tabla de las 3 lipasas con su regulación: solo la primera está regulada; el "Ojo" sobre ATGL y HSL;
  - la insulina inhibe la lipólisis; es el mismo patrón que en glucógeno y en glucólisis frente a gluconeogénesis.
- I-5 Transporte por la sangre:
  - los de cadena corta y media viajan libres; los de cadena larga, unidos a la albúmina (6 a 8 ácidos grasos por albúmina; la albúmina sostiene la presión oncótica);
  - ácido hexadecanoico = palmítico (mnemotecnia hexa + deca);
  - ejemplo de correr en ayunas: el palmitato da 8 acetil-CoA = 8 vueltas de Krebs.
- I-6 Destino del glicerol:
  - va al hígado, porque el adipocito tiene poca glicerol quinasa;
  - ruta: glicerol quinasa → glicerol 3-fosfato deshidrogenasa (NAD+ → NADH) → DHAP → triosa fosfato isomerasa → gliceraldehído 3-fosfato;
  - "depende del estado": en ejercicio va a glucólisis; en ayuno, a gluconeogénesis;
  - en el hígado en ayuno, el acetil-CoA inhibe la PDH y activa la piruvato carboxilasa, y se forman glucosa y cuerpos cetónicos.
- I-7 ¿Adónde va el ácido graso?:
  - mitocondria y peroxisoma;
  - la tabla según el largo de la cadena: corta (2–4), media (4–12), larga (12–20) y muy larga (>20), con su lugar de catabolismo y su transporte (difusión, carnitina o ALDP); el dato obsoleto "desconocido";
  - la L-carnitina como suplemento: por qué no sirve; lo que sirve es tener más mitocondrias, es decir, más músculo, es decir, hacer ejercicio.
- I-8 Activación del ácido graso:
  - lipoacil-CoA, acil-CoA, acetil-CoA y palmitoil-CoA;
  - la acil-CoA sintetasa (tiocinasa) está en la cara citosólica de la membrana externa;
  - se forman acil-adenilato y PPi; luego actúa el tiol de la CoA, se forma el enlace tioéster y sale AMP;
  - ΔG°' de −15 y −19 kJ/mol, y la pirofosfatasa;
  - 1 ATP = 2 equivalentes; mnemotecnia sintetasa / sintasa;
  - la membrana externa es permeable y la interna, selectiva: el acetil-CoA no entra (entra el piruvato) y el acil-CoA tampoco (entra la acil-carnitina).
- I-9 Lanzadera de la carnitina:
  - fases I y II;
  - los 4 componentes con su ubicación y función: acil-CoA sintetasa, CPT I, CACT (antiporte) y CPT II;
  - el funcionamiento paso a paso y "la vida de la carnitina";
  - hay dos pools de CoA; L-carnitina;
  - la CPT I es la etapa limitante; el malonil-CoA (3 C) la inhibe; la ACC lo forma; así se evita el ciclo fútil.
- I-10 Clínica de la carnitina:
  - deficiencia de CPT I: en prematuros por inmadurez y en recién nacidos de término por causa genética; déficit energético muscular y cardíaco;
  - la fórmula se hace con ácidos grasos de cadena corta y media; pronóstico; el caso de la paciente joven;
  - otras deficiencias (transportador, CACT, CPT II) con hipoglucemia hipocetósica;
  - la carnitina: estructura (amonio cuaternario, carboxilato e hidroxilo), deriva de la lisina, viene principalmente de la dieta, se sintetiza en el riñón (70 %) y el hígado (30 %), la usan el músculo y el corazón, el riñón la reabsorbe, ~50 µmol/L en plasma;
  - no tomar carnitina como pre-entreno.
- I-11 β-oxidación:
  - tejidos: músculo, corazón e hígado; los de cadena corta (≤C8) y media no necesitan carnitina; la leche materna;
  - 7 vueltas y 8 acetil-CoA; da más energía por mol que la glucosa, pero es más lenta; el glóbulo rojo no oxida ácidos grasos;
  - nomenclatura de los carbonos α, β y ω;
  - las 4 reacciones con su enzima, coenzima y producto (tabla): trans-Δ2-enoil-CoA, L-β-hidroxiacil-CoA, β-cetoacil-CoA y miristoil-CoA; mnemotecnia "se oxida, se hidrata, se oxida y se corta";
  - la tiolasa conserva la energía del tioéster;
  - el FADH2 va a la CoQ por la ETF, no por el complejo II;
  - la acil-CoA deshidrogenasa es una familia; la deficiencia de MCAD;
  - cis frente a trans y las grasas trans (margarina);
  - la β-oxidación es la síntesis al revés; la espiral de C14 a C4.
- I-12 Agua metabólica: el camello, la rata canguro y el oso; ~130 mol de agua por mol de palmitato (~2,3 kg).
- I-13 Rendimiento energético:
  - el cálculo completo de 108 a 106 y la tabla por enzima;
  - 28 + 80;
  - el "Ojo" del "TCA 12 ATP" (es un valor antiguo);
  - glucosa frente a palmitato: tabla de ATP por mol, ATP por gramo y kcal por gramo.
- I-14 Regulación de la β-oxidación:
  - los 3 controles: disponibilidad de ácido graso; malonil-CoA sobre la CPT I (ACC1 y ACC2; la insulina activa la ACC en el hígado; la AMPK inhibe la ACC en el músculo y el hígado); relación ATP/ADP alta, NADH y FADH2;
  - la tabla de factores;
  - los "Ojo": el malonil-CoA inhibe la CPT I y no la CPT II; la AMPK inhibe la ACC.
- I-15 Cadena impar:
  - propionil-CoA;
  - 3 pasos: propionil-CoA carboxilasa (biotina, ATP, CO2) → D-metilmalonil-CoA; racemasa → L-metilmalonil-CoA; mutasa (vitamina B12) → succinil-CoA;
  - aciduria metilmalónica;
  - reciclaje por malato y enzima málica (CO2, NADPH, piruvato);
  - es la única parte de un ácido graso que aporta carbonos netos a la gluconeogénesis.
- I-16 Peroxisoma:
  - nombres: eicosanoato (20), docosanoato (22), tetracosanoato (24), hexacosanoato (26), "-anoato" y ":0";
  - los 5 pasos; la acil-CoA oxidasa; FADH2 + O2 → H2O2 → catalasa; ese paso no genera ATP; el NADH se exporta;
  - el acetil-CoA sale para formar colesterol y ácidos biliares;
  - datos del libro: 20 % del O2 del hepatocito; no oxida cadena corta; se exporta octanoil-carnitina;
  - X-ALD (ALDP, "Un milagro para Lorenzo") y síndrome de Zellweger (falla la biogénesis del peroxisoma; muerte cerca de los 6 meses); la diferencia entre ambos;
  - tabla mitocondria frente a peroxisoma.
- I-17 Ácidos grasos insaturados:
  - los dobles enlaces naturales son cis y están en posiciones que no calzan;
  - oleico 18:1 cis-Δ9: 3 vueltas, Δ3,Δ2-enoil-CoA isomerasa, 5 vueltas, 9 acetil-CoA con 1 FADH2 menos; la isomerasa no oxida ni reduce;
  - poliinsaturados: 2,4-dienoil-CoA reductasa (consume NADPH) + isomerasa; el linoleico 18:2 cis-Δ9, cis-Δ12 en 6 pasos;
  - la tabla de enzimas adicionales; los insaturados rinden menos ATP.
- I-18 Cuerpos cetónicos:
  - aparecen con β-oxidación excesiva: en ayuno y con dieta cetogénica;
  - dieta cetogénica: tiras de orina a los ~5 días, pérdida de masa muscular, no es recomendable, cetoacidosis; uso en epilepsia severa con evidencia;
  - el nitroprusiato detecta el acetoacetato y no el β-hidroxibutirato; los programas de adelgazamiento abandonados;
  - los 3 cuerpos cetónicos y sus propiedades (son solubles, bajan el pH, solo los produce el hígado); el "Ojo" de la "acetoacetona";
  - cetoacidosis diabética: DM1, se salta una dosis de insulina, en ~24 h puede llegar al coma; se trata con insulina rápido y luego se maneja el pH;
  - la acetona y el aliento afrutado;
  - quién los produce y quién los consume (neurona, músculo, riñón); el cerebro obtiene más del 50 % de su energía de ellos en la inanición.
- I-19 Cetogénesis:
  - ocurre en el hígado, en la mitocondria, con glucagón, a partir del acetil-CoA de una β-oxidación excesiva;
  - la acetona se forma por descarboxilación espontánea;
  - el cerebro usa cuerpos cetónicos desde los 4–5 días; un ayuno de 3–4 días es fisiológico, la cetoacidosis es patológica;
  - las reacciones y su tabla: tiolasa, HMG-CoA sintasa, HMG-CoA liasa, β-hidroxibutirato deshidrogenasa y descarboxilación espontánea;
  - la HMG-CoA sintasa no gasta ATP;
  - HMG-CoA mitocondrial (cetogénesis, liasa) frente a HMG-CoA citosólico (colesterol, reductasa);
  - por qué el acetil-CoA va a cuerpos cetónicos y no a Krebs: los 5 pasos; falta oxalacetato porque el NADH alto lo lleva a malato y a gluconeogénesis; el ATP inhibe la isocitrato deshidrogenasa; hay que recuperar la CoA.
- I-20 Cetogenólisis:
  - sirve para transportar acetil-CoA a los tejidos; ocurre en músculo, riñón y cerebro;
  - la tioforasa (succinil-CoA:acetoacetato CoA transferasa) está ausente en el hígado; los glóbulos rojos y los hepatocitos no usan cuerpos cetónicos;
  - las 3 reacciones; 21,5 ATP por β-hidroxibutirato (no se forma el GTP);
  - tabla cetogénesis frente a cetogenólisis: órgano, compartimento, enzima clave, hormona, balance y par redox.
- I-21 El hepatocito como exportador de combustibles.
- I-22 Regulación de la cetogénesis: los 5 eventos y por qué es una regulación compensatoria.
- I-23 Combustibles durante el ayuno:
  - el gráfico de 40 días y la tabla normal / ayuno / inanición; el β-hidroxibutirato es el que más sube;
  - las 5 fases (tabla de tiempo, origen de la glucosa y combustible del cerebro); el orden glucosa / cuerpos cetónicos en el cerebro; la médula renal;
  - la integración hígado–tejidos;
  - caso clínico: ejercicio intenso después de 4–5 días de ayuno.
- I-24 Trampas de examen: todos los "Ojo" de la síntesis final se convierten en el Jefe de las Trampas.

### Acto II: "La Fábrica del Banquete" (Apunte B)
- II-1 Panorama:
  - los 5 procesos: síntesis de ácidos grasos saturados, elongación y desaturación, síntesis de triglicéridos, eicosanoides y colesterol;
  - los tejidos: hígado, glándula mamaria lactante y tejido adiposo (donde lo relevante es formar triglicéridos);
  - el punto de partida son los carbohidratos, no la grasa;
  - el doble rol del malonil-CoA: sustrato de la ácido graso sintasa e inhibidor de la CPT1; ACC1 y ACC2;
  - la ácido graso sintasa (7 actividades × 2) produce palmitato 16:0, el ácido graso inicial;
  - la elongación y la desaturación ocurren en el retículo liso; el tejido adiposo como "bolsa de limones";
  - la glucosa como responsable del aumento del IMC.
- II-2 Síntesis por exceso de carbohidratos:
  - glucosa → 2 piruvatos → acetil-CoA → lípidos (y los otros destinos de la glucosa: etanol, lactato, CO2);
  - es un proceso de reducción: condensación, reducción, deshidratación y reducción;
  - el NADPH viene de la vía de las pentosas y de la enzima málica;
  - citoplasma frente a retículo liso; las células donde ocurre; el "Ojo" de dónde ocurre cada parte.
- II-3 Catabolismo frente a anabolismo y compartimentos:
  - la tabla comparativa;
  - los compartimentos en células animales y vegetales: citosol, retículo liso, mitocondria, cloroplasto y peroxisomas (glioxisomas);
  - la elongación ocurre en el retículo liso o en la mitocondria; la desaturación, solo en el retículo liso.
- II-4 Fase I, salida del acetil-CoA al citosol:
  - sale como citrato: los 4 pasos, el transportador y la ATP-citrato liasa;
  - regulación de la liasa: la glucosa la activa alostéricamente; la insulina actúa por PKB → PP1 → desfosforilación;
  - la PP1 también actúa sobre la glucógeno sintasa y sobre la enzima bifuncional (PFK2 → F2,6BP → PFK1); la G6P va a la vía de las pentosas;
  - la glucoquinasa tiene Km alto y una proteína reguladora en el núcleo;
  - la inhiben la leptina (el tejido adiposo como glándula endocrina; las miocinas) y los AGPI (ω-3, 6 y 9);
  - reciclaje del oxalacetato: malato deshidrogenasa citosólica, transportador malato/α-cetoglutarato, enzima málica (NADPH) y piruvato carboxilasa (biotina).
- II-5 Fase II, formación del malonil-CoA:
  - la ACC1 usa HCO3−, ATP y biotina;
  - tiene 2 actividades: biotina carboxilasa (Mg2+ y ATP → carboxibiotina) y carboxiltransferasa; el paralelo con la enzima desramificante; malonil-SCoA;
  - existe como protómeros o como polímero (400 Å);
  - activadores: citrato e insulina (por PP1); inhibidores: acil-CoA de cadena larga, leptina, glucagón, adrenalina y cortisol (por fosforilación), AGPI y AMP;
  - el ciclo de fosforilación (PP1 frente a PKA): desfosforilada = activa;
  - por qué ×7: se pierden 7 CO2, se unen 14 carbonos y el acetil inicial aporta 2.
- II-6 Fase III, ácido graso sintasa:
  - consume 14 NADPH; la induce la insulina y la inhiben los AGPI;
  - tiene 7 actividades, la ACP y es un dímero antiparalelo "como un espejo"; los dominios KS, MAT, DH, ER, KR, ACP y TE;
  - la tabla de etapas opuestas a la β-oxidación; mnemotecnia "Con Reducción, Deshidratación y Reducción";
  - la ACP: 4'-fosfopanteteína unida a una serina, deriva del ácido pantoténico, termina en un tiol;
  - el ciclo en 7 pasos: carga del acetilo en la Cys, carga del malonilo en la Pan, condensación con salida de CO2, reducción con NADPH, deshidratación, reducción con NADPH y transferencia;
  - primero se forma butirilo (4 C); son 7 ciclos y la tioesterasa libera el palmitato.
- II-7 Balance del palmitato:
  - 7 malonil-CoA (7 ATP) + 7 ciclos;
  - la ecuación global: 8 acetil-CoA + 7 ATP + 14 NADPH + 14 H+ → palmitato + 8 CoA + 7 ADP + 7 Pi + 14 NADP+ + 6 H2O;
  - por qué son 8 acetil-CoA.
- II-8 β-oxidación frente a biosíntesis:
  - la tabla: lugar, sustrato, producto, cofactores, enzimas y concepto;
  - el "Ojo": la primera etapa de la β-oxidación (con FAD) no se hace si el enlace ya está insaturado.
- II-9 Regulación de la síntesis:
  - las 3 enzimas reguladas: ATP-citrato liasa, ACC (limitante) y ácido graso sintasa;
  - las 3 funciones del citrato citosólico: fuente de acetil-CoA, activador de la ACC e inhibidor de la PFK1;
  - la vía de las pentosas; el resumen de la regulación de la ACC;
  - el palmitoil-CoA como retroalimentación negativa.
- II-10 Isoformas de la ACC:
  - ACC1 es citosólica (hígado, tejido adiposo, glándula mamaria) y sirve para la síntesis;
  - ACC2 está en la membrana mitocondrial externa (hígado, músculo, corazón) y su malonil-CoA inhibe la CPT1;
  - el músculo y el corazón no tienen ACC1.
- II-11 Panorama hepático:
  - el transportador y la acil-CoA sintetasa;
  - en el estado posprandial: GLUT2, PDH, ACC, lipogénesis, glicerol-3-fosfato, triglicéridos y fosfolípidos, VLDL;
  - en ayuno: CPT1, β-oxidación, CO2 y cuerpos cetónicos.
- II-12 Síntesis de triglicéridos:
  - es un triéster de glicerol: 3 esterificaciones;
  - la integración "del muffin al adipocito" en 11 pasos (aldolasa, DHAP → glicerol-3-fosfato);
  - intestinal: los 6 pasos y la vía del monoacilglicerol (acil-CoA sintetasa, acilglicerol aciltransferasa, DAG aciltransferasa);
  - hepática: el glicerol-3-fosfato viene de la DHAP o de la glicerol quinasa; ácido lisofosfatídico, ácido fosfatídico, fosfatasa y DAG aciltransferasa (tabla de pasos 0 a 4); se ensambla en el retículo y el Golgi y sale como VLDL;
  - adipocito: LPL y acil-CoA sintetasa; el glicerol-3-fosfato viene solo de la glucosa, que entra por GLUT4 con insulina; no tiene glicerol quinasa;
  - la "Diferencia" entre hígado, adipocito y enterocito.
- II-13 Transporte de triglicéridos:
  - vía exógena (quilomicrones → remanentes) y vía endógena (VLDL → IDL → LDL; la HDL);
  - estructura del quilomicrón: colesterol libre, triglicéridos, ésteres de colesterol, vitaminas liposolubles, apoA-I, A-IV, B-48, C-II, C-III y E; la C-II activa la LPL y la B-48 es la estructural;
  - los 6 pasos de la LPL;
  - la insulina estimula la LPL del tejido adiposo e inhibe la del músculo, que se activa con la contracción o la estimulación adrenérgica.
- II-14 Elongación:
  - ocurre en el retículo liso (y en la mitocondria);
  - 4 pasos: condensación con malonil-CoA por la β-cetotiolasa (sale CO2), reducción con NADPH, deshidratación y reducción con NADPH;
  - del palmitato (16) se llega al estearato (18).
- II-15 Desaturación:
  - la primera insaturación siempre es en el C9 (palmitoleato 16:1Δ9, oleato 18:1Δ9); el estearato; el linoleato 18:2Δ9,12 solo se forma en plantas;
  - todos los dobles enlaces son cis;
  - las plantas avanzan hacia el carbono ω (C12, C15) y los animales hacia el α (C6, C5);
  - qué es un ω-6; podemos formar el oleato, pero el linoleico es esencial; sus fuentes (aceites vegetales, pescados de aguas frías, algas);
  - mecanismo: NADH-citocromo b5 reductasa (FAD), citocromo b5 (Fe) y Δ9-desaturasa (Fe); son oxidasas de función mixta; el O2 termina como 2 H2O.
- II-16 Poliinsaturados:
  - del linoleato, en plantas, sale el α-linolenato 18:3Δ9,12,15 (ω-3);
  - en animales: γ-linolenato 18:3Δ6,9,12 → eicosatrienoato 20:3Δ8,11,14 → araquidonato 20:4Δ5,8,11,14; al elongar, los dobles enlaces "corren";
  - el araquidonato no es esencial y es el precursor de los eicosanoides;
  - las familias ω-6 y ω-3 (EPA 20:5, DHA 22:6; resolvinas, protectinas y maresinas); el DHA y el cerebro; conviene consumir una mezcla de ambas.
- II-17 Biosíntesis de eicosanoides:
  - la tabla de tipos: PG, TX, HETE y LT;
  - el origen del araquidonato: el linoleico de la dieta, o los fosfolípidos de membrana mediante la PLA2 cuando hay una lesión; el origen del nombre (próstata);
  - los corticoides inhiben la PLA2 (cortisol, hidrocortisona, cortisona, betametasona);
  - la COX forma PG y TX; las lipooxigenasas forman HETEs y LT; el zileutón inhibe la 5-LOX;
  - los 3 grupos: desde el dihomo-γ-linolenato, desde el araquidonato y desde el EPA.
- II-18 Efectos en el vaso:
  - el TXA2 se forma en la plaqueta, inhibe la adenilato ciclasa (↓AMPc), aumenta la agregación y produce vasoconstricción;
  - la PGI2 se forma en el endotelio, estimula la adenilato ciclasa (↑AMPc), disminuye la agregación y relaja el vaso (junto al óxido nítrico);
  - la aspirina en dosis baja (100 mg; 81 mg).
- II-19 HETEs y leucotrienos:
  - los granulocitos;
  - los HETEs: quimiotaxis, estimulan la adenilato ciclasa, producen desgranulación e histamina;
  - los LT: contracción del músculo liso de las vías aéreas, aumento de la permeabilidad capilar y edema, quimiotaxis; el asma.
- II-20 COX-1, COX-2 y AINEs:
  - la tabla de isoenzimas;
  - los AINEs no selectivos: aspirina, diclofenaco, ibuprofeno, ketoprofeno y naproxeno; sus 3 efectos (antiinflamatorio, analgésico y antipirético, con el set point); el paracetamol;
  - el uso prolongado produce gastritis, úlceras y efectos renales; no más de 5 días a una semana;
  - la reacción de la COX en 4 pasos: PLA2, actividad ciclooxigenasa con 2 O2 → PGG2, actividad peroxidasa → PGH2, y de ahí las otras PG y los TX; la PGH2 sintasa;
  - la aspirina acetila una serina (inhibición irreversible); el ibuprofeno y el naproxeno;
  - los coxibs: celecoxib, rofecoxib, valdecoxib y etoricoxib;
  - la "Diferencia" entre AINEs, coxibs y corticoides;
  - las funciones de las PG (PGE1), los TX (TXA2) y los LT (LTA4).
- II-21 Esteroles y colesterol:
  - el acetil-CoA viene de la oxidación peroxisomal y de los aminoácidos cetogénicos; el colesterol tiene 27 C;
  - el IPP (5 C) y sus destinos: esteroides; vitaminas A, D, E y K; ubiquinona y hemo; ergosterol en hongos;
  - las funciones del colesterol: membranas y estabilidad mecánica; hormonas corticales y sexuales (la adrenalina no es esteroidal); vitamina D; ácidos biliares;
  - la estructura: ciclopentanoperhidrofenantreno, los anillos A-B-C-D y los carbonos que vienen del acetato.
- II-22 Fase I, del acetil-CoA al mevalonato:
  - tiolasa, HMG-CoA sintasa citosólica y HMG-CoA reductasa (2 NADPH, limitante);
  - la "Diferencia" con los cuerpos cetónicos;
  - la regulación de la reductasa: la activan la insulina (por PP1) y la tiroxina; la inhiben el glucagón (por PKA), los esteroles (alostéricos), la vitamina E, las estatinas y el AMP;
  - las estatinas (atorvastatina, lovastatina, rosuvastatina, simvastatina): inhibidores competitivos reversibles que bajan la LDL y suben la HDL;
  - LDL y HDL; colesterol total ~180 mg/100 mL; 25–30 % menos de eventos cardiovasculares;
  - es una enzima nocturna, por eso la estatina se toma de noche;
  - antes de 1989–1990 se usaban resinas (colestiramina).
- II-23 Fase II: mevalonato → 3 ATP → descarboxilación → IPP (Δ3) en equilibrio con el DMAPP; el "pozo" de isoprenos.
- II-24 Fase III:
  - DMAPP + IPP → geranil-PP (10 C) → farnesil-PP (15 C), por la preniltransferasa (condensación cabeza-cola);
  - 2 farnesil-PP → escualeno (30 C), por la escualeno sintasa (cabeza-cabeza, con NADPH);
  - se necesitan 6 IPP; por qué el marcaje de carbonos fue difícil.
- II-25 Fase IV y fármacos:
  - el escualeno pasa a escualeno 2,3-epóxido (monooxigenasa, O2, NADPH); la ciclasa forma lanosterol (30 C), que llega a colesterol (27 C; salen 2 CO2 y 1 HCOOH);
  - en plantas se forma estigmasterol; en hongos, ergosterol;
  - los fármacos: escualestatinas; azoles (miconazol, ketoconazol; onicomicosis); KCN; tamoxifeno (receptor de estrógenos, tumores mamarios); clomifeno (cruza la barrera hematoencefálica, sube la LH e induce la ovulación); morfolina; triparanol;
  - la relación estructura-actividad.
- II-26 Destinos del colesterol:
  - hidroxiesteroles (24-hidroxicolesterol);
  - hormonas esteroidales (pregnenolona, por la desmolasa);
  - ácidos biliares (taurocólico; sales biliares);
  - ésteres de colesterol (ACAT);
  - vitamina D;
  - la síntesis final.

## 7. Mecánicas de juego (todas con contenido de los apuntes)
1. Fábrica: una cuadrícula vista desde arriba con cintas y máquinas-enzima. El jugador coloca las enzimas en orden, conecta las coenzimas y elige el compartimento. Hay contadores de ATP, NADH, FADH2, NADPH y GTP. Si el orden, la coenzima o el compartimento están mal, la línea se atasca y Mito explica por qué. Niveles:
   - espiral de β-oxidación del palmitato (tiene que dar 106 netos);
   - oleico y linoleico (agregando la isomerasa y la reductasa);
   - cadena impar;
   - peroxisoma;
   - cetogénesis y cetogenólisis;
   - ciclo de la ácido graso sintasa;
   - elongación;
   - síntesis de triglicéridos en sus tres tejidos;
   - cascada del colesterol;
   - cascada de los eicosanoides.
2. Aduana Mitocondrial (estilo Papers, Please): las moléculas llegan en fila con su "pasaporte" y el jugador las acepta, las rechaza o las desvía a la lanzadera correcta. Casos:
   - el acetil-CoA no cruza; el piruvato sí;
   - los ácidos grasos de cadena corta y media pasan por difusión; los de cadena larga, por la carnitina; los de cadena muy larga van al peroxisoma (ALDP);
   - con malonil-CoA alto, la CPT I queda cerrada;
   - el citrato sale por antiporte; el transportador malato/α-cetoglutarato;
   - la acetona sale libre y los otros cuerpos cetónicos usan transportadores;
   - hay dos pools de CoA;
   - el quilomicrón es demasiado grande para el capilar.
3. Sala de Control Hormonal: se da un estado (posprandial, ayuno, ejercicio, DM1 sin insulina, dieta cetogénica, ayuno de X días) y el jugador prende, apaga, fosforila o desfosforila las enzimas: HSL y perilipinas, ATGL, LPL del adiposo y del músculo, CPT I, ACC1 y ACC2, ATP-citrato liasa, ácido graso sintasa, PDH, piruvato carboxilasa, HMG-CoA reductasa y AMPK. Después se simula. Si deja un ciclo fútil, el ATP se evapora en pantalla.
4. Laboratorio de Carbonos:
   - armar y nombrar ácidos grasos (16:0, 18:1Δ9, 18:2Δ9,12, 18:3, 20:4Δ5,8,11,14, 20:5, 22:6);
   - poner dobles enlaces cis o trans, ubicar α, β y ω, y clasificar en ω-3 u ω-6;
   - usar los prefijos eicosa-, docosa-, tetracosa- y hexacosa-;
   - contar carbonos en la elongación y en los isoprenos (5 → 10 → 15 → 30 → 27).
5. Contador de ATP: palmitato 108/106 con la cuenta por enzima, oleico con un FADH2 menos, β-hidroxibutirato 21,5, glucosa frente a palmitato, y el costo de la síntesis (7 ATP + 14 NADPH). Incluye las trampas: 12 frente a 10, y 7 vueltas frente a 8 acetil-CoA.
6. Detector de Mentiras, en el formato del control: verdadero/falso con justificación. Las afirmaciones llegan como sospechosos; el jugador sella VERDADERO o FALSO y, si es falsa, elige o escribe la corrección. Toma afirmaciones de todo el contenido, con prioridad para los "Ojo".
7. Modo Detective: llega un paciente con síntomas y exámenes, y el jugador tiene que encontrar la falla o el fármaco. Casos:
   - deficiencias de CPT I, CACT, CPT II y del transportador de carnitina;
   - MCAD;
   - aciduria metilmalónica y vitamina B12;
   - X-ALD y Zellweger;
   - cetoacidosis diabética;
   - dieta cetogénica;
   - ayuno seguido de ejercicio intenso;
   - aspirina en dosis baja;
   - uso prolongado de AINE (gastritis);
   - asma (leucotrienos);
   - hipercolesterolemia (estatina de noche);
   - onicomicosis (azoles);
   - tumor mamario estrógeno-dependiente (tamoxifeno);
   - inducción de la ovulación (clomifeno);
   - el prematuro y su fórmula.
8. Microjuegos relámpago (estilo WarioWare): 5 segundos cada uno, en rondas de 10.
9. Duelos, a partir de los recuadros "Diferencia" y de los pares que se confunden:
   - β-oxidación frente a síntesis;
   - cetogénesis frente a cetogenólisis;
   - mitocondria frente a peroxisoma;
   - X-ALD frente a Zellweger;
   - ACC1 frente a ACC2;
   - HMG-CoA mitocondrial frente a citosólico;
   - AINEs, coxibs y corticoides;
   - hígado, adipocito y enterocito;
   - grasa blanca frente a grasa parda;
   - tamoxifeno frente a clomifeno;
   - LPL frente a lipasas intracelulares;
   - sintetasa frente a sintasa;
   - cis frente a trans;
   - TXA2 frente a PGI2;
   - COX-1 frente a COX-2.

## 8. Jefes
- El Ayuno de 40 días: las fases I a V, el cuerpo cetónico que más sube y el cambio de combustible del cerebro.
- Cetoacidosis Diabética.
- El Bebé Prematuro: deficiencia de CPT I; hay que armar la fórmula correcta.
- El Muffin: los 11 pasos desde la glucosa hasta el adipocito.
- La Torcedura: PLA2 → araquidonato → COX o LOX; hay que elegir el fármaco correcto para cada caso.
- Hipercolesterolemia: HMG-CoA reductasa, estatinas, LDL y HDL.
- El Aceite de Lorenzo: peroxisoma y X-ALD.
- El Camello: agua metabólica.
- Jefe final, El Señor de las Trampas: todos los "Ojo" de los dos apuntes.

## 9. Colecciones, progresión y repaso
- Enzimodex con todas las enzimas de los dos apuntes. Cada ficha tiene reacción, ubicación, coenzimas, regulación, tejido, enfermedad, fármaco y mnemotecnia. La rareza depende de cuánto importa en el examen: las reguladas y limitantes son legendarias.
- Otras colecciones: Arsenal de fármacos, Bestiario de enfermedades, Grimorio de mnemotecnias, Gemas (Clave) y Pergaminos (Síntesis).
- Progresión: XP, niveles, rangos, estrellas, logros y racha diaria. El progreso se guarda en el navegador y se puede exportar e importar.
- Repaso espaciado automático (Leitner o SM-2) con todo lo que el jugador falló, y una sección "Repaso de hoy" en el menú principal.
- Modo Examen:
  - Control: verdadero/falso con justificación, en el formato del ramo;
  - Solemne: selección múltiple a–d;
  - ambos se generan desde el banco de preguntas y terminan con una pauta razonada.
- Panel de dominio por capítulo y en el mapa.

## 10. Matriz de cobertura (control de que no falte nada)
- COBERTURA.md tiene una fila por cada sección y subsección de los dos apuntes (A 1.1 a A 24, B 1.1 a B 24), por cada tabla, por cada figura y por cada recuadro. Columnas: ítem, capítulo, paso del video, mecánica o nivel, y preguntas (con sus ID). Ninguna fila puede quedar vacía.
- Banco de preguntas: por cada ítem de la matriz, al menos una verdadero/falso con justificación y una de otro formato (selección múltiple, ordenar, arrastrar o completar). También preguntas inversas (dado el efecto, encontrar la causa) y de cálculo donde aplique.
- Los esquemas de los apuntes se redibujan como esquemas o animaciones SVG propias, a partir de su descripción en contenido/. Las 6 fotos de figuras/fotos/ se muestran tal cual, con un botón "ver figura original". Cada figura aparece en su capítulo.

## 11. Tecnología y código preparado para más apuntes
- HTML, CSS y JavaScript, sin frameworks y sin instalar nada, repartidos en varios archivos chicos para poder editar solo lo necesario. Usa scripts clásicos (no módulos ES), para que index.html se abra con doble clic, sin servidor.
- Estructura sugerida: index.html; css/; js/motor/ (navegación, guardado, reproductor de videos, motor de preguntas, repaso, mapa y mecánicas); js/piezas/ (biblioteca SVG); datos/A/ y datos/B/ (un archivo por capítulo); datos/metabolitos.js; herramientas/ (validador y script de unión).
- Biblioteca de piezas SVG reutilizables, animables con parámetros: cadena de carbonos (cualquier largo, dobles enlaces cis o trans en cualquier posición, numeración C1, α, β y ω); CoA y enlace tioéster; enzima-personaje (nombre, color, expresión); coenzimas (ATP, NADH, FADH2, NADPH, GTP); membranas simple y doble; transportadores y lanzaderas; flechas y signos de activación e inhibición; anillos del colesterol; gota de grasa; células y órganos; y Mito.
- Los videos se escriben como datos: una lista de pasos, y cada paso dice qué piezas aparecen, qué se mueve o transforma, qué dice Mito y qué se resalta. Un reproductor genérico los dibuja y los anima.
- Las mecánicas de la sección 7 son motores genéricos, y cada nivel es un archivo de datos chico.
- Las preguntas son datos con id, capítulo, formato, enunciado, respuesta y justificación.
- Un diccionario único de metabolitos con ID compartidos (acetil-CoA, malonil-CoA, citrato, HMG-CoA...), para que un apunte nuevo se conecte solo al mapa unificado.
- El motor genera todo a partir de los datos: menús, videos, niveles, colecciones, mapa y exámenes. Agregar un apunte tiene que ser agregar sus archivos de datos, sin tocar el motor.
- Guardado con versión, para que agregar temas no borre el progreso.
- Validador (en Node o Python, lo que esté instalado, sin dependencias): revisa que cada capítulo tenga todas sus partes, que cada ID exista, que cada pregunta tenga respuesta y justificación, y que COBERTURA.md no tenga filas vacías en lo ya construido.
- Script de unión: junta todo en un solo archivo, HOMEOSTASIS.html, con las fotos incrustadas, para abrirlo en el celular o compartirlo.
- COMO_AGREGAR_APUNTES.md: cómo pasar un apunte nuevo con herramientas/convertir_apunte.py, cómo describir sus figuras y cómo crear sus archivos de datos, con una plantilla vacía y un ejemplo.

## 12. Las 3 etapas
Al terminar cada etapa: corre el validador, revisa que no haya errores de consola, construye HOMEOSTASIS.html, actualiza PROGRESO.md y COBERTURA.md, y detente para que yo limpie la conversación con /clear. La sesión siguiente empieza leyendo CLAUDE.md y PROGRESO.md, no todo el proyecto.

### Etapa 1: "Ya puedo estudiar el Acto I"
- La sección 2 (inventario, análisis de los videos y COBERTURA.md), CLAUDE.md y PROGRESO.md.
- El motor de estudio completo: todas las pestañas y funciones del HTML base, estilo visual, guardado, biblioteca de piezas SVG, reproductor de videos, motor de preguntas (verdadero/falso con justificación, selección múltiple, ordenar, arrastrar y completar), Detector de Mentiras, repaso espaciado y Modo Examen (Control y Solemne).
- El Acto I completo en el Modo Historia (I-1 a I-24): cada capítulo con su video, la práctica dentro del video, los recuadros como objetos del juego, su Modo Exprés y su banco de preguntas. Por ahora, el paso "nivel jugable" es un desafío de preguntas con tiempo y vidas, que hace de mini-jefe.
- El mapa unificado en su primera versión: el tramo del Acto I navegable, con niebla de guerra e interruptor hormonal.
- HOMEOSTASIS.html listo para usar.

### Etapa 2: "Ya puedo estudiar todo"
- El Acto II completo en el Modo Historia (II-1 a II-26), con la misma estructura.
- El mapa unificado completo: los dos actos conectados, las capas, los estados hormonales con las enzimas reguladas y el mapa de calor de dominio.
- La Enzimodex y las demás colecciones (Arsenal, Bestiario, Grimorio, Gemas y Pergaminos), generadas desde los datos.
- HOMEOSTASIS.html actualizado.

### Etapa 3: "El juego completo"
- Las mecánicas de la sección 7 como motores genéricos, con un nivel para cada capítulo, en reemplazo de los desafíos de preguntas provisionales.
- Los mini-jefes y jefes de la sección 8, la progresión (XP, rangos, logros y racha), el sonido y los efectos.
- COMO_AGREGAR_APUNTES.md.
- Verificación final:
  - el validador pasa;
  - no hay errores de consola en tamaño celular ni en tamaño PC;
  - cada video llega al final;
  - cada nivel se puede ganar y perder;
  - cada pestaña del HTML base funciona;
  - todos los números están recalculados;
  - COBERTURA.md no tiene filas vacías.
- Entrega final: HOMEOSTASIS.html, la tabla "pestaña o función original → dónde quedó" y un resumen de lo que quedó pendiente, si algo no se pudo hacer, y por qué.

# Modelo oficial de carrusel · Gol Élite Pro (aprobado 11-oct-2026)

Una imagen por partido. Orden: por hora de inicio. Partidos: los de Over 1.5 de 80 % o más que no hayan empezado (el partido del día va primero si se hace carrusel del día).
Se entrega como PROMPT para el generador de imágenes del equipo (Gemini/ChatGPT), uno completo por partido, en redes/<fecha>/prompts-carrusel.md.

## Reglas
- NUEVO (Marco, 17-oct-2026): cada lámina lleva el recuadro "LA NOTICIA DEL PARTIDO" entre las estadísticas y el pronóstico: un dato llamativo con fuente abierta (racha, expulsión, baja, récord, lo que está en juego). Las noticias del día se guardan en data/<fecha>/noticias.json; `tools/slides.py` arma las láminas listas y `tools/prompts_noticias.py` el resumen y los prompts.
- Etiqueta de categoría bajo el logo: GOL ÉLITE (≥95), GOLES PLATINO (90–94) o GOLES ESTÁNDAR (80–89), con el porcentaje redondeado.
- Orden del contenido: PRIMERO estadísticas clave de los equipos, AL FINAL probabilidad y marcador sugerido.
- Solo datos verificados. Posición, puntos, forma, goleadores o noticias: solo si hay fuente; si no, omitirlos.
- Uniformes: colores reales de la camiseta de la temporada actual, verificados en la web (fuente en el resumen). Sin logos de patrocinadores ni marcas de ropa. Los ESCUDOS de los equipos SÍ van (decisión de Marco, 12-oct-2026: es un canal deportivo y se presenta a los equipos): escudo oficial de cada club junto a su nombre y en la camiseta de cada chica. Si el generador deforma un escudo, se reemplaza pegando el escudo oficial en PNG en edición. Si ambos equipos visten igual, poner el nombre del equipo bajo cada chica.
- Chicas: mujeres jóvenes adultas (~27 años), sonrientes, de medio cuerpo, pose de presentadora deportiva.
- Números con coma decimal. Nunca "apuesta segura" ni promesas de ganancia.

## Prompt (rellenar los campos entre {llaves})
> Póster deportivo vertical 4:5 (1080x1350), estilo infografía premium. Estadio de noche con reflectores verdes, césped brillante y partículas doradas; paleta negro, verde neón y dorado metálico. Arriba, el logo "GOL ÉLITE PRO" (ÉLITE en dorado) con corona. Título dorado: "{LOCAL} vs {VISITANTE}". Subtítulo verde: "{LIGA} · {DÍA DD DE MES} · {HH:MM} HORA ECUADOR". A la izquierda, una mujer joven adulta (~27 años), sonriente, de medio cuerpo, con {UNIFORME LOCAL}; a la derecha, otra con {UNIFORME VISITANTE}. Camisetas con el escudo del club, sin logos de patrocinadores ni marcas de ropa. Junto al título, el escudo oficial de cada equipo, fiel al real, sin deformar.
> En el centro, un panel negro con borde dorado titulado "ESTADÍSTICAS CLAVE", con íconos dorados y estas líneas:
> • {LOCAL} EN CASA: marca {GF/PJ} y recibe {GC/PJ} goles por partido
> • {dato de promedio de goles en sus partidos de casa o de visita, el más llamativo}
> • {VISITANTE} DE VISITA: marca {GF/PJ} y recibe {GC/PJ} goles por partido
> • {posición/puntos/forma/goleadores — solo si están verificados}
> Después, un recuadro destacado con fondo café oscuro, borde dorado brillante y un ícono de periódico, titulado "LA NOTICIA DEL PARTIDO", con un titular corto en mayúsculas ({TITULAR}) y una o dos frases con el dato que llama la atención ({racha, expulsión, baja, récord o lo que está en juego}), y en letra muy pequeña "Fuente: {MEDIO}".
> Al final, un panel destacado más grande titulado "NUESTRO PRONÓSTICO": "PROBABILIDAD OVER 1.5: {xx}%" (número enorme en verde neón), "Over 2.5: {xx}%" (más pequeño) y "MARCADOR SUGERIDO: {m-m}" (grande, en dorado).
> Abajo, un botón dorado "¡SÍGUENOS!" y en letra pequeña "Over 1.5 = 2 goles o más en el partido, sin importar quién gane · +18 · Probabilidades estadísticas, no garantías". Texto en español, legible y sin errores.


## Regla de porcentajes (aprobada por Marco, 12-oct-2026)
- Se usan los términos que conoce el público: "Over 1.5" y "Over 2.5", con UNA sola nota que explique: "Over 1.5 = 2 goles o más en el partido, sin importar quién gane · Over 2.5 = 3 goles o más".
- Porcentajes en número entero redondeado (regla de Marco, 17-oct-2026): ,5 o más sube al entero siguiente y menos de ,5 se queda (94,5 → 95 %; 94,4 → 94 %). La categoría (GOL ÉLITE ≥95, GOLES PLATINO 90–94, GOLES ESTÁNDAR 80–89, GOLES OPTIMISTAS <80) se decide con ese entero.
- En los aciertos: "Dimos Over 1.5 al X % · Hubo N goles".

## Vocabulario de los prompts (acordado con Marco, 12-oct-2026)
- **Recuadro**: cada bloque donde va un partido (borde dorado, escudos, marcador o pronóstico, "Dimos Over 1.5 al X % · Hubo N goles"). Usar siempre "recuadro", nunca "tarjeta".
- **Historia "¡LO VOLVIÓ A ACERTAR!"** (9:16): título, fecha, presentadora profesional a la izquierda y 3 recuadros a la derecha con los mejores aciertos; zona segura libre del 13 % superior e inferior; nota de Over 1.5, +18 y "Probabilidades estadísticas, no garantías" al pie. Siempre con su ANTI-PROMPT.

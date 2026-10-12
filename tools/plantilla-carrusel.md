# Modelo oficial de carrusel · Gol Élite Pro (aprobado 11-oct-2026)

Una imagen por partido. Orden: por hora de inicio. Partidos: los de 80 % o más de probabilidad de 2 goles o más (Over 1.5) que no hayan empezado (el partido del día va primero si se hace carrusel del día).
Se entrega como PROMPT para el generador de imágenes del equipo (Gemini/ChatGPT), uno completo por partido, en redes/<fecha>/prompts-carrusel.md.

## Reglas
- Orden del contenido: PRIMERO estadísticas clave de los equipos, AL FINAL probabilidad y marcador sugerido.
- Solo datos verificados. Posición, puntos, forma, goleadores o noticias: solo si hay fuente; si no, omitirlos.
- Uniformes: colores reales de la camiseta de la temporada actual, verificados en la web (fuente en el resumen). Sin patrocinadores ni escudos dibujados por la IA (círculo vacío para pegar el escudo después). Si ambos equipos visten igual, poner el nombre del equipo bajo cada chica.
- Chicas: mujeres jóvenes adultas (~27 años), sonrientes, de medio cuerpo, pose de presentadora deportiva.
- Números con coma decimal. Nunca "apuesta segura" ni promesas de ganancia.

## Prompt (rellenar los campos entre {llaves})
> Póster deportivo vertical 4:5 (1080x1350), estilo infografía premium. Estadio de noche con reflectores verdes, césped brillante y partículas doradas; paleta negro, verde neón y dorado metálico. Arriba, el logo "GOL ÉLITE PRO" (ÉLITE en dorado) con corona. Título dorado: "{LOCAL} vs {VISITANTE}". Subtítulo verde: "{LIGA} · {DÍA DD DE MES} · {HH:MM} HORA ECUADOR". A la izquierda, una mujer joven adulta (~27 años), sonriente, de medio cuerpo, con {UNIFORME LOCAL}; a la derecha, otra con {UNIFORME VISITANTE}. Sin logos de patrocinadores; un círculo vacío sobre cada una para el escudo.
> En el centro, un panel negro con borde dorado titulado "ESTADÍSTICAS CLAVE", con íconos dorados y estas líneas:
> • {LOCAL} EN CASA: marca {GF/PJ} y recibe {GC/PJ} goles por partido
> • {dato de promedio de goles en sus partidos de casa o de visita, el más llamativo}
> • {VISITANTE} DE VISITA: marca {GF/PJ} y recibe {GC/PJ} goles por partido
> • {posición/puntos/forma/goleadores — solo si están verificados}
> Al final, un panel destacado más grande titulado "NUESTRO PRONÓSTICO": "PROBABILIDAD DE 2 GOLES O MÁS: {xx}%" (número enorme en verde neón), "3 goles o más: {xx}%" (más pequeño) y "MARCADOR SUGERIDO: {m-m}" (grande, en dorado).
> Abajo, un botón dorado "¡SÍGUENOS!" y en letra pequeña "2+ goles = Over 1.5: 2 goles o más en el partido, sin importar quién gane · +18 · Probabilidades estadísticas, no garantías". Texto en español, legible y sin errores.


## Regla de porcentajes (aprobada por Marco, 12-oct-2026)
- Nunca un porcentaje suelto: siempre "X % de probabilidad de 2 goles o más" (Over 1.5) o "de 3 goles o más" (Over 2.5).
- En redes, número entero hacia abajo (89,9 → 89 %), así nunca cruza de categoría; el decimal sellado queda en el portal.
- En los aciertos: "Dijimos X % de 2+ goles · Hubo N goles".
- Siempre la aclaración: "2+ goles = Over 1.5: 2 goles o más en el partido, sin importar quién gane".

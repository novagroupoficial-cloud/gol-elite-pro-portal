# Prompts de carrusel · lunes 26 de octubre de 2026

Modelo oficial: tools/plantilla-carrusel.md (aprobado 11-oct-2026, con el recuadro "LA NOTICIA DEL PARTIDO" del 17-oct). Un prompt por partido de Over 1.5 de 80 % o más (entero redondeado) que no ha empezado al publicar el kit: hoy es **solo 1**, el partido del día (Sevilla–Osasuna, 86,8 % sellado = 87 %). Los otros 9 partidos del día quedan entre 62 % y 78 % (GOLES OPTIMISTAS) y no llevan prompt: preferimos decirlo antes que inflar números. Pronósticos sellados a las 05:41 ECU en data/2026-10-26/pronosticos.json con el modelo Nova Gol 4.1 (primer día de la versión Kaizen). Porcentajes en entero redondeado (,5 o más sube), igual que el portal y las láminas.

Escudos: escudo oficial de cada club junto a su nombre y en la camiseta de cada chica (regla de Marco, 12-oct-2026). Si el generador lo deforma, pegar el PNG oficial en edición.

**Uniformes:** verificados para la temporada 2026-27 en las fuentes citadas al final (sin mencionar marcas en el prompt).

**La noticia del partido:** previa de FútbolFantasy y ficha de Fútbol Total (medios citados al final). No hay noticias inventadas.

## 1. Sevilla vs Osasuna · LaLiga · 15:00 ECU · PARTIDO DEL DÍA

Datos sellados: Over 1.5 86,8 % · Over 2.5 67,4 % · marcador 1-1 · GOLES ESTÁNDAR (87 %). Fecha y hora verificadas: lunes 26 de octubre de 2026, 21:00 en Madrid = 15:00 hora de Ecuador, jornada 10, estadio Ramón Sánchez-Pizjuán (Fútbol Total y FútbolFantasy).

**PROMPT**

> Póster deportivo vertical 4:5 (1080x1350), estilo infografía premium. Estadio de noche con reflectores verdes, césped brillante y partículas doradas; paleta negro, verde neón y dorado metálico. Arriba, el logo "GOL ÉLITE PRO" (ÉLITE en dorado) con corona y debajo la etiqueta "PARTIDO DEL DÍA · GOLES ESTÁNDAR 87 %". Título dorado: "SEVILLA vs OSASUNA". Subtítulo verde: "LALIGA · LUNES 26 DE OCTUBRE · 15:00 HORA ECUADOR". A la izquierda, una mujer joven adulta (~27 años), sonriente, de medio cuerpo, pose de presentadora deportiva, con la camiseta local 2026-27 del Sevilla: blanca, con cuello rojo con ribete dorado y detalles rojos en los hombros, con el escudo del club; a la derecha, otra mujer joven adulta con la camiseta local 2026-27 de Osasuna: rojo intenso con un relieve sutil de mosaico en la tela, cuello y puños azul marino, con el escudo del club. Camisetas con el escudo del club, sin logos de patrocinadores ni marcas de ropa. Junto al título, el escudo oficial de cada equipo, fiel al real, sin deformar.
> En el centro, un panel negro con borde dorado titulado "ESTADÍSTICAS CLAVE", con íconos dorados y estas líneas:
> • SEVILLA EN CASA: marca 1,25 y recibe 1,75 goles por partido (4 partidos)
> • LOS PARTIDOS DE OSASUNA DE VISITA promedian 5,25 goles (21 en 4)
> • OSASUNA DE VISITA: marca 1,50 y recibe 3,75 goles por partido (4 partidos)
> • SEVILLA ES 6.º CON 14 PUNTOS; OSASUNA SUMA 11 (9 PARTIDOS CADA UNO)
> Después, un recuadro destacado con fondo café oscuro, borde dorado brillante y un ícono de periódico, titulado "LA NOTICIA DEL PARTIDO", con un titular corto en mayúsculas ("SEVILLA, 1 PUNTO DE 9; OSASUNA ESTRENA A ARRASATE") y esta frase: "El Sevilla perdió con Barcelona, cayó 4-1 en el Bernabéu y empató 3-3 en Levante; Osasuna ganó 2-0 al Racing en el regreso de Jagoba Arrasate y no tendrá a Aimar Oroz ni a Del Castillo.", y en letra muy pequeña "Fuente: FútbolFantasy · Fútbol Total".
> Al final, un panel destacado más grande titulado "NUESTRO PRONÓSTICO": "PROBABILIDAD OVER 1.5: 87%" (número enorme en verde neón), "Over 2.5: 67%" (más pequeño) y "MARCADOR SUGERIDO: 1-1" (grande, en dorado).
> Abajo, un botón dorado "¡SÍGUENOS!" y en letra pequeña "Over 1.5 = 2 goles o más en el partido, sin importar quién gane · +18 · Probabilidades estadísticas, no garantías". Texto en español, legible y sin errores.

**ANTI-PROMPT: sin logos de patrocinadores en el pecho ni en las mangas, sin marcas de ropa deportiva, sin casas de apuestas; sin escudos deformados, inventados o de otros clubes; sin caras de futbolistas reales; sin poses provocativas; solo mujeres adultas; sin textos "apuesta segura", "dinero fácil", "gana seguro" ni promesas de ganancia; sin texto en inglés, sin letras deformadas ni números distintos a los indicados.**

## Fuentes
- Estadísticas de casa y fuera: `tools/datos.py` (LaLiga 2026-27 partido a partido; control: suma de GF en casa = suma de GC fuera y PJ casa = PJ fuera; bloque DOM25 con los resultados del domingo 25, cada uno con su fuente). Sevilla: 9 PJ, 14 goles a favor y 16 en contra; Osasuna: 9 PJ, 10 a favor y 18 en contra (coincide con la tabla de Fútbol Total).
- Fecha, hora, posiciones y forma: [Fútbol Total · Sevilla vs Osasuna (21:00 Madrid = 15:00 ECU)](https://futboltotal.futbol/partido/sevilla-vs-osasuna-laliga-1570431) · [Fútbol Peruano · programación del lunes 26 (hora de Perú = Ecuador)](https://www.futbolperuano.com/partidos-por-tv/noticias/programacion-de-partidos-por-tv-del-lunes-26-de-octubre-608796)
- Noticia (bajas, racha, debut de Arrasate): [FútbolFantasy · previa del Sevilla - Osasuna](https://www.futbolfantasy.com/laliga/noticias/153274-posibles-alineaciones-y-previa-fantasy-del-sevilla-osasuna)
- Uniformes 2026-27: [Footy Headlines · camiseta local del Sevilla 2026-27](https://www.footyheadlines.com/es/exclusiva-se-ha-producido-una-filtracion-de-la-camiseta-local-del-sevilla-para-la-temporada-2026-2027.html) (filtración; el club aún no la presentó oficialmente según Bet Brothers: si cambia, usar la blanca tradicional) · [Bet Brothers · equipaciones de LaLiga 2026/27 (Osasuna)](https://betbrothers.es/deportes/equipaciones-laliga-2026-2027/)

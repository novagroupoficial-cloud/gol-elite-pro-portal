# Prompts de carrusel · martes 27 de octubre de 2026

Modelo oficial: tools/plantilla-carrusel.md (aprobado 11-oct-2026, con el recuadro "LA NOTICIA DEL PARTIDO" del 17-oct). Un prompt por partido de Over 1.5 de 80 % o más (entero redondeado) que no ha empezado al publicar el kit: hoy es **solo 1**, el partido del día (Torino–Como, 82,7 % sellado = 83 %). Los otros 5 partidos del día quedan entre 69 % y 79 % (GOLES OPTIMISTAS) y no llevan prompt: preferimos decirlo antes que inflar números. Pronósticos sellados a las 05:39 ECU en data/2026-10-27/pronosticos.json con el modelo Nova Gol 4.1. Porcentajes en entero redondeado (,5 o más sube), igual que el portal y las láminas.

Escudos: escudo oficial de cada club junto a su nombre y en la camiseta de cada chica (regla de Marco, 12-oct-2026). Si el generador lo deforma, pegar el PNG oficial en edición.

**Uniformes:** verificados para la temporada 2026-27 en las fuentes citadas al final (sin mencionar marcas en el prompt). Como juega con su camiseta local (azul), que no choca con el granate del Torino.

**La noticia del partido:** ficha de Fútbol Total (forma, tabla y antecedentes). No hay noticias inventadas.

## 1. Torino vs Como · Serie A · 14:45 ECU · PARTIDO DEL DÍA

Datos sellados: Over 1.5 82,7 % · Over 2.5 60,3 % · marcador 1-1 · GOLES ESTÁNDAR (83 %). Fecha y hora verificadas: martes 27 de octubre de 2026, 20:45 en Italia = 14:45 hora de Ecuador, jornada 9, Stadio Olimpico Grande Torino (Fútbol Total, Tuttosport, sport-flash, Líbero y RPP).

**PROMPT**

> Póster deportivo vertical 4:5 (1080x1350), estilo infografía premium. Estadio de noche con reflectores verdes, césped brillante y partículas doradas; paleta negro, verde neón y dorado metálico. Arriba, el logo "GOL ÉLITE PRO" (ÉLITE en dorado) con corona y debajo la etiqueta "PARTIDO DEL DÍA · GOLES ESTÁNDAR 83 %". Título dorado: "TORINO vs COMO". Subtítulo verde: "SERIE A · MARTES 27 DE OCTUBRE · 14:45 HORA ECUADOR". A la izquierda, una mujer joven adulta (~27 años), sonriente, de medio cuerpo, pose de presentadora deportiva, con la camiseta local 2026-27 del Torino: granate con un sutil dibujo geométrico tono sobre tono en la tela, cuello redondo con detalles en granate oscuro y blanco, con el escudo del club; a la derecha, otra mujer joven adulta con la camiseta local 2026-27 del Como: azul real con finas rayas tono sobre tono, cuello tipo polo con ribetes blancos, rojos y dorados, con el escudo del club. Camisetas con el escudo del club, sin logos de patrocinadores ni marcas de ropa. Junto al título, el escudo oficial de cada equipo, fiel al real, sin deformar.
> En el centro, un panel negro con borde dorado titulado "ESTADÍSTICAS CLAVE", con íconos dorados y estas líneas:
> • TORINO EN CASA: marca 1,50 y recibe 1,75 goles por partido (4 partidos)
> • LOS PARTIDOS DEL TORINO EN CASA promedian 3,25 goles (13 en 4)
> • COMO DE VISITA: marca 2,00 y recibe 1,20 goles por partido (5 partidos)
> • COMO ES 5.º CON 17 PUNTOS; TORINO ES 8.º CON 13 (8 PARTIDOS CADA UNO)
> Después, un recuadro destacado con fondo café oscuro, borde dorado brillante y un ícono de periódico, titulado "LA NOTICIA DEL PARTIDO", con un titular corto en mayúsculas ("TORINO, 3 TRIUNFOS SEGUIDOS; COMO LLEGA GOLEANDO") y esta frase: "El Torino ganó sus últimos 3 de liga (2-1 Udinese, 3-0 en Parma, 3-2 Monza); el Como viene de 2-0 al Sassuolo y 4-1 al Manchester United en la Champions, y los dos últimos cruces terminaron 1-5 y 6-0.", y en letra muy pequeña "Fuente: Fútbol Total".
> Al final, un panel destacado más grande titulado "NUESTRO PRONÓSTICO": "PROBABILIDAD OVER 1.5: 83%" (número enorme en verde neón), "Over 2.5: 60%" (más pequeño) y "MARCADOR SUGERIDO: 1-1" (grande, en dorado).
> Abajo, un botón dorado "¡SÍGUENOS!" y en letra pequeña "Over 1.5 = 2 goles o más en el partido, sin importar quién gane · +18 · Probabilidades estadísticas, no garantías". Texto en español, legible y sin errores.

**ANTI-PROMPT: sin logos de patrocinadores en el pecho ni en las mangas, sin marcas de ropa deportiva, sin casas de apuestas; sin escudos deformados, inventados o de otros clubes; sin caras de futbolistas reales; sin poses provocativas; solo mujeres adultas; sin textos "apuesta segura", "dinero fácil", "gana seguro" ni promesas de ganancia; sin texto en inglés, sin letras deformadas ni números distintos a los indicados.**

## Fuentes
- Estadísticas de casa y fuera: `tools/datos.py` (Serie A 2026-27 partido a partido; control: suma de GF en casa = suma de GC fuera y PJ casa = PJ fuera; J8 completa, 80 partidos). Torino: 8 PJ, 13 goles a favor y 11 en contra; Como: 8 PJ, 14 a favor y 7 en contra (coincide con la tabla de Fútbol Total del 26-oct).
- Fecha, hora, posiciones, forma y antecedentes: [Fútbol Total · Torino vs Como (20:45 Italia = 14:45 ECU)](https://futboltotal.futbol/partido/torino-vs-como-serie-a-2026-10-27) · [Tuttosport · probables alineaciones Torino-Como, 9.ª jornada (martes 27, 20:45)](https://www.tuttosport.com/formazione/calcio/serie-a/2026/10/27-2638210/torino-como) · [sport-flash · programa del 27 de octubre](https://www.sport-flash.com/sports/football/it/calendar/2026-10-27) · [Líbero · partidos del martes 27](https://libero.pe/futbol-internacional/2026/10/26/partidos-de-hoy-martes-27-de-octubre-quienes-juegan-liga-1-serie-efl-cup-2512848)
- Uniformes 2026-27: [Tuttosport · presentación de la camiseta local del Torino 2026/27 (granate, homenaje a Superga)](https://www.tuttosport.com/news/calcio/serie-a/torino/2026/07/03-149640742/torino_presentata_la_nuova_maglia_2026_2027_omaggio_a_superga_per_i_120_anni_di_storia) · [Footy Headlines · camiseta local del Como 2026-27 (azul real; filtración de mayo, presentada el 27-jul según el mismo medio)](https://www.footyheadlines.com/it/la-prima-maglia-adidas-del-como-26-27-sarebbe-la-maglia-perfetta-per-l-italia.html). Si el Como saliera con la visitante: base clara con detalles azul oscuro ([Footy Headlines](https://www.footyheadlines.com/it/6482/la-seconda-maglia-del-como-26-27-e-filtrata.html)).

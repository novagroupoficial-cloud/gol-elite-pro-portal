# Prompts de carrusel · lunes 19 de octubre de 2026

Modelo oficial: tools/plantilla-carrusel.md (aprobado 11-oct-2026, con el recuadro "LA NOTICIA DEL PARTIDO" del 17-oct). La regla es un prompt por partido de Over 1.5 de 80 % o más que no ha empezado. **Hoy ningún partido llega a 80 %** (el más alto es Getafe–Rayo con 77,0 %). Lectura tomada: se entrega solo el prompt del partido del día, que abre el carrusel y la historia, con su etiqueta real "GOLES OPTIMISTAS"; no se agregan otros para no presentar como fuertes partidos que no lo son. Pronósticos sellados a las 05:38 ECU en data/2026-10-19/pronosticos.json. Porcentajes en entero redondeado (,5 o más sube), igual que el portal y las láminas.

Escudos: escudo oficial de cada club junto a su nombre y en la camiseta de cada chica (regla de Marco, 12-oct-2026). Si el generador lo deforma, pegar el PNG oficial en edición.

## 1. Getafe vs Rayo Vallecano · LaLiga · 14:00 ECU · PARTIDO DEL DÍA

Datos sellados: Over 1.5 77,0 % · Over 2.5 52,0 % · marcador 1-1 · GOLES OPTIMISTAS (escala en el portal: 77 %). Previa: Fútbol Total (https://futboltotal.futbol/partido/getafe-vs-rayo-vallecano-la-liga-2026-10-19). Fecha verificada: lunes 19 de octubre de 2026, 15:00 de Nueva York = 14:00 de Ecuador.

**PROMPT**

> Póster deportivo vertical 4:5 (1080x1350), estilo infografía premium. Estadio de noche con reflectores verdes, césped brillante y partículas doradas; paleta negro, verde neón y dorado metálico. Arriba, el logo "GOL ÉLITE PRO" (ÉLITE en dorado) con corona y debajo la etiqueta "PARTIDO DEL DÍA · GOLES OPTIMISTAS". Título dorado: "GETAFE vs RAYO VALLECANO". Subtítulo verde: "LALIGA · LUNES 19 DE OCTUBRE · 14:00 HORA ECUADOR". A la izquierda, una mujer joven adulta (~27 años), sonriente, de medio cuerpo, pose de presentadora deportiva, con la camiseta local 2026/27 de Getafe (azul real intenso con detalles en gris carbón oscuro en el cuello en V cruzado, las costuras de los hombros y los puños anchos; sutil patrón de triángulos en relieve), con el escudo del club; a la derecha, otra mujer joven adulta con la camiseta local 2026/27 de Rayo Vallecano (blanca con la franja diagonal roja que cruza el pecho desde el hombro izquierdo hasta la cadera derecha, mangas raglán negras y detalles dorados en cuello y puños), con el escudo del club. Camisetas con el escudo del club, sin logos de patrocinadores ni marcas de ropa. Junto al título, el escudo oficial de cada equipo, fiel al real, sin deformar.
> En el centro, un panel negro con borde dorado titulado "ESTADÍSTICAS CLAVE", con íconos dorados y estas líneas:
> • GETAFE EN CASA: marca 1,00 y recibe 0,50 goles por partido (4 partidos)
> • LOS PARTIDOS DE RAYO VALLECANO DE VISITA promedian 4,25 goles
> • RAYO VALLECANO DE VISITA: marca 1,25 y recibe 3,00 goles por partido (4 partidos)
> • GOLES ESPERADOS DEL PARTIDO: 2,8 (1,87 Getafe + 0,89 Rayo)
> Después, un recuadro destacado con fondo café oscuro, borde dorado brillante y un ícono de periódico, titulado "LA NOTICIA DEL PARTIDO", con un titular corto en mayúsculas ("EL RAYO NO PIERDE CONTRA EL GETAFE") y esta frase: "En los últimos 6 enfrentamientos, el Rayo ganó 3 y hubo 3 empates; el Getafe no ganó ninguno.", y en letra muy pequeña "Fuente: Fútbol Total".
> Al final, un panel destacado más grande titulado "NUESTRO PRONÓSTICO": "PROBABILIDAD OVER 1.5: 77%" (número enorme en verde neón), "Over 2.5: 52%" (más pequeño) y "MARCADOR SUGERIDO: 1-1" (grande, en dorado).
> Abajo, un botón dorado "¡SÍGUENOS!" y en letra pequeña "Over 1.5 = 2 goles o más en el partido, sin importar quién gane · +18 · Probabilidades estadísticas, no garantías". Texto en español, legible y sin errores.

**ANTI-PROMPT: sin logos de patrocinadores (ni el de la camiseta del Rayo), sin marcas de ropa deportiva (ni Joma ni Umbro), sin casas de apuestas; sin escudos deformados, inventados o de otros clubes; sin caras de futbolistas reales; sin poses provocativas; solo mujeres adultas; sin textos "apuesta segura", "dinero fácil", "gana seguro" ni promesas de ganancia; sin texto en inglés, sin letras deformadas ni números distintos a los indicados.**

## Uniformes · fuentes
- Getafe local 2026/27 (azul real con detalles gris carbón, cuello en V cruzado, patrón de triángulos): [Footy Headlines · filtración de las camisetas 26/27 del Getafe](https://www.footyheadlines.com/es/se-ha-producido-una-filtracion-de-las-camisetas-locales-visitantes-y-de-tercera-del-getafe-26-27.html). Es una filtración, no la presentación oficial: confirmar con la foto oficial del club antes de generar ([Joma · kit 2026/27 del Getafe](https://www.joma-sport.com/blog/en/?p=126055)).
- Rayo Vallecano local 2026/27 (blanca con franja diagonal roja, mangas raglán negras, detalles dorados): [Footy Headlines · camiseta local 26/27](https://www.footyheadlines.com/2381634937/rayo-vallecano-26-27-camiseta-local.html). Alternativa si el Rayo juega de visitante con la segunda: roja con el rayo blanco en el pecho y mangas negras ([Footy Headlines · camiseta visitante 26/27](https://www.footyheadlines.com/6136278618/rayo-vallecano-26-27-camiseta-visitante.html)).
- Estadísticas: tabla de local y visitante de LaLiga en tools/datos.py (control GF casa = GC fuera, PJ casa = PJ fuera).

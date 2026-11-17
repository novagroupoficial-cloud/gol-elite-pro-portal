# Prompts de carrusel · martes 17 de noviembre de 2026

**Hoy no hay prompts de partido.** El modelo oficial (`tools/plantilla-carrusel.md`) pide un prompt por cada partido de Over 1.5 de 80 % o más que no haya empezado. Hoy no hay ninguno: es el último día de la fecha FIFA de selecciones (del 9 al 17 de noviembre) y no juega ninguna de las ligas que seguimos. Solo hay Nations League, eliminatorias Sub-21 y amistosos de selecciones, que el modelo Nova Gol no pronostica. No se inventan partidos, estadísticas ni uniformes.

El carrusel de hoy son las 5 láminas PNG ya generadas en esta carpeta: fecha FIFA con la auditoría del domingo, últimos aciertos, nuestros números, auditoría del domingo (Liga 1 de Perú) y cierre. Si el equipo quiere una portada ilustrada para la lámina 1, puede usar este prompt opcional.

## Prompt opcional · portada "¡ACERTAMOS EL DOMINGO!" (4:5)
**PROMPT**
> Póster deportivo vertical 4:5 (1080x1350), estilo infografía premium. Estadio de noche con reflectores verdes, césped brillante y partículas doradas; paleta negro, verde neón y dorado metálico. Arriba, el logo "GOL ÉLITE PRO" (ÉLITE en dorado) con corona. Título dorado: "HOY: FECHA FIFA". Subtítulo verde: "MARTES 17 DE NOVIEMBRE · ASÍ NOS FUE EL DOMINGO". A la izquierda, una presentadora profesional (mujer joven adulta, ~28 años, sonriente, de medio cuerpo, traje sastre negro y blusa verde esmeralda, sin logos).
> En el centro, un recuadro con borde dorado brillante: a la izquierda el escudo oficial de Comerciantes Unidos junto a su nombre y a la derecha el escudo oficial de Sport Boys junto a su nombre (fieles a los reales, sin deformar), el marcador "3-3" grande en dorado y debajo, en verde: "Partido del día · Dimos Over 1.5 al 77 % · Hubo 6 goles ✔". Encima del recuadro, una cinta dorada "¡ACERTAMOS!".
> Debajo, un recuadro más pequeño: escudo oficial de Juan Pablo II junto a su nombre y escudo oficial de Deportivo Garcilaso junto a su nombre, "2-2" en dorado y "Dimos Over 1.5 al 76 % · Hubo 4 goles ✔".
> Después, un panel negro con borde dorado: "DOMINGO 15 · LIGA 1 DE PERÚ: 2 DE 2" y "Nuestros números: Over 1.5 de 90 % o más, 41 de 46".
> Abajo, un botón dorado "MAÑANA VUELVEN LAS LIGAS" y en letra pequeña "Over 1.5 = 2 goles o más en el partido, sin importar quién gane · Over 2.5 = 3 goles o más · +18 · Probabilidades estadísticas, no garantías". Texto en español, legible y sin errores.

**ANTI-PROMPT**
> Sin logos de patrocinadores, marcas de ropa deportiva ni casas de apuestas; sin escudos deformados, inventados o de otros clubes; sin caras de futbolistas reales; sin poses provocativas; sin números distintos a los indicados; sin "apuesta segura", "gana seguro", "dinero fácil" ni promesas de ganancia; sin marcas de agua.

Nota: si el generador deforma los escudos, pegar encima el PNG oficial de cada club.

## Fuentes
- Resultados: [RPP · Comerciantes Unidos 3-3 Sport Boys](https://rpp.pe/futbol/descentralizado/comerciantes-unidos-vs-sport-boys-en-vivo-a-que-hora-juegan-y-donde-ver-fecha-17-torneo-clausura-2026-via-l1max-partidos-de-hoy-noticia-1717814) y [Futbolperuano.com · Juan Pablo II 2-2 Deportivo Garcilaso](https://www.futbolperuano.com/liga-1/noticias/juan-pablo-ii-vs-deportivo-garcilaso-en-vivo-por-el-torneo-clausura-de-la-liga-1-2026-612714).
- Cifras: `public/api/records.json` (recalculado hoy), con la fuente de cada resultado en `data/<fecha>/auditoria.json`.
- Calendario de hoy (sin ligas): [Fútbol Total](https://futboltotal.futbol/2026-11-17) y [Depor](https://depor.com/resultados/2026-11-17/).
- Uniformes: no aplica hoy (el prompt opcional no lleva jugadoras con uniforme).

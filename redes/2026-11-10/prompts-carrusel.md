# Prompts de carrusel · martes 10 de noviembre de 2026

**Hoy no hay prompts de partido.** El modelo oficial (`tools/plantilla-carrusel.md`) pide un prompt por cada partido de Over 1.5 de 80 % o más que no haya empezado. Hoy no hay ninguno: es fecha FIFA de selecciones (del 9 al 17 de noviembre) y las ligas que seguimos no juegan. Solo hay copas (Copa del Rey, Copa Colombia y Copa AUF), la Champions femenina y amistosos de selecciones, y el modelo Nova Gol no los pronostica. No se inventan partidos, estadísticas ni uniformes.

El carrusel de hoy son las 5 láminas PNG ya generadas en esta carpeta (fecha FIFA, mejores aciertos, auditoría del sábado, auditoría del domingo y cierre). Si el equipo quiere una portada ilustrada para la lámina 1, puede usar este prompt opcional. No lleva uniformes de clubes, así que no hace falta verificar camisetas.

## Prompt opcional · portada "FIN DE SEMANA AUDITADO" (4:5)
**PROMPT**
> Póster deportivo vertical 4:5 (1080x1350), estilo infografía premium. Estadio de noche con reflectores verdes, césped brillante y partículas doradas; paleta negro, verde neón y dorado metálico. Arriba, el logo "GOL ÉLITE PRO" (ÉLITE en dorado) con corona. Título dorado: "HOY: FECHA FIFA". Subtítulo verde: "MARTES 10 DE NOVIEMBRE · ASÍ NOS FUE EL FIN DE SEMANA". A la izquierda, una presentadora profesional (mujer joven adulta, ~28 años, sonriente, de medio cuerpo, traje sastre negro y blusa verde esmeralda, sin logos).
> En el centro, un panel negro con borde dorado titulado "AUDITORÍA DEL FIN DE SEMANA", con íconos dorados y estas líneas:
> • 81 partidos auditados, cada uno con su fuente
> • 63 de 81 con 2 goles o más
> • Over 1.5 de 70 % o más: 51 de 67 (76 %)
> • GOLES PLATINO: 4 de 5 · Over 2.5 con señal: 11 de 16
> Después, dos recuadros con borde dorado brillante, uno por partido del día. En cada uno van el escudo oficial de cada club junto a su nombre (fiel al real, sin deformar), el marcador grande en dorado y una línea en verde:
> 1) "SÁBADO 7 · RB LEIPZIG 5-2 AUGSBURG" · "Dimos Over 1.5 al 92 % · Hubo 7 goles ✔"
> 2) "DOMINGO 8 · CAMBUUR 2-5 PSV" · "Dimos Over 1.5 al 93 % · Hubo 7 goles ✔"
> Al final, un panel más pequeño: "TAMBIÉN PUBLICAMOS LOS FALLOS" y "San Diego 0-1 Sporting KC (90 %) · Monza 0-1 Atalanta (87 %)".
> Abajo, un botón dorado "¡SÍGUENOS!" y en letra pequeña "Over 1.5 = 2 goles o más en el partido, sin importar quién gane · Over 2.5 = 3 goles o más · +18 · Probabilidades estadísticas, no garantías". Texto en español, legible y sin errores.

**ANTI-PROMPT**
> Sin logos de patrocinadores, marcas de ropa deportiva ni casas de apuestas; sin escudos deformados, inventados o de otros clubes; sin caras de futbolistas reales; sin poses provocativas; sin números distintos a los indicados; sin "apuesta segura", "gana seguro", "dinero fácil" ni promesas de ganancia; sin marcas de agua.

## Fuentes
- Resultados: `data/2026-11-07/auditoria.json` y `data/2026-11-08/auditoria.json`, con la fuente de cada partido. RB Leipzig 5-2 Augsburg: [Fútbol Total](https://futboltotal.futbol/partido/rb-leipzig-vs-fc-augsburg-bundesliga-2026-11-07). Cambuur 2-5 PSV: [Fútbol Total](https://futboltotal.futbol/partido/cambuur-vs-psv-eindhoven-eredivisie-2026-11-08).
- Calendario de hoy (sin ligas): [TUDN](https://www.tudn.com/futbol/partidos-hoy-martes-10-noviembre-del-2026-copa-del-rey-y-champions-femenina) y [futbolperuano.com](https://www.futbolperuano.com/partidos-por-tv/).
- Uniformes: no aplica hoy (no hay prompts de partido).

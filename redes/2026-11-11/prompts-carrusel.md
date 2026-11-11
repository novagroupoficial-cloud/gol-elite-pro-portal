# Prompts de carrusel · miércoles 11 de noviembre de 2026

**Hoy no hay prompts de partido.** El modelo oficial (`tools/plantilla-carrusel.md`) pide un prompt por cada partido de Over 1.5 de 80 % o más que no haya empezado. Hoy no hay ninguno: sigue la fecha FIFA de selecciones (del 9 al 17 de noviembre) y no juega ninguna de las ligas que seguimos. Solo hay Champions femenina, Serie B de Brasil, Segunda RFEF, Taça Fares Lopes y amistosos de selecciones, que el modelo Nova Gol no pronostica. No se inventan partidos, estadísticas ni uniformes.

El carrusel de hoy son las 5 láminas PNG ya generadas en esta carpeta: fecha FIFA con nuestros números, partidos del día (aciertos y fallos), resultados por categoría, más récords y cierre. Si el equipo quiere una portada ilustrada para la lámina 1, puede usar este prompt opcional. No lleva uniformes, así que no hace falta verificar camisetas.

## Prompt opcional · portada "NUESTROS NÚMEROS" (4:5)
**PROMPT**
> Póster deportivo vertical 4:5 (1080x1350), estilo infografía premium. Estadio de noche con reflectores verdes, césped brillante y partículas doradas; paleta negro, verde neón y dorado metálico. Arriba, el logo "GOL ÉLITE PRO" (ÉLITE en dorado) con corona. Título dorado: "HOY: FECHA FIFA". Subtítulo verde: "MIÉRCOLES 11 DE NOVIEMBRE · NUESTROS NÚMEROS". A la izquierda, una presentadora profesional (mujer joven adulta, ~28 años, sonriente, de medio cuerpo, traje sastre negro y blusa verde esmeralda, sin logos).
> En el centro, un panel negro con borde dorado titulado "22 DÍAS AUDITADOS · 505 PARTIDOS", con íconos dorados y estas líneas:
> • Over 1.5 de 90 % o más: 41 de 46 (89 %)
> • Récord: 17 aciertos seguidos de 90 % o más
> • GOL ÉLITE: 5 de 5 · GOLES PLATINO: 36 de 41
> • Partidos del día: 16 de 20
> Después, un recuadro con borde dorado brillante: escudo oficial de cada club junto a su nombre (fiel al real, sin deformar), "CAMBUUR 2-5 PSV" con el marcador grande en dorado y la línea en verde "Último partido del día · Dimos Over 1.5 al 93 % · Hubo 7 goles ✔".
> Al final, un panel más pequeño: "TAMBIÉN PUBLICAMOS LOS FALLOS" y "Parma 0-0 Udinese (85 %) · Alianza Lima 1-0 Cienciano (81 %)".
> Abajo, un botón dorado "¡SÍGUENOS!" y en letra pequeña "Over 1.5 = 2 goles o más en el partido, sin importar quién gane · Over 2.5 = 3 goles o más · +18 · Probabilidades estadísticas, no garantías". Texto en español, legible y sin errores.

**ANTI-PROMPT**
> Sin logos de patrocinadores, marcas de ropa deportiva ni casas de apuestas; sin escudos deformados, inventados o de otros clubes; sin caras de futbolistas reales; sin poses provocativas; sin números distintos a los indicados; sin "apuesta segura", "gana seguro", "dinero fácil" ni promesas de ganancia; sin marcas de agua.

## Fuentes
- Cifras: `public/api/records.json` (recalculado hoy) con la fuente de cada resultado en `data/<fecha>/auditoria.json`. Cambuur 2-5 PSV: [Fútbol Total](https://futboltotal.futbol/partido/cambuur-vs-psv-eindhoven-eredivisie-2026-11-08).
- Calendario de hoy (sin ligas): [Fútbol Total](https://futboltotal.futbol/2026-11-11) y [O Povo](https://www.opovo.com.br/esportes/futebol/jogos-de-hoje/2026/11/11/jogos-hoje-11-11-26-ao-vivo-de-futebol-onde-assistir-e-horario.html).
- Uniformes: no aplica hoy (no hay prompts de partido).

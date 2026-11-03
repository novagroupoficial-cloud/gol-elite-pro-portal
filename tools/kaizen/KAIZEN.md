# KAIZEN · Mejora continua del modelo GOL ÉLITE PRO

Autorizado por Marco Rivera el 25-oct-2026: "te autorizo desde este momento… debes todo el tiempo hacer una auditoría… un modelo tipo japonés de Kaizen, de mejoras continuas".

## Reglas del ciclo (PDCA)
1. **Planear:** cada mejora es una hipótesis escrita aquí antes de probarla.
2. **Hacer:** se prueba con `python3 tools/kaizen/backtest.py` sobre TODOS los partidos auditados (entradas selladas de `data/<fecha>/pronosticos.json` y resultados de `auditoria.json`).
3. **Verificar:** solo pasa si mejora el Brier de Over 1.5 y de Over 2.5, si se sostiene en las dos mitades de los días y si el remuestreo (bootstrap) da al menos 90 % de probabilidad de mejora real.
4. **Actuar:** se sube la versión (`VERSION` en `tools/nova_gol_4.py`), se anota aquí con fecha y métricas y se avisa a Marco. Rige solo para los pronósticos nuevos.
- **Lo sellado nunca se recalcula ni se cambia.** Cada pronóstico guarda su `modelo_version`.
- **Volver atrás es un cambio de una línea** (`ALFA = 1.0` reproduce exactamente la versión 4.0).
- **Seguimiento diario:** `python3 tools/kaizen/seguimiento.py` (lo corre la rutina diaria tras la auditoría) escribe `tools/kaizen/seguimiento.json`.

### Métricas
- **Brier:** error cuadrático; menor es mejor.
- **Skill:** compara con "decir siempre la media"; mayor que 0 significa que el modelo aporta.
- **AUC:** discriminación; 0,5 es el azar y 1 es perfecto.
- **Metas:** skill mayor que 0 y AUC de Over 1.5 de 0,60 o más.

## Registro

### 25-oct-2026 · Diagnóstico inicial (202 partidos auditados, del 11 al 24 de octubre, versión 4.0)
- **Over 1.5:**
  - acierto 78,7 %, contra un promedio prometido de 76,6 %: bien calibrado en general;
  - Brier 0,1823, skill −0,088 y AUC 0,447: **no discrimina**;
  - decir siempre la media habría acertado igual.
- **Over 2.5:** Brier 0,2557, skill −0,028 y AUC 0,555. Con señal fuerte (75 % o más) se cumplió 8 de 14.
- **Por franja:** 80 a 89 % cumple menos de lo prometido; menos de 70 % cumple más de lo prometido.
- **Hallazgo:** usar **solo la media de goles de la liga** (Brier 0,1708) supera al modelo. Los datos de equipo, con 3 a 15 partidos por condición, meten ruido.

### 25-oct-2026 · Mejora 1 → versión 4.1 (ALFA = 0,5) · APLICADA
- **Hipótesis:** los factores de ataque y defensa son demasiado extremos con muestras chicas. Hay que encogerlos hacia 1 (factor^ALFA).
- **Resultados con ALFA 0,5:**
  - Over 1.5: Brier de 0,1823 a 0,1746 y AUC de 0,447 a 0,473.
  - Over 2.5: Brier de 0,2557 a 0,2475 y skill de −0,028 a +0,005.
  - Mejora en las dos mitades de los días (del 11 al 18 y del 19 al 24).
  - Bootstrap: 99,7 % (Over 1.5) y 98,5 % (Over 2.5) de probabilidad de mejora real.
- **Por qué 0,5 y no 0,3,** aunque 0,3 rinde algo mejor: es un paso prudente, como pide Kaizen. Con 0,3 casi todos los partidos de una liga quedarían iguales. Se revisa con más datos.
- **Efecto esperado:**
  - menos GOL ÉLITE y GOLES PLATINO (en el historial, 90 % o más: 11 partidos con 10 aciertos, contra 21 partidos con 19);
  - porcentajes menos extremos;
  - Over 2.5 fuerte más exigente.
- **Rige** desde los pronósticos del 26-oct-2026. Los del 25-oct ya estaban sellados con la versión 4.0.

## PRIORIDAD KAIZEN (regla de Marco, 1-nov-2026)
El modelo mejora en este orden:
1. **GOL ÉLITE (95 % o más).** Meta: que se cumpla al menos el 95 %. Cada fallo se analiza uno por uno (`por_categoria` → `fallos` en `seguimiento.json`): liga, partidos jugados en la muestra, versión y noticia.
2. **GOLES PLATINO (90 a 94 %).** Meta: al menos el 90 %. Mismo análisis de cada fallo.
3. **GOLES ESTÁNDAR (80 a 89 %).** Recalibrar la franja que promete de más.
4. **GOLES OPTIMISTAS (menos de 80 %).**
Ninguna mejora de una categoría inferior se acepta si empeora una superior.
**Foco (Marco, 2-nov-2026): el análisis y los ajustes se concentran en GOL ÉLITE y GOLES PLATINO, porque son los que el público usa para apostar.**
- Por eso, en cada partido de 90 % o más la rutina registra de forma OBLIGATORIA: bajas confirmadas (sobre todo de atacantes y de arqueros), situación en la tabla y si algún equipo no tiene nada en juego, cuotas Over/Under 2.5 y últimos 5. Si un dato no existe, se anota "sin dato".
- Al comunicar ÉLITE y PLATINO, se publica su cumplimiento real (no solo el prometido) y se mantiene "+18 · probabilidades estadísticas, no garantías".

## Registro de hipótesis por prioridad (desde 1-nov-2026)
- ❌ **DESCARTADA (1-nov):** "PLATINO/ÉLITE falla por muestras cortas (<4 partidos por condición)". Datos: con menos de 4 partidos, 13/15 (87 %); de 4 a 6, 15/16 (94 %); 7 o más, 7/8 (88 %). No hay diferencia: no se aplica.
- 🔬 **EN MEDICIÓN (desde el 1-nov, decisión hacia el 15-nov):** "PLATINO/ÉLITE con bajas de atacantes o con un equipo sin nada en juego baja una categoría". Origen:
  - los 4 fallos de PLATINO terminaron 1-0;
  - Cincinnati 1-0 Philadelphia (Philadelphia sin 4 jugadores, entre ellos atacantes, y ya clasificado);
  - Ajax 1-0 AZ (2.º contra 5.º);
  - indicio de la base histórica: noticias con "bajas", 2/6 en Over 1.5.

  Se mide con las etiquetas de `historial.py` (`bajas` y, desde ahora, `sin_nada_en_juego`). No cambia porcentajes, solo la categoría con que se destaca. Necesita al menos 30 partidos PLATINO/ÉLITE con noticia antes de decidir.

- 🔬 **ABIERTA (3-nov-2026, aprobada por Marco): "modo copas" para Champions League y torneos entre ligas.**
  - **Problema:** el modelo usa la tabla casa/fuera y la media de UNA liga. En Champions se cruzan ligas de nivel distinto. Por eso hoy esos partidos quedan "sin pronóstico" (el 3-nov fueron 9 partidos).
  - **Hipótesis:** si se ajusta el ataque y la defensa de cada equipo por un coeficiente de nivel de su liga (público y verificable: coeficiente UEFA por país) y se usa como base la media de goles de la propia Champions (local/visita), el Over 1.5 y el Over 2.5 de copas quedan calibrados.
  - **Prueba:**
    - todos los partidos de la fase liga 2026-27 ya jugados (jornadas 1 a 3) cuyos dos equipos tengan tabla verificada en `datos.py`;
    - tablas reconstruidas al corte previo de cada partido con el historial de git, para no usar datos del futuro;
    - comparar con la referencia "media de goles de la Champions" por Brier, skill y AUC.
  - **Regla de aceptación:** la del ciclo; además, al menos 40 partidos y que no toque nada de las ligas nacionales. ÉLITE y PLATINO de copas no se publican hasta tener 30 casos auditados.
  - **Mientras tanto:** los partidos de copas siguen "sin pronóstico" y no se inventan números.

## Base estadística propia: semana por semana y mes por mes (pedido de Marco, 25-oct-2026)
- `tools/kaizen/seguimiento.json` guarda, para lo SELLADO:
  - `por_semana` (lunes a domingo) y `por_mes`, con partidos, aciertos de Over 1.5, GOLES PLATINO/GOL ÉLITE, señales de Over 2.5 fuertes y moderadas, goles reales vs esperados, aciertos por liga, Brier, skill y AUC;
  - `comparacion_versiones` (lo sellado con la versión nueva vs lo que habría dado la 4.0 en los mismos partidos);
  - `avisos` (ALERTA KAIZEN y BUENA NOTICIA KAIZEN, también por liga).
- `tools/kaizen/historial_partidos.csv` es la base partido a partido: probabilidad, resultado, goles, noticia y etiquetas, lista de SportyTrader, últimos 5 y cuotas.
- **Cada lunes** la rutina escribe `tools/kaizen/semanas/<año>-S<semana>.md`, el informe de la semana anterior comparado con la previa.
- **El primer día de cada mes** escribe `tools/kaizen/meses/<año>-<mes>.md`.
- **Primer aviso (25-oct):** Alemania se cumple mucho menos de lo prometido (57 % real vs 88 % prometido, 14 partidos). Muestra corta de la Bundesliga; candidata a la próxima mejora.

## Over 2.5: prioridad de Marco (25-oct-2026)
- **Situación:** es el punto más flojo.
  - Con la versión 4.0: AUC 0,555 y skill −0,028. Con señal fuerte se cumplió 8 de 14; el sábado 24, 1 de 5.
  - Con la 4.1, el skill sube a +0,005: apenas aporta.
- **Plan para darle más datos,** en orden de impacto esperado:
  1. **Cuotas de mercado Over/Under 2.5.** Son el mejor predictor conocido y el modelo ya las acepta (`cuota_over25` y `cuota_under25`). Desde el 26-oct la rutina las registra cuando la fuente abierta las muestra.
  2. **Últimos 5 partidos:** forma reciente y goles. Desde el 26-oct se registran.
  3. **xG por equipo** cuando haya una fuente abierta.
  4. **Revisar los umbrales de señal fuerte y moderada** con 300 o más partidos.
- **Seguimiento:** la rutina informa cada día el Brier, skill y AUC de Over 2.5 y cuántas señales fuertes y moderadas se cumplieron en los últimos 7 días, con ALERTA KAIZEN si empeora.

## Próximas mejoras (en cola)
1. **Últimos 5 partidos (fase de medición):** la rutina registra en `data/<fecha>/ultimos5.json` los últimos 5 resultados de cada equipo de los partidos de 80 % o más, con su fuente. Cuando haya 100 o más partidos con ese dato, se prueba en el modelo (`Equipo.u5_gf/u5_gc/u5_pj` ya existe).
2. **Fuente automática:** football-data.org (ya contratada por el Dashboard) para las ligas grandes, para no gastar lecturas web.
3. **Temporada anterior** como base, para equipos con pocos partidos jugados.
4. **Recalibración por franja** (corregir la tendencia a prometer de más entre 80 y 89 %) una vez que haya 300 o más partidos.
5. **Over 2.5:** revisar los umbrales de señal (fuerte 75 % y moderada 65 %) con la versión 4.1.

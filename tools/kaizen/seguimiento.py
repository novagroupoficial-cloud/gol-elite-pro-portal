"""Kaizen · seguimiento diario de lo SELLADO (lo que realmente publicamos). Lo corre la rutina diaria tras la auditoría.
Escribe tools/kaizen/seguimiento.json: métricas totales, últimos 7 días y por día, por versión del modelo.
Uso: python3 tools/kaizen/seguimiento.py"""
import json, os, sys, datetime as dt
AQUI = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, AQUI); sys.path.insert(0, os.path.dirname(AQUI))
import backtest as B
X = B.partidos()
def bloque(xs):
    if len(xs) < 5: return None
    y15 = [x['gl'] + x['gv'] >= 2 for x in xs]; y25 = [x['gl'] + x['gv'] >= 3 for x in xs]
    return dict(over15=B.metricas([x['o15_sellado'] / 100 for x in xs], y15), over25=B.metricas([x['o25_sellado'] / 100 for x in xs], y25))
dias = sorted(set(x['fecha'] for x in X))
out = dict(actualizado=(dt.datetime.now(dt.timezone.utc) - dt.timedelta(hours=5)).strftime('%Y-%m-%d %H:%M ECU'),
           nota='Brier: menor es mejor. skill > 0: aporta frente a decir siempre la media. AUC: 0,5 = azar, 1 = perfecto. Metas Kaizen: skill > 0 y AUC Over 1.5 >= 0,60.',
           total=bloque(X), ultimos_7_dias=bloque([x for x in X if x['fecha'] in dias[-7:]]),
           por_version={}, por_dia={d: bloque([x for x in X if x['fecha'] == d]) for d in dias})
for v in sorted(set(x['p'].get('modelo_version', '4.0') for x in X)):
    out['por_version'][v] = bloque([x for x in X if x['p'].get('modelo_version', '4.0') == v])

# Cortes por SEMANA (lunes a domingo, ISO) y por MES (pedido de Marco, 25-oct-2026): base estadística propia
def semana(f):
    y, w, _ = dt.date.fromisoformat(f).isocalendar(); return f"{y}-S{w:02d}"
def resumen(xs):
    b = bloque(xs)
    if not b: return None
    g = [x['gl'] + x['gv'] for x in xs]
    f25 = [x for x in xs if x['o25_sellado'] >= 74.5]; m25 = [x for x in xs if 64.5 <= x['o25_sellado'] < 74.5]
    hi = [x for x in xs if x['o15_sellado'] >= 89.5]
    b.update(partidos=len(xs), dias=sorted(set(x['fecha'] for x in xs)), aciertos_over15=sum(v >= 2 for v in g), goles_por_partido=round(sum(g) / len(g), 2),
             goles_esperados=round(sum(x['p'].get('goles_esperados') or 0 for x in xs) / len(xs), 2),
             platino_o_elite=f"{sum(x['gl'] + x['gv'] >= 2 for x in hi)}/{len(hi)}",
             over25_fuerte=f"{sum(x['gl'] + x['gv'] >= 3 for x in f25)}/{len(f25)}", over25_moderada=f"{sum(x['gl'] + x['gv'] >= 3 for x in m25)}/{len(m25)}",
             por_liga={l: f"{sum(x['gl'] + x['gv'] >= 2 for x in xs if x['liga'] == l)}/{sum(1 for x in xs if x['liga'] == l)}" for l in sorted(set(x['liga'] for x in xs))})
    return b
out['por_semana'] = {w: resumen([x for x in X if semana(x['fecha']) == w]) for w in sorted(set(semana(x['fecha']) for x in X))}
out['por_mes'] = {m: resumen([x for x in X if x['fecha'][:7] == m]) for m in sorted(set(x['fecha'][:7] for x in X))}

# Avisos Kaizen: alertas (empeora) y buenas noticias (mejora), sobre los últimos 7 días con partidos
avisos = []
u = out['ultimos_7_dias']
if u:
    for m, nom in (('over15', 'Over 1.5'), ('over25', 'Over 2.5')):
        if u[m]['skill'] < -0.10: avisos.append(f"ALERTA KAIZEN: {nom} no aporta en los últimos 7 días (skill {u[m]['skill']:+})")
        if u[m]['auc'] < 0.40: avisos.append(f"ALERTA KAIZEN: {nom} no distingue en los últimos 7 días (AUC {u[m]['auc']})")
        if u[m]['skill'] > 0: avisos.append(f"BUENA NOTICIA KAIZEN: {nom} ya aporta en los últimos 7 días (skill {u[m]['skill']:+})")
        if u[m]['auc'] >= 0.60: avisos.append(f"BUENA NOTICIA KAIZEN: {nom} alcanzó la meta de discriminación (AUC {u[m]['auc']})")
# Comparación de versiones sobre los MISMOS partidos de la versión nueva (lo sellado con 4.1 vs lo que habría dado 4.0)
import nova_gol_4 as M
nuevos = [x for x in X if x['p'].get('modelo_version', '4.0') != '4.0']
if len(nuevos) >= 20:
    a0 = M.ALFA; M.ALFA = 1.0
    try: viejo = [B.produccion(x['p']) for x in nuevos]
    finally: M.ALFA = a0
    y15 = [x['gl'] + x['gv'] >= 2 for x in nuevos]; y25 = [x['gl'] + x['gv'] >= 3 for x in nuevos]
    comp = dict(partidos=len(nuevos),
                sellado=dict(over15=B.metricas([x['o15_sellado'] / 100 for x in nuevos], y15), over25=B.metricas([x['o25_sellado'] / 100 for x in nuevos], y25)),
                version_4_0=dict(over15=B.metricas([v[0] for v in viejo], y15), over25=B.metricas([v[1] for v in viejo], y25)))
    out['comparacion_versiones'] = comp
    for m, nom in (('over15', 'Over 1.5'), ('over25', 'Over 2.5')):
        if comp['sellado'][m]['brier'] < comp['version_4_0'][m]['brier']:
            avisos.append(f"BUENA NOTICIA KAIZEN: la versión nueva supera a la 4.0 en {nom} en {len(nuevos)} partidos reales (Brier {comp['sellado'][m]['brier']} vs {comp['version_4_0'][m]['brier']})")
        else:
            avisos.append(f"ALERTA KAIZEN: la versión nueva NO supera a la 4.0 en {nom} en {len(nuevos)} partidos reales (Brier {comp['sellado'][m]['brier']} vs {comp['version_4_0'][m]['brier']})")
# Ligas que se apartan del resto (últimos 7 días, mínimo 6 partidos): aciertos Over 1.5 muy por debajo o por encima de lo prometido
ul = [x for x in X if x['fecha'] in dias[-7:]]
for l in sorted(set(x['liga'] for x in ul)):
    xs = [x for x in ul if x['liga'] == l]
    if len(xs) >= 6:
        real = 100 * sum(x['gl'] + x['gv'] >= 2 for x in xs) / len(xs); prom = sum(x['o15_sellado'] for x in xs) / len(xs)
        if real < prom - 20: avisos.append(f"ALERTA KAIZEN: {l} se cumple mucho menos de lo prometido ({real:.0f} % real vs {prom:.0f} % prometido, {len(xs)} partidos)")
        elif real > prom + 15: avisos.append(f"BUENA NOTICIA KAIZEN: {l} se cumple más de lo prometido ({real:.0f} % real vs {prom:.0f} % prometido, {len(xs)} partidos)")
out['avisos'] = avisos
json.dump(out, open(os.path.join(AQUI, 'seguimiento.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for a in out['avisos']: print(a)
t = out['total']['over15']; print(f"Kaizen: {t['n']} partidos · Over 1.5 Brier {t['brier']} · skill {t['skill']:+} · AUC {t['auc']} · versiones {list(out['por_version'])}")

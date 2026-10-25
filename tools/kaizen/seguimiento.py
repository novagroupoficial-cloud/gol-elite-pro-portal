"""Kaizen · seguimiento diario de lo SELLADO (lo que realmente publicamos). Lo corre la rutina diaria tras la auditoría.
Escribe tools/kaizen/seguimiento.json: métricas totales, últimos 7 días y por día, por versión del modelo.
Uso: python3 tools/kaizen/seguimiento.py"""
import json, os, sys, datetime as dt
AQUI = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, AQUI)
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
json.dump(out, open(os.path.join(AQUI, 'seguimiento.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
t = out['total']['over15']; print(f"Kaizen: {t['n']} partidos · Over 1.5 Brier {t['brier']} · skill {t['skill']:+} · AUC {t['auc']} · versiones {list(out['por_version'])}")

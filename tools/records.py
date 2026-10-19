"""Récords de aciertos de GOL ÉLITE PRO (Marco, 19-oct-2026).
Uso: python3 tools/records.py   -> public/api/records.json (lo muestra portal.py en "Nuestros récords")
Junta todos los días auditados con datos partido a partido (data/<fecha>/auditoria.json 'resultados', o
pronosticos.json + resultados-en-vivo.json) y los recalcula con la escala actual (porcentaje redondeado, ,5 sube).
Nunca cambia lo sellado: solo cuenta."""
import json, os, glob, datetime as dt
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from nova_gol_4 import entero, categoria_o15
DIAS = {}
for d in sorted(glob.glob('../data/2026-*')):
    f = os.path.basename(d); filas = []
    a = f'{d}/auditoria.json'
    if os.path.exists(a):
        au = json.load(open(a, encoding='utf-8'))
        for r in au.get('resultados', []):
            if r.get('estado') == 'terminado' and r.get('resultado') and r.get('over15') is not None:
                filas.append(dict(hora=r.get('hora',''), local=r['local'], visita=r['visita'], over15=r['over15'], over25=r.get('over25'), resultado=r['resultado']))
        fecha = au.get('fecha', f)
    else:
        fecha = f
    if not filas and os.path.exists(f'{d}/pronosticos.json') and os.path.exists(f'{d}/resultados-en-vivo.json'):
        P = {(p['local'], p['visita']): p for p in json.load(open(f'{d}/pronosticos.json', encoding='utf-8')) if not p.get('sin')}
        for r in json.load(open(f'{d}/resultados-en-vivo.json', encoding='utf-8')):
            p = P.get((r['local'], r['visita']))
            if p and r.get('estado') == 'terminado' and r.get('resultado'):
                filas.append(dict(hora=p.get('hora',''), local=r['local'], visita=r['visita'], over15=p['over15'], over25=p.get('over25'), resultado=r['resultado']))
    if filas:
        for x in filas: x['goles'] = sum(int(g) for g in x['resultado'].split('-'))
        DIAS[fecha] = filas
CATS = ['GOL ÉLITE', 'GOLES PLATINO', 'GOLES ESTÁNDAR', 'GOLES OPTIMISTAS']
cat = {c: [0, 0] for c in CATS}; o25 = [0, 0]; top90 = [0, 0]; top80 = [0, 0]
mejor_dia = None; goleada = None; racha = 0; racha_max = 0
for fecha in sorted(DIAS):
    a80 = [0, 0]
    for x in sorted(DIAS[fecha], key=lambda x: (x['hora'], x['local'])):
        c = categoria_o15(x['over15']); ok = x['goles'] >= 2
        cat[c][1] += 1; cat[c][0] += ok
        if x.get('over25') is not None and entero(x['over25']) >= 65: o25[1] += 1; o25[0] += x['goles'] >= 3
        if entero(x['over15']) >= 90:
            top90[1] += 1; top90[0] += ok
            racha = racha + 1 if ok else 0; racha_max = max(racha_max, racha)
        if entero(x['over15']) >= 80:
            top80[1] += 1; top80[0] += ok; a80[1] += 1; a80[0] += ok
            if ok and (goleada is None or x['goles'] > goleada['goles']):
                goleada = dict(fecha=fecha, partido=f"{x['local']} {x['resultado']} {x['visita']}", goles=x['goles'], over15=entero(x['over15']))
    if a80[1] >= 5 and (mejor_dia is None or a80[0] / a80[1] > mejor_dia['pct']):
        mejor_dia = dict(fecha=fecha, aciertos=a80[0], partidos=a80[1], pct=round(a80[0] / a80[1], 3))
pdd = []
for fecha in sorted(DIAS):
    a = f'../data/{fecha}/auditoria.json'
    for cand in [a] + glob.glob('../data/*/auditoria.json'):
        if os.path.exists(cand):
            au = json.load(open(cand, encoding='utf-8'))
            if au.get('fecha') == fecha and au.get('partido_del_dia'):
                pdd.append(dict(fecha=fecha, **{k: au['partido_del_dia'].get(k) for k in ('partido', 'resultado', 'goles', 'acierto', 'over15')})); break
pdd_ok = sum(1 for p in pdd if p.get('acierto'))
racha_pdd = 0
for p in reversed(pdd):
    if p.get('acierto'): racha_pdd += 1
    else: break
out = dict(actualizado=(dt.datetime.now(dt.timezone.utc) - dt.timedelta(hours=5)).strftime('%Y-%m-%d %H:%M ECU'),
           dias=sorted(DIAS), partidos=sum(len(v) for v in DIAS.values()),
           nota='Recalculado con la escala actual (porcentaje redondeado: ,5 sube). Over 1.5 = 2 goles o más.',
           categorias={c: dict(aciertos=v[0], partidos=v[1]) for c, v in cat.items()},
           over90=dict(aciertos=top90[0], partidos=top90[1], racha_actual=racha, racha_max=racha_max),
           over80=dict(aciertos=top80[0], partidos=top80[1]), over25_senal=dict(aciertos=o25[0], partidos=o25[1]),
           partido_del_dia=dict(aciertos=pdd_ok, dias=len(pdd), racha_actual=racha_pdd, detalle=pdd),
           mejor_dia_80=mejor_dia, mayor_goleada_acertada=goleada)
json.dump(out, open('../public/api/records.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps({k: out[k] for k in ('dias', 'partidos', 'categorias', 'over90', 'over80', 'over25_senal', 'mejor_dia_80', 'mayor_goleada_acertada')}, ensure_ascii=False))
print('pdd', pdd_ok, len(pdd), racha_pdd)

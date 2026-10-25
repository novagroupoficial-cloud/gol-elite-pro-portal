"""Kaizen · BASE HISTÓRICA de GOL ÉLITE PRO (pedido de Marco, 25-oct-2026).
Junta TODOS los partidos pronosticados: probabilidad sellada vs resultado real, goles, noticia del partido,
si estaba en la lista de SportyTrader, últimos 5 y cuotas (cuando existan). Se regenera completa cada día.
Uso: python3 tools/kaizen/historial.py  ->  tools/kaizen/historial_partidos.csv (Excel, ';') y .json
También etiqueta cada noticia (bajas, racha mala/buena, defensa débil, descenso, goleada reciente…) para
medir si las noticias anticipan el resultado: tools/kaizen/analisis_noticias.json."""
import json, glob, os, csv, math, re
AQUI = os.path.dirname(os.path.abspath(__file__)); RAIZ = os.path.dirname(os.path.dirname(AQUI))
ent = lambda p: int(math.floor(round(p, 1) + 0.5 + 1e-9))
cat = lambda n: 'GOL ÉLITE' if n >= 95 else 'GOLES PLATINO' if n >= 90 else 'GOLES ESTÁNDAR' if n >= 80 else 'GOLES OPTIMISTAS'
ETQ = {  # etiqueta: palabras clave (en minúsculas) que aparecen en la noticia
 'bajas': r'baja|lesion|suspend|no viaja|fuera por|sin su|descartad|deja fuera|ausencia',
 'regreso_figura': r'vuelve|regresa|recupera',
 'racha_mala': r'derrotas? (seguidas|en sus)|sin ganar|crisis|mala racha|no gana|perdió \d de',
 'racha_buena': r'victorias? seguidas|invicto|racha de victorias|ganó \d de|llega goleando',
 'defensa_debil': r'recibe|recibió|en contra|goles en contra|defensa',
 'goleada_reciente': r'\d-[5-9]|[5-9]-\d|golea',
 'descenso': r'descenso|\búltimo\b|\búltima\b|penúltimo|colista',
 'muchos_goles_h2h': r'duelos con muchos goles|últimos \d (duelos|enfrentamientos)|terminaron \d-\d',
 'muestra_corta': r'muestra corta|pocos datos|solo \d partidos',
}
filas = []
for d in sorted(glob.glob(os.path.join(RAIZ, 'data', '2026-*'))):
    f = os.path.basename(d); pf = os.path.join(d, 'pronosticos.json')
    if not os.path.exists(pf): continue
    P = [p for p in json.load(open(pf, encoding='utf-8')) if not p.get('sin')]
    A = {}
    if os.path.exists(os.path.join(d, 'auditoria.json')):
        A = {(r['local'], r['visita']): r for r in json.load(open(os.path.join(d, 'auditoria.json'), encoding='utf-8')).get('resultados', [])}
    N = json.load(open(os.path.join(d, 'noticias.json'), encoding='utf-8')).get('partidos', {}) if os.path.exists(os.path.join(d, 'noticias.json')) else {}
    ST = set()
    if os.path.exists(os.path.join(d, 'sportytrader.json')):
        ST = {k for k in json.load(open(os.path.join(d, 'sportytrader.json'), encoding='utf-8')).get('partidos', [])}
    U5 = json.load(open(os.path.join(d, 'ultimos5.json'), encoding='utf-8')) if os.path.exists(os.path.join(d, 'ultimos5.json')) else {}
    for p in P:
        k = f"{p['local']}|{p['visita']}"; a = A.get((p['local'], p['visita']), {}); n = N.get(k, {})
        res = a.get('resultado') if a.get('estado') == 'terminado' else None
        g = sum(int(x) for x in res.split('-')) if res else None
        txt = (n.get('titular', '') + ' ' + n.get('texto', '')).lower()
        u = U5.get(k, {}) if isinstance(U5, dict) else {}
        filas.append(dict(fecha=f, hora=p.get('hora'), liga=p['liga'], local=p['local'], visita=p['visita'],
            version=p.get('modelo_version', '4.0'), over15=p['over15'], over15_entero=ent(p['over15']), categoria=cat(ent(p['over15'])),
            over25=p['over25'], marcador_estimado=p.get('marcador'), goles_esperados=p.get('goles_esperados'),
            pj_local_casa=(p.get('casa') or [None])[0], pj_visita_fuera=(p.get('fuera') or [None])[0],
            estado=a.get('estado', 'sin auditar'), resultado=res, goles=g,
            acierto_over15=(g >= 2) if g is not None else None, acierto_over25=(g >= 3) if g is not None else None,
            marcador_exacto=(res == p.get('marcador')) if res else None,
            en_sportytrader=(k in ST) if ST else None,
            noticia_titular=n.get('titular'), noticia=n.get('texto'), noticia_fuente=n.get('url'),
            etiquetas=','.join(e for e, rx in ETQ.items() if n and re.search(rx, txt)),
            cuota_over25=u.get('cuota_over25'), cuota_under25=u.get('cuota_under25'), fuente_resultado=a.get('fuente')))
json.dump(filas, open(os.path.join(AQUI, 'historial_partidos.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
with open(os.path.join(AQUI, 'historial_partidos.csv'), 'w', encoding='utf-8-sig', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=list(filas[0]), delimiter=';'); w.writeheader(); w.writerows(filas)
# Análisis de noticias: ¿los partidos con cada etiqueta superan o no lo que prometimos?
T = [x for x in filas if x['goles'] is not None]
an = {}
for e in list(ETQ) + ['(con noticia)', '(sin noticia)']:
    if e == '(con noticia)': s = [x for x in T if x['noticia']]
    elif e == '(sin noticia)': s = [x for x in T if not x['noticia']]
    else: s = [x for x in T if e in (x['etiquetas'] or '').split(',')]
    if s:
        an[e] = dict(partidos=len(s), over15_real=round(100 * sum(x['acierto_over15'] for x in s) / len(s), 1),
                     over15_prometido=round(sum(x['over15'] for x in s) / len(s), 1),
                     over25_real=round(100 * sum(x['acierto_over25'] for x in s) / len(s), 1),
                     over25_prometido=round(sum(x['over25'] for x in s) / len(s), 1),
                     goles_reales=round(sum(x['goles'] for x in s) / len(s), 2),
                     goles_esperados=round(sum(x['goles_esperados'] or 0 for x in s) / len(s), 2))
json.dump(dict(nota='Con menos de 30 partidos por etiqueta es solo indicio, no conclusión.', etiquetas=an),
          open(os.path.join(AQUI, 'analisis_noticias.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f"Base histórica: {len(filas)} pronósticos · {len(T)} con resultado · {sum(1 for x in filas if x['noticia'])} con noticia")
for e, v in an.items(): print(f"  {e:18s} n={v['partidos']:3d} · Over 1.5 real {v['over15_real']} vs prometido {v['over15_prometido']} · Over 2.5 real {v['over25_real']} vs {v['over25_prometido']} · goles {v['goles_reales']} vs {v['goles_esperados']}")

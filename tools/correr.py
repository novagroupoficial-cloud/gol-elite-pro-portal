import json,sys
from nova_gol_4 import Equipo, pronostico
from datos import L
P=[ # hora (Ecuador), liga, local, visita — viernes 23-oct-2026 (rutina recuperada 16:1x ECU; calendario: RPP (hora Perú = Ecuador), TUDN (Liga MX, hora centro de México +1 h), Valor Final (Brasileirão, Brasília -2 h); SportyTrader no accesible en esta ejecución). Solo partidos que aún no empiezan.
 ('16:30', 'ARG', 'Gimnasia Mendoza', 'Platense'),
 ('18:00', 'BRA', 'Cruzeiro', 'Remo'),
 ('19:15', 'ARG', 'Tigre', 'Atletico Tucuman'),
 ('20:00', 'MEX', 'Necaxa', 'Juarez'),
 ('22:00', 'MEX', 'Atlante', 'A. San Luis'),
]
out=[]
for h,lg,a,b in P:
    d=L.get(lg)
    if not d or a not in d['casa'] or b not in d['fuera']:
        out.append(dict(hora=h,liga=lg,local=a,visita=b,sin=True)); continue
    ca,fu=d['casa'][a],d['fuera'][b]
    r=pronostico(d['HG'],d['AG'],Equipo(*ca),Equipo(*fu))
    out.append(dict(hora=h,liga=lg,local=a,visita=b,casa=ca,fuera=fu,HG=round(d['HG'],2),AG=round(d['AG'],2),**r))
    print(f"{h} {lg} {a} {ca} – {b} {fu}: O1.5 {r['over15']} O2.5 {r['over25']} {r['marcador']} xG {r['goles_esperados']} {r['categoria']}")
json.dump(out,open('pron.json','w'),ensure_ascii=False,indent=1)

import json,sys
from nova_gol_4 import Equipo, pronostico
from datos import L
P=[ # hora (Ecuador), liga, local, visita — domingo 15-nov-2026 (rutina diaria 05:2x ECU): fecha FIFA; solo la Liga 1 de Perú (fecha 17 del Clausura, última; programación definitiva Bolavip/futbolperuano, Perú = hora de Ecuador). Sin partidos hoy de COL (cuadrangulares por sortear), BRA (paro FIFA), MEX (vuelve el 20-nov), ARG (octavos desde el 20-nov), CHI (28-nov), ECU (fecha 7 desde el 20-nov), MLS ni Europa. Uruguay (Danubio–Liverpool, Defensor–Peñarol): sin tabla casa/fuera verificable. SportyTrader no accesible.
 ('13:00','PER','Comerciantes Unidos','Sport Boys'),
 ('15:15','PER','Juan Pablo II','Deportivo Garcilaso'),
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

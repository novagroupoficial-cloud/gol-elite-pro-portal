import json,sys
from nova_gol_4 import Equipo, pronostico
from datos import L
P=[ # hora (Ecuador), liga, local, visita — miércoles 11-nov-2026 (rutina diaria 05:2x ECU): fecha FIFA de selecciones (9–17 nov). Sin partidos de las ligas del portal (revisado: Fútbol Total, O Povo, Minuto60/Liga BetPlay desde el 12-nov, Primicias/LigaPro; SportyTrader no accesible). Solo Champions femenina, Serie B Brasil, Segunda RFEF, Taça Fares Lopes y amistosos: sin pronóstico.
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

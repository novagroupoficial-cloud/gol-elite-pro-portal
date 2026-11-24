import json,sys
from nova_gol_4 import Equipo, pronostico
from datos import L
P=[ # hora (Ecuador), liga, local, visita — martes 24-nov-2026 (rutina diaria 05:2x ECU). Calendario: valorfinal.com.br/brasileirao/2026/rodada-37 + CBF (18:00 BRT −2 h), publimetro.co/vanguardia (cuadrangulares fecha 2, hora COL = ECU), mlssoccer.com (22:00 ET = ECU). SportyTrader no accesible desde la rutina. Hoy no hay ligas europeas (jornada de Champions).
 ('16:00','BRA','Chapecoense','Palmeiras'),
 ('18:20','COL','Millonarios','Bucaramanga'),
 ('20:30','COL','América de Cali','Deportivo Cali'),
 ('22:00','USA','San Jose Earthquakes','Houston Dynamo'),
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

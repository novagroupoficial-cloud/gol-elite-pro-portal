import json,sys
from nova_gol_4 import Equipo, pronostico
from datos import L
P=[ # hora (Ecuador), liga, local, visita — miércoles 25-nov-2026 (rutina diaria 05:2x ECU). Calendario: rpp.pe + libero.pe + alairelibre.cl + elliberal.com.ar (agendas del 25-nov), publimetro.co (cuadrangulares fecha 2), lance.com.br + otempo.com.br (Atlético-MG–Corinthians, cierre de la 36ª, 20h BRT). SportyTrader no accesible desde la rutina. Hoy no hay ligas europeas (jornada de Champions) ni MLS (Game 2 el 27/28-nov).
 ('18:00','BRA','Atletico MG','Corinthians'),
 ('18:20','COL','Santa Fe','Once Caldas'),
 ('19:00','ARG','Boca Juniors','Independiente Rivadavia'),
 ('19:00','ECU','Barcelona SC','Independiente del Valle'),
 ('20:00','MEX','Toluca','Atlas'),
 ('20:30','COL','Atlético Nacional','Independiente Medellín'),
 ('22:10','MEX','Monterrey','América'),
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

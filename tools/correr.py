import json,sys
from nova_gol_4 import Equipo, pronostico
from datos import L
P=[ # hora (Ecuador), liga, local, visita — martes 27-oct-2026 (rutina diaria 05:2x ECU). Calendario: libero.pe y rpp.pe (agenda del martes 27, hora de Perú = Ecuador); Serie A cotejada con sport-flash.com (18:30 y 20:45 hora de Italia, UTC+1 tras el cambio de hora del 25-oct = 12:30 y 14:45 ECU). SportyTrader no accesible en esta ejecución. Perú (Juan Pablo II–Sport Huancayo, 15:00) sin pronóstico: tabla sin actualizar desde el 17-oct.
 ('12:30','ITA','Sassuolo','Lazio'),
 ('14:45','ITA','Roma','Cagliari'),
 ('14:45','ITA','Torino','Como'),
 ('17:00','ARG','Argentinos Juniors','Independiente Rivadavia'),
 ('18:00','COL','Cúcuta','Águilas Doradas'),
 ('20:05','COL','Boyacá Chicó','Junior'),
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

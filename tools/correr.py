import json,sys
from nova_gol_4 import Equipo, pronostico
from datos import L
P=[ # hora (Ecuador), liga, local, visita — sábado 14-nov-2026 (rutina diaria 05:2x ECU): fecha FIFA; solo la Liga BetPlay (fecha 19, 7 partidos simultáneos 15:30 COL = 15:30 ECU; programación Publimetro/Dimayor). Sin partidos hoy de BRA (paro FIFA), MEX (vuelve el 20-nov), ARG (octavos desde el 20-nov), PER (desde el 15-nov), CHI (fecha 29 el 28-nov), ECU (fecha 7 desde el 20-nov), MLS ni Europa. SportyTrader no accesible.
 ('15:30','COL','Millonarios','Alianza (ex Alianza Petrolera)'),
 ('15:30','COL','Deportivo Pereira','América de Cali'),
 ('15:30','COL','Cúcuta','Jaguares de Córdoba'),
 ('15:30','COL','Deportivo Cali','Tolima'),
 ('15:30','COL','Atlético Nacional','Once Caldas'),
 ('15:30','COL','Águilas Doradas','Independiente Medellín'),
 ('15:30','COL','Bucaramanga','Fortaleza'),
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

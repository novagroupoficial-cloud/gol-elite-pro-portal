import json,sys
from nova_gol_4 import Equipo, pronostico
from datos import L
P=[ # hora (Ecuador), liga, local, visita — miércoles 21-oct-2026 (calendario: RPP, Bolavip (Liga MX, hora centro de México +1 h), Fútbol Total (MLS, Levante–Athletic), El Gol Digital; SportyTrader no accesible en esta ejecución)
 ('13:00', 'ESP', 'Levante', 'Athletic Club'),
 ('18:00', 'USA', 'Cincinnati', 'DC United'),
 ('18:15', 'COL', 'Llaneros', 'Deportivo Cali'),
 ('20:00', 'MEX', 'Toluca', 'Tijuana'),
 ('20:00', 'MEX', 'Atlas', 'America'),
 ('20:00', 'MEX', 'Puebla', 'Monterrey'),
 ('20:20', 'COL', 'Santa Fe', 'Jaguares de Córdoba'),
 ('22:00', 'MEX', 'Pachuca', 'Cruz Azul'),
 ('22:10', 'MEX', 'Santos Laguna', 'Pumas UNAM'),
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

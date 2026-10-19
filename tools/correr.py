import json,sys
from nova_gol_4 import Equipo, pronostico
from datos import L
P=[ # hora (Ecuador), liga, local, visita — lunes 19-oct-2026 (calendario: Líbero y RPP, hora de Perú = Ecuador; SportyTrader no accesible en esta ejecución)
 ('11:30', 'ITA', 'Monza', 'Cagliari'),
 ('13:45', 'ITA', 'Parma', 'Torino'),
 ('14:00', 'ENG', 'Tottenham Hotspur', 'Coventry City'),
 ('14:00', 'ESP', 'Getafe', 'Rayo Vallecano'),
 ('15:30', 'ECU', 'Mushuc Runa', 'Orense'),
 ('17:00', 'ARG', 'Newells Old Boys', 'Central Cordoba SdE'),
 ('17:00', 'ARG', 'Sarmiento', 'Barracas Central'),
 ('18:00', 'BRA', 'Corinthians', 'Vitória'),
 ('19:15', 'ARG', 'Deportivo Riestra', 'Union Santa Fe'),
 ('20:05', 'COL', 'Pasto', 'Alianza (ex Alianza Petrolera)'),
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

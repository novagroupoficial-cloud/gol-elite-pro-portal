import json,sys
from nova_gol_4 import Equipo, pronostico
from datos import L
P=[ # hora (Ecuador), liga, local, visita — lunes 12-oct-2026
 ('14:00','ENG','Coventry','Newcastle'),
 ('14:00','ESP','Levante','Sevilla'),
 ('14:00','BRA','Coritiba','Botafogo'),
 ('14:00','ARG','Lanus','Velez Sarsfield'),
 ('16:30','ARG','Gimnasia Mendoza','Newells Old Boys'),
 ('17:30','BRA','Chapecoense','Athletico-PR'),
 ('19:00','BRA','Bragantino','Cruzeiro'),
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

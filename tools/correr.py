import json,sys
from nova_gol_4 import Equipo, pronostico
from datos import L
P=[ # hora, liga, local, visita
 ('08:00','ENG','Crystal Palace','Nottm Forest'),
 ('08:00','ITA','Lecce','Bologna'),
 ('08:00','ITA','Lazio','Monza'),
 ('08:00','FRA','Nice','Strasbourg'),
 ('09:15','ESP','Real Sociedad','Deportivo'),
 ('10:30','ENG','Liverpool','Manchester City'),
 ('11:00','ITA','Sassuolo','AC Milan'),
 ('11:30','ESP','Real Betis','Osasuna'),
 ('11:30','ECU','Universidad Católica','Macará'),
 ('13:45','ITA','Cagliari','Juventus'),
 ('13:45','FRA','Troyes','Marseille'),
 ('14:00','ESP','Racing','Valencia'),
 ('14:00','BRA','Atletico MG','Santos'),
 ('15:30','BRA','Flamengo','Fluminense'),
 ('15:30','BRA','Palmeiras','Corinthians'),
 ('16:30','ECU','LDU Quito','Barcelona SC'),
 ('18:00','MEX','A. San Luis','Santos Laguna'),
 ('18:10','MEX','Pachuca','Necaxa'),
 ('20:15','MEX','Pumas UNAM','Cruz Azul'),
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

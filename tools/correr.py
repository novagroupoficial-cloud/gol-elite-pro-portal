import json,sys
from nova_gol_4 import Equipo, pronostico
from datos import L
P=[ # hora (Ecuador), liga, local, visita — martes 20-oct-2026 (calendario: Líbero, RPP y Noticias de Bariloche; Liga MX también Sport-Flash; Millonarios–Once Caldas: Publimetro y Fútbol Total; SportyTrader no accesible en esta ejecución)
 ('16:30', 'COL', 'Deportivo Pereira', 'Boyacá Chicó'),
 ('18:15', 'COL', 'Internacional de Bogotá (ex La Equidad)', 'Fortaleza'),
 ('18:30', 'COL', 'Cúcuta', 'Atlético Nacional'),
 ('19:07', 'MEX', 'Guadalajara', 'Necaxa'),
 ('20:00', 'MEX', 'A. San Luis', 'Queretaro'),
 ('20:00', 'MEX', 'Juarez', 'Atlante'),
 ('20:30', 'COL', 'Millonarios', 'Once Caldas'),
 ('22:00', 'MEX', 'Tigres UANL', 'Leon'),
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

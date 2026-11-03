import json,sys
from nova_gol_4 import Equipo, pronostico
from datos import L
P=[ # hora (Ecuador), liga, local, visita — martes 3-nov-2026 (chat con Marco, 09:4x ECU; la rutina diaria de hoy no terminó). SportyTrader no accesible en esta sesión. Calendario: La República, Infobae y DSN (hora de Perú = Ecuador). Champions League (9 partidos), Championship, Paraguay y Venezuela: sin pronóstico (sin tabla casa/fuera común o verificable).
 ('15:00','PER','Comerciantes Unidos','ADT'),
 ('15:30','COL','Deportivo Pereira','Tolima'),
 ('15:30','ECU','Mushuc Runa','Manta'),
 ('17:30','BRA','Chapecoense','Mirassol'),
 ('18:20','COL','Pasto','Jaguares de Córdoba'),
 ('19:30','BRA','Internacional','Coritiba'),
 ('20:00','PER','Alianza Lima','Cienciano'),
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

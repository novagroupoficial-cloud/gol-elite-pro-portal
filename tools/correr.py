import json,sys
from nova_gol_4 import Equipo, pronostico
from datos import L
P=[ # hora (Ecuador), liga, local, visita — lunes 23-nov-2026 (rutina diaria 05:2x ECU). Calendario: fantacalcio, brentfordfc.com, gidstats, sport-flash, tribunadejundiai (CBF), mlssoccer.com, Libero.pe (CET −6 h; BRT/ART −2 h; ET −0). SportyTrader no accesible desde la rutina.
 ('14:45','ITA','Monza','Fiorentina'),
 ('15:00','ENG','Brentford','Everton'),
 ('15:00','ESP','Levante','Elche'),
 ('15:00','ARG','Gimnasia LP','Newells Old Boys'),
 ('17:30','BRA','Internacional','Vitória'),
 ('18:00','BRA','Botafogo','São Paulo'),
 ('19:00','BRA','Santos','Grêmio'),
 ('20:00','USA','St Louis City','Los Angeles FC'),
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

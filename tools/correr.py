import json,sys
from nova_gol_4 import Equipo, pronostico
from datos import L
P=[ # hora (Ecuador), liga, local, visita — miércoles 4-nov-2026 (rutina diaria 05:2x ECU). SportyTrader no accesible (error del sitio). Calendario: valorfinal (BRA, rodada 34, hora de Brasília −2 h), futboltotal (COL, hora de Chicago +1 h) y futbolperuano/bolavip (PER, reprogramado). Champions League (9 partidos): sin pronóstico (modo copas en medición).
 ('17:30','BRA','Athletico-PR','Vasco da Gama'),
 ('17:30','BRA','Flamengo','Grêmio'),
 ('18:30','COL','Cúcuta','Santa Fe'),
 ('19:30','BRA','Botafogo','Atletico MG'),
 ('19:30','BRA','São Paulo','Corinthians'),
 ('20:30','COL','Millonarios','América de Cali'),
 ('20:30','PER','Universitario','Sport Boys'),
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

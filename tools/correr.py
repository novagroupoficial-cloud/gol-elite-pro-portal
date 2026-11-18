import json,sys
from nova_gol_4 import Equipo, pronostico
from datos import L
P=[ # hora (Ecuador), liga, local, visita — miércoles 18-nov-2026 (rutina diaria 05:2x ECU): vuelve el Brasileirão (35ª rodada, 6 partidos; RS Notícia/RPP/LiveSoccerTV, Brasília −2 h) + Liga 1 Perú (Alianza Atlético–Melgar, pendiente de la fecha 17; Depor/RPP). Copa del Rey (copa, equipos de categorías inferiores) sin tabla de liga: sin pronóstico. Sin partidos de las demás ligas del portal. SportyTrader no accesible.
 ('15:00','PER','Alianza Atlético','Melgar'),
 ('17:30','BRA','Coritiba','Santos'),
 ('18:00','BRA','Remo','Chapecoense'),
 ('18:30','BRA','Flamengo','Athletico-PR'),
 ('18:30','BRA','Cruzeiro','Palmeiras'),
 ('19:30','BRA','Corinthians','Botafogo'),
 ('19:30','BRA','Grêmio','Bahia'),
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

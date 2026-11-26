import json,sys
from nova_gol_4 import Equipo, pronostico
from datos import L
P=[ # hora (Ecuador), liga, local, visita — jueves 26-nov-2026 (rutina diaria 05:2x ECU). Calendario: flashscore.com.br + sport-flash + valorfinal (São Paulo–Remo, 37ª, 20h BRT); excelsior.com.mx + de10.com.mx + sport-flash + larepublica.pe (cuartos de ida Liga MX; León–Cruz Azul 21:10 CDMX, Infobae dice 21:00: vale la mayoría). SportyTrader no accesible desde la rutina. Hoy no hay ligas europeas (Europa/Conference League), ni MLS, COL, ECU, ARG, PER, CHI.
 ('18:00','BRA','São Paulo','Remo'),
 ('20:00','MEX','Pachuca','Guadalajara'),
 ('22:10','MEX','León','Cruz Azul'),
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

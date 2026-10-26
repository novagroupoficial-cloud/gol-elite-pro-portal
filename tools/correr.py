import json,sys
from nova_gol_4 import Equipo, pronostico
from datos import L
P=[ # hora (Ecuador), liga, local, visita — lunes 26-oct-2026 (rutina diaria 05:2x ECU). Calendario: futbolperuano.com (programación del lunes 26, hora de Perú = Ecuador) y libero.pe; horas cotejadas con Fútbol Total (Sevilla–Osasuna 21:00 Madrid = 15:00 ECU) y campeonatochileno.cl (U. de Chile–Everton 18:00 Chile = 16:00 ECU). SportyTrader no accesible (WebFetch pide permiso). El Informador (hora CDMX) daba 1 h menos: descartado. Solo partidos que aún no empiezan.
 ('13:45','POR','Santa Clara','Benfica'),
 ('14:30','FRA','Paris Saint-Germain','Lyon'),
 ('15:00','ESP','Sevilla','Osasuna'),
 ('16:00','CHI','U. de Chile','Everton'),
 ('17:00','ARG','Union Santa Fe','Estudiantes LP'),
 ('17:30','BRA','Coritiba','Grêmio'),
 ('18:00','BRA','Flamengo','Atletico MG'),
 ('18:00','COL','Jaguares de Córdoba','Llaneros'),
 ('19:15','ARG','Instituto Cordoba','Deportivo Riestra'),
 ('20:05','COL','Santa Fe','Bucaramanga'),
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

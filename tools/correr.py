import json,sys
from nova_gol_4 import Equipo, pronostico
from datos import L
P=[ # hora (Ecuador), liga, local, visita — viernes 27-nov-2026 (rutina diaria 05:2x ECU). Calendario: sport-flash.com (páginas por liga/país) + sportschau.de + sporza.be + bundesliga.com + fantacalcio.it + Teleamazonas/El Universo (LigaPro hexagonal descenso F8) + El Espectador (cuadrangulares COL F3) + mlssoccer.com/columbuscrew.com (playoffs R1 J2) + RPP/Libero. SportyTrader no accesible desde la rutina. Sin partidos hoy: ARG, PER, CHI, Liga MX, hexagonal del título LigaPro.
 ('14:00','NED','Groningen','Willem II'),
 ('14:00','ECU','Delfín','Orense'),
 ('14:30','GER','Werder Bremen','Borussia Monchengladbach'),
 ('14:45','ITA','Venezia','Bologna'),
 ('14:45','FRA','Brest','Paris FC'),
 ('15:00','ENG','Nottingham Forest','Chelsea'),
 ('15:00','ESP','Levante','Racing de Santander'),
 ('15:15','POR','Maritimo','Nacional'),
 ('16:30','ECU','Deportivo Cuenca','Manta'),
 ('18:00','BRA','Fluminense','Cruzeiro'),
 ('18:35','COL','Deportivo Cali','Bucaramanga'),
 ('20:00','USA','Columbus Crew','Inter Miami'),
 ('20:40','COL','Millonarios','América de Cali'),
 ('22:00','USA','Real Salt Lake','Vancouver Whitecaps'),
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

import json,sys
from nova_gol_4 import Equipo, pronostico
from datos import L
P=[ # hora (Ecuador), liga, local, visita — sábado 24-oct-2026 (rutina diaria 05:25 ECU). Calendario: Fútbol Total (agenda del día en hora de Ecuador), footballwebpages (ESP/GER/NED, hora británica -6 h), Ligue1.com (J8), Valor Final (Brasileirão, Brasília -2 h), Informador (Liga MX, centro de México +1 h), VAVEL (MLS, ET -1 h), Primicias (LigaPro). SportyTrader no accesible (WebFetch pide permiso). Solo partidos que aún no empiezan.
 ('06:30','ENG','Aston Villa','Manchester City'),
 ('07:00','ESP','Rayo Vallecano','Elche'),
 ('08:00','ITA','Como','Sassuolo'),
 ('08:00','ITA','Cagliari','Bologna'),
 ('08:30','GER','Mainz 05','Werder Bremen'),
 ('08:30','GER','SC Paderborn','Hamburger SV'),
 ('08:30','GER','RB Leipzig','Elversberg'),
 ('08:30','GER','1. FC Koln','Schalke 04'),
 ('08:30','GER','Augsburg','Union Berlin'),
 ('09:00','ENG','Arsenal','Everton'),
 ('09:00','ENG','Coventry City','Fulham'),
 ('09:15','ESP','Racing Santander','Espanyol'),
 ('09:30','NED','FC Utrecht','PEC Zwolle'),
 ('11:00','ITA','Napoli','Roma'),
 ('11:30','ENG','Chelsea','Tottenham Hotspur'),
 ('11:30','ESP','Valencia','Villarreal'),
 ('11:30','GER','Borussia Dortmund','Eintracht Frankfurt'),
 ('11:30','ECU','Manta','Deportivo Cuenca'),
 ('11:45','NED','Willem II','Cambuur'),
 ('12:30','USA','CF Montreal','Nashville SC'),
 ('12:45','ARG','Banfield','Lanus'),
 ('13:45','ITA','Lazio','Parma'),
 ('13:45','FRA','Lens','Paris FC'),
 ('14:00','ESP','Atletico Madrid','Deportivo La Coruna'),
 ('14:00','NED','ADO Den Haag','Heerenveen'),
 ('14:00','ECU','Orense','Delfín'),
 ('14:30','BRA','Internacional','Botafogo'),
 ('14:30','BRA','Mirassol','São Paulo'),
 ('14:30','BRA','Vitória','Athletico-PR'),
 ('14:30','USA','Columbus Crew','Toronto'),
 ('15:00','ARG','Talleres Cordoba','Defensa y Justicia'),
 ('16:30','BRA','Palmeiras','Bragantino'),
 ('16:30','BRA','Vasco da Gama','Corinthians'),
 ('16:30','USA','New York RB','Inter Miami'),
 ('16:30','ECU','LDU Quito','Macará'),
 ('17:15','ARG','San Lorenzo','Newells Old Boys'),
 ('17:30','BRA','Chapecoense','Fluminense'),
 ('18:00','MEX','Leon','Toluca'),
 ('18:00','COL','Boyacá Chicó','Bucaramanga'),
 ('18:30','USA','Orlando City','New York City'),
 ('18:30','USA','DC United','Cincinnati'),
 ('18:30','USA','Philadelphia','New England'),
 ('18:30','USA','Atlanta United','Chicago Fire'),
 ('19:00','MEX','Monterrey','Guadalajara'),
 ('19:30','ARG','Rosario Central','Huracan'),
 ('19:30','USA','Houston Dynamo','Minnesota United'),
 ('19:30','USA','Dallas','SJ Earthquakes'),
 ('19:30','USA','Sporting KC','Austin'),
 ('19:30','USA','Real Salt Lake','St. Louis City'),
 ('20:00','BRA','Santos','Bahia'),
 ('20:10','COL','Junior','Águilas Doradas'),
 ('20:30','USA','Colorado Rapids','Vancouver'),
 ('21:00','MEX','Pumas UNAM','Tigres UANL'),
 ('21:30','USA','San Diego','Seattle'),
 ('21:30','USA','Portland','Charlotte'),
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

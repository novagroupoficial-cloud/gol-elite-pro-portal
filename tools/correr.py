import json,sys
from nova_gol_4 import Equipo, pronostico
from datos import L
P=[ # hora (Ecuador), liga, local, visita — domingo 25-oct-2026 (rutina diaria 05:4x ECU). Calendario: Fútbol Total (agenda del día; la página muestra UTC-4: se resta 1 h), Primicias (LigaPro fecha 4 de la fase final, hora de Ecuador), sport-flash (Liga MX, hora del centro de México +1 h) y VAVEL (MLS, ET -1 h). SportyTrader no accesible (WebFetch pide permiso). Solo partidos que aún no empiezan. Europa ya en horario de invierno.
 ('06:15','NED','Fortuna Sittard','Excelsior'),
 ('06:30','ITA','Inter','Fiorentina'),
 ('08:00','ESP','Athletic Club','Getafe'),
 ('08:30','NED','PSV','Feyenoord'),
 ('08:30','NED','NEC','FC Groningen'),
 ('09:00','ENG','Liverpool','Brighton & Hove Albion'),
 ('09:00','ENG','Manchester United','AFC Bournemouth'),
 ('09:00','ENG','Hull City','Brentford'),
 ('09:00','ENG','Crystal Palace','Newcastle United'),
 ('09:00','ITA','Genoa','Venezia'),
 ('09:00','ITA','Atalanta','Frosinone'),
 ('09:00','FRA','Monaco','Lille'),
 ('09:30','GER','Hoffenheim','Bayer Leverkusen'),
 ('10:15','ESP','Celta Vigo','Real Betis'),
 ('10:45','NED','Sparta Rotterdam','Ajax'),
 ('11:15','FRA','Auxerre','Le Mans'),
 ('11:15','FRA','Toulouse','Troyes'),
 ('11:15','FRA','Rennes','Strasbourg'),
 ('11:15','FRA','Angers','Lorient'),
 ('11:15','FRA','Marseille','Le Havre'),
 ('11:30','ENG','Sunderland','Leeds United'),
 ('11:30','GER','SC Freiburg','Bayern Munich'),
 ('11:30','ECU','Leones del Norte','Libertad'),
 ('12:00','ITA','Lecce','Juventus'),
 ('12:30','ESP','Real Sociedad','Levante'),
 ('12:45','ARG','Aldosivi','Belgrano'),
 ('14:00','NED','AZ','FC Twente'),
 ('14:00','COL','Fortaleza','Deportivo Cali'),
 ('14:00','ECU','Emelec','Guayaquil City'),
 ('14:45','ITA','Udinese','AC Milan'),
 ('15:00','ESP','Barcelona','Real Madrid'),
 ('15:00','ARG','Independiente','Boca Juniors'),
 ('16:05','COL','Alianza (ex Alianza Petrolera)','Internacional de Bogotá (ex La Equidad)'),
 ('16:30','ECU','Aucas','Barcelona SC'),
 ('17:15','ARG','River Plate','Racing Club'),
 ('18:00','MEX','Atlas','Puebla'),
 ('18:10','COL','Atlético Nacional','Independiente Medellín'),
 ('19:30','ARG','Central Cordoba SdE','Velez Sarsfield'),
 ('19:30','ARG','Barracas Central','Estudiantes Rio Cuarto'),
 ('20:00','MEX','America','Pachuca'),
 ('20:00','MEX','Queretaro','Cruz Azul'),
 ('20:00','USA','Los Angeles FC','LA Galaxy'),
 ('22:10','MEX','Tijuana','Santos Laguna'),
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

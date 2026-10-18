import json,sys
from nova_gol_4 import Equipo, pronostico
from datos import L
P=[ # hora (Ecuador), liga, local, visita — domingo 18-oct-2026 (Udinese–Lecce 05:30 y PEC Zwolle–Go Ahead Eagles 05:15 ya habían empezado al sellar)
 ('07:00', 'ESP', 'Osasuna', 'Racing Santander'),
 ('07:30', 'NED', 'Cambuur', 'AZ'),
 ('08:00', 'ENG', 'AFC Bournemouth', 'Sunderland'),
 ('08:00', 'ENG', 'Brighton & Hove Albion', 'Crystal Palace'),
 ('08:00', 'ENG', 'Leeds United', 'Manchester United'),
 ('08:00', 'ITA', 'Fiorentina', 'Como'),
 ('08:00', 'FRA', 'Angers', 'Marseille'),
 ('08:30', 'GER', 'Bayer Leverkusen', 'SC Freiburg'),
 ('09:15', 'ESP', 'Celta Vigo', 'Alaves'),
 ('09:45', 'NED', 'FC Groningen', 'Ajax'),
 ('10:15', 'FRA', 'Le Havre', 'Auxerre'),
 ('10:15', 'FRA', 'Lorient', 'Monaco'),
 ('10:15', 'FRA', 'Paris FC', 'Rennes'),
 ('10:30', 'ENG', 'Nottingham Forest', 'Arsenal'),
 ('10:30', 'GER', 'Borussia Monchengladbach', 'Hoffenheim'),
 ('11:00', 'ITA', 'AC Milan', 'Atalanta'),
 ('11:00', 'PER', 'Sporting Cristal', 'Comerciantes Unidos'),
 ('11:30', 'ESP', 'Malaga', 'Real Sociedad'),
 ('11:30', 'ECU', 'Delfín', 'Manta'),
 ('12:45', 'ARG', 'Racing Club', 'Independiente'),
 ('13:00', 'NED', 'NEC', 'Fortuna Sittard'),
 ('13:00', 'NED', 'FC Twente', 'FC Utrecht'),
 ('13:15', 'PER', 'FC Cajamarca', 'CD Moquegua'),
 ('13:45', 'ITA', 'Juventus', 'Lazio'),
 ('13:45', 'FRA', 'Lyon', 'Nice'),
 ('14:00', 'ESP', 'Real Madrid', 'Sevilla'),
 ('14:00', 'BRA', 'Grêmio', 'Cruzeiro'),
 ('14:00', 'BRA', 'Fluminense', 'Santos'),
 ('14:00', 'ECU', 'Leones del Norte', 'Emelec'),
 ('14:00', 'COL', 'Águilas Doradas', 'Tolima'),
 ('15:30', 'PER', 'Alianza Atlético', 'Universitario'),
 ('16:00', 'ARG', 'Estudiantes LP', 'San Lorenzo'),
 ('16:00', 'ARG', 'Estudiantes Rio Cuarto', 'Aldosivi'),
 ('16:00', 'USA', 'Cincinnati', 'Columbus Crew'),
 ('16:00', 'COL', 'Bucaramanga', 'América de Cali'),
 ('16:30', 'BRA', 'Bahia', 'Flamengo'),
 ('16:30', 'ECU', 'Barcelona SC', 'Universidad Católica'),
 ('17:30', 'BRA', 'Remo', 'Bragantino'),
 ('18:05', 'COL', 'Llaneros', 'Santa Fe'),
 ('18:15', 'ARG', 'Belgrano', 'River Plate'),
 ('18:30', 'PER', 'Cienciano', 'UTC'),
 ('20:00', 'MEX', 'Monterrey', 'Pachuca'),
 ('20:10', 'COL', 'Deportivo Cali', 'Junior'),
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

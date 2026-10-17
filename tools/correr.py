import json,sys
from nova_gol_4 import Equipo, pronostico
from datos import L
P=[ # hora (Ecuador), liga, local, visita — sábado 17-oct-2026
 ('06:30', 'ENG', 'Everton', 'Chelsea'),
 ('07:00', 'ESP', 'Espanyol', 'Atletico Madrid'),
 ('08:00', 'ITA', 'Venezia', 'Napoli'),
 ('08:30', 'GER', 'Elversberg', 'Augsburg'),
 ('08:30', 'GER', 'Hamburger SV', 'VfB Stuttgart'),
 ('08:30', 'GER', 'Schalke 04', 'Mainz 05'),
 ('08:30', 'GER', 'Union Berlin', 'Borussia Dortmund'),
 ('08:30', 'GER', 'Werder Bremen', 'SC Paderborn'),
 ('09:00', 'ENG', 'Brentford', 'Liverpool'),
 ('09:00', 'ENG', 'Fulham', 'Hull City'),
 ('09:00', 'ENG', 'Manchester City', 'Ipswich Town'),
 ('09:15', 'ESP', 'Villarreal', 'Elche'),
 ('09:30', 'NED', 'ADO Den Haag', 'PSV'),
 ('10:15', 'FRA', 'Strasbourg', 'Paris Saint-Germain'),
 ('11:00', 'ITA', 'Bologna', 'Inter'),
 ('11:30', 'ECU', 'Libertad', 'Guayaquil City'),
 ('11:30', 'ENG', 'Newcastle United', 'Aston Villa'),
 ('11:30', 'ESP', 'Real Betis', 'Barcelona'),
 ('11:30', 'GER', 'Bayern Munich', 'RB Leipzig'),
 ('13:00', 'ARG', 'Banfield', 'Argentinos Juniors'),
 ('13:00', 'NED', 'Telstar', 'Feyenoord'),
 ('13:30', 'USA', 'Philadelphia', 'Charlotte'),
 ('13:45', 'FRA', 'Lille', 'Brest'),
 ('13:45', 'FRA', 'Troyes', 'Lens'),
 ('13:45', 'ITA', 'Roma', 'Genoa'),
 ('14:00', 'ECU', 'Macará', 'Independiente del Valle'),
 ('14:00', 'ESP', 'Valencia', 'Athletic Club'),
 ('14:00', 'NED', 'Sparta Rotterdam', 'Willem II'),
 ('15:00', 'COL', 'Boyacá Chicó', 'Atlético Nacional'),
 ('15:00', 'PER', 'Juan Pablo II', 'Sport Boys'),
 ('15:30', 'ARG', 'Independiente Rivadavia', 'Tigre'),
 ('15:30', 'ARG', 'Platense', 'Lanus'),
 ('15:30', 'USA', 'Minnesota United', 'St. Louis City'),
 ('16:00', 'BRA', 'Botafogo', 'Chapecoense'),
 ('16:30', 'BRA', 'Atletico MG', 'Coritiba'),
 ('16:30', 'ECU', 'Aucas', 'LDU Quito'),
 ('17:30', 'BRA', 'Athletico-PR', 'Palmeiras'),
 ('18:00', 'ARG', 'Atletico Tucuman', 'Rosario Central'),
 ('18:00', 'ARG', 'Velez Sarsfield', 'Gimnasia Mendoza'),
 ('18:00', 'COL', 'Millonarios', 'Jaguares de Córdoba'),
 ('18:00', 'MEX', 'Santos Laguna', 'Queretaro'),
 ('18:00', 'PER', 'Melgar', 'Deportivo Garcilaso'),
 ('18:07', 'MEX', 'Guadalajara', 'Tigres UANL'),
 ('18:30', 'USA', 'Atlanta United', 'Inter Miami'),
 ('18:30', 'USA', 'New England', 'Chicago Fire'),
 ('18:30', 'USA', 'New York RB', 'Toronto'),
 ('18:30', 'USA', 'Orlando City', 'DC United'),
 ('19:00', 'BRA', 'São Paulo', 'Vasco da Gama'),
 ('19:30', 'USA', 'Austin', 'Vancouver'),
 ('19:30', 'USA', 'Houston Dynamo', 'Dallas'),
 ('19:30', 'USA', 'Sporting KC', 'Real Salt Lake'),
 ('20:00', 'MEX', 'Leon', 'America'),
 ('20:00', 'MEX', 'Toluca', 'A. San Luis'),
 ('20:10', 'COL', 'Independiente Medellín', 'Once Caldas'),
 ('20:30', 'PER', 'Alianza Lima', 'Atlético Grau'),
 ('21:30', 'USA', 'LA Galaxy', 'San Diego'),
 ('21:30', 'USA', 'Portland', 'Colorado Rapids'),
 ('21:30', 'USA', 'SJ Earthquakes', 'Nashville SC'),
 ('21:30', 'USA', 'Seattle', 'CF Montreal'),
 ('22:00', 'MEX', 'Cruz Azul', 'Juarez'),
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

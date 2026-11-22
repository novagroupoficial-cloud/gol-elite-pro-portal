import json,sys
from nova_gol_4 import Equipo, pronostico
from datos import L
P=[ # hora (Ecuador), liga, local, visita — domingo 22-nov-2026 (rutina diaria 05:2x ECU). Calendario: bundesliga.com/hessenschau, sportschau, t-online, orange.fr, sporza/penzcentrum, Terra, El Esquiú, Extra, Bolavip, encancha, Publimetro (horas CET −6 h; Brasil/Argentina/Chile −2 h; CDMX +1 h). SportyTrader no accesible desde la rutina.
 ('06:15','NED','Twente','Willem II'),
 ('06:30','ITA','Juventus','Venezia'),
 ('08:00','ESP','Barcelona','Villarreal'),
 ('08:30','NED','Ajax','ADO Den Haag'),
 ('08:30','NED','Sparta Rotterdam','AZ'),
 ('09:00','ENG','Hull City','Brighton'),
 ('09:00','ITA','Bologna','Udinese'),
 ('09:00','ITA','Sassuolo','Genoa'),
 ('09:00','FRA','Paris FC','Angers'),
 ('09:30','GER','Augsburg','Mainz'),
 ('10:00','CHI','Huachipato','Concepcion'),
 ('10:15','ESP','Racing de Santander','Real Sociedad'),
 ('10:45','NED','Go Ahead Eagles','Fortuna Sittard'),
 ('11:15','FRA','Lorient','Rennes'),
 ('11:30','ENG','Liverpool','Manchester United'),
 ('11:30','GER','Werder Bremen','Hamburger SV'),
 ('11:30','ECU','Manta','Delfín'),
 ('12:00','ITA','AC Milan','Frosinone'),
 ('12:30','ESP','Osasuna','Málaga'),
 ('14:00','BRA','Athletico-PR','Remo'),
 ('14:00','ARG','Rosario Central','Gimnasia Mendoza'),
 ('14:00','ECU','Orense','Mushuc Runa'),
 ('14:45','ITA','Atalanta','Inter'),
 ('14:45','FRA','Marseille','Le Mans'),
 ('15:00','ESP','Getafe','Atlético de Madrid'),
 ('15:00','PER','Sporting Cristal','Cienciano'),
 ('15:00','PER','Sport Huancayo','Universitario'),
 ('16:00','CHI','Colo-Colo','U. Catolica'),
 ('16:30','BRA','Fluminense','Mirassol'),
 ('16:30','ECU','LDU Quito','Aucas'),
 ('17:00','ARG','River Plate','Lanus'),
 ('17:30','BRA','Bragantino','Vasco da Gama'),
 ('18:07','MEX','Guadalajara','Cruz Azul'),
 ('18:30','CHI','D. Limache','La Serena'),
 ('20:00','ARG','Instituto Cordoba','Huracan'),
 ('20:10','MEX','Querétaro','Necaxa'),
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

import json,sys
from nova_gol_4 import Equipo, pronostico
from datos import L
P=[ # hora (Ecuador), liga, local, visita — domingo 1-nov-2026 (rutina diaria 05:2x ECU). SportyTrader no accesible en esta ejecución (búsqueda sin resultados). Calendario: libero.pe (hora Perú = Ecuador) cotejado con futboltotal.futbol (muestra UTC-6: +1 h), ESPN (MLS, LigaPro; ET = UTC-5 desde el 1-nov), TUDN (Liga MX, centro de México UTC-6: +1 h), teleamazonas.com (LigaPro), alairelibre.cl (CHI, hora Chile UTC-3: -2 h), vavel.com (COL, ET). Sin discrepancias de hora una vez convertidas las zonas.
 ('06:15','NED','PEC Zwolle','ADO Den Haag'),
 ('06:30','ITA','Como','Venezia'),
 ('08:00','ESP','Getafe','Sevilla'),
 ('08:30','NED','Excelsior','FC Twente'),
 ('08:30','NED','Telstar','FC Utrecht'),
 ('09:00','ITA','Frosinone','Torino'),
 ('09:00','ITA','Lazio','Cagliari'),
 ('09:00','FRA','Strasbourg','Auxerre'),
 ('09:30','GER','Union Berlin','1. FC Koln'),
 ('10:00','CHI','Huachipato','La Serena'),
 ('10:15','ESP','Racing Santander','Real Madrid'),
 ('10:30','POR','Arouca','Nacional'),
 ('10:45','NED','FC Groningen','Sparta Rotterdam'),
 ('11:00','ECU','Universidad Católica','Aucas'),
 ('11:00','PER','CD Moquegua','Los Chankas'),
 ('11:15','FRA','Paris FC','Monaco'),
 ('11:15','FRA','Lyon','Angers'),
 ('11:30','ENG','Liverpool','Arsenal'),
 ('11:30','GER','Eintracht Frankfurt','Hamburger SV'),
 ('12:00','ITA','Lecce','Genoa'),
 ('12:15','CHI','Cobresal','Everton'),
 ('12:30','ESP','Elche','Valencia'),
 ('13:00','POR','Maritimo','Santa Clara'),
 ('13:00','POR','Academico Viseu','Rio Ave'),
 ('13:00','ARG','Boca Juniors','River Plate'),
 ('13:15','PER','Cusco FC','Sport Boys'),
 ('13:30','ECU','Independiente del Valle','LDU Quito'),
 ('14:45','ITA','Juventus','Napoli'),
 ('14:45','FRA','Marseille','Toulouse'),
 ('15:00','ESP','Athletic Club','Real Sociedad'),
 ('15:15','CHI','U. Catolica','U. de Chile'),
 ('15:30','POR','Sporting Braga','Famalicao'),
 ('15:30','PER','Atlético Grau','Universitario'),
 ('15:30','USA','Vancouver','Seattle'),
 ('16:00','ECU','Guayaquil City','Libertad'),
 ('16:05','COL','Deportivo Cali','Boyacá Chicó'),
 ('16:30','ARG','Belgrano','Barracas Central'),
 ('16:30','ARG','Newells Old Boys','Union Santa Fe'),
 ('16:30','USA','Atlanta United','Toronto'),
 ('16:30','USA','Nashville SC','New York RB'),
 ('18:00','MEX','Santos Laguna','Necaxa'),
 ('18:10','COL','Independiente Medellín','Alianza (ex Alianza Petrolera)'),
 ('18:45','ARG','Lanus','Gimnasia Mendoza'),
 ('19:00','USA','New England','Inter Miami'),
 ('20:00','MEX','Cruz Azul','Leon'),
 ('20:30','USA','Los Angeles FC','Minnesota United'),
 ('21:45','USA','Portland','Houston Dynamo'),
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

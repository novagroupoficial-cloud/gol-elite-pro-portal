import json,sys
from nova_gol_4 import Equipo, pronostico
from datos import L
P=[ # hora (Ecuador), liga, local, visita — sábado 28-nov-2026 (rutina diaria 05:2x ECU). Calendario: sport-flash.com (por liga) + bundesliga.com J11 + ligue1.com J12 + fantacalcio.it (Lega) + 101greatgoals (Premier) + valorfinal (BRA 37ª) + mlssoccer.com (playoffs R1 J2) + El Universo / barcelonasc.com.ec (LigaPro F8) + infobae/cadena3 (ARG cuartos) + winsports/deportesrcn (COL F3) + cooperativa.cl (CHI F29). SportyTrader no accesible desde la rutina. Sin partidos hoy: PER (semifinal el dom 29), hexagonal del descenso LigaPro. Final de la Copa Libertadores (Palmeiras–Estudiantes, sede neutral): sin pronóstico.
 ('08:00','ESP','Real Betis','Rayo Vallecano'),
 ('09:00','ITA','Frosinone','Parma'),
 ('09:30','GER','Mainz','Union Berlin'),
 ('09:30','GER','Hamburger SV','Bayern Munich'),
 ('09:30','GER','FC Koln','Elversberg'),
 ('09:30','GER','Paderborn','Schalke 04'),
 ('10:00','ENG','Manchester United','Brentford'),
 ('10:00','ENG','Leeds United','Coventry City'),
 ('10:15','ESP','Málaga','Athletic Club'),
 ('10:30','NED','Excelsior','Telstar'),
 ('10:30','POR','Arouca','Rio Ave'),
 ('10:30','POR','Moreirense','Santa Clara'),
 ('11:15','FRA','Angers','Lens'),
 ('11:30','ECU','Universidad Católica','Independiente del Valle'),
 ('12:00','ITA','Torino','Lazio'),
 ('12:30','ENG','Ipswich Town','Aston Villa'),
 ('12:30','ESP','Elche','Atlético de Madrid'),
 ('12:30','GER','VfB Stuttgart','Eintracht Frankfurt'),
 ('12:30','USA','Charlotte FC','Chicago Fire'),
 ('12:45','NED','PSV','Go Ahead Eagles'),
 ('13:00','POR','Academico Viseu','Alverca'),
 ('14:00','ECU','Macará','LDU Quito'),
 ('14:30','USA','Houston Dynamo','San Jose Earthquakes'),
 ('14:45','ITA','Inter','Genoa'),
 ('14:45','FRA','Paris Saint-Germain','Lorient'),
 ('14:45','FRA','Le Mans','Lille'),
 ('14:45','FRA','Le Havre','Strasbourg'),
 ('14:45','FRA','Nice','Troyes'),
 ('15:00','ESP','Real Madrid','Alavés'),
 ('15:00','NED','Cambuur','Sparta Rotterdam'),
 ('15:30','POR','Guimaraes','Estrela Amadora'),
 ('16:00','CHI','Coquimbo Unido','D. Limache'),
 ('16:30','ECU','Barcelona SC','Aucas'),
 ('16:30','USA','Philadelphia Union','New England Revolution'),
 ('18:00','ARG','Velez Sarsfield','Independiente'),
 ('18:30','CHI','Colo-Colo','La Serena'),
 ('18:30','USA','FC Cincinnati','Nashville SC'),
 ('19:00','BRA','Botafogo','Bahia'),
 ('19:30','COL','Santa Fe','Atlético Nacional'),
 ('20:00','ARG','Instituto Cordoba','River Plate'),
 ('20:00','MEX','Atlas','Toluca'),
 ('20:30','USA','Los Angeles FC','St Louis City'),
 ('22:10','MEX','América','Monterrey'),
 ('22:30','USA','Portland Timbers','FC Dallas'),
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

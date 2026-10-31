import json,sys
from nova_gol_4 import Equipo, pronostico
from datos import L
P=[ # hora (Ecuador), liga, local, visita — sábado 31-oct-2026 (rutina diaria 05:2x ECU). Calendario: libero.pe y rpp.pe (hora Perú = Ecuador) cotejados con skysports (ENG), vavel (ESP, MLS, COL), soccernews (ITA, GER), hessenschau (GER), foot01/sportschau (FRA), 365scores (POR), fcupdate.nl + planetsport (NED), eleconomista.com.ar + futboltotal (ARG), umdoisesportes (BRA), t13.cl/alairelibre.cl (CHI), elmercurio.com.ec/extra.ec (ECU), bolavip/lodehoy (MEX), aquehorajuegan (PER). SportyTrader no accesible en esta ejecución (sin resultados en la búsqueda). Sin discrepancias de hora entre fuentes salvo MEX ±10 min (se usa bolavip).
 ('07:30','ENG','Chelsea','Manchester United'),
 ('08:00','ESP','Levante','Atletico Madrid'),
 ('09:00','ITA','Bologna','Monza'),
 ('09:30','GER','Werder Bremen','Hoffenheim'),
 ('09:30','GER','Schalke 04','RB Leipzig'),
 ('09:30','GER','Borussia Monchengladbach','SC Paderborn'),
 ('09:30','GER','Bayer Leverkusen','VfB Stuttgart'),
 ('09:30','GER','Augsburg','SC Freiburg'),
 ('10:00','ENG','Manchester City','Brighton & Hove Albion'),
 ('10:00','ENG','Hull City','Ipswich Town'),
 ('10:00','ENG','Coventry City','Sunderland'),
 ('10:00','ENG','Brentford','Nottingham Forest'),
 ('10:00','ENG','AFC Bournemouth','Leeds United'),
 ('10:15','ESP','Rayo Vallecano','Celta Vigo'),
 ('10:30','POR','Moreirense','Estrela Amadora'),
 ('10:30','NED','Feyenoord','Fortuna Sittard'),
 ('11:30','ECU','Delfín','Deportivo Cuenca'),
 ('12:00','ITA','Udinese','Roma'),
 ('12:00','USA','Charlotte','Orlando City'),
 ('12:30','ENG','Tottenham Hotspur','Crystal Palace'),
 ('12:30','ESP','Real Betis','Malaga'),
 ('12:30','GER','Bayern Munich','Borussia Dortmund'),
 ('12:45','NED','PSV','Willem II'),
 ('12:45','NED','Heerenveen','NEC'),
 ('12:45','ARG','Defensa y Justicia','Independiente'),
 ('13:00','USA','Columbus Crew','DC United'),
 ('13:00','USA','New York City','CF Montreal'),
 ('13:00','USA','Cincinnati','Philadelphia'),
 ('14:00','ECU','Emelec','Leones del Norte'),
 ('14:00','BRA','Coritiba','Vitória'),
 ('14:00','USA','Sporting KC','Dallas'),
 ('14:00','USA','St. Louis City','San Diego'),
 ('14:45','ITA','AC Milan','Inter'),
 ('14:45','FRA','Troyes','Le Mans'),
 ('15:00','ENG','Aston Villa','Fulham'),
 ('15:00','ESP','Barcelona','Alaves'),
 ('15:00','NED','Ajax','AZ'),
 ('15:00','NED','Cambuur','Go Ahead Eagles'),
 ('15:00','ARG','Deportivo Riestra','Talleres Cordoba'),
 ('15:30','POR','FC Porto','Estoril'),
 ('15:30','PER','Alianza Atlético','Juan Pablo II'),
 ('16:00','USA','LA Galaxy','Austin'),
 ('16:00','USA','SJ Earthquakes','Real Salt Lake'),
 ('16:30','ECU','Macará','Barcelona SC'),
 ('17:15','ARG','Velez Sarsfield','San Lorenzo'),
 ('18:00','MEX','Pachuca','Tigres UANL'),
 ('18:00','CHI','OHiggins','Nublense'),
 ('18:00','COL','Llaneros','Junior'),
 ('19:30','ARG','Estudiantes LP','Instituto Cordoba'),
 ('20:00','MEX','Monterrey','Tijuana'),
 ('20:07','MEX','Guadalajara','Atlante'),
 ('20:30','USA','Colorado Rapids','Chicago Fire'),
 ('22:00','MEX','America','Toluca'),
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

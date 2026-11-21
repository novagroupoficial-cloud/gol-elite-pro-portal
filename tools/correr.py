import json,sys
from nova_gol_4 import Equipo, pronostico
from datos import L
P=[ # hora (Ecuador), liga, local, visita — sábado 21-nov-2026 (rutina diaria 05:2x ECU), vuelven las ligas tras la fecha FIFA. Calendario: Sport-Flash (páginas por país con zona horaria) cruzado con Flashscore, hessenschau, ligue1.com/t-online, Ziggo/sporza, Récord, SI.com, A Crítica, Publimetro, El Mercurio, alairelibre, ESPN. SportyTrader no accesible desde la rutina.
 ('07:30','ENG','Manchester City','Fulham'),
 ('08:00','ESP','Alavés','Deportivo La Coruña'),
 ('09:00','ITA','Como','Cagliari'),
 ('09:00','ITA','Lazio','Lecce'),
 ('09:30','GER','Bayer Leverkusen','Paderborn'),
 ('09:30','GER','Borussia Monchengladbach','Borussia Dortmund'),
 ('09:30','GER','Eintracht Frankfurt','Hoffenheim'),
 ('09:30','GER','Union Berlin','RB Leipzig'),
 ('09:30','GER','Elversberg','Freiburg'),
 ('10:00','ENG','Aston Villa','Sunderland'),
 ('10:00','ENG','Bournemouth','Nottingham Forest'),
 ('10:00','ENG','Tottenham','Ipswich Town'),
 ('10:00','ENG','Chelsea','Leeds United'),
 ('10:00','ENG','Coventry City','Crystal Palace'),
 ('10:00','CHI','Coquimbo Unido','Everton'),
 ('10:15','ESP','Rayo Vallecano','Valencia'),
 ('10:30','NED','NEC','PSV'),
 ('11:15','FRA','Nice','Paris Saint-Germain'),
 ('12:00','ITA','Parma','Roma'),
 ('12:30','ENG','Newcastle','Arsenal'),
 ('12:30','ESP','Sevilla','Real Betis'),
 ('12:30','GER','Schalke 04','VfB Stuttgart'),
 ('12:45','NED','Feyenoord','Excelsior'),
 ('12:45','NED','FC Utrecht','Cambuur'),
 ('13:00','ARG','Defensa y Justicia','Barracas Central'),
 ('14:00','USA','New England Revolution','Philadelphia Union'),
 ('14:00','ECU','Técnico Universitario','Deportivo Cuenca'),
 ('14:30','BRA','Palmeiras','Flamengo'),
 ('14:45','FRA','Lille','Lyon'),
 ('14:45','FRA','Lens','Toulouse'),
 ('14:45','FRA','Strasbourg','Brest'),
 ('14:45','FRA','Monaco','Auxerre'),
 ('14:45','ITA','Napoli','Torino'),
 ('15:00','ESP','Real Madrid','Celta de Vigo'),
 ('15:00','ARG','Argentinos Juniors','Independiente'),
 ('15:30','BRA','Bahia','Coritiba'),
 ('16:00','USA','FC Dallas','Portland Timbers'),
 ('16:00','CHI','OHiggins','U. de Chile'),
 ('16:30','ECU','Universidad Católica','Barcelona SC'),
 ('17:50','MEX','Pachuca','Toluca'),
 ('18:00','MEX','Santos Laguna','León'),
 ('18:00','USA','Inter Miami','Columbus Crew'),
 ('18:30','CHI','U. Concepcion','Nublense'),
 ('19:00','BRA','Chapecoense','Cruzeiro'),
 ('20:00','MEX','Pumas UNAM','Monterrey'),
 ('20:15','COL','Once Caldas','Atlético Nacional'),
 ('15:30','PER','Alianza Lima','FC Cajamarca'),  # hora corregida (Líbero: 15:30 Perú = Ecuador)
 ('22:00','MEX','Tigres UANL','América'),
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

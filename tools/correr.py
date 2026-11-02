import json,sys
from nova_gol_4 import Equipo, pronostico
from datos import L
P=[ # hora (Ecuador), liga, local, visita — lunes 2-nov-2026 (rutina diaria 05:2x ECU). SportyTrader no accesible en esta ejecución (permiso de WebFetch sin respuesta). Calendario: futboltotal.futbol (UTC-6: +1 h), depor.com/resultados/2026-11-02 (UTC-10: +5 h, comprobado en 8 partidos), calcioefinanza (ITA), maxifoot (Lorient-Brest movido al lunes), laliga.com, abola.pt (POR), T13/ESPN (CHI, hora Chile UTC-3: -2 h), elmercurio.com.ec/Primicias (ECU), Vanguardia (COL), gidstats/El Economista (ARG), starting11 (BRA). Sin discrepancias una vez convertidas las zonas.
 ('11:00','PER','Sport Huancayo','Melgar'),
 ('12:30','ITA','Sassuolo','Fiorentina'),
 ('13:15','PER','UTC','Deportivo Garcilaso'),
 ('14:45','ITA','Atalanta','Parma'),
 ('14:45','FRA','Lorient','Brest'),
 ('15:00','ENG','Newcastle United','Everton'),
 ('15:00','ESP','Deportivo La Coruna','Osasuna'),
 ('15:15','POR','Benfica','Alverca'),
 ('15:15','POR','Gil Vicente','Guimaraes'),
 ('15:30','ECU','Orense','Técnico Universitario'),
 ('15:30','PER','Sporting Cristal','FC Cajamarca'),
 ('16:00','CHI','D. Limache','Audax Italiano'),
 ('16:05','COL','Águilas Doradas','Fortaleza'),
 ('17:00','ARG','Defensa y Justicia','Independiente'),
 ('17:00','ARG','Platense','Central Cordoba SdE'),
 ('18:00','BRA','Bragantino','Santos'),
 ('18:30','CHI','Concepcion','Palestino'),
 ('19:15','ARG','Atletico Tucuman','Argentinos Juniors'),
 ('19:15','ARG','Independiente Rivadavia','Banfield'),
 ('20:15','COL','Bucaramanga','Atlético Nacional'),
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

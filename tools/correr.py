import json,sys
from nova_gol_4 import Equipo, pronostico
from datos import L
P=[ # hora (Ecuador), liga, local, visita — miércoles 28-oct-2026 (rutina diaria 05:2x ECU). Calendario: libero.pe y rpp.pe (agenda del miércoles 28, hora de Perú = Ecuador; coinciden en todos los partidos). SportyTrader no accesible en esta ejecución. U. Católica–Audax Italiano (Chile, 18:30) excluido: suspendido el 22-oct sin nueva fecha (biobiochile, radioagricultura, prensafutbol), aunque las agendas aún lo listan. Sin pronóstico: Liga 1 de Perú (tabla sin actualizar desde el 17-oct) y copas (Carabao Cup, DFB Pokal, Copa Argentina, Copa Ecuador: sin tabla casa/fuera de la competición).
 ('12:30','ITA','AC Milan','Bologna'),
 ('12:30','ITA','Parma','Udinese'),
 ('12:30','ITA','Venezia','Inter'),
 ('14:45','ITA','Genoa','Juventus'),
 ('14:45','ITA','Monza','Napoli'),
 ('17:30','BRA','Bragantino','Chapecoense'),
 ('17:30','BRA','Fluminense','Internacional'),
 ('17:30','BRA','Santos','Palmeiras'),
 ('18:00','COL','Once Caldas','Alianza (ex Alianza Petrolera)'),
 ('19:30','BRA','Bahia','São Paulo'),
 ('19:30','BRA','Remo','Botafogo'),
 ('20:05','COL','Internacional de Bogotá (ex La Equidad)','Independiente Medellín'),
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

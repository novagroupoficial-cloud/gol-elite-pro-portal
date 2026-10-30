import json,sys
from nova_gol_4 import Equipo, pronostico
from datos import L
P=[ # hora (Ecuador), liga, local, visita — viernes 30-oct-2026 (rutina diaria recuperada por el refresco de las 16:12 ECU; la de 05:24 del 29 y del 30 no corrió). Calendario: Fútbol Total (fichas de la fecha 15 del Clausura, hora America/Chicago = UTC-5 = Ecuador; 19:15 ECU = 01:15 del 31 en Madrid). SportyTrader no accesible en esta ejecución (permiso no respondido). Solo ARG: su tabla está al día (fecha 14 completa, 210 PJ, fecha 15 empieza hoy). Otras ligas de esta noche sin pronóstico: tablas sin los partidos del 28-29-oct y sin tiempo de verificarlos antes del inicio.
 ('17:00','ARG','Huracan','Tigre'),
 ('17:00','ARG','Estudiantes Rio Cuarto','Gimnasia LP'),
 ('19:15','ARG','Racing Club','Aldosivi'),
 ('19:15','ARG','Sarmiento','Rosario Central'),
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

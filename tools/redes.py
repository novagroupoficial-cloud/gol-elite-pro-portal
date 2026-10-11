"""Kit de redes del día: historia 1080x1920 y carrusel 1080x1350 (HTML -> PNG con Playwright).
Uso: python3 tools/redes.py AAAA-MM-DD "HH:MM sellado"  (lee tools/pron.json y tools/kit.json)"""
import json, os, sys, base64, html
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from enlaces import COL
FECHA=sys.argv[1]; SELLO=sys.argv[2] if len(sys.argv)>2 else ''
P=[p for p in json.load(open('pron.json')) if not p.get('sin')]
K=json.load(open('kit.json'))          # partido del día, textos, auditoría, fecha larga
e=html.escape
NOM={'ENG':'Premier League','ITA':'Serie A','FRA':'Ligue 1','ESP':'LaLiga','BRA':'Brasileirão Serie A','MEX':'Liga MX','ECU':'LigaPro Ecuador','GER':'Bundesliga','NED':'Eredivisie','POR':'Liga Portugal','USA':'MLS','ARG':'Liga Profesional'}
ES={'Nottm Forest':'Nottingham Forest','Bologna':'Bolonia','Nice':'Niza','Strasbourg':'Estrasburgo','Deportivo':'Deportivo La Coruña','AC Milan':'Milan','Real Betis':'Betis','Marseille':'Marsella','Racing':'Racing Santander','Atletico MG':'Atlético MG','A. San Luis':'Atlético San Luis','Pumas UNAM':'Pumas','Universidad Católica':'U. Católica'}
n=lambda x:ES.get(x,x)
f1=lambda v:f"{v:.1f}".replace('.',',')
f2=lambda v:f"{v:.2f}".replace('.',',')
def ink(c):
    r,g,b=(int(c[i:i+2],16) for i in (1,3,5)); return '#111' if 0.299*r+0.587*g+0.114*b>150 else '#fff'
def cat(o): return 'GOL ÉLITE 95' if o>=95 else 'GOL ÉLITE' if o>=90 else 'RANGO 80' if o>=80 else 'RANGO 70' if o>=70 else 'MENOS DE 70'
def escudo(t,size):
    c=COL.get(t,'#2a3a32'); ini=''.join(w[0] for w in n(t).replace('.','').split()[:2]).upper()
    return f'<div class="esc" style="width:{size}px;height:{size}px;background:{c};color:{ink(c)};font-size:{size*.36:.0f}px">{e(ini)}</div>'
foto='data:image/jpeg;base64,'+base64.b64encode(open(K.get('foto','../assets/presentadora.jpg'),'rb').read()).decode()
top=next(p for p in P if p['local']==K['local'])
pjL,gfL,gcL=top['casa']; pjV,gfV,gcV=top['fuera']
def _ff(fam,w,f): return '@font-face{font-family:"%s";font-weight:%d;src:url(data:font/woff2;base64,%s) format("woff2")}'%(fam,w,base64.b64encode(open('../assets/fuentes/'+f,'rb').read()).decode())
FUENTES=_ff('Barlow Condensed',700,'barlow-condensed-latin-700-normal.woff2')+_ff('Barlow Condensed',800,'barlow-condensed-latin-800-normal.woff2')+_ff('IBM Plex Sans',400,'ibm-plex-sans-latin-400-normal.woff2')+_ff('IBM Plex Sans',600,'ibm-plex-sans-latin-600-normal.woff2')
CSS='''<style>'''+FUENTES+'''
*{box-sizing:border-box}body{margin:0}
.lienzo{position:relative;overflow:hidden;color:#eef4ef;font-family:"IBM Plex Sans",sans-serif;
 background:radial-gradient(900px 600px at 50% -80px,#1b6b43 0%,transparent 70%),radial-gradient(500px 400px at 0 100%,#0f4a2c 0%,transparent 70%),#05100b}
.luces{position:absolute;inset:0;background:radial-gradient(160px 160px at 8% 4%,rgba(180,255,210,.35),transparent 70%),radial-gradient(160px 160px at 92% 4%,rgba(180,255,210,.35),transparent 70%)}
.marca{font-family:"Barlow Condensed";font-weight:800;letter-spacing:.04em;text-align:center}
.marca b{color:#e6b84a}
.oro{background:linear-gradient(180deg,#fff,#fff1b8 40%,#e6b84a 75%,#a8740f);-webkit-background-clip:text;background-clip:text;color:transparent}
.disp{white-space:nowrap;font-family:"Barlow Condensed";font-weight:800;text-transform:uppercase;line-height:.95}
.esc{border-radius:50%;display:grid;place-items:center;font-family:"Barlow Condensed";font-weight:800;border:6px solid #e6b84a;box-shadow:0 0 40px rgba(230,184,74,.35)}
.caja{background:linear-gradient(180deg,rgba(14,40,27,.92),rgba(5,16,11,.92));border:2px solid #e6b84a;border-radius:22px;box-shadow:0 0 40px rgba(46,232,138,.15)}
.verde{color:#2ee88a}.dor{color:#e6b84a}
.pie{position:absolute;left:0;right:0;bottom:0;padding:22px 40px;background:#030a07;border-top:2px solid #e6b84a;display:flex;justify-content:space-between;align-items:center;font-family:"Barlow Condensed";font-weight:700;font-size:30px}
.legal{font-size:22px;color:#9fb2a6}
</style>'''

def historia():
    return CSS+f'''<div class="lienzo" style="width:1080px;height:1920px">
<div class="luces"></div>
<div class="marca" style="position:absolute;top:60px;left:0;right:0;font-size:84px">GOL <b>ÉLITE</b> PRO</div>
<div class="disp oro" style="position:absolute;top:170px;left:60px;right:60px;text-align:center;font-size:130px">Partido del día</div>
<div class="disp" style="position:absolute;top:310px;left:0;right:0;text-align:center;font-size:44px;color:#2ee88a;letter-spacing:.08em">{e(cat(top['over15']))} · mayor probabilidad por jugar</div>
<img src="{foto}" style="position:absolute;left:0;bottom:120px;height:1180px;width:auto;mask-image:linear-gradient(90deg,#000 70%,transparent);-webkit-mask-image:linear-gradient(90deg,#000 70%,transparent)">
<div style="position:absolute;right:50px;top:400px;width:600px;display:grid;gap:26px">
 <div style="display:flex;align-items:center;justify-content:space-between">{escudo(top['local'],200)}<div class="disp oro" style="font-size:90px">VS</div>{escudo(top['visita'],200)}</div>
 <div class="disp" style="text-align:center;font-size:62px">{e(n(top['local']))}<br><span class="dor" style="font-size:44px">vs</span><br>{e(n(top['visita']))}</div>
 <div style="text-align:center;font-size:34px;font-weight:600">{e(NOM[top['liga']])}<br><span class="dor">{e(K['fecha_larga'])} · {top['hora']} ECU</span></div>
 <div class="caja" style="padding:26px;display:grid;gap:18px">
  <div style="display:flex;justify-content:space-between;align-items:center"><span class="disp" style="font-size:56px">Over 1.5</span><span class="disp verde" style="font-size:96px">{f1(top['over15'])}%</span></div>
  <div style="display:flex;justify-content:space-between;align-items:center"><span class="disp" style="font-size:56px">Over 2.5</span><span class="disp" style="font-size:80px">{f1(top['over25'])}%</span></div>
  <div style="display:flex;justify-content:space-between;align-items:center"><span class="disp" style="font-size:44px">Marcador estimado</span><span class="disp dor" style="font-size:80px">{top['marcador']}</span></div>
 </div>
 <div class="caja" style="padding:22px 26px;font-size:30px;line-height:1.35">
  <b class="dor">Por qué:</b> {e(n(top['local']))} marca <b>{f2(gfL/pjL)}</b> en casa · {e(n(top['visita']))} recibe <b>{f2(gcV/pjV)}</b> fuera · goles esperados <b class="verde">{f1(top['goles_esperados'])}</b>
 </div>
</div>
<div class="pie"><span>Modelo Nova Gol 4.0 · {e(SELLO)}</span><span class="legal">+18 · No garantiza resultados</span></div>
</div>'''

def slide(contenido):
    return CSS+f'''<div class="lienzo" style="width:1080px;height:1350px"><div class="luces"></div>
<div class="marca" style="position:absolute;top:40px;left:0;right:0;font-size:64px">GOL <b>ÉLITE</b> PRO</div>{contenido}
<div class="pie"><span>Nova Gol 4.0 · {e(K['fecha_larga'])}</span><span class="legal">+18 · No garantiza resultados</span></div></div>'''

def fila(p,big=False):
    return f'''<div style="display:grid;grid-template-columns:110px 1fr 160px 150px;gap:16px;align-items:center;padding:16px 22px;border-bottom:1px solid #1f3a2b">
<span class="disp dor" style="font-size:40px">{p['hora']}</span><span style="font-size:30px;font-weight:600;line-height:1.15">{e(n(p['local']))}<br>{e(n(p['visita']))}</span>
<span class="disp verde" style="font-size:52px;text-align:right">{f1(p['over15'])}%</span><span class="disp" style="font-size:38px;text-align:right;color:#cfe">{f1(p['over25'])}%</span></div>'''

def carrusel():
    s=[]
    # 1 partido del día
    s.append(slide(f'''<div class="disp oro" style="position:absolute;top:130px;left:0;right:0;text-align:center;font-size:110px">Partido del día</div>
<div class="disp verde" style="position:absolute;top:250px;left:0;right:0;text-align:center;font-size:40px;letter-spacing:.08em">{e(cat(top['over15']))} · {e(NOM[top['liga']])} · {top['hora']} ECU</div>
<img src="{foto}" style="position:absolute;right:-40px;bottom:100px;height:880px;opacity:.95;mask-image:linear-gradient(270deg,#000 60%,transparent);-webkit-mask-image:linear-gradient(270deg,#000 60%,transparent)">
<div style="position:absolute;left:60px;top:340px;width:620px;display:grid;gap:24px">
 <div style="display:flex;gap:24px;align-items:center">{escudo(top['local'],150)}<span class="disp oro" style="font-size:70px">VS</span>{escudo(top['visita'],150)}</div>
 <div class="disp" style="font-size:72px;white-space:normal">{e(n(top['local']))} <span class="dor">vs</span> {e(n(top['visita']))}</div>
 <div class="caja" style="padding:24px;display:grid;grid-template-columns:repeat(3,1fr);text-align:center;gap:10px">
  <div><div style="font-size:24px;color:#9fb2a6">OVER 1.5</div><div class="disp verde" style="font-size:72px">{f1(top['over15'])}%</div></div>
  <div><div style="font-size:24px;color:#9fb2a6">OVER 2.5</div><div class="disp" style="font-size:72px">{f1(top['over25'])}%</div></div>
  <div><div style="font-size:24px;color:#9fb2a6">MARCADOR</div><div class="disp dor" style="font-size:72px">{top['marcador']}</div></div></div>
 <div style="font-size:30px;color:#cfe">Desliza para ver las estadísticas que lo justifican →</div></div>'''))
    # 2 estadísticas que lo justifican
    datos=[('Goles a favor en casa · '+n(top['local']),f2(gfL/pjL),f'{gfL} goles en {pjL} partidos'),
           ('Goles en contra en casa · '+n(top['local']),f2(gcL/pjL),f'{gcL} goles en {pjL} partidos'),
           ('Goles a favor fuera · '+n(top['visita']),f2(gfV/pjV),f'{gfV} goles en {pjV} partidos'),
           ('Goles en contra fuera · '+n(top['visita']),f2(gcV/pjV),f'{gcV} goles en {pjV} partidos'),
           ('Goles esperados del partido',f1(top['goles_esperados']),f"{f2(top['lambda_local'])} {n(top['local'])} + {f2(top['lambda_visita'])} {n(top['visita'])}"),
           ('Media de la liga',f"{f2(top['HG'])} / {f2(top['AG'])}",'goles del local / del visitante por partido')]
    filas=''.join(f'<div style="display:grid;grid-template-columns:1fr 260px;align-items:center;padding:18px 26px;border-bottom:1px solid #1f3a2b"><div><div style="font-size:30px;font-weight:600">{e(a)}</div><div style="font-size:24px;color:#9fb2a6">{e(c)}</div></div><div class="disp verde" style="font-size:66px;text-align:right">{b}</div></div>' for a,b,c in datos)
    extra=''.join(f'<li>{e(x)}</li>' for x in K.get('contexto',[]))
    s.append(slide(f'''<div class="disp oro" style="position:absolute;top:120px;left:0;right:0;text-align:center;font-size:84px">Estadísticas que lo justifican</div>
<div class="caja" style="position:absolute;left:50px;right:50px;top:240px">{filas}</div>
<ul style="position:absolute;left:70px;right:70px;top:1000px;font-size:28px;line-height:1.4;margin:0;padding-left:28px">{extra}</ul>'''))
    # 3 resto de rango 80
    otros=[p for p in sorted(P,key=lambda p:-p['over15']) if p['over15']>=80 and p is not top and p['hora']>K.get('desde','00:00')]
    s.append(slide(f'''<div class="disp oro" style="position:absolute;top:120px;left:0;right:0;text-align:center;font-size:90px">Más pronósticos del día</div>
<div style="position:absolute;top:230px;left:0;right:0;text-align:center;font-size:30px;color:#9fb2a6">Over 1.5 de 80 % o más · <span class="verde">Over 1.5</span> · Over 2.5</div>
<div class="caja" style="position:absolute;left:50px;right:50px;top:300px">{''.join(fila(p) for p in otros[:8])}</div>'''))
    # 4 auditoría
    A=K['auditoria']
    tiles=''.join(f'<div class="caja" style="padding:28px;text-align:center"><div class="disp {c}" style="font-size:110px">{v}</div><div style="font-size:28px">{e(t)}</div></div>' for v,t,c in A['tiles'])
    s.append(slide(f'''<div class="disp oro" style="position:absolute;top:120px;left:0;right:0;text-align:center;font-size:96px">Así nos fue ayer</div>
<div style="position:absolute;top:235px;left:0;right:0;text-align:center;font-size:32px;color:#9fb2a6">{e(A['titulo'])}</div>
<div style="position:absolute;left:60px;right:60px;top:320px;display:grid;grid-template-columns:1fr 1fr;gap:24px">{tiles}</div>
<div style="position:absolute;left:70px;right:70px;top:1010px;font-size:28px;line-height:1.4">{e(A['nota'])}</div>'''))
    # 5 cierre
    s.append(slide(f'''<img src="{foto}" style="position:absolute;left:-30px;bottom:100px;height:1000px;mask-image:linear-gradient(90deg,#000 60%,transparent);-webkit-mask-image:linear-gradient(90deg,#000 60%,transparent)">
<div style="position:absolute;right:60px;top:220px;width:560px;display:grid;gap:30px;text-align:right">
<div class="disp oro" style="font-size:110px;white-space:normal">¿Cuál es tu pronóstico?</div>
<div style="font-size:36px">Déjalo en los comentarios y compáralo con el nuestro.</div>
<div class="caja" style="padding:26px;text-align:center"><div class="disp" style="font-size:52px;white-space:normal">Miembros Fundadores</div><div style="font-size:30px" class="dor">Análisis gratis hasta el 30 de noviembre de 2026</div><div style="font-size:28px;margin-top:8px">gol-elite-pro.netlify.app</div></div>
<div class="legal">Probabilidades estadísticas, no garantías. Solo mayores de 18 años. Presentadora creada con IA.</div></div>'''))
    return s

os.makedirs(f'../redes/{FECHA}',exist_ok=True)
open(f'../redes/{FECHA}/historia.html','w',encoding='utf-8').write(historia())
for i,h in enumerate(carrusel(),1): open(f'../redes/{FECHA}/carrusel-{i}.html','w',encoding='utf-8').write(h)
print('html listo')

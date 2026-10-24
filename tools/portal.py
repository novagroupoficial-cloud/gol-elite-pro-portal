import json, html, base64, os, sys, re
os.chdir(os.path.dirname(os.path.abspath(__file__)))
P=[p for p in json.load(open('pron.json')) if not p.get('sin')]
FECHA_PRON=(P[0].get('sellado','')[:10] if P else '')
NOM={'ENG':'Premier League','ITA':'Serie A','FRA':'Ligue 1','ESP':'LaLiga','BRA':'Brasileirão','MEX':'Liga MX','ECU':'LigaPro','ARG':'Liga Profesional','GER':'Bundesliga','NED':'Eredivisie','POR':'Liga Portugal','USA':'MLS','COL':'Liga BetPlay','PER':'Liga 1','CHI':'Primera División'}
PAIS={'ENG':'Inglaterra','ITA':'Italia','FRA':'Francia','ESP':'España','BRA':'Brasil','MEX':'México','ECU':'Ecuador','ARG':'Argentina','GER':'Alemania','NED':'Países Bajos','POR':'Portugal','USA':'EE. UU.','COL':'Colombia','PER':'Perú','CHI':'Chile'}
ES={'Borussia Monchengladbach':"M'gladbach",'AFC Bournemouth':'Bournemouth','Brighton & Hove Albion':'Brighton','SC Freiburg':'Friburgo','Malaga':'Málaga','Alaves':'Alavés','Marseille':'Marsella','Monaco':'Mónaco','Estudiantes Rio Cuarto':'Est. Río Cuarto','Estudiantes LP':'Estudiantes','Comerciantes Unidos':'Comerciantes U.','Universidad Católica':'U. Católica','Columbus Crew':'Columbus Crew','Cincinnati':'FC Cincinnati','Nottm Forest':'Nottingham Forest','Bologna':'Bolonia','Nice':'Niza','Strasbourg':'Estrasburgo','Deportivo':'Deportivo La Coruña','AC Milan':'Milan','Real Betis':'Betis','Marseille':'Marsella','Racing':'Racing Santander','Atletico MG':'Atlético MG','A. San Luis':'Atlético San Luis','Pumas UNAM':'Pumas','Coventry':'Coventry City','Newcastle':'Newcastle United','Lanus':'Lanús','Velez Sarsfield':'Vélez Sarsfield','Gimnasia Mendoza':'Gimnasia (Mendoza)','Newells Old Boys':"Newell's Old Boys",'Bragantino':'Red Bull Bragantino','Athletico-PR':'Athletico Paranaense','Bayern Munich':'Bayern Múnich','Atletico Madrid':'Atlético de Madrid','Paris Saint-Germain':'PSG','Leon':'León','America':'América','Queretaro':'Querétaro','Juarez':'FC Juárez','Atletico Tucuman':'Atlético Tucumán','Philadelphia':'Philadelphia Union','New England':'New England Revolution','Seattle':'Seattle Sounders','Portland':'Portland Timbers','Austin':'Austin FC','Dallas':'FC Dallas','Toronto':'Toronto FC','New York RB':'New York Red Bulls','SJ Earthquakes':'San José Earthquakes','San Diego':'San Diego FC','Charlotte':'Charlotte FC','Colorado Rapids':'Colorado Rapids','Houston Dynamo':'Houston Dynamo','Minnesota United':'Minnesota United','Real Betis':'Real Betis','Guadalajara':'Chivas','Tigres UANL':'Tigres','Tottenham Hotspur':'Tottenham','Central Cordoba SdE':'Central Córdoba','Union Santa Fe':'Unión','Alianza (ex Alianza Petrolera)':'Alianza FC','Pasto':'Deportivo Pasto','Newells Old Boys':"Newell's",'Deportivo Riestra':'Riestra','Internacional de Bogotá (ex La Equidad)':'Inter Bogotá','Boyacá Chicó':'Boyacá Chicó'}
n=lambda x:ES.get(x,x)
e=html.escape
f1=lambda v:f"{v:.1f}".replace('.',',')
from nova_gol_4 import entero
pc=lambda v:str(entero(v))  # % públicos: redondeo de Marco (,5 sube)
def cat(o):
    o=entero(o)
    return ('elite','GOL ÉLITE') if o>=95 else ('plat','GOLES PLATINO') if o>=90 else ('r80','GOLES ESTÁNDAR') if o>=80 else ('r70','GOLES OPTIMISTAS')
def key(p): return f"{p['local']}|{p['visita']}"

# ---- Noticias (hechos de fuentes citadas al pie; texto propio) ----
NEWS_PRED={}  # (sin uso en la portada actual)
NEWS_DEST=[]
FUENTES=[
 ("SoccerSTATS · local y visitante Liga MX (más resultados partido a partido)","https://www.soccerstats.com/homeaway.asp?league=mexico"),
 ("SoccerSTATS · local y visitante MLS (más resultados partido a partido)","https://www.soccerstats.com/homeaway.asp?league=usa"),
 ("SoccerSTATS · local y visitante Liga BetPlay (más resultados partido a partido)","https://www.soccerstats.com/homeaway.asp?league=colombia2"),
 ("Fútbol Total · agenda del sábado 24 de octubre (hora de Ecuador) y fichas de los partidos","https://futboltotal.futbol/2026-10-24"),
 ("Football Web Pages · LaLiga, Bundesliga y Eredivisie 2026-27 (resultados y calendario)","https://www.footballwebpages.co.uk/german-bundesliga/fixtures-results/october"),
 ("VAVEL · resultados y calendario de la MLS 2026 y de la Ligue 1 2026-27","https://www.vavel.com/en-us/data/mls/results/"),
 ("Ligue 1 · programación de la jornada 8","https://ligue1.com/en/articles/l1_article_5797-programmations-tv-j6-j7-et-j8-l1-2627"),
 ("Valor Final · 32.ª fecha del Brasileirão","https://valorfinal.com.br/brasileirao/2026/rodada-32"),
 ("El Informador · jornada 14 de la Liga MX","https://www.informador.mx/deportes/liga-mx-calendario-de-partidos-de-la-jornada-14-del-apertura-2026-horarios-y-donde-verlos-en-vivo-20261022-0066.html"),
 ("Primicias · fecha 4 de la fase final de la LigaPro","https://www.primicias.ec/deportes/donde-ver-fecha/teleamazonas-fechas-partidos-horarios-fecha4-hexagonal-cuadrangular-ver-tv-135546/"),
]
idx={key(p):p for p in P}

def chips(p):
    c,t=cat(p['over15'])
    return f'<span class="badge {c}">{t}</span>'
# Estadísticas extra (public/api/estadisticas.json) y noticia del partido (data/<fecha>/noticias.json), si son del mismo día
try:
    _EST=json.load(open('../public/api/estadisticas.json',encoding='utf-8'))
    _EX={(x['local'],x['visitante']):x for x in _EST['partidos']}
    _NOT=json.load(open(f"../data/{_EST['fecha']}/noticias.json",encoding='utf-8'))['partidos'] if os.path.exists(f"../data/{_EST['fecha']}/noticias.json") else {}
except Exception: _EX,_NOT={},{}
def extra(p):
    x=_EX.get((p['local'],p['visita'])); nt=_NOT.get(f"{p['local']}|{p['visita']}"); h=''
    if x and abs(x['over15']-p['over15'])<0.05:
        m=x['modelo_extra']
        h+=f'''<div class="nga-g" style="margin-top:12px"><div><b>Ambos marcan</b><span>{pc(m['ambos_marcan'])} %</span></div><div><b>Over 3.5</b><span>{pc(m['over35'])} %</span></div>
<div><b>1X2</b><span>{e(n(p['local']))} {pc(m['gana_local'])} % · empate {pc(m['empate'])} % · {e(n(p['visita']))} {pc(m['gana_visit'])} %</span></div>
<div><b>Marcadores más probables</b><span>{', '.join(f"{a} ({pc(v)} %)" for a,v in m['marcadores_top6'][:3])}</span></div></div>'''
    if nt: h+=f'''<div class="noti"><b>📰 La noticia del partido · {e(nt['titular'])}</b><p>{e(nt['texto'])}</p><a href="{e(nt['url'])}" target="_blank" rel="noopener">Fuente: {e(nt['fuente'])} ↗</a></div>'''
    return h
def stats(p):
    pjL,gfL,gcL=p['casa']; pjV,gfV,gcV=p['fuera']
    return f'''<div class="nga"><div class="nga-h">Nova Gol Analytics · datos del partido</div>
<div class="nga-g"><div><b>{e(n(p['local']))}</b> en casa<span>{f1(gfL/pjL)} GF · {f1(gcL/pjL)} GC por partido · {pjL} PJ</span></div>
<div><b>{e(n(p['visita']))}</b> fuera<span>{f1(gfV/pjV)} GF · {f1(gcV/pjV)} GC por partido · {pjV} PJ</span></div>
<div><b>Goles esperados</b><span>{f1(p['lambda_local'])} + {f1(p['lambda_visita'])} = {f1(p['goles_esperados'])}</span></div>
<div><b>Media de la liga</b><span>{f1(p['HG'])} local · {f1(p['AG'])} visitante</span></div></div>{extra(p)}</div>'''

from enlaces import LINK, PRED, DEST, COL, ACIERTOS, LLEGAN
def ink(hexc):
    r,g,b=(int(hexc[i:i+2],16) for i in (1,3,5)); return '#111' if (0.299*r+0.587*g+0.114*b)>150 else '#fff'
def img(p):
    a,b=p['local'],p['visita']; ca,cb=COL.get(a,'#2a3a32'),COL.get(b,'#3a4a42')
    def nombre(t,y,col):
        t=e(n(t)).upper(); w=min(len(t)*17,250)
        adj=f' textLength="{w:.0f}" lengthAdjust="spacingAndGlyphs"' if len(t)*17>250 else ''
        return f'<text x="18" y="{y}" font-family="Barlow Condensed,Arial Narrow,sans-serif" font-weight="800" font-size="30" fill="{col}"{adj}>{t}</text>'
    return f"""<svg class="ph" viewBox="0 0 320 150" preserveAspectRatio="xMinYMid slice" role="img" aria-label="{e(n(a))} contra {e(n(b))}"><rect width="320" height="150" fill="{cb}"/><path d="M0 0H320V62L0 88Z" fill="{ca}"/>
{nombre(a,50,ink(ca))}{nombre(b,124,ink(cb))}
<circle cx="292" cy="75" r="18" fill="#0e1c16"/><text x="292" y="82" text-anchor="middle" font-family="Barlow Condensed,sans-serif" font-weight="800" font-size="18" fill="#e0b34a">VS</text>
<text x="18" y="18" font-family="IBM Plex Sans,sans-serif" font-weight="600" font-size="11" fill="{ink(ca)}" opacity=".85">{NOM[p['liga']].upper()} · {p['hora']} ECU</text></svg>"""
def dato(k):
    nt=_NOT.get(k)
    if not nt: return ''
    fu=f'<a href="{e(nt["url"])}" target="_blank" rel="noopener">{e(nt["fuente"])}</a>' if not nt['url'].startswith('https://gol-elite-pro') else e(nt['fuente'])
    return f'<p class="dato"><b>📰 {e(nt["titular"].capitalize())}.</b> {e(nt["texto"])} <small>({fu})</small></p>'
def card(k,big=False):
    p=idx[k]; tit,medio,url=LINK[k]
    return f'''<article class="news {'big' if big else ''}" data-ko="{p['hora']}"><a class="nl" href="{url}" target="_blank" rel="noopener">{img(p)}</a>
<div class="nb"><div class="news-top">{chips(p)}<span class="live" hidden>En juego / jugado</span></div>
<h3><a href="{url}" target="_blank" rel="noopener">{e(tit)}</a></h3>{dato(k)}
<div class="src">{e(medio)} · <a href="{url}" target="_blank" rel="noopener">Leer la noticia ↗</a></div>
<div class="odds"><div class="odd"><span>Over 1.5</span><b>{pc(p['over15'])}%</b></div><div class="odd"><span>Over 2.5</span><b>{pc(p['over25'])}%</b></div><div class="odd"><span>Marcador</span><b>{p['marcador']}</b></div></div></div></article>'''
import datetime as _dt
_ahora=(_dt.datetime.now(_dt.timezone.utc).replace(tzinfo=None)-_dt.timedelta(hours=5)).strftime('%H:%M') if (_dt.datetime.now(_dt.timezone.utc).replace(tzinfo=None)-_dt.timedelta(hours=5)).date().isoformat()==FECHA_PRON else '00:00'
_pend=[p for p in P if p['hora']>_ahora]
top=max(_pend or P,key=lambda p:p['over15'])
sec1=''.join(card(k) for k in PRED if k!=key(top))
sec2=''.join(card(k) for k in DEST)
def goles(r):
    m=re.match(r'\s*(\d+)-(\d+)',r); return int(m[1])+int(m[2]) if m else '?'
# Éxito estrella y récords (tools/records.py -> public/api/records.json)
import subprocess; subprocess.run([sys.executable,'records.py'],stdout=subprocess.DEVNULL)  # se recalcula en cada publicación
try: _R=json.load(open('../public/api/records.json',encoding='utf-8'))
except Exception: _R=None
DIAS_ES=['lunes','martes','miércoles','jueves','viernes','sábado','domingo']
def _fl(iso):
    import datetime as _d; d=_d.date.fromisoformat(iso); return f"{DIAS_ES[d.weekday()]} {d.day}"
estrella=recs=''
if _R:
    u=_R['partido_del_dia']['detalle'][-1] if _R['partido_del_dia']['detalle'] else None
    if u and u.get('acierto'):
        estrella=f'''<div class="estrella"><span class="es-t">⭐ ÉXITO ESTRELLA · {e(_fl(u['fecha']))}</span><b>{e(n(u['partido'].split(' vs ')[0]))} {e(u['resultado'])} {e(n(u['partido'].split(' vs ')[1]))}</b>
<span>Dimos Over 1.5 al {pc(u['over15'])} % · Hubo {u['goles']} goles · {e(cat(u['over15'])[1])}</span>
<span class="es-r">Partido del día cumplido {_R['partido_del_dia']['racha_actual']} días seguidos · {_R['over90']['racha_actual']} aciertos seguidos en partidos de 90 % o más</span></div>'''
    C=_R['categorias']; q=lambda d:f"{d['aciertos']}/{d['partidos']}"; pq=lambda d:f"{round(d['aciertos']*100/d['partidos'])} %" if d['partidos'] else '—'
    g=_R.get('mayor_goleada_acertada') or {}
    recs=f'''<div class="recs"><h3>🏆 Nuestros récords</h3><div class="kpis">
<div class="kpi g"><b>{q(_R['over90'])}</b><span>Over 1.5 de 90 % o más ({pq(_R['over90'])})</span></div>
<div class="kpi g"><b>{_R['over90']['racha_max']}</b><span>aciertos seguidos de 90 % o más (récord)</span></div>
<div class="kpi"><b>{q(_R['partido_del_dia'] | dict(partidos=_R['partido_del_dia']['dias']))}</b><span>partidos del día cumplidos</span></div>
<div class="kpi"><b>{q(_R['over80'])}</b><span>Over 1.5 de 80 % o más ({pq(_R['over80'])})</span></div>
<div class="kpi"><b>{q(C['GOL ÉLITE'])}</b><span>GOL ÉLITE (95 % o más)</span></div>
<div class="kpi"><b>{q(C['GOLES PLATINO'])}</b><span>GOLES PLATINO (90 a 94 %)</span></div>
<div class="kpi"><b>{q(C['GOLES ESTÁNDAR'])}</b><span>GOLES ESTÁNDAR (80 a 89 %)</span></div>
<div class="kpi"><b>{g.get('goles','—')}</b><span>goles en la mayor goleada acertada: {e(g.get('partido',''))}</span></div></div>
<p class="legal">{len(_R['dias'])} días auditados partido a partido ({_R['partidos']} partidos), recalculados con la escala actual. Se publican aciertos y fallos.</p></div>'''

# Cuadro "cómo se cumplen nuestras probabilidades" y jornada anterior completa (aciertos y fallos), desde records.json
calib=ayer=''
if _R and _R.get('calibracion'):
    fil=''.join(f"<tr><td>{e(c['franja'])}</td><td>{c['partidos']}</td><td><b>{round(c['aciertos']*100/c['partidos'])} %</b> <small>({c['aciertos']}/{c['partidos']})</small></td><td>{pc(c['prometido'])} %</td></tr>" for c in _R['calibracion'])
    calib=f'''<div class="recs"><h3>📊 Cómo se cumplen nuestras probabilidades</h3><div class="tw"><table class="cal"><thead><tr><th>Le dimos Over 1.5</th><th>Partidos</th><th>Se cumplió</th><th>Prometido</th></tr></thead><tbody>{fil}</tbody></table></div>
<p class="legal">Todos los partidos auditados ({_R['partidos']}), comparando la probabilidad que publicamos con lo que pasó en la cancha. Arriba de 90 % el modelo cumple lo que promete; entre 80 y 89 % se ha cumplido menos de lo prometido. Lo publicamos tal cual: aciertos y fallos.</p></div>'''
if _R and _R.get('ultima_jornada'):
    J=_R['ultima_jornada']; ok=sum(x['acierto'] for x in J['partidos'])
    fil=''.join(f"<tr class=\"{'ok' if x['acierto'] else 'ko'}\"><td>{'✅' if x['acierto'] else '❌'}</td><td>{e(n(x['local']))} <b>{e(x['resultado'])}</b> {e(n(x['visita']))}</td><td>{pc(x['over15'])} %</td><td>{x['goles']}</td></tr>" for x in J['partidos'])
    ayer=f'''<div class="recs"><h3>📋 Todos los pronósticos del {e(_fl(J['fecha']))}: {ok} de {len(J['partidos'])} en Over 1.5</h3><div class="tw"><table class="cal"><thead><tr><th></th><th>Partido</th><th>Dimos</th><th>Goles</th></tr></thead><tbody>{fil}</tbody></table></div></div>'''
acier=''.join(f'''<a class="ac" href="{u}" target="_blank" rel="noopener"><span class="ac-ok">✔</span><div><b>{e(m)}</b><span class="ac-r">{e(r)}</span><small>Dimos Over 1.5 al {e(pc.split(' · ')[0])} · hubo {goles(r)} goles{(' · '+e(pc.split(' · ')[1])) if ' · ' in pc else ''} · {e(md)} ↗</small></div></a>''' for m,r,pc,md,u in ACIERTOS)
def llegan(k):
    p=idx.get(k)
    if not p: return ''
    pjL,gfL,gcL=p['casa']; pjV,gfV,gcV=p['fuera']
    li=''.join(f'<li>{e(x)}</li>' for x in LLEGAN[k] if not x.startswith('Fuente'))
    fu=''.join(e(x) for x in LLEGAN[k] if x.startswith('Fuente'))
    return f'''<article class="ll"><div class="ll-h"><span class="lg">{NOM[p['liga']]} · {p['hora']} ECU</span>{chips(p)}</div>
<h3>{e(n(p['local']))} <span>vs</span> {e(n(p['visita']))}</h3>
<div class="ll-k"><div><b>{f1(gfL/pjL)}</b><span>GF casa {e(n(p['local']))}</span></div><div><b>{f1(gcL/pjL)}</b><span>GC casa</span></div><div><b>{f1(gfV/pjV)}</b><span>GF fuera {e(n(p['visita']))}</span></div><div><b>{f1(gcV/pjV)}</b><span>GC fuera</span></div></div>
<ul>{li}</ul><div class="ll-p"><span>Over 1.5 <b>{pc(p['over15'])}%</b></span><span>Over 2.5 <b>{pc(p['over25'])}%</b></span><span>Marcador <b>{p['marcador']}</b></span></div><small class="src">{fu}</small></article>'''
secll=''.join(llegan(k) for k in sorted(LLEGAN,key=lambda k:-idx[k]['over15'] if k in idx else 0))


ligas=[]
for p in sorted(P,key=lambda p:p['hora']):
    if p['liga'] not in ligas: ligas.append(p['liga'])
tabs='<button class="tab on" data-l="all">Todos</button>'+''.join(f'<button class="tab" data-l="{l}">{PAIS[l]}</button>' for l in ligas)
rows=''
for p in sorted(P,key=lambda p:(p['hora'],-p['over15'])):
    c,t=cat(p['over15'])
    rows+=f'''<details class="ev {c}" data-l="{p['liga']}" data-ko="{p['hora']}"><summary>
<div class="ev-t"><span class="ko">{p['hora']}</span><span class="live" hidden>●</span></div>
<div class="ev-m"><span class="lg">{NOM[p['liga']]}</span><span class="tm">{e(n(p['local']))}</span><span class="tm">{e(n(p['visita']))}</span></div>
<div class="ev-o"><div class="odd {'hot' if entero(p['over15'])>=80 else ''}"><span>Over 1.5</span><b>{pc(p['over15'])}%</b></div><div class="odd {'hot' if p['over25']>=65 else ''}"><span>Over 2.5</span><b>{pc(p['over25'])}%</b></div><div class="odd"><span>Marcador</span><b>{p['marcador']}</b></div></div>
<div class="ev-c">{chips(p)}</div></summary>{stats(p)}</details>'''

SIN=['Liga Portugal (Estrela–Casa Pia, Alverca–Arouca y Gil Vicente–FC Porto): todavía no tenemos tablas de local y visitante verificadas de la temporada 2026-27.','Primera Nacional de Argentina (Almagro–Tristán Suárez, Quilmes–San Martín de Tucumán, Ferro–Chaco For Ever y Deportivo Madryn–San Telmo): sin tablas de local y visitante verificadas.']  # sin pronóstico hoy
fu=''.join(f'<li id="f{i+1}"><a href="{u}" target="_blank" rel="noopener">{e(t)}</a></li>' for i,(t,u) in enumerate(FUENTES))

# Ranking del día (tools/refresco.py). Solo se muestra si corresponde a los mismos partidos de pron.json (evita mostrar el de ayer).
RANK=open('ranking.html',encoding='utf-8').read() if os.path.exists('ranking.html') else ''
if RANK and RANK.split('\n',1)[0]!='<!--partidos:'+';'.join(sorted(key(p) for p in P))+'-->': RANK=''
FOTO=base64.b64encode(open('../assets/presentadora.jpg','rb').read()).decode()
top=max(_pend or P,key=lambda p:p['over15'])
out=f'''<title>Gol Élite Pro · Portada</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<style>
:root{{color-scheme:dark;--bg:#06110c;--panel:#0d1c15;--panel2:#12261c;--ink:#eef4ef;--muted:#9fb2a6;--line:#1f3a2b;--bar:#030a07;--bar-ink:#eef4ef;--acc:#2ee88a;--acc-ink:#03140b;--gold:#e6b84a;--gold2:#fff1b8;--gold-bg:#1d1808;--odd:#132a1f;--odd-hot:#0f3a25;--chip0:#7f948a;
--disp:"Barlow Condensed","Arial Narrow",system-ui,sans-serif;--body:"IBM Plex Sans",system-ui,-apple-system,"Segoe UI",sans-serif}}
body{{background:radial-gradient(1200px 500px at 50% -120px,#0f4a2c 0%,transparent 70%),var(--bg)}}
*{{box-sizing:border-box}}
body{{background-color:var(--bg);color:var(--ink);font-family:var(--body);font-size:15px;line-height:1.5}}
a{{color:var(--acc)}}
.bar{{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;background:var(--bar);color:var(--bar-ink)}}
.bar-in{{max-width:1240px;margin:0 auto;padding:10px 16px;display:flex;align-items:center;gap:16px;flex-wrap:wrap}}
.logo{{font-family:var(--disp);font-weight:800;font-size:24px;letter-spacing:.04em}}
.logo span{{color:var(--gold)}}
.logo small{{display:block;font-family:var(--body);font-weight:500;font-size:11px;letter-spacing:.08em;opacity:.7;text-transform:uppercase}}
.menu{{display:flex;gap:16px;font-weight:600;font-size:14px;flex-wrap:wrap}}
.menu a{{color:var(--bar-ink);text-decoration:none;opacity:.85}}
.cta{{margin-left:auto;background:linear-gradient(180deg,var(--gold2),var(--gold));color:#1b1403;font-weight:700;border-radius:4px;padding:8px 14px;font-size:14px;text-decoration:none}}
.tabs{{background:#0a1711;border-bottom:1px solid var(--line);position:sticky;top:calc(env(safe-area-inset-top,0px) + 58px);z-index:4}}
.tabs-in{{max-width:1240px;margin:0 auto;padding:0 16px;display:flex;gap:4px;overflow-x:auto}}
.tab{{font:600 14px var(--body);background:none;border:0;border-bottom:3px solid transparent;color:var(--muted);padding:12px 12px;cursor:pointer;white-space:nowrap}}
.tabl{{font:700 14px var(--body);color:var(--gold);text-decoration:none;padding:12px 12px;white-space:nowrap;border-bottom:3px solid transparent}}
.tab.on{{color:var(--ink);border-color:var(--acc)}}
.wrap{{max-width:1240px;margin:0 auto;padding-inline:16px;padding-block:20px 48px;display:grid;grid-template-columns:minmax(0,1fr) 320px;gap:24px}}
main{{display:grid;gap:28px;min-width:0}}
aside{{display:grid;gap:16px;align-content:start;min-width:0}}
.sh{{display:flex;align-items:baseline;gap:6px 12px;flex-wrap:wrap;margin-bottom:12px}}
.sh h2{{font-family:var(--disp);font-size:34px;font-weight:800;margin:0;text-wrap:balance;text-transform:uppercase;letter-spacing:.02em;background:linear-gradient(180deg,var(--gold2),var(--gold) 60%,#b07d1c);-webkit-background-clip:text;background-clip:text;color:transparent}}
.sh p{{margin:0;color:var(--muted);font-size:14px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:12px}}
.news{{background:var(--panel);border:1px solid #2a4a38;box-shadow:0 0 0 1px rgba(230,184,74,.08),0 8px 24px rgba(0,0,0,.35);border-radius:6px;overflow:hidden;display:grid;align-content:start}}
.ph{{display:block;width:100%;height:auto;max-width:100%}}
.nb{{padding:12px 14px 14px;display:grid;gap:8px}}
.news h3 a{{color:var(--ink);text-decoration:none}} .news h3 a:hover{{text-decoration:underline}}
.src{{font-size:13px;color:var(--muted)}} .src a{{font-weight:600}}
.news.big{{grid-column:1/-1;border:2px solid var(--gold);grid-template-columns:minmax(0,1.2fr) minmax(0,1fr)}} .news.big .nb{{align-content:center}} @media (min-width:701px){{.news.big .nl{{display:block;min-height:100%}} .news.big .ph{{height:100%;min-height:180px}}}}
@media (max-width:700px){{.news.big{{grid-template-columns:minmax(0,1fr)}}}}
.news h3{{font-family:var(--disp);font-size:22px;line-height:1.1;margin:0;text-wrap:balance}}
.news.big h3{{font-size:30px}}
.news p{{margin:0;font-size:14px;color:var(--ink)}}
.news sup a{{text-decoration:none;font-weight:600;margin-left:2px}}
.news-top{{display:flex;gap:8px;align-items:center;flex-wrap:wrap}}
.lg{{font-size:12px;text-transform:uppercase;letter-spacing:.06em;color:var(--muted);font-weight:600}}
.teams{{font-weight:600}} .teams span{{color:var(--muted);font-weight:400}}
.badge{{font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.05em;padding:2px 8px;border-radius:3px;background:var(--odd);color:var(--acc)}}
.badge.elite{{background:linear-gradient(180deg,var(--gold2),var(--gold));color:#1b1403}} .dato{{margin:6px 0 8px;font-size:13px;line-height:1.4;color:var(--muted)}} .dato b{{color:var(--gold)}} .dato small a{{color:var(--muted)}} .estrella{{display:grid;gap:4px;margin:0 0 14px;padding:16px 18px;border-radius:12px;border:2px solid var(--gold);background:linear-gradient(180deg,var(--gold-bg),var(--panel));box-shadow:0 0 30px -12px var(--gold)}} .estrella .es-t{{font-family:"Barlow Condensed",sans-serif;font-weight:800;letter-spacing:.08em;color:var(--gold)}} .estrella b{{font-family:"Barlow Condensed",sans-serif;font-size:30px;line-height:1.05}} .estrella .es-r{{color:var(--acc);font-weight:600}} .recs{{margin:0 0 14px}} .tw{{overflow-x:auto}} .cal{{width:100%;border-collapse:collapse;font-size:14px;font-variant-numeric:tabular-nums}} .cal th,.cal td{{padding:7px 8px;border-bottom:1px solid var(--line);text-align:left}} .cal th{{color:var(--muted);font-weight:600;font-size:12px}} .cal tr.ko td{{color:var(--muted)}} .cal small{{color:var(--muted)}} .recs h3{{margin:0 0 8px}} .noti{{margin-top:10px;padding:10px 12px;border:1px solid var(--gold);border-radius:8px;background:var(--gold-bg)}} .noti b{{color:var(--gold2)}} .noti p{{margin:4px 0;color:var(--ink)}} .noti a{{font-size:12px;color:var(--gold)}} .badge.plat{{background:linear-gradient(180deg,#f4f7f6,#aebbb6);color:#101815}} .badge.r70{{color:var(--muted)}} .badge.r00{{color:var(--chip0);background:transparent;border:1px solid var(--line)}}
.live{{font-size:12px;font-weight:700;color:#c0392b}}
.odds{{display:grid;grid-template-columns:repeat(3,1fr);gap:6px;margin-top:4px}}
.odd{{background:var(--odd);border-radius:4px;padding:6px 8px;display:grid;text-align:center;gap:0}}
.odd span{{white-space:nowrap;font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:.05em}}
.odd b{{white-space:nowrap;font-family:var(--disp);font-size:20px;font-variant-numeric:tabular-nums}}
.odd.hot{{background:var(--odd-hot)}} .odd.hot b{{color:var(--acc);text-shadow:0 0 12px rgba(46,232,138,.35)}}
.book{{background:var(--panel);border:1px solid var(--line);border-radius:6px;overflow:hidden}}
.ev{{border-bottom:1px solid var(--line)}} .ev:last-child{{border-bottom:0}}
.ev summary{{list-style:none;display:grid;grid-template-columns:56px minmax(0,1fr) 230px 110px;gap:12px;align-items:center;padding:10px 14px;cursor:pointer}}
.ev summary::-webkit-details-marker{{display:none}}
.ev summary:hover{{background:var(--panel2)}}
.ev[open] summary{{background:var(--panel2)}}
.ev-t .ko{{font-family:var(--disp);font-size:20px;font-weight:700}}
.ev-m{{display:grid;min-width:0}} .tm{{font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.ev-o{{display:grid;grid-template-columns:repeat(3,1fr);gap:6px}}
.ev-c{{text-align:right}}
.ev.r00 .ev-o b{{color:var(--muted)}}
.nga{{padding:12px 14px 16px;background:var(--panel2);border-top:1px dashed var(--line)}}
.nga-h{{font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--acc);margin-bottom:8px}}
.nga-g{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:10px}}
.nga-g div{{display:grid}} .nga-g span{{color:var(--muted);font-size:14px;font-variant-numeric:tabular-nums}}
.box{{background:var(--panel);border:1px solid var(--line);border-radius:6px;padding:14px 16px;display:grid;gap:8px}}
.box h3{{font-family:var(--disp);font-size:22px;margin:0}}
.box ul{{margin:0;padding-left:18px;display:grid;gap:4px;font-size:14px}}
.kpis{{display:grid;grid-template-columns:1fr 1fr;gap:8px}}
.kpi{{background:var(--odd);border-radius:4px;padding:8px}} .kpi b{{font-family:var(--disp);font-size:26px;display:block;line-height:1}} .kpi span{{font-size:12px;color:var(--muted)}}
.kpi.g b{{color:var(--gold)}}
.legal{{font-size:13px;color:var(--muted)}}
.preview{{background:var(--gold-bg);color:var(--gold2);border:1px dashed var(--gold);border-radius:6px;padding:10px 14px;font-size:14px}}
@media (max-width:340px){{.bar .cta{{font-size:11px!important;padding:6px 7px!important}} .bar .logo{{font-size:15px!important}} .bar-in{{gap:6px!important}}}}
@media (max-width:400px){{.logo small{{display:none}} .bar-in{{gap:10px}} .bar .cta{{font-size:12px;padding:6px 8px}} .bar .logo{{font-size:17px}}}}
.acg{{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:10px}}
.ac{{display:flex;gap:12px;align-items:center;background:var(--panel);border:1px solid #2a4a38;border-left:4px solid var(--acc);border-radius:6px;padding:12px 14px;text-decoration:none;color:var(--ink)}}
.ac:hover{{border-color:var(--gold)}} .ac-ok{{font-size:22px;color:var(--acc);font-weight:800}}
.ac div{{display:grid;min-width:0}} .ac b{{font-size:15px}} .ac-r{{font-family:var(--disp);font-size:28px;font-weight:800;color:var(--gold);line-height:1.1}} .ac small{{color:var(--muted);font-size:12px}}
.llg{{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:12px}}
.ll{{background:var(--panel);border:1px solid #2a4a38;border-radius:6px;padding:14px;display:grid;gap:10px;align-content:start}}
.ll-h{{display:flex;gap:8px;align-items:center;flex-wrap:wrap}} .ll h3{{font-family:var(--disp);font-size:24px;margin:0;line-height:1.1}} .ll h3 span{{color:var(--gold);font-size:18px}}
.ll-k{{display:grid;grid-template-columns:repeat(4,1fr);gap:6px}} .ll-k div{{background:var(--odd);border-radius:4px;padding:6px;text-align:center;display:grid}}
.ll-k b{{font-family:var(--disp);font-size:24px;color:var(--acc)}} .ll-k span{{font-size:10.5px;color:var(--muted);line-height:1.2}}
.ll ul{{margin:0;padding-left:18px;font-size:14px;display:grid;gap:4px}}
.ll-p{{display:flex;gap:12px;flex-wrap:wrap;font-size:14px;border-top:1px dashed var(--line);padding-top:8px}} .ll-p b{{color:var(--gold)}}
/* home */.home{{display:inline-flex;align-items:center;gap:6px;background:#e6b84a;color:#1b1403;font:700 14px system-ui,sans-serif;padding:8px 12px;border-radius:999px;text-decoration:none;flex-shrink:0}}.home:hover{{background:#fff1b8}}
.fab{{position:fixed;right:16px;bottom:calc(16px + env(safe-area-inset-bottom,0px));z-index:9;width:52px;height:52px;border-radius:50%;display:grid;place-items:center;background:#e6b84a;color:#1b1403;box-shadow:0 6px 20px rgba(0,0,0,.45),0 0 0 2px #0e1c16;text-decoration:none}}.fab svg{{width:24px;height:24px}}.fab:hover{{background:#fff1b8}}
.hide{{display:none}}
.nota-over{{margin:-12px 0 0;padding:10px 14px;border-left:4px solid var(--gold);background:var(--panel);border-radius:4px;font-size:14px;color:var(--muted)}} .nota-over b{{color:var(--ink)}}
.hero{{position:relative;display:grid;grid-template-columns:240px minmax(0,1fr);gap:0;border:2px solid var(--gold);border-radius:8px;overflow:hidden;background:linear-gradient(120deg,#0b2a1b,#06110c 60%);box-shadow:0 0 30px rgba(46,232,138,.12)}}
.hero img{{width:100%;height:100%;object-fit:cover;object-position:top;display:block;max-width:100%}}
.hero-b{{padding:20px 22px;display:grid;gap:10px;align-content:center}}
.hero-k{{font-family:var(--disp);font-size:16px;letter-spacing:.14em;text-transform:uppercase;color:var(--acc);font-weight:700}}
.hero h2{{font-family:var(--disp);font-weight:800;font-size:clamp(30px,4.2vw,46px);line-height:1;margin:0;text-transform:uppercase;background:linear-gradient(180deg,#fff,var(--gold2) 45%,var(--gold));-webkit-background-clip:text;background-clip:text;color:transparent;text-wrap:balance}}
.hero .vsx{{font-family:var(--disp);font-size:24px;font-weight:700;display:flex;gap:8px;align-items:center;flex-wrap:wrap}} .hero .vsx .hk{{color:var(--gold)}}
.hero .odds{{max-width:420px}}
.hero .odd b{{font-size:28px}}
.hero p{{margin:0;color:var(--muted);font-size:14px;max-width:52ch}}
@media (max-width:640px){{.home span{{display:none}} .logo{{white-space:nowrap;font-size:19px}} .logo small{{font-size:9px}} .cta{{white-space:nowrap}} .home{{padding:9px}} .hero{{grid-template-columns:minmax(0,1fr)}} .hero img{{height:260px;object-position:top}} .hero .vsx{{font-size:20px}} .hero-b{{padding:14px}} .hero .odd b{{font-size:20px}}}}

@media (max-width:980px){{.wrap{{grid-template-columns:minmax(0,1fr)}}}}
@media (max-width:640px){{.bar-in{{flex-wrap:nowrap}} .logo{{font-size:21px}} .cta{{padding:7px 10px;font-size:13px}} .ev summary{{grid-template-columns:62px minmax(0,1fr);}} .ev-t .ko{{font-size:18px}} .ev-o{{grid-column:1/-1}} .ev-c{{display:none}} .menu{{display:none}} .tabs{{position:static}} .news.big h3{{font-size:26px}}}}
.ev-t{{display:flex;align-items:center;gap:4px}}
</style>
<header class="bar"><div class="bar-in"><a class="home" href="/" aria-label="Ir al inicio" title="Inicio"><svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="M3 11.5 12 4l9 7.5V20a1 1 0 0 1-1 1h-5v-6h-6v6H4a1 1 0 0 1-1-1z" fill="currentColor"/></svg><span>Inicio</span></a><div class="logo">GOL <span>ÉLITE</span> PRO<small>con Nova Gol Analytics</small></div>
<nav class="menu" aria-label="Principal"><a href="#aciertos">Aciertos</a><a href="#predicciones">Predicciones</a><a href="#llegan">Cómo llegan</a><a href="#destacados">Destacados</a><a href="#partidos">Partidos</a><a href="/galeria.html">Galería</a></nav>
<a class="cta" href="#fundadores">Miembro Fundador</a></div></header>
<div class="tabs"><div class="tabs-in" role="tablist"><a class="tabl" href="/galeria.html">★ Galería de aciertos</a>{tabs}</div></div>
<div class="wrap"><main>
<div class="preview">Vista previa del nuevo diseño de la portada. Datos reales del sábado 24 de octubre; se integrará al portal cuando llegue el código.</div>
<section class="hero" aria-label="Partido del día"><img src="data:image/jpeg;base64,{FOTO}" alt="Presentadora de Gol Élite Pro">
<div class="hero-b"><div class="hero-k">Partido con mayor probabilidad del día</div><div class="src">Sábado 24 de octubre de 2026 · sellado 05:59 ECU · el de mayor Over 1.5 que aún no empieza</div>
<h2>{e(n(top['local']))} vs {e(n(top['visita']))}</h2>
<div class="vsx">{NOM[top['liga']]} · <span class="hk">{top['hora']} ECU</span> {chips(top)}</div>
<div class="odds"><div class="odd hot"><span>Over 1.5</span><b>{pc(top['over15'])}%</b></div><div class="odd hot"><span>Over 2.5</span><b>{pc(top['over25'])}%</b></div><div class="odd"><span>Marcador</span><b>{top['marcador']}</b></div></div>
<p>Probabilidades del modelo Nova Gol 4.0, calculadas con datos de local y visitante. Referencia estadística, no garantía.</p><div class="src">{e(LINK[key(top)][1])} · <a href="{LINK[key(top)][2]}" target="_blank" rel="noopener">Leer la noticia del partido ↗</a></div></div></section>
<p class="nota-over"><b>¿Qué es Over 1.5?</b> Que en el partido haya <b>2 goles o más</b>, sin importar quién gane. Over 2.5 = 3 goles o más.</p>
{RANK}
<section id="aciertos"><div class="sh"><h2>Últimos aciertos auditados</h2><p>Última jornada auditada: viernes 23 de octubre · 2 de 5 partidos con 2 goles o más (Over 1.5) · el partido del día acertó: Necaxa 1-1 FC Juárez, hubo 2 goles y fue el marcador exacto · también publicamos los fallos · toca para ver el resultado en su medio</p></div>
{estrella}{recs}{ayer}{calib}<div class="acg">{acier}</div><p class="legal" style="margin-top:8px"><a href="/galeria.html">Ver todos los aciertos en la Galería →</a></p></section>
<section id="predicciones"><div class="sh"><h2>Nuestras principales predicciones</h2><p>Over 1.5 de 80 % o más · toca una noticia para leerla en su medio</p></div>
<div class="grid">{sec1 or '<p class="legal">Hoy ningún partido llega a 80 % en Over 1.5. El más alto está arriba, como partido del día; todos los demás están en «Partidos del día». Preferimos decirlo antes que inflar números.</p>'}</div></section>
<section id="destacados"><div class="sh"><h2>Lo más importante del sábado</h2><p>Los partidos que más se miran hoy</p></div>
<div class="grid">{sec2}</div></section>
<section id="llegan"><div class="sh"><h2>Cómo llegan los favoritos de hoy</h2><p>Estadísticas que respaldan nuestras mayores probabilidades</p></div>
<div class="llg">{secll}</div></section>
<section id="partidos"><div class="sh"><h2>Partidos del día</h2><p>Sábado 24 de octubre de 2026 · pronósticos sellados a las 05:59 (hora de Ecuador), solo partidos aún no empezados · toca un partido para ver sus datos</p></div>
<div class="book">{rows}</div></section>
</main>
<aside>
<section class="box" id="historial"><h3>Auditoría del viernes 23</h3>
<div class="kpis"><div class="kpi g"><b>1/1</b><span>Partido del día · Over 1.5</span></div><div class="kpi"><b>1/3</b><span>Over 1.5 de 70 % o más (33 %)</span></div><div class="kpi"><b>2/5</b><span>Over 1.5 en todos los partidos</span></div><div class="kpi"><b>1/5</b><span>Marcadores exactos</span></div></div>
<p class="legal">5 partidos auditados con resultado final y fuente. Partido del día: Necaxa 1-1 FC Juárez (dimos Over 1.5 al 83 %; hubo 2 goles, marcador exacto) ✔. Fallos: Atlante 0-1 Atlético San Luis (81 %) y Cruzeiro 1-0 Remo (80 %), los dos con 1 gol; tampoco llegó a 2 goles Tigre 0-1 Atlético Tucumán (41 %). Acierto con menos de 70 %: Gimnasia Mendoza 1-2 Platense (66 %, 3 goles). Ningún Over 2.5 con señal. Acumulado de la galería: 17/17 GOL ÉLITE y 103/137 en Over 1.5 de 70 % o más (75 %). Pronósticos sellados antes de cada partido y nunca modificados.</p><a class="cta" style="margin:0;justify-self:start" href="/galeria.html">Ver galería de aciertos →</a></section>
<section class="box"><h3>Escala Nova Gol 4.0</h3><ul><li><span class="badge elite">GOL ÉLITE</span> Over 1.5 de 95 % o más</li><li><span class="badge plat">GOLES PLATINO</span> de 90 % a 94 %</li><li><span class="badge r80">GOLES ESTÁNDAR</span> de 80 % a 89 %</li><li><span class="badge r70">GOLES OPTIMISTAS</span> menos de 80 %</li></ul><p class="legal">Porcentajes redondeados: ,5 o más sube (94,8 → 95 %); menos de ,5 se queda (94,4 → 94 %).</p></section>
<section class="box"><h3>Sin pronóstico hoy</h3><p class="legal">Sin datos verificables de local y visitante. No inventamos números.</p>{('<ul>'+''.join(f'<li>{e(s)}</li>' for s in SIN)+'</ul>') if SIN else '<p class="legal">Hoy todos los partidos revisados tienen datos verificados de local y visitante.</p>'}</section>
<section class="box legal" id="fundadores"><h3>Uso responsable</h3><p>Análisis estadístico informativo para mayores de 18 años. La probabilidad no garantiza resultados ni promete ganancias.</p>
<p>Las noticias enlazan a sus medios de origen. Las imágenes de los partidos son ilustraciones propias de Gol Élite Pro.</p><p>Estadísticas de local y visitante: SoccerSTATS, Sports Mole, Football Web Pages, VAVEL y Fútbol Total (resultados recientes sumados partido a partido), verificadas con sumas cruzadas: goles a favor en casa = goles en contra fuera.</p></section>
</aside></div>
<a class="fab" href="/" aria-label="Volver al inicio" title="Inicio"><svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="M3 11.5 12 4l9 7.5V20a1 1 0 0 1-1 1h-5v-6h-6v6H4a1 1 0 0 1-1-1z" fill="currentColor"/></svg></a>
<script>
(function(){{
  // hora actual en Ecuador (UTC-5) para marcar partidos ya iniciados
  var now=new Date(Date.now()-5*3600e3), hm=now.getUTCHours()*60+now.getUTCMinutes(), dia=now.toISOString().slice(0,10);
  if(dia==="2026-10-24"){{document.querySelectorAll('[data-ko]').forEach(function(el){{var t=el.getAttribute('data-ko').split(':');if(hm>=(+t[0])*60+(+t[1])){{var l=el.querySelector('.live');if(l)l.hidden=false;}}}});}}
  var tabs=document.querySelectorAll('.tab');
  tabs.forEach(function(b){{b.addEventListener('click',function(){{tabs.forEach(function(x){{x.classList.remove('on')}});b.classList.add('on');var l=b.getAttribute('data-l');
    document.querySelectorAll('.ev').forEach(function(ev){{ev.classList.toggle('hide',l!=='all'&&ev.getAttribute('data-l')!==l)}});
    document.getElementById('partidos').scrollIntoView({{behavior:'smooth',block:'start'}});}})}});
}})();
</script>'''
open('_portada.html','w',encoding='utf-8').write(out)
print('ok',len(P))

import json, html, base64, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
P=[p for p in json.load(open('pron.json')) if not p.get('sin')]
NOM={'ENG':'Premier League','ITA':'Serie A','FRA':'Ligue 1','ESP':'LaLiga','BRA':'Brasileirão','MEX':'Liga MX','ECU':'LigaPro'}
PAIS={'ENG':'Inglaterra','ITA':'Italia','FRA':'Francia','ESP':'España','BRA':'Brasil','MEX':'México','ECU':'Ecuador'}
ES={'Nottm Forest':'Nottingham Forest','Bologna':'Bolonia','Nice':'Niza','Strasbourg':'Estrasburgo','Deportivo':'Deportivo La Coruña','AC Milan':'Milan','Real Betis':'Betis','Marseille':'Marsella','Racing':'Racing Santander','Atletico MG':'Atlético MG','A. San Luis':'Atlético San Luis','Pumas UNAM':'Pumas'}
n=lambda x:ES.get(x,x)
e=html.escape
f1=lambda v:f"{v:.1f}".replace('.',',')
def cat(o):
    return ('elite','GOL ÉLITE') if o>=90 else ('r80','Rango 80') if o>=80 else ('r70','Rango 70') if o>=70 else ('r00','Menos de 70')
def key(p): return f"{p['local']}|{p['visita']}"

# ---- Noticias (hechos de fuentes citadas al pie; texto propio) ----
NEWS_PRED={
 'Crystal Palace|Nottm Forest':("El partido con más goles esperados del domingo",
   "Palace recibe 3,5 goles por partido en Selhurst Park y Forest marca 2,0 por salida: el modelo lo pone en 90,7 % de Over 1.5. Palace llega 15.º, con 11 goles encajados en cinco fechas y bajas de Henderson, Mateta y Tomiyasu, más la sanción de Disasi. En Forest, Igor Jesus se perderá alrededor de un mes y Milenkovic se pierde este partido. Ojo: los tres últimos duelos de Premier entre ellos terminaron 1-1.",[0]),
 'Sassuolo|AC Milan':("Milan de Amorim visita a un Sassuolo goleador en casa",
   "Sassuolo marca 2,5 por partido como local y el Milan anota 1,7 fuera: 84,9 % de Over 1.5. El Milan llega quinto con 11 puntos tras golear 3-0 al Lecce; Sassuolo viene de perder 2-1 en Monza. Estupiñán arrastra molestias de la selección y es duda.",[1]),
 'Atletico MG|Santos':("Santos, una defensa que concede fuera de casa",
   "Santos encaja 1,6 goles por salida y Atlético MG promedia 1,7 a favor en el Arena MRV: 85,0 % de Over 1.5, el más alto de Sudamérica hoy. Es la fecha 30 del Brasileirão, 14:00 hora de Ecuador.",[2]),
 'Universidad Católica|Macará':("Católica, la mejor ofensiva local de la LigaPro, recibe al segundo",
   "Católica hizo 35 goles en 14 partidos de local en la fase inicial (2,5 por partido) y Macará recibió 1,3 por salida: 82,3 % de Over 1.5. Es la fecha 2 del hexagonal: Macará es segundo con 54 puntos y Católica tercera con 51. Goleadores en cancha: Fajardo (11) por Católica; Posse (12) y Campana (10) por Macará.",[3]),
 'A. San Luis|Santos Laguna':("Santos Laguna, de las defensas más frágiles de visita",
   "Santos Laguna recibe 2,4 goles por partido fuera de casa y San Luis marca 1,2 en casa: 84,7 % de Over 1.5.",[]),
 'Pachuca|Necaxa':("Pachuca–Necaxa: dos defensas que conceden",
   "Pachuca recibe 2,0 por partido en casa y Necaxa 2,0 fuera: 83,7 % de Over 1.5, aunque la muestra es corta (4 y 4 partidos).",[]),
 'Pumas UNAM|Cruz Azul':("Pumas busca revancha de la final del Clausura",
   "Cruz Azul fue campeón del Clausura 2026 en el Olímpico Universitario, con gol de Rotondi en el 90+4. Hoy ambos llegan con tres partidos sin ganar; Cruz Azul ha recibido 18 goles en diez fechas y Paradela es duda. Modelo: 81,5 % de Over 1.5.",[4]),
 'Lazio|Monza':("Monza, de las visitas que más goles reciben",
   "Monza encaja 2,7 goles por salida y Lazio solo recibe 1,0 en casa: 84,2 % de Over 1.5, con un 1-1 como marcador más probable.",[]),
 'Nice|Strasbourg':("Estrasburgo: partidos abiertos lejos de casa",
   "Estrasburgo marca 2,3 y recibe 2,7 por salida; Niza promedia 1,0 a favor en casa: 82,2 % de Over 1.5.",[]),
 'Racing|Valencia':("Racing Santander hace goles en El Sardinero",
   "Racing marca 2,3 por partido en casa y recibe 1,7; Valencia hizo solo 0,7 por salida: 80,2 % de Over 1.5, el límite del Rango 80.",[]),
}
NEWS_DEST=[
 ('Liverpool|Manchester City',"Clásico en Anfield: el líder perfecto contra un Liverpool golpeado",
   "Manchester City llega con cinco victorias en cinco fechas de Premier. Liverpool tiene dudas de Isak y Gakpo y bajas en ataque y defensa; Foden cumple sanción en el City. El modelo ve un partido más cerrado de lo que sugiere el cartel: 74,3 % de Over 1.5 y 1-1 como marcador más probable.",[5]),
 ('LDU Quito|Barcelona SC',"Liga–Barcelona en Quito, sin hinchada visitante",
   "Fecha 2 del hexagonal final, 16:30 en el Rodrigo Paz. Liga ganó 2-1 a Católica en la fecha 1; Barcelona aún no debuta porque su partido con IDV se postergó. Es el partido más cerrado del día para el modelo: 41,0 % de Over 1.5, con 0-0 como marcador más probable. Liga marcó solo 0,9 por partido en casa en la fase inicial.",[6,3]),
 ('Palmeiras|Corinthians',"Dérbi con Corinthians sin técnico titular",
   "Tras la salida de Fernando Diniz, Corinthians llega con comisión interina (Léo Porto y William Batista). Palmeiras, que recibe solo 0,6 goles por partido en casa, es el local más sólido del Brasileirão. Modelo: 65,1 % de Over 1.5, 1-0 como marcador más probable.",[7]),
 ('Flamengo|Fluminense',"Fla-Flu en la fecha 30",
   "Flamengo marca 2,0 por partido en casa y recibe 0,7; Fluminense hace 1,4 por salida. Modelo: 79,4 % de Over 1.5 y 55,5 % de Over 2.5.",[]),
]
FUENTES=[
 ("Sports Mole · Crystal Palace vs Nottingham Forest","https://www.sportsmole.co.uk/football/crystal-palace/preview/crystal-palace-vs-nottm-forest-prediction-team-news-lineups_606578.html"),
 ("Pazzidifanta · Sassuolo-Milan, probabili formazioni","https://www.pazzidifanta.com/news/sassuolo-milan-probabile-formazione-6a-giornata-serie-a-2026-2027-459799"),
 ("Fútbol Total · Atlético MG vs Santos","https://futboltotal.futbol/partido/atletico-mg-vs-santos-campeonato-brasileno-de-serie-a-2026-10-11"),
 ("Primicias · Fecha 2 del hexagonal final","https://www.primicias.ec/deportes/ligapro/fecha-2-hexagonal-final-boletos-copa-libertadores-134545/"),
 ("Claro Sports · Pumas busca revancha","https://www.clarosports.com/us/cruz-azul-vuelve-a-donde-fue-campeon-pumas-busca-revancha-de-la-final-del-clausura-2026/"),
 ("Khel Now · Liverpool vs Manchester City","https://khelnow.com/football/liverpool-vs-manchester-city-preview-premier-league-202610"),
 ("Primicias · LDU vs Barcelona SC","https://www.primicias.ec/deportes/ligapro/liga-de-quito/ldu-barcelonasc-venta-entradas-precios-fecha2-primer-hexagonal-134100/"),
 ("Tribuna de Jundiaí · Corinthians para el clásico","https://tribunadejundiai.com.br/mais/esportes/corinthians-prepara-comissao-emergencial-para-classico/"),
]
idx={key(p):p for p in P}

def chips(p):
    c,t=cat(p['over15'])
    return f'<span class="badge {c}">{t}</span>'
def stats(p):
    pjL,gfL,gcL=p['casa']; pjV,gfV,gcV=p['fuera']
    return f'''<div class="nga"><div class="nga-h">Nova Gol Analytics · datos del partido</div>
<div class="nga-g"><div><b>{e(n(p['local']))}</b> en casa<span>{f1(gfL/pjL)} GF · {f1(gcL/pjL)} GC por partido · {pjL} PJ</span></div>
<div><b>{e(n(p['visita']))}</b> fuera<span>{f1(gfV/pjV)} GF · {f1(gcV/pjV)} GC por partido · {pjV} PJ</span></div>
<div><b>Goles esperados</b><span>{f1(p['lambda_local'])} + {f1(p['lambda_visita'])} = {f1(p['goles_esperados'])}</span></div>
<div><b>Media de la liga</b><span>{f1(p['HG'])} local · {f1(p['AG'])} visitante</span></div></div></div>'''

from enlaces import LINK, PRED, DEST, COL
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
def card(k,big=False):
    p=idx[k]; tit,medio,url=LINK[k]
    return f'''<article class="news {'big' if big else ''}" data-ko="{p['hora']}"><a class="nl" href="{url}" target="_blank" rel="noopener">{img(p)}</a>
<div class="nb"><div class="news-top">{chips(p)}<span class="live" hidden>En juego / jugado</span></div>
<h3><a href="{url}" target="_blank" rel="noopener">{e(tit)}</a></h3>
<div class="src">{e(medio)} · <a href="{url}" target="_blank" rel="noopener">Leer la noticia ↗</a></div>
<div class="odds"><div class="odd"><span>Over 1.5</span><b>{f1(p['over15'])}%</b></div><div class="odd"><span>Over 2.5</span><b>{f1(p['over25'])}%</b></div><div class="odd"><span>Marc.</span><b>{p['marcador']}</b></div></div></div></article>'''
top=max(P,key=lambda p:p['over15'])
sec1=''.join(card(k) for k in PRED if k!=key(top))
sec2=''.join(card(k) for k in DEST)

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
<div class="ev-o"><div class="odd {'hot' if p['over15']>=80 else ''}"><span>O1.5</span><b>{f1(p['over15'])}</b></div><div class="odd {'hot' if p['over25']>=65 else ''}"><span>O2.5</span><b>{f1(p['over25'])}</b></div><div class="odd"><span>Marc.</span><b>{p['marcador']}</b></div></div>
<div class="ev-c">{chips(p)}</div></summary>{stats(p)}</details>'''

SIN=['Juventud LP–Racing (Uruguay)','Benfica–Vitória Guimarães','San Lorenzo–Riestra','Cerro Largo–Albion','UTC–Sporting Cristal','Coquimbo–Colo Colo','Rubio Ñu–Olimpia','Platense–Argentinos','Rosario Central–Ind. Rivadavia','Sport Boys–Alianza Atlético','Jaguares–Tolima','Racing–Belgrano','Libertad–Guaraní','Escorpiones–Saprissa','St. Louis–LA Galaxy','Cusco–Alianza Lima','Talleres–Independiente','América–Medellín']
fu=''.join(f'<li id="f{i+1}"><a href="{u}" target="_blank" rel="noopener">{e(t)}</a></li>' for i,(t,u) in enumerate(FUENTES))

FOTO=base64.b64encode(open('../assets/presentadora.jpg','rb').read()).decode()
top=max(P,key=lambda p:p['over15'])
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
.badge.elite{{background:linear-gradient(180deg,var(--gold2),var(--gold));color:#1b1403}} .badge.r70{{color:var(--muted)}} .badge.r00{{color:var(--chip0);background:transparent;border:1px solid var(--line)}}
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
@media (max-width:400px){{.logo small{{display:none}} .bar-in{{gap:10px}} .bar .cta{{font-size:12px;padding:6px 8px}} .bar .logo{{font-size:17px}}}}
/* home */.home{{display:inline-flex;align-items:center;gap:6px;background:#e6b84a;color:#1b1403;font:700 14px system-ui,sans-serif;padding:8px 12px;border-radius:999px;text-decoration:none;flex-shrink:0}}.home:hover{{background:#fff1b8}}
.fab{{position:fixed;right:16px;bottom:calc(16px + env(safe-area-inset-bottom,0px));z-index:9;width:52px;height:52px;border-radius:50%;display:grid;place-items:center;background:#e6b84a;color:#1b1403;box-shadow:0 6px 20px rgba(0,0,0,.45),0 0 0 2px #0e1c16;text-decoration:none}}.fab svg{{width:24px;height:24px}}.fab:hover{{background:#fff1b8}}
.hide{{display:none}}
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
<nav class="menu" aria-label="Principal"><a href="#predicciones">Predicciones</a><a href="#destacados">Destacados</a><a href="#partidos">Partidos</a><a href="/galeria.html">Galería</a></nav>
<a class="cta" href="#fundadores">Miembro Fundador</a></div></header>
<div class="tabs"><div class="tabs-in" role="tablist"><a class="tabl" href="/galeria.html">★ Galería de aciertos</a>{tabs}</div></div>
<div class="wrap"><main>
<div class="preview">Vista previa del nuevo diseño de la portada. Datos reales del domingo 11 de octubre; se integrará al portal cuando llegue el código.</div>
<section class="hero" aria-label="Partido del día"><img src="data:image/jpeg;base64,{FOTO}" alt="Presentadora de Gol Élite Pro">
<div class="hero-b"><div class="hero-k">Partido con mayor probabilidad del día</div>
<h2>{e(n(top['local']))} vs {e(n(top['visita']))}</h2>
<div class="vsx">{NOM[top['liga']]} · <span class="hk">{top['hora']} ECU</span> {chips(top)}</div>
<div class="odds"><div class="odd hot"><span>Over 1.5</span><b>{f1(top['over15'])}%</b></div><div class="odd hot"><span>Over 2.5</span><b>{f1(top['over25'])}%</b></div><div class="odd"><span>Marcador</span><b>{top['marcador']}</b></div></div>
<p>Probabilidades del modelo Nova Gol 4.0, calculadas con datos de local y visitante. Referencia estadística, no garantía.</p><div class="src">{e(LINK[key(top)][1])} · <a href="{LINK[key(top)][2]}" target="_blank" rel="noopener">Leer la noticia del partido ↗</a></div></div></section>
<section id="predicciones"><div class="sh"><h2>Nuestras principales predicciones</h2><p>Over 1.5 de 80 % o más · toca una noticia para leerla en su medio</p></div>
<div class="grid">{sec1}</div></section>
<section id="destacados"><div class="sh"><h2>Lo más importante del domingo</h2><p>Los partidos que más se miran hoy</p></div>
<div class="grid">{sec2}</div></section>
<section id="partidos"><div class="sh"><h2>Partidos del día</h2><p>Toca un partido para ver sus datos de Nova Gol Analytics</p></div>
<div class="book">{rows}</div></section>
</main>
<aside>
<section class="box" id="historial"><h3>Auditoría del sábado 10</h3>
<div class="kpis"><div class="kpi g"><b>5/5</b><span>GOL ÉLITE · Over 1.5</span></div><div class="kpi"><b>21/25</b><span>Over 1.5 de 70 % o más (84 %)</span></div><div class="kpi"><b>8/11</b><span>Over 2.5 con señal (73 %)</span></div><div class="kpi"><b>3/29</b><span>Marcadores exactos</span></div></div>
<p class="legal">Fallos: Real Madrid 1-0, Lorient 1-0, Vasco 0-0 y River 1-0. Pronósticos sellados antes de cada partido y nunca modificados.</p><a class="cta" style="margin:0;justify-self:start" href="/galeria.html">Ver galería de aciertos →</a></section>
<section class="box"><h3>Escala Nova Gol 4.0</h3><ul><li><span class="badge elite">GOL ÉLITE</span> Over 1.5 de 90 % o más</li><li><span class="badge r80">Rango 80</span> de 80 % a 89,9 %</li><li><span class="badge r70">Rango 70</span> de 70 % a 79,9 %</li><li><span class="badge r00">Menos de 70</span> no recomendado</li></ul></section>
<section class="box"><h3>Sin pronóstico hoy</h3><p class="legal">Sin datos verificables de local y visitante. No inventamos números.</p><ul>{''.join(f'<li>{e(s)}</li>' for s in SIN)}</ul></section>
<section class="box legal" id="fundadores"><h3>Uso responsable</h3><p>Análisis estadístico informativo para mayores de 18 años. La probabilidad no garantiza resultados ni promete ganancias.</p>
<p>Las noticias enlazan a sus medios de origen. Las imágenes de los partidos son ilustraciones propias de Gol Élite Pro.</p><p>Estadísticas: SoccerSTATS (tablas de local y visitante) y Wikipedia (LigaPro, fase inicial 2026).</p></section>
</aside></div>
<a class="fab" href="/" aria-label="Volver al inicio" title="Inicio"><svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="M3 11.5 12 4l9 7.5V20a1 1 0 0 1-1 1h-5v-6h-6v6H4a1 1 0 0 1-1-1z" fill="currentColor"/></svg></a>
<script>
(function(){{
  // hora actual en Ecuador (UTC-5) para marcar partidos ya iniciados
  var now=new Date(Date.now()-5*3600e3), hm=now.getUTCHours()*60+now.getUTCMinutes(), dia=now.toISOString().slice(0,10);
  if(dia==="2026-10-11"){{document.querySelectorAll('[data-ko]').forEach(function(el){{var t=el.getAttribute('data-ko').split(':');if(hm>=(+t[0])*60+(+t[1])){{var l=el.querySelector('.live');if(l)l.hidden=false;}}}});}}
  var tabs=document.querySelectorAll('.tab');
  tabs.forEach(function(b){{b.addEventListener('click',function(){{tabs.forEach(function(x){{x.classList.remove('on')}});b.classList.add('on');var l=b.getAttribute('data-l');
    document.querySelectorAll('.ev').forEach(function(ev){{ev.classList.toggle('hide',l!=='all'&&ev.getAttribute('data-l')!==l)}});
    document.getElementById('partidos').scrollIntoView({{behavior:'smooth',block:'start'}});}})}});
}})();
</script>'''
open('_portada.html','w',encoding='utf-8').write(out)
print('ok',len(P))

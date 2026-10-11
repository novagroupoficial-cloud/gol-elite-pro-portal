import json, html, re
P=json.load(open('pron.json'))
NOM={'ENG':'Premier League','ITA':'Serie A','FRA':'Ligue 1','ESP':'LaLiga','BRA':'Brasileirão','MEX':'Liga MX','ECU':'LigaPro Ecuador'}
ES={'Nottm Forest':'Nottingham Forest','Bologna':'Bolonia','Nice':'Niza','Strasbourg':'Estrasburgo','Deportivo':'Deportivo La Coruña','Manchester City':'Manchester City','AC Milan':'Milan','Real Betis':'Betis','Marseille':'Marsella','Racing':'Racing Santander','Atletico MG':'Atlético MG','A. San Luis':'Atlético San Luis','Pumas UNAM':'Pumas','Barcelona SC':'Barcelona SC'}
n=lambda x:ES.get(x,x)
f1=lambda v:f"{v:.1f}".replace('.',',')
def porque(p):
    pjL,gfL,gcL=p['casa']; pjV,gfV,gcV=p['fuera']; HG,AG=p['HG'],p['AG']
    a,b=gfL/pjL,gcL/pjL; c,d=gfV/pjV,gcV/pjV
    pro,con=[],[]
    (pro if a>=HG else con).append(f"{n(p['local'])} marca {f1(a)} en casa (media de la liga {f1(HG)})")
    (pro if d>=HG else con).append(f"{n(p['visita'])} recibe {f1(d)} fuera")
    (pro if c>=AG else con).append(f"{n(p['visita'])} marca {f1(c)} fuera (media {f1(AG)})")
    (pro if b>=AG else con).append(f"{n(p['local'])} recibe {f1(b)} en casa")
    if min(pjL,pjV)<=3: con.append(f"muestra corta ({pjL} y {pjV} PJ): el modelo la acerca a la media de la liga")
    s=f"<div class='dato'>{html.escape(n(p['local']))} en casa: {f1(a)} GF y {f1(b)} GC por partido ({pjL} PJ). {html.escape(n(p['visita']))} fuera: {f1(c)} GF y {f1(d)} GC ({pjV} PJ).</div>"
    if pro: s+=f"<div class='pq'><b>A favor de goles:</b> {html.escape('; '.join(pro))}.</div>"
    if con: s+=f"<div class='pq con'><b>Dato en contra:</b> {html.escape('; '.join(con))}.</div>"
    return s
def chip(o25):
    if o25>=75: return '<span class="chip s3">Señal fuerte</span>'
    if o25>=65: return '<span class="chip s2">Señal moderada</span>'
    if o25>=55: return '<span class="chip s1">Señal informativa</span>'
    return ''
G=[('elite','GOL ÉLITE','Over 1.5 de 90 % o más',lambda x:x>=90),('g80','Rango 80 %','Over 1.5 entre 80 % y 89,9 %',lambda x:80<=x<90),
   ('g70','Rango 70 %','Over 1.5 entre 70 % y 79,9 %',lambda x:70<=x<80),('g00','Menos de 70 %','Over 1.5 por debajo de 70 %',lambda x:x<70)]
V=[p for p in P if not p.get('sin')]
sec='';res=''
for cid,tit,sub,c in G:
    ps=sorted([p for p in V if c(p['over15'])],key=lambda p:-p['over15'])
    res+=f'<a class="rc {cid}" href="#{cid}"><span class="rn">{len(ps)}</span><span class="rt">{tit}</span></a>'
    if not ps: continue
    rows=''
    for p in ps:
        rows+=f'''<tr><td class="hora">{p['hora']}</td><td><div class="liga">{NOM[p['liga']]}</div><div class="match">{html.escape(n(p['local']))} <span class="vs">vs</span> {html.escape(n(p['visita']))}</div>{porque(p)}</td>
<td class="num big"><div class="bar"><span style="width:{p['over15']}%"></span></div>{f1(p['over15'])} %</td><td class="num">{f1(p['over25'])} %<div>{chip(p['over25'])}</div></td><td class="num">{f1(p['under25'])} %</td><td class="num">{f1(p['goles_esperados'])}</td><td class="num score">{p['marcador']}</td></tr>'''
    sec+=f'''<section class="grupo {cid}" id="{cid}"><header class="ghead"><h2>{tit}</h2><p>{sub} · {len(ps)} partido{'s' if len(ps)!=1 else ''}</p></header>
<div class="tw"><table><thead><tr><th>Hora<br>ECU</th><th>Partido y por qué</th><th>Over 1.5</th><th>Over 2.5</th><th>Under 2.5</th><th>Goles<br>esperados</th><th>Marcador<br>probable</th></tr></thead><tbody>{rows}</tbody></table></div></section>'''
SIN=[('09:00','Juventud de Las Piedras vs Racing Montevideo','Uruguay'),('12:00','Benfica vs Vitória Guimarães','Liga Portugal'),('12:45','San Lorenzo vs Deportivo Riestra','Argentina'),('13:00','Cerro Largo vs Albion','Uruguay'),('13:00','UTC Cajamarca vs Sporting Cristal','Perú'),('13:00','Coquimbo Unido vs Colo Colo','Chile'),('15:00','Rubio Ñu vs Olimpia','Paraguay'),('15:00','Platense vs Argentinos Juniors','Argentina'),('15:00','Rosario Central vs Independiente Rivadavia','Argentina'),('15:30','Sport Boys vs Alianza Atlético','Perú'),('16:05','Jaguares de Córdoba vs Deportes Tolima','Colombia'),('17:15','Racing Club vs Belgrano','Argentina'),('17:20','Libertad vs Guaraní','Paraguay'),('18:00','Escorpiones Belén vs Saprissa','Costa Rica'),('18:00','St. Louis City vs LA Galaxy','MLS'),('18:30','Cusco FC vs Alianza Lima','Perú'),('19:30','Talleres vs Independiente','Argentina'),('20:15','América de Cali vs Independiente Medellín','Colombia')]
sin=''.join(f"<li><span class='hora'>{h}</span> <b>{html.escape(m)}</b> <span class='liga'>{l}</span></li>" for h,m,l in SIN)
src=open('../artifact-files/9706a553-a9aa-4c21-a041-3157889e7c68/index.html',encoding='utf-8').read()
css=src[src.index('<style>\n/* Layout'):src.index('</style>',src.index('<style>\n/* Layout'))]
css+='''.pq{font-size:14px;margin-top:4px;max-width:62ch;color:var(--ink)}
.pq b{color:var(--pitch);font-weight:600}.pq.con b{color:var(--gold)}
</style>'''
out=f'''<title>Nova Gol 4.0 · 11 de octubre</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">
{css}
<div class="wrap">
<header class="top"><div class="eyebrow">Nova Gol Analytics · Modelo Nova Gol 4.0</div>
<h1>Pronósticos del domingo 11 de octubre de 2026</h1>
<p>{len(V)} partidos con pronóstico, agrupados por la probabilidad de Over 1.5, cada uno con sus datos a favor y en contra. Pronósticos sellados entre las 07:33 y las 07:41, hora de Ecuador, antes del inicio de cada partido. No se modificarán: mañana se agrega el resultado real para la auditoría.</p></header>
<nav class="resumen" aria-label="Resumen por rango">{res}</nav>
{sec}
<div class="cols">
<section class="box"><h2>Sin pronóstico por falta de datos</h2>
<p>No conseguí estadísticas verificables de local y visitante para estos partidos, y el modelo no inventa datos. Si tu app los muestra, mándame la previa y los agrego antes del inicio.</p>
<ul>{sin}</ul></section>
<section class="box"><h2>Cómo leer la tabla</h2><ul>
<li><b>Over 1.5</b>: 2 goles o más. <b>Over 2.5</b>: 3 o más. <b>Under 2.5</b>: 2 o menos.</li>
<li><b>GF/GC</b>: goles a favor y en contra por partido. <b>PJ</b>: partidos jugados en esa condición.</li>
<li><b>A favor de goles</b>: datos por encima de la media de la liga que empujan el pronóstico. <b>Dato en contra</b>: lo que podría hacerlo fallar.</li>
<li>Over 2.5: señal fuerte desde 75 %, moderada desde 65 %, informativa desde 55 %.</li>
<li>El marcador probable es la celda más probable del modelo: es orientativo y acierta pocas veces (3 de 29 el sábado).</li></ul></section>
</div>
<section class="box legal"><h2>Notas del modelo y fuentes</h2>
<p>Probabilidades estimadas con datos históricos de referencia (Poisson con corrección Dixon-Coles). No son una garantía de resultado. Contenido para mayores de 18 años; úsalo con criterio. No se usaron xG ni cuotas, así que su peso se repartió entre los datos de goles.</p>
<p>Fuentes: SoccerSTATS, tablas de local y visitante (Premier League, Serie A, Ligue 1, LaLiga, Brasileirão y Liga MX Apertura), con la última actualización disponible el 11 de octubre; en Premier, Serie A y Ligue 1 esa actualización puede ir algunas jornadas atrás. LigaPro Ecuador: Fase Inicial 2026 completa (Wikipedia, cuadro de resultados), porque el hexagonal recién empieza. Cada tabla se verificó: los goles a favor en casa de la liga cuadran con los goles en contra fuera.</p></section>
</div>'''
open('../pub/nova-gol-11-octubre.html','w',encoding='utf-8').write(out)
print(len(V), len(SIN))

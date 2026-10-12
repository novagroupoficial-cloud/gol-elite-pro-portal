"""Refresco horario: ranking del día (de mayor a menor Over 1.5) con estado y resultado.
Uso: python3 tools/refresco.py AAAA-MM-DD
Lee  data/<fecha>/pronosticos.json (sellado, nunca se modifica) y data/<fecha>/resultados-en-vivo.json (provisional).
Escribe public/api/hoy.json (feed del Dashboard) y tools/ranking.html (bloque que portal.py inserta en la portada).
Después: python3 tools/portal.py && python3 tools/envolver.py"""
import json, os, sys, html, datetime as dt
os.chdir(os.path.dirname(os.path.abspath(__file__)))
F=sys.argv[1]
ahora=dt.datetime.now(dt.timezone.utc).replace(tzinfo=None)-dt.timedelta(hours=5)
P=[p for p in json.load(open(f'../data/{F}/pronosticos.json',encoding='utf-8')) if not p.get('sin')]
SIN=[p for p in json.load(open(f'../data/{F}/pronosticos.json',encoding='utf-8')) if p.get('sin')]
rp=f'../data/{F}/resultados-en-vivo.json'
R={f"{r['local']}|{r['visita']}":r for r in (json.load(open(rp,encoding='utf-8')) if os.path.exists(rp) else [])}
NOM={'ENG':'Premier League','ESP':'LaLiga','ITA':'Serie A','GER':'Bundesliga','FRA':'Ligue 1','NED':'Eredivisie','POR':'Liga Portugal','BRA':'Brasileirão','MEX':'Liga MX','USA':'MLS','ECU':'LigaPro','ARG':'Liga Profesional','COL':'Liga BetPlay','PER':'Liga 1','CHI':'Liga de Primera'}
ES={'Coventry':'Coventry City','Newcastle':'Newcastle United','Lanus':'Lanús','Velez Sarsfield':'Vélez Sarsfield','Gimnasia Mendoza':'Gimnasia (Mendoza)','Newells Old Boys':"Newell's Old Boys",'Bragantino':'Red Bull Bragantino','Athletico-PR':'Athletico Paranaense','Atletico MG':'Atlético MG','Nottm Forest':'Nottingham Forest','AC Milan':'Milan'}
n=lambda x:ES.get(x,x); e=html.escape; f1=lambda v:f"{v:.1f}".replace('.',',')
def estado(p):
    r=R.get(f"{p['local']}|{p['visita']}")
    if r and r['estado']=='terminado':
        gl,gv=map(int,r['resultado'].split('-')); g=gl+gv
        return dict(estado='terminado',resultado=r['resultado'],goles=g,acierto_over15=g>=2,acierto_over25=g>=3,
                    marcador_exacto=r['resultado']==p['marcador'],fuente=r['fuente'])
    if r and r['estado']=='anulado': return dict(estado='anulado',resultado=None,fuente=r.get('fuente'))
    h,m=map(int,p['hora'].split(':')); ko=ahora.replace(hour=h,minute=m,second=0,microsecond=0)
    return dict(estado='en juego / sin confirmar' if ahora>=ko and ahora.strftime('%Y-%m-%d')==F else 'por jugar',resultado=None)
rank=sorted(P,key=lambda p:(-p['over15'],p['hora']))
items=[]
for i,p in enumerate(rank,1):
    s=estado(p)
    items.append(dict(puesto=i,hora_ecuador=p['hora'],liga=NOM.get(p['liga'],p['liga']),local=p['local'],visitante=p['visita'],
      over15=p['over15'],over25=p['over25'],marcador=p['marcador'],goles_esperados=p['goles_esperados'],categoria=p['categoria'],
      senal_over25=p['senal_o25'],casa_local=dict(zip(['pj','gf','gc'],p['casa'])),fuera_visitante=dict(zip(['pj','gf','gc'],p['fuera'])),
      sellado=p.get('sellado'),**s))
term=[x for x in items if x['estado']=='terminado']
t70=[x for x in term if x['over15']>=70]; s65=[x for x in term if x['over25']>=65]
resumen=dict(terminados=len(term),total=len(items),over15_70=[sum(x['acierto_over15'] for x in t70),len(t70)],
             over25_senal=[sum(x['acierto_over25'] for x in s65),len(s65)],marcadores_exactos=sum(x['marcador_exacto'] for x in term))
stamp=ahora.strftime('%H:%M')
feed=dict(fecha=F,actualizado=f"{F} {stamp} ECU (UTC-5)",zona_horaria='America/Guayaquil (UTC-5)',modelo='Nova Gol 4.0 (Poisson + Dixon-Coles)',
  fuente_sellada=f'data/{F}/pronosticos.json',aviso='+18 · Probabilidades estadísticas, no garantías. Resultados provisionales hasta la auditoría oficial.',
  orden='de mayor a menor Over 1.5',resumen_del_dia=resumen,
  rango_80_90=[x for x in items if 80<=x['over15']<=90],todos=items,sin_pronostico=[f"{p['local']} vs {p['visita']}" for p in SIN])
os.makedirs('../public/api',exist_ok=True)
json.dump(feed,open('../public/api/hoy.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
def chip(x):
    if x['estado']=='terminado':
        ok=x['acierto_over15']
        return f'<a class="rk-st {"ok" if ok else "ko"}" href="{e(x["fuente"])}" target="_blank" rel="noopener">Final {x["resultado"]} {"✔" if ok else "✘"}</a>'
    if x['estado']=='anulado': return '<span class="rk-st">Anulado</span>'
    if x['estado'].startswith('en juego'): return '<span class="rk-st live">En juego</span>'
    return f'<span class="rk-st">{x["hora_ecuador"]} ECU</span>'
filas=''.join(f'''<div class="rk-row"><span class="rk-n">{x["puesto"]}</span><div class="rk-m"><b>{e(n(x["local"]))} vs {e(n(x["visitante"]))}</b><span>{e(x["liga"])} · {x["hora_ecuador"]} ECU</span></div>
<div class="rk-o"><span>O1.5</span><b class="{"hot" if x["over15"]>=80 else ""}">{f1(x["over15"])}%</b></div><div class="rk-o"><span>O2.5</span><b>{f1(x["over25"])}%</b></div>{chip(x)}</div>''' for x in items)
a,b=resumen['over15_70']
tally=f'Terminados: {len(term)} de {len(items)} · Over 1.5 de 70 % o más: {a}/{b}' if term else 'Aún no termina ningún partido'
css='''<style>.rk{background:var(--panel);border:1px solid var(--line);border-radius:6px;overflow:hidden}
.rk-row{display:grid;grid-template-columns:30px minmax(0,1fr) 74px 74px 118px;gap:10px;align-items:center;padding:10px 14px;border-bottom:1px solid var(--line)}
.rk-row:last-child{border-bottom:0}.rk-n{font-family:var(--disp);font-size:22px;font-weight:800;color:var(--gold)}
.rk-m{display:grid;min-width:0}.rk-m b{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.rk-m span{font-size:12px;color:var(--muted)}
.rk-o{display:grid;text-align:center;background:var(--odd);border-radius:4px;padding:4px}.rk-o span{font-size:11px;color:var(--muted)}.rk-o b{font-family:var(--disp);font-size:19px}.rk-o b.hot{color:var(--acc)}
.rk-st{font-size:13px;font-weight:700;text-align:center;border-radius:4px;padding:6px 4px;background:var(--odd);color:var(--muted);text-decoration:none;white-space:nowrap}
.rk-st.ok{background:var(--odd-hot);color:var(--acc)}.rk-st.ko{background:#3a1d19;color:#f0998b}.rk-st.live{color:#e0b34a}
@media (max-width:640px){.rk-row{grid-template-columns:26px minmax(0,1fr) 64px 64px;}.rk-st{grid-column:2/-1}}</style>'''
frag=f'''{css}<section id="ranking"><div class="sh"><h2>Ranking del día</h2><p>Todos los pronósticos de hoy, de mayor a menor Over 1.5 · actualizado {stamp} ECU · {tally}</p></div>
<div class="rk">{filas}</div><p class="legal" style="margin-top:8px">Over 1.5 = 2 goles o más en el partido · Over 2.5 = 3 goles o más. Probabilidades selladas en la mañana (nunca se cambian); el resultado se agrega cada hora con enlace a su fuente y es provisional hasta la auditoría oficial. +18 · Probabilidades estadísticas, no garantías.</p></section>'''
marca='<!--partidos:'+';'.join(sorted(f"{p['local']}|{p['visita']}" for p in P))+'-->'
open('ranking.html','w',encoding='utf-8').write(marca+'\n'+frag)
print('ranking', stamp, tally)

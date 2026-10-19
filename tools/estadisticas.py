"""Estadísticas de los partidos GOL ÉLITE (Over 1.5 >= 95) y GOLES PLATINO (90 a 94,9), mientras el Dashboard no entregue.
Uso: python3 tools/estadisticas.py AAAA-MM-DD
Lee lo sellado (no cambia ninguna probabilidad) y escribe data/<fecha>/estadisticas.json y public/api/estadisticas.json
según tools/contrato-estadisticas.md. Lo no verificado queda en null."""
import json, os, sys, datetime as dt
from math import exp, factorial
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from nova_gol_4 import RHO, MAXG, categoria_o15, entero
F=sys.argv[1]; MIN=int(sys.argv[2]) if len(sys.argv)>2 else 80  # umbral de Over 1.5 redondeado
H=json.load(open('../public/api/hoy.json',encoding='utf-8'))
S={(p['local'],p['visita']):p for p in json.load(open(f'../data/{F}/pronosticos.json',encoding='utf-8')) if not p.get('sin')}
po=lambda k,l: exp(-l)*l**k/factorial(k)
def tau(i,j,a,b):
    return {(0,0):1-a*b*RHO,(0,1):1+a*RHO,(1,0):1+b*RHO,(1,1):1-RHO}.get((i,j),1.0)
def grid(a,b):
    g={(i,j):po(i,a)*po(j,b)*tau(i,j,a,b) for i in range(MAXG+1) for j in range(MAXG+1)}
    s=sum(g.values()); return {k:v/s for k,v in g.items()}
r1=lambda x: round(x*100,1)
def stats(t,cond,media_liga_gf,media_liga_gc):
    pj,gf,gc=t
    return dict(condicion=cond,pj=pj,gf_pj=round(gf/pj,2) if pj else None,gc_pj=round(gc/pj,2) if pj else None,
                goles_pj=round((gf+gc)/pj,2) if pj else None,
                indice_ataque=round(gf/pj/media_liga_gf,2) if pj else None,
                indice_defensa=round(gc/pj/media_liga_gc,2) if pj else None,
                ultimos5=None,temporada=None)
out=[];
elite=[p for p in H['todos'] if entero(p['over15'])>=MIN]
for p in elite:
    s=S[(p['local'],p['visitante'])]
    a,b=s['lambda_local'],s['lambda_visita']; g=grid(a,b)
    tot=lambda f: sum(v for (i,j),v in g.items() if f(i,j))
    dist=[r1(tot(lambda i,j,n=n:i+j==n)) for n in range(7)]+[r1(tot(lambda i,j:i+j>=7))]
    top=sorted(g.items(),key=lambda kv:-kv[1])[:6]
    L=stats(s['casa'],'en casa',s['HG'],s['AG']); V=stats(s['fuera'],'fuera',s['AG'],s['HG'])
    claves=[f"{p['local']} en casa: {L['gf_pj']:.2f} goles a favor y {L['gc_pj']:.2f} en contra por partido ({L['pj']} PJ)".replace('.',','),
            f"{p['visitante']} fuera: {V['gf_pj']:.2f} a favor y {V['gc_pj']:.2f} en contra por partido ({V['pj']} PJ)".replace('.',','),
            f"Sus partidos promedian {L['goles_pj']:.1f} y {V['goles_pj']:.1f} goles".replace('.',','),
            f"Goles esperados por el modelo: {s['goles_esperados']:.1f}".replace('.',','),
            f"Ambos marcan: {r1(tot(lambda i,j:i>0 and j>0)):.0f} %"]
    out.append(dict(hora_ecuador=p['hora_ecuador'],liga=p['liga'],local=p['local'],visitante=p['visitante'],
        over15=p['over15'],over25=p['over25'],marcador=p['marcador'],goles_esperados=s['goles_esperados'],
        categoria=categoria_o15(p['over15']),senal_over25=p['senal_over25'],destacado=False,
        lambda_local=a,lambda_visita=b,
        modelo_extra=dict(over05=r1(tot(lambda i,j:i+j>=1)),over35=r1(tot(lambda i,j:i+j>=4)),over45=r1(tot(lambda i,j:i+j>=5)),
            ambos_marcan=r1(tot(lambda i,j:i>0 and j>0)),gana_local=r1(tot(lambda i,j:i>j)),empate=r1(tot(lambda i,j:i==j)),
            gana_visit=r1(tot(lambda i,j:i<j)),distribucion=dist,marcadores_top6=[[f"{i}-{j}",r1(v)] for (i,j),v in top]),
        media_liga=dict(local=s['HG'],visitante=s['AG']),
        local_stats=L,visitante_stats=V,referencia_1x2=None,h2h=[],datos_clave=claves,
        fuentes=[s['fuente_datos']],corte_datos=s['sellado'][:10]))
if out: max(out,key=lambda x:x['over15'])['destacado']=True
ahora=(dt.datetime.now(dt.timezone.utc).replace(tzinfo=None)-dt.timedelta(hours=5)).strftime('%Y-%m-%d %H:%M')
J=dict(fecha=F,generado_ecuador=f"{ahora} ECU (UTC-5)",fuente_pronosticos="public/api/hoy.json",modelo="GOL ÉLITE PRO 4.0 (Nova Gol 4.0)",
       generado_por="Claude (provisional mientras el Dashboard Gol 4.0 no entregue)",
       criterio=f"Over 1.5 redondeado de {MIN} % o más",
       aviso="+18 · Probabilidades estadísticas, no garantías.",partidos=out,sin_estadisticas=[])
for f in (f'../data/{F}/estadisticas.json','../public/api/estadisticas.json'):
    json.dump(J,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
for x in out: print(x['hora_ecuador'],x['local'],'-',x['visitante'],x['over15'],x['modelo_extra']['ambos_marcan'],x['modelo_extra']['over35'],x['modelo_extra']['gana_local'],x['modelo_extra']['empate'],x['modelo_extra']['gana_visit'],x['local_stats']['pj'],x['visitante_stats']['pj'])

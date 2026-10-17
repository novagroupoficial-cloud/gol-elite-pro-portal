"""Láminas del carrusel con el recuadro nuevo "LA NOTICIA DEL PARTIDO" (Marco, 17-oct-2026).
Uso: python3 tools/slides.py AAAA-MM-DD "HH:MM"   -> redes/<fecha>/laminas/NN-local-visita.html (+ PNG con png.mjs)
Lee public/api/estadisticas.json (GOL ÉLITE, GOLES PLATINO, GOLES ESTÁNDAR) y data/<fecha>/noticias.json.
Solo partidos que empiezan a la hora indicada o después. Porcentajes con el redondeo de Marco (,5 sube)."""
import json, os, sys, base64, html, re
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from nova_gol_4 import entero, categoria_o15
from enlaces import COL
F=sys.argv[1]; DESDE=sys.argv[2] if len(sys.argv)>2 else '00:00'
J=json.load(open('../public/api/estadisticas.json',encoding='utf-8'))
NOT=json.load(open(f'../data/{F}/noticias.json',encoding='utf-8'))['partidos']
e=html.escape; pc=lambda v:str(entero(v)); f2=lambda v:f"{v:.2f}".replace('.',',')
ES={'Bayern Munich':'Bayern Múnich','Newcastle United':'Newcastle','Philadelphia':'Philadelphia Union','Charlotte':'Charlotte FC','Atletico MG':'Atlético-MG',
    'New England':'New England','Sporting KC':'Sporting KC','A. San Luis':'Atlético San Luis','Leon':'León','America':'América','Seattle':'Seattle Sounders',
    'Portland':'Portland Timbers','Juarez':'FC Juárez','Independiente Rivadavia':'Ind. Rivadavia','Independiente del Valle':'Ind. del Valle','Sparta Rotterdam':'Sparta Rotterdam'}
n=lambda x:ES.get(x,x)
DIA={'2026-10-17':'SÁBADO 17 DE OCTUBRE'}.get(F,F)
def _ff(fam,w,f): return '@font-face{font-family:"%s";font-weight:%d;src:url(data:font/woff2;base64,%s) format("woff2")}'%(fam,w,base64.b64encode(open('../assets/fuentes/'+f,'rb').read()).decode())
FUENTES=_ff('Barlow Condensed',700,'barlow-condensed-latin-700-normal.woff2')+_ff('Barlow Condensed',800,'barlow-condensed-latin-800-normal.woff2')+_ff('IBM Plex Sans',400,'ibm-plex-sans-latin-400-normal.woff2')+_ff('IBM Plex Sans',600,'ibm-plex-sans-latin-600-normal.woff2')
def ink(c):
    r,g,b=(int(c[i:i+2],16) for i in (1,3,5)); return '#111' if 0.299*r+0.587*g+0.114*b>150 else '#fff'
def escudo(t,size):
    c=COL.get(t,'#2a3a32'); ini=''.join(w[0] for w in n(t).replace('.','').replace('-',' ').split()[:2]).upper()
    return f'<div class="esc" style="width:{size}px;height:{size}px;background:{c};color:{ink(c)};font-size:{size*.36:.0f}px">{e(ini)}</div>'
CSS='<style>'+FUENTES+'''
*{box-sizing:border-box}body{margin:0}
.l{position:relative;width:1080px;height:1350px;overflow:hidden;color:#eef4ef;font-family:"IBM Plex Sans",sans-serif;
 background:radial-gradient(900px 600px at 50% -80px,#1b6b43 0%,transparent 70%),radial-gradient(500px 400px at 0 100%,#0f4a2c 0%,transparent 70%),#05100b}
.D{font-family:"Barlow Condensed";font-weight:800;text-transform:uppercase;line-height:.95}
.marca{position:absolute;top:34px;left:0;right:0;text-align:center;font-family:"Barlow Condensed";font-weight:800;font-size:54px;letter-spacing:.04em}.marca b{color:#e6b84a}
.cat{position:absolute;top:104px;left:0;right:0;text-align:center}.cat span{display:inline-block;padding:6px 22px;border-radius:99px;font-family:"Barlow Condensed";font-weight:800;font-size:30px;letter-spacing:.08em}
.c-e{background:linear-gradient(180deg,#fff1b8,#e6b84a);color:#1b1403}.c-p{background:linear-gradient(180deg,#f4f7f6,#aebbb6);color:#101815}.c-s{background:#0f3a25;color:#2ee88a;border:2px solid #2ee88a}
.vs{position:absolute;top:170px;left:40px;right:40px;display:grid;grid-template-columns:1fr auto 1fr;align-items:center;gap:20px;text-align:center}
.vs .t{display:flex;flex-direction:column;align-items:center;gap:12px}.vs .nm{font-size:44px}
.esc{border-radius:50%;display:grid;place-items:center;font-family:"Barlow Condensed";font-weight:800;border:5px solid #e6b84a}
.x{font-size:56px;color:#e6b84a}
.sub{position:absolute;top:420px;left:0;right:0;text-align:center;font-family:"Barlow Condensed";font-weight:700;font-size:30px;color:#2ee88a;letter-spacing:.06em}
.caja{position:absolute;left:40px;right:40px;border-radius:22px;padding:22px 30px}
.st{top:476px;background:rgba(5,16,11,.85);border:2px solid #1f4a32}
.st h3,.nt h3{margin:0 0 12px;font-family:"Barlow Condensed";font-weight:800;font-size:32px;letter-spacing:.08em;color:#e6b84a}
.g{display:grid;grid-template-columns:1fr 1fr;gap:10px 26px}.g div{font-size:24px;color:#cfe0d6}.g b{display:block;font-family:"Barlow Condensed";font-weight:800;font-size:44px;color:#fff}
.nt{top:792px;background:linear-gradient(180deg,#2a1d05,#130d02);border:3px solid #e6b84a;box-shadow:0 0 36px rgba(230,184,74,.35)}
.nt .tit{font-family:"Barlow Condensed";font-weight:800;font-size:40px;color:#fff;line-height:1}.nt p{margin:8px 0 0;font-size:25px;line-height:1.3;color:#f3e7c6}.nt small{color:#b59a5b;font-size:18px}
.pr{top:1060px;background:rgba(5,16,11,.92);border:2px solid #2ee88a;display:grid;grid-template-columns:1.25fr 1fr 1fr;gap:10px;text-align:center;padding:16px 20px}
.pr span{display:block;font-size:20px;color:#9fb2a6;letter-spacing:.08em}.pr b{font-family:"Barlow Condensed";font-weight:800;font-size:64px}
.pie{position:absolute;left:0;right:0;bottom:0;padding:14px 40px;background:#030a07;border-top:2px solid #e6b84a;font-size:19px;color:#9fb2a6;text-align:center;line-height:1.35}
</style>'''
def lamina(p):
    k=f"{p['local']}|{p['visitante']}"; nt=NOT[k]; L=p['local_stats']; V=p['visitante_stats']; m=p['modelo_extra']
    cat=categoria_o15(p['over15']); cc={'GOL ÉLITE':'c-e','GOLES PLATINO':'c-p'}.get(cat,'c-s')
    return f'''<!doctype html><meta charset="utf-8">{CSS}<div class="l">
<div class="marca">GOL <b>ÉLITE</b> PRO</div>
<div class="cat"><span class="{cc}">{'★ ' if cat=='GOL ÉLITE' else ''}{e(cat)}</span></div>
<div class="vs"><div class="t">{escudo(p['local'],150)}<div class="D nm">{e(n(p['local']))}</div></div><div class="D x">VS</div><div class="t">{escudo(p['visitante'],150)}<div class="D nm">{e(n(p['visitante']))}</div></div></div>
<div class="sub">{e(p['liga'].upper())} · {DIA} · {e(p['hora_ecuador'])} HORA ECUADOR</div>
<div class="caja st"><h3>ESTADÍSTICAS CLAVE</h3><div class="g">
<div><b>{f2(L['gf_pj'])} / {f2(L['gc_pj'])}</b>{e(n(p['local']))} en casa: goles a favor / en contra por partido ({L['pj']} PJ)</div>
<div><b>{f2(V['gf_pj'])} / {f2(V['gc_pj'])}</b>{e(n(p['visitante']))} de visita: a favor / en contra ({V['pj']} PJ)</div>
<div><b>{pc(m['ambos_marcan'])} %</b>probabilidad de que ambos marquen</div>
<div><b>{f"{p['goles_esperados']:.1f}".replace('.',',')}</b>goles esperados en el partido</div></div></div>
<div class="caja nt"><h3>📰 LA NOTICIA DEL PARTIDO</h3><div class="tit">{e(nt['titular'])}</div><p>{e(nt['texto'])}</p><small>Fuente: {e(nt['fuente'])}</small></div>
<div class="caja pr"><div><span>OVER 1.5</span><b style="color:#2ee88a">{pc(p['over15'])}%</b></div><div><span>OVER 2.5</span><b>{pc(p['over25'])}%</b></div><div><span>MARCADOR</span><b style="color:#e6b84a">{e(p['marcador'])}</b></div></div>
<div class="pie">Over 1.5 = 2 goles o más en el partido, sin importar quién gane · Over 2.5 = 3 goles o más<br>Modelo Nova Gol 4.0 · +18 · Probabilidades estadísticas, no garantías</div></div>'''
if __name__=='__main__':
    sel=[p for p in J['partidos'] if p['hora_ecuador']>=DESDE and f"{p['local']}|{p['visitante']}" in NOT]
    sel.sort(key=lambda p:(-entero(p['over15']),p['hora_ecuador']))
    out=f'../redes/{F}/laminas'; os.makedirs(out,exist_ok=True)
    for i,p in enumerate(sel,1):
        slug=re.sub(r'[^a-z0-9]+','-',(p['local']+'-'+p['visitante']).lower()).strip('-')
        open(f'{out}/{i:02d}-{slug}.html','w',encoding='utf-8').write(lamina(p))
    falt=[f"{p['local']}|{p['visitante']}" for p in J['partidos'] if p['hora_ecuador']>=DESDE and f"{p['local']}|{p['visitante']}" not in NOT]
    print(len(sel),'láminas', '· sin noticia:',falt)

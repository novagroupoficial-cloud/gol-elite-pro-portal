"""Resumen estadístico + prompts por partido con el recuadro "LA NOTICIA DEL PARTIDO" (Marco, 17-oct-2026).
Uso: python3 tools/prompts_noticias.py AAAA-MM-DD "HH:MM"  -> redes/<fecha>/prompts-noticias.md"""
import json, os, re, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from nova_gol_4 import entero, categoria_o15
F=sys.argv[1]; DESDE=sys.argv[2] if len(sys.argv)>2 else '00:00'
J=json.load(open('../public/api/estadisticas.json',encoding='utf-8'))
NOT=json.load(open(f'../data/{F}/noticias.json',encoding='utf-8'))['partidos']
viejo=open(f'../redes/{F}/prompts-carrusel.md',encoding='utf-8').read()
from slides import n, DIA
pc=lambda v:str(entero(v)); f2=lambda v:f"{v:.2f}".replace('.',','); f1=lambda v:f"{v:.1f}".replace('.',',')
def chicas(p):
    import unicodedata
    sn=lambda x:unicodedata.normalize('NFKD',x).encode('ascii','ignore').decode().lower()
    w1=sn(n(p['local']).replace('-',' ').split()[0]); w2=sn(n(p['visitante']).replace('-',' ').split()[0])
    for sec in viejo.split('\n## ')[1:]:
        h=sn(sec.split('\n')[0])
        if w1 in h and w2 in h:
            m=re.search(r'A la izquierda, una mujer.*?(?=Junto al título)',sec,re.S)
            if m: return m.group(0).strip()
    return (f"A la izquierda, una mujer joven adulta (~27 años), sonriente, de medio cuerpo, pose de presentadora deportiva, con una camiseta con los colores tradicionales de {n(p['local'])} y el escudo del club; "
            f"a la derecha, otra mujer joven adulta con una camiseta con los colores tradicionales de {n(p['visitante'])} y el escudo del club "
            "(uniformes 2026 NO verificados en la web: confirmar con la foto oficial de cada club antes de generar). Camisetas con el escudo del club, sin logos de patrocinadores ni marcas de ropa.")
sel=[p for p in J['partidos'] if p['hora_ecuador']>=DESDE and f"{p['local']}|{p['visitante']}" in NOT]
sel.sort(key=lambda p:(-entero(p['over15']),p['hora_ecuador']))
out=[f"# Resumen estadístico y prompts con noticia · {DIA.capitalize()} de 2026",
 "",f"Partidos GOL ÉLITE, GOLES PLATINO y GOLES ESTÁNDAR que empiezan a las {DESDE} ECU o después, de mayor a menor Over 1.5. Pronósticos sellados a las 05:55 ECU; porcentajes redondeados (,5 sube). Datos de local en casa y visitante de visita (temporada actual).",""]
for i,p in enumerate(sel,1):
    k=f"{p['local']}|{p['visitante']}"; nt=NOT[k]; L=p['local_stats']; V=p['visitante_stats']; m=p['modelo_extra']; cat=categoria_o15(p['over15'])
    loc,vis=n(p['local']),n(p['visitante'])
    out+=["---",f"## {i}. {loc} vs {vis} · {p['liga']} · {p['hora_ecuador']} ECU · {cat}" + (" · PARTIDO DEL DÍA" if i==1 else ""),"",
     f"**Pronóstico:** Over 1.5 **{pc(p['over15'])} %** · Over 2.5 **{pc(p['over25'])} %** · marcador {p['marcador']} · goles esperados {f1(p['goles_esperados'])}","",
     "**Resumen estadístico**",
     f"- {loc} en casa: {f2(L['gf_pj'])} goles a favor y {f2(L['gc_pj'])} en contra por partido ({L['pj']} PJ); sus partidos promedian {f1(L['goles_pj'])} goles.",
     f"- {vis} de visita: {f2(V['gf_pj'])} a favor y {f2(V['gc_pj'])} en contra por partido ({V['pj']} PJ); sus partidos promedian {f1(V['goles_pj'])} goles.",
     f"- Ambos marcan {pc(m['ambos_marcan'])} % · Over 3.5 {pc(m['over35'])} % · gana {loc} {pc(m['gana_local'])} %, empate {pc(m['empate'])} %, gana {vis} {pc(m['gana_visit'])} %.",
     *([f"- ⚠️ Muestra chica ({min(L['pj'],V['pj'])} partidos en casa o de visita): la temporada va empezando."] if min(L['pj'],V['pj'])<=3 else []),
     f"- Marcadores más probables: " + ", ".join(f"{s} ({pc(v)} %)" for s,v in m['marcadores_top6'][:3]) + ".",
     "", f"**La noticia del partido:** {nt['titular']}. {nt['texto']} Fuente: [{nt['fuente']}]({nt['url']})." + (f" ⚠️ {nt['verificar']}" if nt.get('verificar') else ""),
     "","**PROMPT DE LA LÁMINA (4:5, 1080 × 1350)**","",
     f"> Póster deportivo vertical 4:5 (1080x1350), estilo infografía premium. Estadio de noche con reflectores verdes, césped brillante y partículas doradas; paleta negro, verde neón y dorado metálico. Arriba, el logo \"GOL ÉLITE PRO\" (ÉLITE en dorado) con corona y, debajo, una etiqueta \"{cat}\". Título dorado: \"{loc.upper()} vs {vis.upper()}\". Subtítulo verde: \"{p['liga'].upper()} · {DIA} · {p['hora_ecuador']} HORA ECUADOR\". {chicas(p)} Junto al título, el escudo oficial de cada equipo, fiel al real, sin deformar.",
     f"> Primero, un panel negro con borde verde titulado \"ESTADÍSTICAS CLAVE\": \"{loc.upper()} EN CASA: {f2(L['gf_pj'])} goles a favor y {f2(L['gc_pj'])} en contra por partido\" · \"{vis.upper()} DE VISITA: {f2(V['gf_pj'])} a favor y {f2(V['gc_pj'])} en contra\" · \"AMBOS MARCAN: {pc(m['ambos_marcan'])} %\" · \"GOLES ESPERADOS: {f1(p['goles_esperados'])}\".",
     f"> Después, un recuadro destacado con fondo café oscuro, borde dorado brillante y un ícono de periódico, titulado \"LA NOTICIA DEL PARTIDO\", con el titular grande en blanco \"{nt['titular']}\" y debajo el texto: \"{nt['texto']}\" y en letra muy pequeña \"Fuente: {nt['fuente']}\".",
     f"> Al final, un panel con borde verde neón titulado \"NUESTRO PRONÓSTICO\": \"OVER 1.5: {pc(p['over15'])}%\" (número enorme en verde neón), \"OVER 2.5: {pc(p['over25'])}%\" (más pequeño, blanco) y \"MARCADOR SUGERIDO: {p['marcador']}\" (grande, en dorado).",
     "> Abajo, un botón dorado \"¡SÍGUENOS!\" y en letra pequeña \"Over 1.5 = 2 goles o más en el partido, sin importar quién gane · Over 2.5 = 3 goles o más · +18 · Probabilidades estadísticas, no garantías\". Texto en español, legible y sin errores.",
     "","**ANTI-PROMPT:** sin logos de patrocinadores, sin marcas de ropa deportiva, sin casas de apuestas; sin escudos deformados, inventados o de otros clubes; sin caras de futbolistas reales; sin poses provocativas; solo mujeres adultas; sin \"apuesta segura\", \"dinero fácil\", \"gana seguro\" ni promesas de ganancia; sin texto en inglés, sin letras deformadas ni números distintos a los indicados.",""]
top=sel[0]; nt=NOT[f"{top['local']}|{top['visitante']}"]; loc,vis=n(top['local']),n(top['visitante'])
out+=["---","## Historia del partido del día (9:16, 1080 × 1920)","",
 f"> Historia vertical 9:16 (1080x1920), estadio de noche verde neón y dorado. Arriba \"GOL ÉLITE PRO\" y \"PARTIDO DEL DÍA\" en dorado grande, con la etiqueta \"{categoria_o15(top['over15'])}\". Escudos oficiales de {loc} y {vis} frente a frente con \"VS\". Una presentadora joven adulta (~27 años), sonriente, de medio cuerpo, con chaqueta negra y blusa verde. Recuadro dorado \"LA NOTICIA DEL PARTIDO\": \"{nt['titular']}\" y debajo \"{nt['texto']}\". Panel final: \"OVER 1.5: {pc(top['over15'])}%\" enorme en verde neón, \"OVER 2.5: {pc(top['over25'])}%\" y \"MARCADOR: {top['marcador']}\". Hora: \"{top['hora_ecuador']} HORA ECUADOR\". Pie: \"Over 1.5 = 2 goles o más · +18 · Probabilidades estadísticas, no garantías\".","",
 "## Reel de 30 segundos (voz femenina ~28 años, español neutro)","",
 "| Tiempo | Imagen | Voz en off |","|---|---|---|",
 f"| 0–3 s | Logo y estadio | \"Hoy, sábado 17, tenemos {len([p for p in sel if entero(p['over15'])>=95])} GOL ÉLITE y {len([p for p in sel if 90<=entero(p['over15'])<95])} GOLES PLATINO por jugar.\" |",
 f"| 3–10 s | Lámina 1 | \"{loc} contra {vis}, a las {top['hora_ecuador']} hora de Ecuador. Over uno punto cinco al {pc(top['over15'])} por ciento… es decir, dos goles o más, sin importar quién gane.\" |",
 f"| 10–17 s | Recuadro de la noticia | \"{nt['texto']}\" |"]
for j,p in enumerate(sel[1:4],2):
    nt2=NOT[f"{p['local']}|{p['visitante']}"]
    out.append(f"| {17+(j-2)*4}–{21+(j-2)*4} s | Lámina {j} | \"{n(p['local'])}–{n(p['visitante'])}: {pc(p['over15'])} por ciento. {nt2['titular'].capitalize()}.\" |")
out+=["| 29–30 s | Cierre | \"Todas las estadísticas en GOL ÉLITE PRO. Más de 18 años; probabilidades, no garantías.\" |","",
 "## Fuentes",""]+[f"- [{NOT[f'{p['local']}|{p['visitante']}']['fuente']} · {n(p['local'])}–{n(p['visitante'])}]({NOT[f'{p['local']}|{p['visitante']}']['url']})" for p in sel]
open(f'../redes/{F}/prompts-noticias.md','w',encoding='utf-8').write('\n'.join(out)+'\n'); print(len(sel),'partidos')

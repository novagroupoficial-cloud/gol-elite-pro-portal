"""Convierte tools/_portada.html (salida de portal.py) en public/index.html:
quita el aviso de vista previa, agrega formulario de Miembros Fundadores (Netlify Forms) y pie legal."""
import re, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
src=open('_portada.html',encoding='utf-8').read()
body=src[src.index('</title>')+8:]
body=re.sub(r'<div class="preview">.*?</div>\n','',body,flags=re.S)
form=open('plantillas/formulario.html',encoding='utf-8').read()
pie=open('plantillas/pie.html',encoding='utf-8').read()
css=open('plantillas/extra.css',encoding='utf-8').read()
body=body.replace('<section class="box legal" id="fundadores">',form+'\n<section class="box legal" id="uso">')
body=body.replace('<script>',pie+'\n<script>',1).replace('href="#fundadores"','href="#fundadores-form"')
head=open('plantillas/head.html',encoding='utf-8').read()
open('../public/index.html','w',encoding='utf-8').write(head+body+'<style>'+css+'</style></body></html>')
print('public/index.html actualizado')

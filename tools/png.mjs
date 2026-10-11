// Renderiza los .html de una carpeta a .png (historia 1080x1920, carrusel 1080x1350).
// Uso: node tools/png.mjs redes/AAAA-MM-DD   (requiere: npm i playwright)
import { chromium } from 'playwright';
import fs from 'fs'; import path from 'path';
const dir=path.resolve(process.argv[2]);
const base='/opt/pw-browsers';
let exe; try{ const d=fs.readdirSync(base).find(x=>x.startsWith('chromium-')); if(d) exe=path.join(base,d,'chrome-linux','chrome'); }catch{}
const b=await chromium.launch(exe&&fs.existsSync(exe)?{executablePath:exe}:{});
for (const f of fs.readdirSync(dir).filter(x=>x.endsWith('.html'))){
  const h=f.startsWith('historia')?1920:1350;
  const p=await b.newPage({viewport:{width:1080,height:h}});
  await p.goto('file://'+path.join(dir,f)); await p.waitForTimeout(800);
  await p.screenshot({path:path.join(dir,f.replace('.html','.png'))}); await p.close();
  fs.unlinkSync(path.join(dir,f));
}
await b.close();

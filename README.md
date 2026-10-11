# Gol Élite Pro · Portal

Portal público de Gol Élite Pro con los pronósticos del modelo **Nova Gol 4.0** (Nova Gol Analytics).

- `public/` — lo que publica Netlify (portada, privacidad, términos, gracias).
- `tools/` — scripts del modelo y del generador de la portada.
  - `nova_gol_4.py` — modelo Over 1.5 / Over 2.5 (Poisson + Dixon-Coles).
  - `datos.py` — tablas de local y visitante del día (PJ, GF, GC) y medias de liga.
  - `correr.py` — calcula los pronósticos del día → `pron.json`.
  - `enlaces.py` — titulares y enlaces de noticias, colores de los equipos.
  - `portal.py` — genera la portada.
- `data/AAAA-MM-DD/` — registro de cada día: pronósticos sellados y auditorías. **Nunca se modifica un pronóstico ya publicado.**
- `assets/` — imágenes propias (presentadora y fotos de equipos generadas por el equipo).

Netlify publica automáticamente cada cambio en la rama `main`.

## Actualización diaria
1. Editar `tools/datos.py` (tablas casa/fuera del día, verificadas) y la lista de partidos en `tools/correr.py`.
2. `python3 tools/correr.py` → `tools/pron.json` (sellar la hora; copiar a `data/AAAA-MM-DD/pronosticos.json`).
3. Editar `tools/enlaces.py` (titular, medio y URL de cada noticia; listas PRED y DEST; colores).
4. `python3 tools/portal.py && python3 tools/envolver.py` → `public/index.html`.
5. Auditoría del día anterior: resultados reales con fuentes → `data/AYER/auditoria.json` y bloque de auditoría en la portada.
6. Commit y push a `main`; Netlify publica solo.

## Galería de aciertos (public/galeria.html)
- Datos en `public/historial/historial.json` (una entrada por jornada auditada: fecha, título, imagen, resumen, aciertos destacados, fallos).
- Imágenes en `public/historial/AAAA-MM-DD.jpg` (la imagen de resultados que sube el equipo; si no hay, la lámina "Así nos fue ayer" del kit).
- Nunca se borran ni editan jornadas pasadas: es la constancia histórica.

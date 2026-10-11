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

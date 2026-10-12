# Contrato · Estadísticas del rango 80–90 % (Dashboard → Portal)

Intercambio diario entre **GOL ÉLITE PRO** (calcula y publica los pronósticos) y el **Dashboard de estadísticas** (skill `gol-elite-estadisticas-80-90`).

## Flujo
1. GOL ÉLITE PRO sella los pronósticos del día y publica `public/api/hoy.json` (lista `rango_80_90`).
2. El Dashboard lee `public/api/hoy.json`. **No recalcula ni cambia** ninguna probabilidad: toma `rango_80_90` tal cual.
3. El Dashboard junta las estadísticas verificadas de esos partidos y escribe:
   - `data/AAAA-MM-DD/estadisticas.json`: registro del día; no se edita después.
   - `public/api/estadisticas.json`: copia del día, la que lee el portal.
4. Commit y push a `main`. Netlify publica `https://gol-elite-pro.netlify.app/api/estadisticas.json`.
5. GOL ÉLITE PRO muestra esas estadísticas en el portal: fichas del día, carrusel con "ESTADÍSTICAS CLAVE" y la historia del partido destacado.

## Esquema de `estadisticas.json`
```json
{
  "fecha": "AAAA-MM-DD",
  "generado_ecuador": "AAAA-MM-DD HH:MM ECU (UTC-5)",
  "fuente_pronosticos": "public/api/hoy.json",
  "modelo": "GOL ÉLITE PRO 4.0 (Nova Gol 4.0)",
  "aviso": "+18 · Probabilidades estadísticas, no garantías.",
  "dashboard_url": "https://claude.ai/artifact/…",
  "partidos": [
    {
      "hora_ecuador": "14:00", "liga": "LaLiga", "local": "Levante", "visitante": "Sevilla",
      "over15": 89.9, "over25": 73.2, "marcador": "1-1", "goles_esperados": 3.8,
      "destacado": true,
      "modelo_extra": {
        "over05": 97.0, "over35": 52.0, "over45": 31.0, "ambos_marcan": 66.0,
        "gana_local": 38.0, "empate": 21.0, "gana_visit": 41.0,
        "distribucion": [2.1, 7.5, 13.6, 18.0, 19.0, 15.9, 11.0, 12.9],
        "marcadores_top6": [["1-1", 9.8], ["1-2", 8.9]]
      },
      "local_stats": {
        "condicion": "en casa", "pj": 2, "gf_pj": 3.5, "gc_pj": 3.0, "goles_pj": 6.5,
        "indice_ataque": 2.01, "indice_defensa": 2.29,
        "ultimos5": [{"fecha": "2026-10-05", "rival": "X", "condicion": "L", "marcador": "2-1", "res": "V"}],
        "temporada": {"pj": 8, "pct_over15": 87.5, "pct_over25": 62.5, "pct_ambos_marcan": 75.0, "vallas_invictas": 1, "sin_marcar": 0}
      },
      "visitante_stats": { "…": "mismo formato, condicion 'fuera'" },
      "referencia_1x2": {"local": 34.8, "empate": 28.8, "visitante": 36.4, "fuente": "proveedor de resultados"},
      "h2h": [],
      "datos_clave": ["Levante promedia 6,5 goles por partido en casa", "…"],
      "fuentes": ["SoccerSTATS (hasta DD-MM)", "proveedor de resultados"],
      "corte_datos": "AAAA-MM-DD"
    }
  ],
  "sin_estadisticas": [{"local": "…", "visitante": "…", "motivo": "sin datos verificables"}]
}
```
- `null` o lista vacía = dato no verificado. Nunca se rellena con estimaciones.
- `datos_clave`: de 3 a 5 frases cortas por partido, listas para el panel "ESTADÍSTICAS CLAVE" del carrusel.
- `destacado`: `true` solo en el partido con el Over 1.5 más alto del rango (va como historia y en primer lugar del carrusel).

## Retroalimentación (día siguiente)
El Dashboard agrega `data/AYER/estadisticas-auditoria.json` con el resultado real de cada partido del rango, el acierto de Over 1.5 y de Over 2.5, y la calibración acumulada del rango 80–90 % (partidos, aciertos y % real frente al % medio pronosticado). GOL ÉLITE PRO puede usarlo en la Galería de aciertos.

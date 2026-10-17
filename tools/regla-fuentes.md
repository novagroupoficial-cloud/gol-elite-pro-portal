# Regla de fuentes de partidos (Marco, 17-oct-2026)

**SportyTrader es la fuente de referencia del calendario** (fecha, hora y si el partido se juega),
porque es la que siguen las casas de apuestas (bet365, etc.).
https://www.sportytrader.com/es/pronosticos/futbol/  (la web muestra la hora UTC-4: restar 1 h para Ecuador)

- Si dos fuentes discrepan en fecha u hora → vale SportyTrader y se descarta la otra.
- Un partido que SportyTrader no publica NO es una discrepancia: se mantiene si otra fuente
  oficial confirma la fecha (SportyTrader no cubre todas las ligas).
- Excepción: si el club o la liga anuncian OFICIALMENTE que el partido ya se jugó o se movió,
  se avisa a Marco antes de pronosticarlo (ej.: NYCFC–LAFC, movido al 6-may-2026).
- Corregir la hora de un partido sellado no cambia el pronóstico: se deja `nota_hora`.

# Escala de categorías (Marco, 17-oct-2026) — reemplaza GOL ÉLITE 95 / GOL ÉLITE / Rango 80 / Rango 70 / Menos de 70
| Over 1.5 | Categoría |
|---|---|
| 95 % o más (tras redondear) | **GOL ÉLITE** |
| 90 a 94 % | **GOLES PLATINO** |
| 80 a 89 % | **GOLES ESTÁNDAR** |
| menos de 80 % | **GOLES OPTIMISTAS** |
Las entradas viejas de la Galería y las auditorías anteriores conservan la escala de su día.

# Redondeo de porcentajes (Marco, 17-oct-2026)
- Decimal ,5 o más → sube al entero siguiente; menos de ,5 → se queda (95,5 → 96 %; 95,4 → 95 %; 94,8 → 95 %; 89,5 → 90 %).
- La categoría se decide con ese entero: 94,8 → 95 % → GOL ÉLITE; 89,8 → 90 % → GOLES PLATINO.
- Se muestra el entero en el portal, Telegram y redes. El archivo sellado (`data/`) conserva el decimal original.
- Funciones: `entero()` en `tools/nova_gol_4.py` y en `netlify/lib/telegram.mjs`.

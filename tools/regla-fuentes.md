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

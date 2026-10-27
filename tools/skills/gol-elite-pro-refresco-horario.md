---
name: gol-elite-pro-refresco-horario
description: "Refresco cada hora del sistema GOL ÉLITE PRO: mantiene el RANKING DEL DÍA (todos los pronósticos de hoy de mayor a menor Over 1.5, con Over 2.5, estado y resultado) en la portada y en el feed del Dashboard (public/api/hoy.json), registra resultados con fuente, reintenta la rutina diaria si no se hizo, integra las estadísticas del Dashboard y vigila que Netlify publique. Si algo falla, queda pendiente para la hora siguiente."
---

# GOL ÉLITE PRO — refresco horario

## 0. Propósito
Mantener el sistema al día entre una rutina diaria y la siguiente, sin esperar a Marco:
- Si la rutina diaria (tarea "Gol Elite Pro diario", 05:24 ECU) no se completó, **reintentarla** en la hora siguiente, y así cada hora hasta lograrlo.
- Registrar, a medida que terminan, los **resultados de los partidos de hoy** con fuente.
- Mantener el **feed del Dashboard** (`public/api/hoy.json`) con pronósticos y resultados.
- Integrar las estadísticas del Dashboard (`public/api/estadisticas.json`) al portal cuando lleguen.
- Vigilar que **Netlify publique** lo que está en `main`.

Cada ejecución es corta e independiente. Lo que no se pueda hacer en una hora (sin conexión, sin créditos, un sitio caído, un resultado aún no publicado) **queda anotado como pendiente** en `data/<HOY>/refresco.json` y la ejecución de la hora siguiente lo retoma. Nunca reintentar en bucle dentro de la misma ejecución.

Relación con otras skills: `gol-elite-pro-trabajo-diario` (rutina completa), `nova-gol-estadistica` (modelo y reglas de auditoría), `nova-dashboard-gol-4` y `tools/contrato-estadisticas.md` (intercambio con el Dashboard). Esta skill no reemplaza ninguna: las coordina.

## 1. Reglas que nunca cambian
- Un pronóstico sellado en `data/` **nunca se modifica** ni se recalcula. Una auditoría ya escrita no se rehace. La Galería nunca se edita hacia atrás.
- Nunca inventar datos ni resultados. Un resultado solo cuenta con **partido terminado** y una **fuente abierta y citada** (URL). Si dos fuentes discrepan, queda "pendiente".
- Over 1.5 acierta con 2+ goles; Over 2.5 con 3+ (90 min + descuento). Aplazado o suspendido = "anulado".
- Hora de referencia: Ecuador (UTC-5). Usar `TZ=America/Guayaquil date`.
- Siempre "+18" y "probabilidades estadísticas, no garantías". Prohibido "apuesta segura", "dinero fácil", "gana seguro".
- Commits con autor "Nova Group" <novagroup.oficial@gmail.com>. Hacer `git pull --rebase` justo antes de cada push (otras sesiones y el Dashboard escriben en `main`). Sin commits vacíos: si no cambió nada, no se hace commit.
- La web solo con WebSearch/WebFetch. Si un sitio pide permiso o falla, no usar curl ni Python para saltarlo: probar otra fuente o dejarlo pendiente.

## 2. Estado entre horas: `data/<HOY>/refresco.json`
```json
{
  "fecha": "AAAA-MM-DD",
  "ultima_ejecucion": "AAAA-MM-DD HH:MM ECU",
  "ultima_ok": "AAAA-MM-DD HH:MM ECU",
  "rutina_diaria": "hecha | pendiente | en_curso",
  "rutina_diaria_inicio": "AAAA-MM-DD HH:MM ECU o null",
  "pendientes": ["texto corto de cada cosa que quedó para la próxima hora"],
  "deploy": {"ok": true, "fallos_seguidos": 0, "ultima_revision": "HH:MM"},
  "avisos_enviados": ["partido_del_dia", "cierre_del_dia", "deploy", "rutina_recuperada"]
}
```
Se crea en la primera ejecución del día. Se actualiza y se sube en el mismo commit que los demás cambios (si no hay otros cambios, solo se sube si cambió `pendientes`, `rutina_diaria` o `deploy`).

## 3. Pasos de cada hora (en este orden; cortar a los ~40 min y dejar el resto en `pendientes`)
1. **Preparar:** `git clone --depth 20` del repo `novagroupoficial-cloud/gol-elite-pro-portal` (o `git pull`). Fijar HOY y AYER en hora de Ecuador. Leer `data/<HOY>/refresco.json` si existe.
2. **Rutina diaria pendiente.** Si son las 08:00 ECU o más tarde, falta `data/<HOY>/pronosticos.json` y la rutina no está `en_curso` desde hace menos de 120 min:
   - marcar `rutina_diaria: "en_curso"` con hora de inicio, hacer commit y push de inmediato (para que la hora siguiente no la duplique);
   - ejecutar la skill `gol-elite-pro-trabajo-diario` completa, pronosticando solo partidos que aún no empiezan;
   - al terminar, `rutina_diaria: "hecha"` y aviso "rutina_recuperada".
   Si falta solo `data/<AYER>/auditoria.json` (los pronósticos de hoy existen), hacer solo la auditoría y la Galería de ayer (pasos 1 y 1b de la rutina diaria).
3. **Resultados de hoy.** Para cada partido de `data/<HOY>/pronosticos.json` cuya hora de inicio + 2 h 15 min ya pasó y que no tenga resultado registrado:
   - buscar "Equipo A Equipo B result <fecha>" con WebSearch y abrir con WebFetch un informe final (ESPN, medios del país, sitio de la liga). Exigir que diga que terminó.
   - escribir en `data/<HOY>/resultados-en-vivo.json` (lista; solo se AGREGAN partidos, un partido ya registrado no se toca salvo para pasar de "pendiente" a "terminado"):
     `{"local","visita","hora","resultado":"3-3","goles":6,"estado":"terminado|pendiente|anulado","over15_dado","over25_dado","acierto_over15","acierto_over25","marcador_exacto","fuente":"URL","registrado":"HH:MM ECU"}`
   - Este archivo es **provisional**: la auditoría oficial (`auditoria.json`) la escribe la rutina diaria de mañana, que puede reutilizar estas fuentes.
4. **Ranking del día y feed (cada hora, aunque no haya resultados nuevos).** Ejecutar `python3 tools/refresco.py <HOY>` y luego `python3 tools/portal.py && python3 tools/envolver.py`. El script:
   - ordena TODOS los pronósticos sellados de hoy de mayor a menor Over 1.5 (con Over 2.5, marcador, hora y liga);
   - marca cada partido como "por jugar", "en juego" o "Final X-Y ✔/✘" (enlace a la fuente) según `resultados-en-vivo.json`;
   - escribe `public/api/hoy.json` (feed del Dashboard: `todos` en ese orden, `rango_80_90`, `resumen_del_dia`, `actualizado`) y `tools/ranking.html`, que portal.py inserta en la portada como sección "Ranking del día" con la hora de actualización.
   No cambia ninguna probabilidad. Si portal.py falla, no publicar a medias: anotar en `pendientes`.
5. **Estadísticas del Dashboard.** Si `public/api/estadisticas.json` es de HOY, el paso 4 ya lo incluye al regenerar el portal (según `tools/contrato-estadisticas.md`).
6. **Verificar publicación.** WebFetch `https://gol-elite-pro.netlify.app/index` (sin .html, para evitar caché) y comprobar que muestra la fecha de HOY (o la de ayer si aún no corre la rutina diaria). Si no coincide con lo que hay en `main`, sumar `deploy.fallos_seguidos`; si coincide, ponerlo en 0.
7. **Publicar:** si hubo cambios (el ranking cambia de hora cada vez que hay partidos por jugar o en juego, así que normalmente habrá commit mientras dure la jornada), commit "Refresco HH:MM ECU <HOY>: <qué cambió>" y push. Si el push es rechazado, `git pull --rebase` y reintentar una vez; si vuelve a fallar, dejarlo en `pendientes`.

### Día interno (`data/<HOY>/interno.json`)
Si existe, Marco decidió NO publicar los pronósticos de ese día (27-oct-2026: "no vale publicarlos, están muy bajos; solo queda para nosotros y evaluar los resultados"). Los pasos no cambian: se buscan y registran resultados igual y se corren `refresco.py`, `portal.py` y `envolver.py`. Los scripts ya hacen lo demás: el ranking completo va a `data/<HOY>/ranking-interno.json`, `public/api/hoy.json` queda sin partidos y la portada muestra "Hoy no publicamos pronósticos". En el paso 5, comprobar ese aviso en vez del ranking. Los avisos a Marco (fin de partido, cierre del día) se envían igual, porque son internos. No se usa el kit de redes de ese día.

## 4. Cuándo avisar a Marco (PushNotification con `<routine_summary>`)
Solo una vez por motivo y por día (registrar en `avisos_enviados`). El resto de las horas, silencio.
- **partido_del_dia:** cuando termina el partido del día: "Acertamos/Fallamos: <partido> <resultado> · dimos Over 1.5 al X % · hubo N goles".
- **cierre_del_dia:** cuando todos los partidos de hoy están terminados o anulados: aciertos de Over 1.5 de 70 % o más (x/y), Over 2.5 con señal, marcadores exactos y fallos.
- **rutina_recuperada:** si este refresco tuvo que hacer la rutina diaria (o la auditoría) porque la de la mañana no salió.
- **deploy:** si `deploy.fallos_seguidos` llega a 3 (el portal en vivo no refleja `main` durante 3 horas): decir qué fecha muestra la web y qué hay en `main`.
- **bloqueo:** si 3 ejecuciones seguidas no pudieron clonar el repo, hacer push o leer la web: decir qué falla y qué hace falta (permiso, conexión de GitHub, créditos).

## 5. Fallos frecuentes
| Síntoma | Acción |
|---|---|
| Resultado solo en un titular, sin informe final | dejar "pendiente" y reintentar la hora siguiente |
| WebFetch pide permiso y nadie responde | probar otra fuente encontrada con WebSearch; si no hay, "pendiente" |
| La web en vivo muestra otra fecha u otro diseño | contar en `deploy.fallos_seguidos`; no "arreglar" el portal tocando código |
| Push rechazado | `git pull --rebase`, revisar que no se pisen archivos de otra sesión, reintentar una vez |
| La ejecución anterior quedó `en_curso` más de 120 min | considerarla caída y retomar la rutina diaria |

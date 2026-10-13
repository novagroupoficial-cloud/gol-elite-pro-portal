// GOL ÉLITE PRO → Telegram: arma los mensajes a partir del feed public/api/hoy.json
// (el mismo que actualiza cada hora la tarea "Gol Elite Pro refresco horario").
// Nunca recalcula probabilidades: solo copia lo sellado y los resultados con fuente.

export const PORTAL = "https://gol-elite-pro.netlify.app";
const NOTA = "ℹ️ Over 1.5 = 2 goles o más en el partido, sin importar quién gane · Over 2.5 = 3 goles o más.";
const LEGAL = "+18 · Probabilidades estadísticas, no garantías.";
const DIAS = ["domingo", "lunes", "martes", "miércoles", "jueves", "viernes", "sábado"];
const MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"];

export const esc = (s) => String(s ?? "").replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
export const pct = (v) => (typeof v === "number" ? v.toFixed(1).replace(".", ",") + " %" : "—");

// Hora de Ecuador (UTC-5, sin horario de verano)
export function ahoraEcuador(ms = Date.now()) {
  const d = new Date(ms - 5 * 3600e3);
  return { fecha: d.toISOString().slice(0, 10), minutos: d.getUTCHours() * 60 + d.getUTCMinutes() };
}

export function fechaLarga(iso) {
  const [y, m, d] = iso.split("-").map(Number);
  const dt = new Date(Date.UTC(y, m - 1, d));
  return `${DIAS[dt.getUTCDay()]} ${d} de ${MESES[m - 1]}`;
}

export const clave = (p) => `${p.hora_ecuador}|${p.local}|${p.visitante}`;
const terminado = (p) => p.estado === "terminado" && p.resultado;
const anulado = (p) => p.estado === "anulado";

export function mensajeRanking(feed) {
  const filas = (feed.todos || []).slice(0, 20).map((p, i) => {
    const bajo = p.over15 < 70 ? " <i>(menos de 70: no recomendado)</i>" : "";
    return `${i + 1}. <b>${esc(p.hora_ecuador)}</b> · ${esc(p.local)} vs ${esc(p.visitante)} <i>(${esc(p.liga)})</i>\n` +
      `    Over 1.5 <b>${pct(p.over15)}</b> · Over 2.5 ${pct(p.over25)} · Marcador ${esc(p.marcador)}${bajo}`;
  });
  return [
    `⚽ <b>GOL ÉLITE PRO · Pronósticos del ${fechaLarga(feed.fecha)}</b>`,
    `Ranking de mayor a menor Over 1.5 · modelo Nova Gol 4.0 · sellados antes de cada partido (hora de Ecuador).`,
    "",
    filas.join("\n\n"),
    "",
    NOTA,
    `📊 Estadísticas de cada partido: ${PORTAL}`,
    LEGAL,
  ].join("\n");
}

function lineaResultado(p) {
  if (anulado(p)) return `⚪ <b>${esc(p.local)} vs ${esc(p.visitante)}</b> · aplazado o anulado (no cuenta)`;
  const ok = p.acierto_over15 === true;
  const icono = p.over15 < 70 ? (ok ? "☑️" : "▫️") : ok ? "✅" : "❌";
  const o25 = p.acierto_over25 === true ? " · Over 2.5 ✔" : "";
  const exacto = p.marcador_exacto ? " · ¡marcador exacto!" : "";
  const fuente = p.fuente ? ` · <a href="${esc(p.fuente)}">fuente</a>` : "";
  return `${icono} <b>${esc(p.local)} ${esc(p.resultado)} ${esc(p.visitante)}</b>\n` +
    `    Dimos Over 1.5 al ${pct(p.over15)} · hubo ${p.goles === 1 ? "1 gol" : `${p.goles ?? "?"} goles`}${o25}${exacto}${fuente}`;
}

export function mensajeResultados(feed, nuevos) {
  const titulo = nuevos.length === 1 ? "🔔 <b>Resultado final</b>" : `🔔 <b>Resultados finales (${nuevos.length})</b>`;
  return [titulo, "", nuevos.map(lineaResultado).join("\n\n"), "", NOTA, LEGAL].join("\n");
}

export function mensajeCierre(feed) {
  const r = feed.resumen_del_dia || {};
  const [a, n] = r.over15_70 || [0, 0];
  const [a25, n25] = r.over25_senal || [0, 0];
  const fallos = (feed.todos || []).filter((p) => terminado(p) && p.over15 >= 70 && p.acierto_over15 === false)
    .map((p) => `${esc(p.local)} ${esc(p.resultado)} ${esc(p.visitante)} (dimos ${pct(p.over15)})`);
  return [
    `🏁 <b>Cierre del ${fechaLarga(feed.fecha)}</b>`,
    "",
    `Over 1.5 de 70 % o más: <b>${a}/${n}</b>${n ? ` (${Math.round((a * 100) / n)} %)` : ""}`,
    `Over 2.5 con señal: <b>${a25}/${n25}</b>`,
    `Marcadores exactos: <b>${r.marcadores_exactos ?? 0}</b>`,
    fallos.length ? `\nNo se cumplió en: ${fallos.join(" · ")}` : "\nSin fallos en Over 1.5 de 70 % o más.",
    "",
    "Resultados provisionales; la auditoría oficial sale mañana temprano en la Galería.",
    `🏆 Galería de aciertos: ${PORTAL}/galeria.html`,
    LEGAL,
  ].join("\n");
}

// Decide qué enviar. estado = {ranking, resultados:[claves], cierre}
export function pendientes(feed, estado, ahora) {
  const out = [];
  const todos = feed.todos || [];
  if (!estado.ranking && todos.length && feed.fecha === ahora.fecha && ahora.minutos >= 5 * 60 + 30) {
    // El ranking solo tiene sentido antes de que empiecen los partidos de la tarde.
    out.push({ tipo: "ranking", saltar: ahora.minutos > 13 * 60 });
  }
  const enviados = new Set(estado.resultados || []);
  const nuevos = todos.filter((p) => (terminado(p) || anulado(p)) && !enviados.has(clave(p)));
  if (nuevos.length) out.push({ tipo: "resultados", partidos: nuevos });
  const todosCerrados = todos.length > 0 && todos.every((p) => terminado(p) || anulado(p));
  if (!estado.cierre && todosCerrados) out.push({ tipo: "cierre" });
  return out;
}

export async function enviar(token, chat, texto) {
  const r = await fetch(`https://api.telegram.org/bot${token}/sendMessage`, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({ chat_id: chat, text: texto.slice(0, 4000), parse_mode: "HTML", disable_web_page_preview: true }),
  });
  const j = await r.json().catch(() => ({}));
  if (!j.ok) throw new Error(`Telegram respondió: ${j.description || r.status}`);
  return j.result?.message_id;
}

export async function leerFeed() {
  const base = Netlify.env.get("URL") || PORTAL;
  const r = await fetch(`${base}/api/hoy.json?t=${Date.now()}`, { headers: { "cache-control": "no-cache" } });
  if (!r.ok) throw new Error(`No se pudo leer api/hoy.json (${r.status})`);
  return r.json();
}

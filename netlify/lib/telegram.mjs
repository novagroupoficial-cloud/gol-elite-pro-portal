// GOL ÉLITE PRO → Telegram: arma los mensajes a partir del feed public/api/hoy.json
// (el mismo que actualiza cada hora la tarea "Gol Elite Pro refresco horario").
// Nunca recalcula probabilidades: solo copia lo sellado y los resultados con fuente.

export const PORTAL = "https://gol-elite-pro.netlify.app";
const NOTA = "ℹ️ Over 1.5 = 2 goles o más en el partido, sin importar quién gane · Over 2.5 = 3 goles o más.";
const LEGAL = "+18 · Probabilidades estadísticas, no garantías.";
const DIAS = ["domingo", "lunes", "martes", "miércoles", "jueves", "viernes", "sábado"];
const MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"];

export const esc = (s) => String(s ?? "").replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
// Regla de Marco (17-oct-2026): decimal 5 o más sube al entero siguiente (94,5 -> 95; 94,4 -> 94).
export const entero = (v) => Math.floor(Math.round(v * 10) / 10 + 0.5 + 1e-9);
export const categoria = (x) => { const v = entero(x); return v >= 95 ? "💎 GOL ÉLITE" : v >= 90 ? "🥈 GOLES PLATINO" : v >= 80 ? "GOLES ESTÁNDAR" : "GOLES OPTIMISTAS"; };
export const pct = (v) => (typeof v === "number" ? entero(v) + " %" : "—");

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
    const bajo = "";
    return `${i + 1}. <b>${esc(p.hora_ecuador)}</b> · ${esc(p.local)} vs ${esc(p.visitante)} <i>(${esc(p.liga)})</i>\n` +
      `    Over 1.5 <b>${pct(p.over15)}</b> · Over 2.5 ${pct(p.over25)} · Marcador ${esc(p.marcador)} · <b>${categoria(p.over15)}</b>${bajo}`;
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
    `    Dimos Over 1.5 al ${pct(p.over15)} · hubo ${p.goles === 1 ? "1 gol" : `${p.goles ?? "?"} goles`} · ${categoria(p.over15)}${o25}${exacto}${fuente}`;
}

export function mensajeResultados(feed, nuevos) {
  const titulo = nuevos.length === 1 ? "🔔 <b>Resultado final</b>" : `🔔 <b>Resultados finales (${nuevos.length})</b>`;
  return [titulo, "", nuevos.map(lineaResultado).join("\n\n"), "", NOTA, LEGAL].join("\n");
}

const CATS = ["💎 GOL ÉLITE", "🥈 GOLES PLATINO", "GOLES ESTÁNDAR", "GOLES OPTIMISTAS"];
const RANGO = { "💎 GOL ÉLITE": "95 % o más", "🥈 GOLES PLATINO": "90 a 94 %", "GOLES ESTÁNDAR": "80 a 89 %", "GOLES OPTIMISTAS": "menos de 80 %" };
const golesTxt = (g) => (g === 1 ? "1 gol" : `${g} goles`);
const nombre = (p) => `${esc(p.local)} ${esc(p.resultado)} ${esc(p.visitante)}`;

// Resumen del día (Marco, 18-oct-2026): pone en contexto los resultados frente a lo que pronosticamos.
export function mensajeCierre(feed) {
  const fin = (feed.todos || []).filter(terminado);
  const anul = (feed.todos || []).filter(anulado).length;
  const del = [...(feed.todos || [])].sort((a, b) => (a.puesto || 99) - (b.puesto || 99))[0];
  const filas = CATS.map((c) => {
    const xs = fin.filter((p) => categoria(p.over15) === c);
    const a = xs.filter((p) => p.acierto_over15).length;
    return xs.length ? `• <b>${c}</b> (${RANGO[c]}): <b>${a} de ${xs.length}</b> (${Math.round((a * 100) / xs.length)} %)` : null;
  }).filter(Boolean);
  const s25 = fin.filter((p) => entero(p.over25) >= 65);
  const a25 = s25.filter((p) => p.acierto_over25).length;
  const exactos = fin.filter((p) => p.marcador_exacto);
  const altos = fin.filter((p) => entero(p.over15) >= 80);
  const brillos = altos.filter((p) => p.acierto_over15).sort((a, b) => b.goles - a.goles || b.over15 - a.over15).slice(0, 4);
  const fallos = altos.filter((p) => p.acierto_over15 === false);
  const out = [`🏁 <b>RESUMEN DEL ${fechaLarga(feed.fecha).toUpperCase()}</b>`, `${fin.length} partidos terminados${anul ? ` · ${anul} aplazado(s), no cuentan` : ""}.`, ""];
  if (del && terminado(del)) {
    out.push(`⭐ <b>Partido del día:</b> ${nombre(del)} ${del.acierto_over15 ? "✅" : "❌"}`,
      `    Dimos Over 1.5 al ${pct(del.over15)} · Hubo ${golesTxt(del.goles)}`, "");
  }
  out.push("📊 <b>¿Se cumplió el Over 1.5?</b>", ...filas,
    `• Over 2.5 con señal (65 % o más): <b>${a25} de ${s25.length}</b>`,
    `• Marcadores exactos: <b>${exactos.length}</b>${exactos.length ? ` (${exactos.slice(0, 5).map(nombre).join(", ")})` : ""}`, "");
  if (brillos.length) out.push("🔥 <b>Lo mejor del día</b>", ...brillos.map((p) => `• ${nombre(p)}: dimos Over 1.5 al ${pct(p.over15)} · hubo ${golesTxt(p.goles)}`), "");
  if (fallos.length) out.push(`⚠️ <b>No se cumplió (80 % o más):</b> ${fallos.map((p) => `${nombre(p)} (${pct(p.over15)})`).join(" · ")}`, "");
  out.push("Publicamos aciertos y fallos. Auditoría oficial mañana temprano en la Galería.",
    `🏆 ${PORTAL}/galeria.html`, NOTA, LEGAL);
  return out.join("\n");
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

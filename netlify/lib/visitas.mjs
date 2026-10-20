// Resumen de visitas del portal para Marco (mensaje privado de Telegram, nunca al canal).
import { getStore } from "@netlify/blobs";
import { ahoraEcuador, fechaLarga, enviar } from "./telegram.mjs";

const n = (x) => Number(x || 0).toLocaleString("es-EC");

export async function mensajeVisitas() {
  const store = getStore({ name: "visitas", consistency: "strong" });
  const hoy = ahoraEcuador().fecha;
  const ayer = ahoraEcuador(Date.now() - 864e5).fecha;
  const d = (await store.get(`dia-${hoy}`, { type: "json" })) || { visitas: 0, visitantes: 0 };
  const a = await store.get(`dia-${ayer}`, { type: "json" });
  const t = (await store.get("total", { type: "json" })) || { desde: hoy, visitas: 0, visitantes: 0 };

  // Mejor día y total del mes (hasta 60 días hacia atrás)
  let mejor = null, mesV = 0, mesP = 0;
  for (let i = 0; i < 60; i++) {
    const f = ahoraEcuador(Date.now() - i * 864e5).fecha;
    if (f < t.desde) break;
    const x = await store.get(`dia-${f}`, { type: "json" });
    if (!x) continue;
    if (!mejor || x.visitas > mejor.visitas) mejor = x;
    if (f.slice(0, 7) === hoy.slice(0, 7)) { mesV += x.visitas; mesP += x.visitantes; }
  }
  const comp = a ? ` (ayer: ${n(a.visitas)})` : "";
  return [
    `👁 <b>Visitas del portal · ${fechaLarga(hoy)}</b>`,
    ``,
    `Visitas de hoy: <b>${n(d.visitas)}</b>${comp}`,
    `Visitantes de hoy: <b>${n(d.visitantes)}</b>`,
    `Este mes: ${n(mesV)} visitas · ${n(mesP)} visitantes`,
    mejor ? `Mejor día: ${fechaLarga(mejor.fecha)} con ${n(mejor.visitas)} visitas` : null,
    `Total desde el ${t.desde.split("-").reverse().join("/")}: ${n(t.visitas)} visitas`,
    ``,
    `Registro completo: https://gol-elite-pro.netlify.app/api/visitas`,
  ].filter((x) => x !== null).join("\n");
}

// Envía el resumen a Marco. "llave" evita duplicados (un envío por llave).
export async function avisarMarco(llave) {
  const token = Netlify.env.get("TELEGRAM_BOT_TOKEN");
  const marco = Netlify.env.get("TELEGRAM_MARCO_CHAT");
  if (!token || !marco) return { enviado: false, motivo: "Falta TELEGRAM_MARCO_CHAT (o la clave del bot) en Netlify." };
  if (marco === Netlify.env.get("TELEGRAM_CANAL")) return { enviado: false, motivo: "TELEGRAM_MARCO_CHAT no puede ser el canal público." };
  const store = getStore({ name: "visitas", consistency: "strong" });
  if (await store.get(llave)) return { enviado: false, motivo: "Ya enviado." };
  await enviar(token, marco, await mensajeVisitas());
  await store.set(llave, new Date().toISOString());
  return { enviado: true };
}

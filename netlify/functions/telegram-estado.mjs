// /api/telegram-estado — revisa la conexión con Telegram sin mostrar la clave del bot.
//   GET /api/telegram-estado             → ¿hay clave?, ¿hay canal?, nombre del bot y canales donde lo agregaron
//   GET /api/telegram-estado?prueba=1    → envía un mensaje de prueba al canal (máximo uno cada 10 minutos)
import { getStore } from "@netlify/blobs";
import { enviar, ahoraEcuador, PORTAL } from "../lib/telegram.mjs";

const json = (o, status = 200) =>
  new Response(JSON.stringify(o, null, 1), { status, headers: { "content-type": "application/json; charset=utf-8", "cache-control": "no-store" } });

export default async (req) => {
  const token = Netlify.env.get("TELEGRAM_BOT_TOKEN");
  const canal = Netlify.env.get("TELEGRAM_CANAL") || null;
  const out = { token_configurado: Boolean(token), canal_configurado: canal };
  if (!token) return json({ ...out, siguiente_paso: "Guardar TELEGRAM_BOT_TOKEN en Netlify (alcance Functions) y volver a publicar." });

  const api = (m) => fetch(`https://api.telegram.org/bot${token}/${m}`).then((r) => r.json()).catch(() => ({ ok: false }));
  const me = await api("getMe");
  out.bot = me.ok ? `@${me.result.username}` : "la clave no es válida";
  const up = await api("getUpdates?allowed_updates=%5B%22my_chat_member%22%2C%22channel_post%22%5D");
  const vistos = new Map();
  for (const u of up.result || []) {
    const c = u.my_chat_member?.chat || u.channel_post?.chat;
    if (c && c.type === "channel") vistos.set(c.id, { id: c.id, titulo: c.title, usuario: c.username ? `@${c.username}` : null });
  }
  out.canales_donde_esta_el_bot = [...vistos.values()];

  const store = getStore({ name: "telegram", consistency: "strong" });
  out.envios_de_hoy = await store.get(`estado-${ahoraEcuador().fecha}`, { type: "json" });

  if (new URL(req.url).searchParams.get("prueba") === "1") {
    if (!canal) return json({ ...out, prueba: "Falta TELEGRAM_CANAL." }, 400);
    const ultima = Number((await store.get("ultima-prueba")) || 0);
    if (Date.now() - ultima < 10 * 60e3) return json({ ...out, prueba: "Ya se envió una prueba hace menos de 10 minutos." }, 429);
    try {
      await enviar(token, canal, `✅ <b>GOL ÉLITE PRO</b> conectado a Telegram.\nAquí llegarán cada día los pronósticos, los resultados y el cierre de la jornada.\n${PORTAL}\n+18 · Probabilidades estadísticas, no garantías.`);
      await store.set("ultima-prueba", String(Date.now()));
      out.prueba = "Mensaje de prueba enviado.";
    } catch (e) {
      out.prueba = `No se pudo enviar: ${e.message}`;
    }
  }
  return json(out);
};

export const config = { path: "/api/telegram-estado", method: ["GET"] };

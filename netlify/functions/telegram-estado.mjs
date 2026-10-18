// /api/telegram-estado — revisa la conexión con Telegram sin mostrar la clave del bot.
//   GET /api/telegram-estado             → ¿hay clave?, ¿hay canal?, nombre del bot y canales donde lo agregaron
//   GET /api/telegram-estado?prueba=1    → envía un mensaje de prueba al canal (máximo uno cada 10 minutos)
//   GET /api/telegram-estado?resumen=AAAA-MM-DD → envía al canal el resumen de ese día (una sola vez por fecha)
import { getStore } from "@netlify/blobs";
import { enviar, ahoraEcuador, PORTAL, mensajeCierre } from "../lib/telegram.mjs";

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
  if (!up.ok) out.aviso_actualizaciones = up.description || "Telegram no entregó actualizaciones";
  else if (!vistos.size) out.aviso_actualizaciones = "Sin novedades del canal: publica cualquier mensaje en el canal y vuelve a consultar.";

  const store = getStore({ name: "telegram", consistency: "strong" });
  out.envios_de_hoy = await store.get(`estado-${ahoraEcuador().fecha}`, { type: "json" });

  const dia = new URL(req.url).searchParams.get("resumen");
  if (dia) {
    if (!canal) return json({ ...out, resumen: "Falta TELEGRAM_CANAL." }, 400);
    if (!/^\d{4}-\d{2}-\d{2}$/.test(dia)) return json({ ...out, resumen: "Fecha inválida (AAAA-MM-DD)." }, 400);
    const k = `resumen-manual-${dia}`;
    if (await store.get(k)) return json({ ...out, resumen: `El resumen del ${dia} ya se envió.` }, 409);
    const base = Netlify.env.get("URL") || PORTAL;
    const r = await fetch(`${base}/api/dias/${dia}.json?t=${Date.now()}`);
    if (!r.ok) return json({ ...out, resumen: `No hay datos publicados del ${dia}.` }, 404);
    try {
      await enviar(token, canal, mensajeCierre(await r.json()));
      await store.set(k, String(Date.now()));
      out.resumen = `Resumen del ${dia} enviado al canal.`;
    } catch (e) {
      out.resumen = `No se pudo enviar: ${e.message}`;
    }
    return json(out);
  }
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

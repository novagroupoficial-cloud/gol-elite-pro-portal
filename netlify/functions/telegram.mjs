// Aviso automático a Telegram, cada hora en el minuto 20 (UTC y Ecuador comparten los minutos).
// Va después del refresco horario (minuto 09) y de su publicación en Netlify.
// No hace nada mientras falten TELEGRAM_BOT_TOKEN o TELEGRAM_CANAL en las variables de entorno.
import { getStore } from "@netlify/blobs";
import { leerFeed, pendientes, ahoraEcuador, enviar, clave, mensajeRanking, mensajeResultados, mensajeCierre } from "../lib/telegram.mjs";

export default async () => {
  const token = Netlify.env.get("TELEGRAM_BOT_TOKEN");
  const canal = Netlify.env.get("TELEGRAM_CANAL");
  if (!token || !canal) {
    console.log("Telegram desactivado: faltan TELEGRAM_BOT_TOKEN o TELEGRAM_CANAL.");
    return;
  }
  const feed = await leerFeed();
  const ahora = ahoraEcuador();
  // Solo el feed de hoy o de ayer (partidos de la noche que terminan después de medianoche)
  const ayer = ahoraEcuador(Date.now() - 864e5).fecha;
  if (feed.fecha !== ahora.fecha && feed.fecha !== ayer) {
    console.log(`Feed de ${feed.fecha}: nada que enviar.`);
    return;
  }
  const store = getStore({ name: "telegram", consistency: "strong" });
  const k = `estado-${feed.fecha}`;
  const estado = (await store.get(k, { type: "json" })) || { ranking: false, resultados: [], cierre: false };

  for (const t of pendientes(feed, estado, ahora)) {
    try {
      if (t.tipo === "ranking") {
        if (!t.saltar) await enviar(token, canal, mensajeRanking(feed));
        estado.ranking = true;
      } else if (t.tipo === "resultados") {
        await enviar(token, canal, mensajeResultados(feed, t.partidos));
        estado.resultados = [...(estado.resultados || []), ...t.partidos.map(clave)];
      } else if (t.tipo === "cierre") {
        await enviar(token, canal, mensajeCierre(feed));
        estado.cierre = true;
      }
      estado.actualizado = new Date().toISOString();
      await store.setJSON(k, estado); // se guarda tras cada envío: nunca se repite un mensaje
      console.log(`Enviado: ${t.tipo}${t.saltar ? " (omitido por la hora)" : ""}`);
    } catch (e) {
      console.error(`Falló ${t.tipo}: ${e.message}. Se reintenta en la hora siguiente.`);
      break;
    }
  }
};

export const config = { schedule: "20 * * * *" };

// Mensaje PRIVADO a Marco con las visitas del día, todos los días a las 23:55 de Ecuador (04:55 UTC).
// Va a TELEGRAM_MARCO_CHAT (su chat personal con el bot), nunca al canal público.
// No hace nada mientras falte TELEGRAM_MARCO_CHAT en las variables de entorno de Netlify.
import { avisarMarco } from "../lib/visitas.mjs";
import { ahoraEcuador } from "../lib/telegram.mjs";

export default async () => {
  try {
    const r = await avisarMarco(`aviso-${ahoraEcuador().fecha}`);
    console.log("Visitas a Marco:", JSON.stringify(r));
  } catch (e) {
    console.log("Visitas a Marco: error", e.message);
  }
};

export const config = { schedule: "55 4 * * *" };

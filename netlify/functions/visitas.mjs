// /api/visitas — contador de visitas del portal (Marco, 20-oct-2026).
//   POST /api/visitas  {"nueva":true|false}  → suma 1 visita (y 1 visitante del día si "nueva") y devuelve los totales
//   GET  /api/visitas                          → totales y registro de los últimos 60 días (hora de Ecuador)
// No guarda IP, nombre ni ningún dato personal: solo números por día. Ignora robots y buscadores.
import { getStore } from "@netlify/blobs";

const json = (o, status = 200) =>
  new Response(JSON.stringify(o, null, 1), { status, headers: { "content-type": "application/json; charset=utf-8", "cache-control": "no-store" } });

const fechaEcuador = (ms = Date.now()) => new Date(ms - 5 * 3600e3).toISOString().slice(0, 10);
const ROBOT = /bot|crawl|spider|slurp|preview|facebookexternalhit|whatsapp|telegram|headless|lighthouse|monitor|curl|wget|python|node-fetch/i;

export default async (req) => {
  const store = getStore({ name: "visitas", consistency: "strong" });
  const hoy = fechaEcuador();

  if (req.method === "POST") {
    const ua = req.headers.get("user-agent") || "";
    if (!ROBOT.test(ua)) {
      let nueva = false;
      try { nueva = Boolean((await req.json()).nueva); } catch {}
      const d = (await store.get(`dia-${hoy}`, { type: "json" })) || { fecha: hoy, visitas: 0, visitantes: 0 };
      const t = (await store.get("total", { type: "json" })) || { desde: hoy, visitas: 0, visitantes: 0 };
      d.visitas++; t.visitas++;
      if (nueva) { d.visitantes++; t.visitantes++; }
      await store.setJSON(`dia-${hoy}`, d);
      await store.setJSON("total", t);
      return json({ hoy: d, total: t });
    }
  }

  const t = (await store.get("total", { type: "json" })) || { desde: hoy, visitas: 0, visitantes: 0 };
  const dias = [];
  for (let i = 0; i < 60; i++) {
    const f = fechaEcuador(Date.now() - i * 86400e3);
    const d = await store.get(`dia-${f}`, { type: "json" });
    if (d) dias.push(d);
    if (f < t.desde) break;
  }
  return json({
    nota: "Visitas = páginas abiertas de la portada. Visitantes = personas distintas en el día (un mismo navegador cuenta una vez por día). Hora de Ecuador.",
    hoy: dias.find((d) => d.fecha === hoy) || { fecha: hoy, visitas: 0, visitantes: 0 },
    total: t,
    dias,
  });
};

export const config = { path: "/api/visitas", method: ["GET", "POST"] };

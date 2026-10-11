"""Nova Gol 4.0 — modelo Over 1.5 / Over 2.5 (Poisson + Dixon-Coles).

Uso:
    from nova_gol_4 import Equipo, pronostico
    r = pronostico(LHG=1.55, LAG=1.20,
                   local=Equipo(pj=4, gf=10, gc=8),
                   visita=Equipo(pj=3, gf=7, gc=5))
"""
from dataclasses import dataclass
from math import exp, factorial

RHO = -0.08          # corrección Dixon-Coles
K = 4                # partidos "virtuales" de contracción hacia la media de liga
MAXG = 10            # tabla de marcadores 0..10


@dataclass
class Equipo:
    pj: int                    # partidos jugados (local: en casa; visita: fuera)
    gf: float                  # goles a favor totales en ese split
    gc: float                  # goles en contra totales en ese split
    xg: float | None = None    # xG total (opcional)
    xga: float | None = None   # xGA total (opcional)
    u5_gf: float | None = None # goles a favor en los últimos 5 (total, opcional)
    u5_gc: float | None = None
    u5_pj: int = 0             # cuántos de los últimos 5 hay (0 si no hay)
    ajuste: float = 1.0        # contexto (bajas, motivación); se limita 0,90–1,10


def _contraer(total, pj, media):
    return (total + K * media) / (pj + K)


def _metrica(total, pj, u5_total, u5_pj, xg_total, media):
    """0,60 últimos5 + 0,40 temporada (0,30/0,70 con <3 recientes); luego 0,60 goles + 0,40 xG.
    Datos faltantes: su peso pasa a los disponibles (nunca se inventan)."""
    temp = _contraer(total, pj, media)
    if u5_total is not None and u5_pj > 0:
        rec = _contraer(u5_total, u5_pj, media)
        w = 0.60 if u5_pj >= 3 else 0.30
        goles = w * rec + (1 - w) * temp
    else:
        goles = temp
    if xg_total is not None:
        return 0.60 * goles + 0.40 * _contraer(xg_total, pj, media)
    return goles


def _lim(x, a, b):
    return max(a, min(b, x))


def _poisson(k, lam):
    return exp(-lam) * lam ** k / factorial(k)


def _tau(i, j, ll, lv):
    if i == 0 and j == 0: return 1 - ll * lv * RHO
    if i == 0 and j == 1: return 1 + ll * RHO
    if i == 1 and j == 0: return 1 + lv * RHO
    if i == 1 and j == 1: return 1 - RHO
    return 1.0


def _lambda_desde_over25(p):
    """λ total cuyo P(total>=3) Poisson simple = p (búsqueda binaria)."""
    lo, hi = 0.05, 8.0
    for _ in range(60):
        m = (lo + hi) / 2
        o25 = 1 - sum(_poisson(k, m) for k in range(3))
        lo, hi = (m, hi) if o25 < p else (lo, m)
    return (lo + hi) / 2


def pronostico(LHG, LAG, local: Equipo, visita: Equipo, cuota_over25=None, cuota_under25=None):
    gfL = _metrica(local.gf, local.pj, local.u5_gf, local.u5_pj, local.xg, LHG)
    gcL = _metrica(local.gc, local.pj, local.u5_gc, local.u5_pj, local.xga, LAG)
    gfV = _metrica(visita.gf, visita.pj, visita.u5_gf, visita.u5_pj, visita.xg, LAG)
    gcV = _metrica(visita.gc, visita.pj, visita.u5_gc, visita.u5_pj, visita.xga, LHG)

    ataL, defV = _lim(gfL / LHG, .6, 1.6), _lim(gcV / LHG, .6, 1.6)
    ataV, defL = _lim(gfV / LAG, .6, 1.6), _lim(gcL / LAG, .6, 1.6)
    ll = LHG * ataL * defV * _lim(local.ajuste, .9, 1.1)
    lv = LAG * ataV * defL * _lim(visita.ajuste, .9, 1.1)

    aviso = None
    if cuota_over25 and cuota_under25:
        po = (1 / cuota_over25) / (1 / cuota_over25 + 1 / cuota_under25)  # sin margen
        lam_m = _lambda_desde_over25(po)
        lam_mod = ll + lv
        lam_f = 0.65 * lam_mod + 0.35 * lam_m
        ll, lv = ll * lam_f / lam_mod, lv * lam_f / lam_mod
        p_mod = 1 - sum(_poisson(k, lam_mod) for k in range(3))
        dif = abs(p_mod - po) * 100
        aviso = "AUDITAR" if dif > 6 else "CAUTELA" if dif > 3 else None

    tabla = {(i, j): _poisson(i, ll) * _poisson(j, lv) * _tau(i, j, ll, lv)
             for i in range(MAXG + 1) for j in range(MAXG + 1)}
    s = sum(tabla.values())
    tabla = {k: v / s for k, v in tabla.items()}

    o15 = 1 - sum(v for (i, j), v in tabla.items() if i + j <= 1)
    o25 = 1 - sum(v for (i, j), v in tabla.items() if i + j <= 2)
    top = max(tabla.values())
    empatados = [k for k, v in tabla.items() if abs(v - top) < 1e-12]
    quiere3 = o25 >= 0.5
    marcador = sorted(empatados, key=lambda k: ((k[0] + k[1] >= 3) != quiere3, k))[0]

    o15p, o25p = round(o15 * 100, 1), round(o25 * 100, 1)
    return {
        "lambda_local": round(ll, 2), "lambda_visita": round(lv, 2),
        "goles_esperados": round(ll + lv, 1),
        "over15": o15p, "over25": o25p, "under25": round(100 - o25p, 1),
        "marcador": f"{marcador[0]}-{marcador[1]}",
        "categoria": categoria_o15(o15p), "senal_o25": senal_o25(o25p),
        "aviso_mercado": aviso,
    }


def categoria_o15(p):
    return "GOL ÉLITE" if p >= 90 else "Rango 80" if p >= 80 else "Rango 70" if p >= 70 else "Menos de 70"


def senal_o25(p):
    return "fuerte" if p >= 75 else "moderada" if p >= 65 else "informativa" if p >= 55 else "sin señal"


def wilson(aciertos, n, z=1.96):
    """Intervalo de confianza 95 % de Wilson para un % de acierto."""
    if n == 0: return (None, None)
    p = aciertos / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    m = z * ((p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5) / d
    return round((c - m) * 100, 1), round((c + m) * 100, 1)


if __name__ == "__main__":
    r = pronostico(1.55, 1.20, Equipo(4, 10, 8), Equipo(3, 7, 5))
    print(r)
    print("21/25 →", wilson(21, 25))

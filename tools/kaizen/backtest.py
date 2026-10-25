"""Kaizen GOL ÉLITE PRO — banco de pruebas (Marco autorizó mejora continua el 25-oct-2026).
Recalcula TODOS los partidos auditados con una variante del modelo y la compara con producción.
No toca nada sellado: solo lee data/<fecha>/pronosticos.json (entradas) y auditoria.json (resultados).
Uso:  python3 tools/kaizen/backtest.py
Métricas: Brier (error cuadrático, menor es mejor), Skill vs "decir siempre la media" (>0 = aporta),
AUC (discriminación: 0,5 = azar, 1 = perfecto), calibración por franja."""
import json, glob, os, sys, importlib, math
AQUI = os.path.dirname(os.path.abspath(__file__)); RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, 'tools'))
import nova_gol_4 as M

def partidos():
    out = []
    for f in sorted(glob.glob(os.path.join(RAIZ, 'data', '2026-*', 'auditoria.json'))):
        d = os.path.dirname(f); fecha = os.path.basename(d)
        pf = os.path.join(d, 'pronosticos.json')
        if not os.path.exists(pf): continue
        P = {(p['local'], p['visita']): p for p in json.load(open(pf, encoding='utf-8')) if not p.get('sin') and p.get('casa')}
        for r in json.load(open(f, encoding='utf-8')).get('resultados', []):
            p = P.get((r['local'], r['visita']))
            if p and r.get('estado') == 'terminado' and r.get('resultado'):
                g = [int(x) for x in r['resultado'].split('-')]
                out.append(dict(fecha=fecha, liga=p['liga'], p=p, gl=g[0], gv=g[1], o15_sellado=p['over15'], o25_sellado=p['over25']))
    return out

def auc(ps, ys):
    pos = [p for p, y in zip(ps, ys) if y]; neg = [p for p, y in zip(ps, ys) if not y]
    if not pos or not neg: return float('nan')
    return sum((a > b) + 0.5 * (a == b) for a in pos for b in neg) / (len(pos) * len(neg))

def metricas(ps, ys):
    n = len(ys); base = sum(ys) / n
    b = sum((p - y) ** 2 for p, y in zip(ps, ys)) / n; b0 = sum((base - y) ** 2 for y in ys) / n
    ll = -sum(math.log(max(1e-6, p if y else 1 - p)) for p, y in zip(ps, ys)) / n
    return dict(n=n, brier=round(b, 4), skill=round(1 - b / b0, 3), auc=round(auc(ps, ys), 3), logloss=round(ll, 4),
                media_pred=round(sum(ps) / n, 3), real=round(base, 3))

def correr(variante, X):
    """variante(p) -> (o15, o25) en 0..1"""
    p15, p25 = [], []
    for x in X:
        a, b = variante(x['p']); p15.append(a); p25.append(b)
    y15 = [x['gl'] + x['gv'] >= 2 for x in X]; y25 = [x['gl'] + x['gv'] >= 3 for x in X]
    return metricas(p15, y15), metricas(p25, y25), p15

def produccion(p, **kw):
    r = M.pronostico(p['HG'], p['AG'], M.Equipo(*p['casa']), M.Equipo(*p['fuera']))
    return r['over15'] / 100, r['over25'] / 100

def con_parametros(K=None, LIM=None, RHO=None):
    def f(p):
        k0, rho0, lim0 = M.K, M.RHO, M._lim
        try:
            if K is not None: M.K = K
            if RHO is not None: M.RHO = RHO
            if LIM is not None: M._lim = lambda x, a, b: max(LIM[0], min(LIM[1], x))
            return produccion(p)
        finally:
            M.K, M.RHO, M._lim = k0, rho0, lim0
    return f

def solo_liga(p):
    """Referencia: solo la media de goles de la liga (sin datos de equipos)."""
    lam = p['HG'] + p['AG']; P = lambda k: math.exp(-lam) * lam ** k / math.factorial(k)
    return 1 - P(0) - P(1), 1 - P(0) - P(1) - P(2)

if __name__ == '__main__':
    X = partidos()
    print(f"Partidos auditados con entradas: {len(X)} · días: {sorted(set(x['fecha'] for x in X))}")
    def con_alfa(a):
        def f(p):
            a0 = M.ALFA; M.ALFA = a
            try: return produccion(p)
            finally: M.ALFA = a0
        return f
    V = [('Lo sellado (lo que se publicó)', lambda p: (p['over15'] / 100, p['over25'] / 100)),
         ('Versión 4.0 (ALFA 1,0)', con_alfa(1.0)), (f'Versión vigente {M.VERSION} (ALFA {M.ALFA})', produccion),
         ('Solo media de la liga (referencia)', solo_liga)]
    for a in (0.3, 0.7): V.append((f'ALFA {a}', con_alfa(a)))
    print(f"{'Variante':38s} | O1.5 Brier  skill   AUC  | O2.5 Brier  skill   AUC")
    for nom, f in V:
        m15, m25, _ = correr(f, X)
        print(f"{nom:38s} | {m15['brier']:.4f} {m15['skill']:+.3f} {m15['auc']:.3f} | {m25['brier']:.4f} {m25['skill']:+.3f} {m25['auc']:.3f}")

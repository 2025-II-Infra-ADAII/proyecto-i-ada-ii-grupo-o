from itertools import permutations

def calcular_costo(finca, perm):
    tiempo_inicio = 0
    costo_total = 0

    for i in perm:
        ts, tr, p = finca[i]
        fin_riego = tiempo_inicio + tr
        retraso = max(0, fin_riego - ts)
        costo_total += p * retraso
        tiempo_inicio = fin_riego

    return costo_total


def roFB(finca):
    n = len(finca)
    mejor_perm = None
    costo_minimo = float('inf')

    for perm in permutations(range(n)):
        costo = calcular_costo(finca, perm)
        if costo < costo_minimo:
            costo_minimo = costo
            mejor_perm = perm

    if mejor_perm is None:
        return [], 0

    return list(mejor_perm), costo_minimo

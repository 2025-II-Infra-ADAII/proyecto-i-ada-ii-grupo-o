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

    return mejor_perm, costo_minimo


# Ejemplo de prueba del PDF
if __name__ == "__main__":
    finca = [(10, 3, 4), (5, 3, 3), (2, 2, 1), (8, 1, 1), (6, 4, 2)]
    perm, costo = roFB(finca)
    print("Mejor orden de riego:", perm)
    print("Costo mínimo:", costo)

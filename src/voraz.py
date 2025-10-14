def roV(finca):
    orden = sorted(range(len(finca)), key=lambda i: finca[i][0])

    timpo = 0
    costo = 0
    for i in orden:
        ts, tr, p = finca[i]    
        fin_riego = timpo + tr
        retraso = max(0, fin_riego - ts)
        costo += retraso * p
        timpo = fin_riego

    return orden, costo

if __name__ == "__main__":
    finca = [
        (10, 3, 4),
        (5, 3, 4),
        (2, 2, 1)
    ]
    orden, costo = roV(finca)
    print("Orden de riego:", orden)
    print("Costo total:", costo)
   
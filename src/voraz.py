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


   
from src.voraz import roV 

def orden_ts():
    finca = [
        (10, 3, 4),
        (5, 3, 4),
        (2, 2, 1)
    ]
    orden_esperado = [2, 1, 0]
    orden, costo = roV(finca)
    assert orden == [2,1,0]
    assert costo == 0
    

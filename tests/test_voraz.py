import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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
def test_costo_positivo_si_hay_retraso():
    finca = [(4, 3, 4), (5, 3, 4), (2, 2, 1)]
    orden, costo = roV(finca)
    assert costo > 0            # Si hay retraso, el costo debe ser positivo

def test_tipos_de_retorno():
    finca = [(6, 4, 2), (3, 2, 1)]
    orden, costo = roV(finca)
    assert isinstance(orden, list)
    assert isinstance(costo, (int, float))
    

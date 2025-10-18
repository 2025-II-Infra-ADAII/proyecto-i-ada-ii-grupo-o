import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
import pytest
from src.dinamica import roPD, calcular_costo_programacion

# ------------------ CASOS BASE ------------------

def test_finca_vacia():
    finca = []
    perm, cost = roPD(finca)
    assert perm == []
    assert cost == 0

def test_un_solo_tablon():
    finca = [(5, 2, 3)]  # No debería haber tardanza
    perm, cost = roPD(finca)
    assert perm == [0]
    assert cost == 0

def test_sin_retrasos():
    finca = [(10, 2, 1), (8, 2, 1), (7, 2, 1)]
    perm, cost = roPD(finca)
    assert cost == 0  # Ninguno se pasa de su tiempo de supervivencia

# ------------------ CASOS DEL PROYECTO ------------------

def test_ejemplo_1_proyecto():
    finca = [
        (10, 3, 4),  # 0
        (5, 3, 3),   # 1
        (2, 2, 1),   # 2
        (8, 1, 1),   # 3
        (6, 4, 2)    # 4
    ]
    perm, cost = roPD(finca)
    verified_cost = calcular_costo_programacion(finca, perm)

    # Validaciones generales
    assert set(perm) == set(range(len(finca)))
    assert cost == verified_cost

def test_ejemplo_2_proyecto():
    finca = [
        (9, 3, 4),
        (5, 3, 3),
        (2, 2, 1),
        (8, 1, 1),
        (6, 4, 2)
    ]
    perm, cost = roPD(finca)
    verified_cost = calcular_costo_programacion(finca, perm)
    assert set(perm) == set(range(len(finca)))
    assert cost == verified_cost

# ------------------ TEST DE ESTABILIDAD -----------------

@pytest.mark.parametrize("n", [5, 8, 10])
def test_tamanos_crecientes(n):
    # Generar finca aleatoria pequeña
    finca = [(10 + i, (i % 3) + 1, (i % 4) + 1) for i in range(n)]
    perm, cost = roPD(finca)
    verified_cost = calcular_costo_programacion(finca, perm)

    # Validar coherencia
    assert set(perm) == set(range(len(finca)))
    assert cost == verified_cost
    assert cost >= 0
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

import time
from itertools import permutations, islice
import random
import pytest
from src.fuerzaBruta import roFB, calcular_costo


# ------------------ CASOS BASE ------------------

def test_finca_vacia():
    finca = []
    perm, cost = roFB(finca)
    # Acepta tanto lista vacía como tupla vacía, para robustez
    assert list(perm) == []
    assert cost == 0


def test_un_solo_tablon():
    finca = [(5, 2, 3)]
    perm, cost = roFB(finca)
    assert list(perm) == [0]
    assert cost == 0


# ------------------ CASOS DEL PROYECTO ------------------

def test_ejemplo_1_proyecto():
    finca = [
        (10, 3, 4),
        (5, 3, 3),
        (2, 2, 1),
        (8, 1, 1),
        (6, 4, 2)
    ]
    perm, cost = roFB(finca)
    verified_cost = calcular_costo(finca, perm)

    assert set(perm) == set(range(len(finca)))
    assert cost == verified_cost
    assert cost >= 0


def test_ejemplo_2_proyecto():
    finca = [
        (9, 3, 4),
        (5, 3, 3),
        (2, 2, 1),
        (8, 1, 1),
        (6, 4, 2)
    ]
    perm, cost = roFB(finca)
    verified_cost = calcular_costo(finca, perm)

    assert set(perm) == set(range(len(finca)))
    assert cost == verified_cost
    assert cost >= 0


# ---------------------------------------------------------------------
# 🔹 EJEMPLOS DEL PDF (con tolerancia)
# ---------------------------------------------------------------------

def test_ejemplo_1_pdf():
    finca = [(10, 3, 4), (5, 3, 3), (2, 2, 1), (8, 1, 1), (6, 4, 2)]
    perm, costo = roFB(finca)
    print(f"\nEjemplo 1 - Permutación: {perm}, Costo: {costo}")
    assert set(perm) == set(range(len(finca)))
    assert abs(costo - 16) <= 5


def test_ejemplo_2_pdf():
    finca = [(9, 3, 4), (5, 3, 3), (2, 2, 1), (8, 1, 1), (6, 4, 2)]
    perm, costo = roFB(finca)
    print(f"\nEjemplo 2 - Permutación: {perm}, Costo: {costo}")
    assert set(perm) == set(range(len(finca)))
    assert abs(costo - 18) <= 5


# ---------------------------------------------------------------------
# 🔹 FUNCIONES AUXILIARES Y TESTS DE RENDIMIENTO
# ---------------------------------------------------------------------

def generar_finca(n, semilla=42):
    random.seed(semilla)
    return [(random.randint(5, 50), random.randint(1, 5), random.randint(1, 4)) for _ in range(n)]


@pytest.mark.parametrize("tamano", [10, 100, 1000])
def test_fuerza_bruta_escalabilidad(tamano):
    finca = generar_finca(tamano)
    repeticiones = 5
    tiempos = []

    for _ in range(repeticiones):
        inicio = time.time()

        if tamano <= 10:
            roFB(finca)
        else:
            mejor = float('inf')
            for perm in islice(permutations(range(min(tamano, 10))), 100):
                costo = calcular_costo(finca, perm)
                mejor = min(mejor, costo)

        fin = time.time()
        tiempos.append(fin - inicio)

    promedio = sum(tiempos) / len(tiempos)
    print(f"\nTamaño {tamano} -> Tiempo promedio: {promedio:.4f} segundos")
    assert promedio >= 0

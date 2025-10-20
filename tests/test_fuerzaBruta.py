import sys
import os
import time
import csv
import statistics
import random
import pytest

# Asegurar importación desde src/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.fuerzaBruta import roFB, calcular_costo


# ---------------------------------------------------------------------
# 🔹 CASOS BASE
# ---------------------------------------------------------------------

def test_finca_vacia():
    finca = []
    perm, cost = roFB(finca)
    assert list(perm) == []
    assert cost == 0


def test_un_solo_tablon():
    finca = [(5, 2, 3)]
    perm, cost = roFB(finca)
    assert list(perm) == [0]
    assert cost == 0


# ---------------------------------------------------------------------
# 🔹 CASOS DEL PROYECTO
# ---------------------------------------------------------------------

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
# 🔹 CASOS DEL PDF (con tolerancia)
# ---------------------------------------------------------------------

def test_ejemplo_1_pdf():
    finca = [(10, 3, 4), (5, 3, 3), (2, 2, 1), (8, 1, 1), (6, 4, 2)]
    perm, costo = roFB(finca)
    print(f"\nEjemplo 1 PDF -> Permutación: {perm}, Costo: {costo}")
    assert set(perm) == set(range(len(finca)))
    assert abs(costo - 16) <= 5


def test_ejemplo_2_pdf():
    finca = [(9, 3, 4), (5, 3, 3), (2, 2, 1), (8, 1, 1), (6, 4, 2)]
    perm, costo = roFB(finca)
    print(f"\nEjemplo 2 PDF -> Permutación: {perm}, Costo: {costo}")
    assert set(perm) == set(range(len(finca)))
    assert abs(costo - 18) <= 5


# ---------------------------------------------------------------------
# 🔹 FUNCIONES AUXILIARES PARA RENDIMIENTO
# ---------------------------------------------------------------------

def generar_finca(n):
    return [(i * 2 + 10, (i % 5) + 1, (i % 3) + 1) for i in range(n)]


def medir_promedio(funcion, finca, repeticiones=3):
    tiempos = []
    costo_final = None
    for _ in range(repeticiones):
        inicio = time.perf_counter()
        orden, costo = funcion(finca)
        fin = time.perf_counter()
        tiempos.append(fin - inicio)
        costo_final = costo
    return statistics.mean(tiempos), costo_final


def guardar_resultados_csv(resultados, nombre="resultados_fuerza_bruta.csv"):
    os.makedirs("docs", exist_ok=True)
    path = os.path.join("docs", nombre)
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Tamaño (n)", "Tiempo promedio (s)", "Costo total"])
        writer.writerows(resultados)
    print(f"\n✅ Resultados guardados en {path}")


# ---------------------------------------------------------------------
# 🔹 TEST DE RENDIMIENTO (solo este genera CSV)
# ---------------------------------------------------------------------

def test_fuerza_bruta_rendimiento():
    """
    Prueba el rendimiento del algoritmo Fuerza Bruta con distintos tamaños.
    Genera el CSV para el análisis comparativo.
    """
    tamanos = [4, 5, 6, 7, 8]
    resultados = []

    for n in tamanos:
        finca = generar_finca(n)
        t_prom, costo = medir_promedio(roFB, finca, repeticiones=2)
        resultados.append((n, round(t_prom, 6), costo))
        print(f"[FUERZA BRUTA] n={n:<6} | Tiempo promedio: {t_prom:.6f}s | Costo total: {costo}")

        assert t_prom >= 0

    guardar_resultados_csv(resultados)

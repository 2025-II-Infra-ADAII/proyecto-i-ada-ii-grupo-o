import sys
import os
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.voraz import roV

# ------------------ PRUEBAS UNITARIAS -----------------

def test_orden_ts():
    start = time.perf_counter()

    finca = [
        (10, 3, 4),
        (5, 3, 4),
        (2, 2, 1)
    ]
    orden, costo = roV(finca)

    end = time.perf_counter()
    print(f"\nTiempo test_orden_ts: {end - start:.6f} segundos")

    assert orden == [2, 1, 0]
    assert costo == 0


def test_costo_positivo_si_hay_retraso():
    start = time.perf_counter()

    finca = [(4, 3, 4), (5, 3, 4), (2, 2, 1)]
    orden, costo = roV(finca)

    end = time.perf_counter()
    print(f"Tiempo test_costo_positivo_si_hay_retraso: {end - start:.6f} segundos")

    assert costo > 0  # Si hay retraso, el costo debe ser positivo


def test_tipos_de_retorno():
    start = time.perf_counter()

    finca = [(6, 4, 2), (3, 2, 1)]
    orden, costo = roV(finca)

    end = time.perf_counter()
    print(f"Tiempo test_tipos_de_retorno: {end - start:.6f} segundos")

    assert isinstance(orden, list)
    assert isinstance(costo, (int, float))

import sys
import os
import time
import statistics

# Asegurar que se pueda importar desde src/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.voraz import roV


def generar_finca_fija(n):
    """
    Genera una finca determinista de tamaño n (no aleatoria).
    """
    finca = []
    for i in range(n):
        ts = i * 2 + 10          # tiempo de supervivencia
        tr = (i % 5) + 1         # tiempo de riego entre 1 y 5
        p = (i % 3) + 1          # penalización entre 1 y 3
        finca.append((ts, tr, p))
    return finca


def medir_tiempo(funcion, finca):
    """
    Mide el tiempo que tarda en ejecutar la función de riego.
    Devuelve el costo y la duración en segundos.
    """
    inicio = time.time()
    orden, costo = funcion(finca)
    fin = time.time()
    return costo, fin - inicio


def probar_tamano(n):
    """
    Ejecuta 5 repeticiones del algoritmo voraz con una finca de tamaño n.
    Verifica que las salidas sean válidas y que el tiempo no sea excesivo.
    """
    finca = generar_finca_fija(n)
    tiempos = []

    for _ in range(5):  # 5 repeticiones
        costo, duracion = medir_tiempo(roV, finca)
        tiempos.append(duracion)

        # Validaciones unitarias:
        orden, _ = roV(finca)
        assert isinstance(orden, list)
        assert len(orden) == n
        assert isinstance(costo, (int, float))

    # Calcular el tiempo promedio
    promedio = statistics.mean(tiempos)
    print(f"Tamaño {n:>6} | Promedio: {promedio:.6f}s")

    # Asegurarse de que el tiempo sea razonable (ajustable)
    assert promedio < 10, f"El algoritmo fue demasiado lento para n={n}"


def test_juguete():
    """Prueba un caso pequeño (10 tablones)."""
    probar_tamano(10)


def test_pequeno():
    """Prueba un caso de 100 tablones."""
    probar_tamano(100)


def test_mediano():
    """Prueba un caso de 1000 tablones."""
    probar_tamano(1000)


def test_grande():
    """Prueba un caso de 10000 tablones."""
    probar_tamano(10000)


def test_extra_grande():
    """Prueba un caso de 50000 tablones."""
    probar_tamano(50000)

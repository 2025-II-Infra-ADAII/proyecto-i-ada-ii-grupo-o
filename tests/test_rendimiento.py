import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time
from src.voraz import roV

def generar_finca_fija(n):
    """
    Genera una finca determinista de tamaño n.
    Los valores crecen con el índice, no son aleatorios.
    """
    finca = []
    for i in range(n):
        ts = i * 2 + 10          # tiempo de supervivencia
        tr = (i % 5) + 1         # tiempo de riego entre 1 y 5
        p = (i % 3) + 1          # penalización entre 1 y 3
        finca.append((ts, tr, p))
    return finca


def medir_tiempo(funcion, finca, nombre):
    """Mide el tiempo de ejecución y el costo total."""
    inicio = time.time()
    _, costo = funcion(finca)
    fin = time.time()
    duracion = fin - inicio
    print(f"{nombre:<10} | n={len(finca):>6} | Tiempo: {duracion:.6f}s | Costo total: {costo}")


def test_rendimiento_voraz():
    """Evalúa el rendimiento del algoritmo Voraz con diferentes tamaños."""
    tamanos = [10, 100, 1000, 10000, 50000]
    print("\n=== Rendimiento del algoritmo Voraz ===")
    for n in tamanos:
        finca = generar_finca_fija(n)
        medir_tiempo(roV, finca, "Voraz")


    

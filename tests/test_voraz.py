import sys
import os
import time
import csv
import statistics

# Asegurar que se pueda importar desde src/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.voraz import roV


# ------------------- GENERADORES Y MEDICIÓN -------------------

def generar_finca(n):
    """
    Genera una finca determinista de tamaño n.
    Cada tablón tiene (ts, tr, p) distintos pero controlados.
    """
    return [(i * 2 + 10, (i % 5) + 1, (i % 3) + 1) for i in range(n)]


def medir_promedio(funcion, finca, repeticiones=5):
    """
    Ejecuta la función varias veces y devuelve el tiempo promedio y costo.
    """
    tiempos = []
    costo_final = None

    for _ in range(repeticiones):
        inicio = time.perf_counter()
        orden, costo = funcion(finca)
        fin = time.perf_counter()

        # Validaciones unitarias
        assert isinstance(orden, list)
        assert isinstance(costo, (int, float))
        assert len(orden) == len(finca)

        tiempos.append(fin - inicio)
        costo_final = costo

    promedio = statistics.mean(tiempos)
    return promedio, costo_final


def guardar_resultados_csv(resultados, nombre="resultados_voraz.csv"):
    """
    Guarda los resultados experimentales en docs/resultados_voraz.csv.
    """
    os.makedirs("docs", exist_ok=True)
    path = os.path.join("docs", nombre)
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Tamaño (n)", "Tiempo promedio (s)", "Costo total"])
        writer.writerows(resultados)
    print(f"\n✅ Resultados guardados en {path}")


# ------------------- PRUEBAS UNITARIAS -------------------

def test_voraz_rendimiento():
    """
    Prueba el rendimiento del algoritmo voraz con distintos tamaños de entrada.
    Cumple los tres criterios del informe:
    1. Mide tiempos reales con tamaños de prueba.
    2. Usa 5 repeticiones por tamaño y calcula el promedio.
    3. Guarda los resultados para comparar con la complejidad teórica.
    """
    tamanos = [10, 100, 1000, 10000, 50000]
    resultados = []

    for n in tamanos:
        finca = generar_finca(n)
        t_prom, costo = medir_promedio(roV, finca, repeticiones=5)
        resultados.append((n, round(t_prom, 6), costo))
        print(f"[VORAZ] n={n:<6} | Tiempo promedio: {t_prom:.6f}s | Costo total: {costo}")

        # Asegurar tiempos válidos
        assert t_prom >= 0

    guardar_resultados_csv(resultados)
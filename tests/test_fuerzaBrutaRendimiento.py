import sys
import os
import time
import csv
import statistics
import math
import matplotlib.pyplot as plt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.fuerzaBruta import roFB


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
    promedio = statistics.mean(tiempos)
    return promedio, costo_final


def guardar_resultados_csv(resultados, nombre="resultados_fuerza_bruta.csv"):
    os.makedirs("docs", exist_ok=True)
    path = os.path.join("docs", nombre)
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Tamaño (n)", "Tiempo promedio (s)", "Costo total"])
        writer.writerows(resultados)
    print(f"\n✅ Resultados guardados en {path}")


def generar_grafico_comparacion(resultados, nombre="grafico_fuerza_bruta.png"):
    os.makedirs("docs", exist_ok=True)
    tamanos = [r[0] for r in resultados]
    tiempos = [r[1] for r in resultados]

    # Curva teórica O(n!) escalada
    factorial_ref = [math.factorial(n) for n in tamanos]
    max_factorial = max(factorial_ref)
    max_tiempo = max(tiempos)
    factorial_escalado = [f * (max_tiempo / max_factorial) for f in factorial_ref]

    # ----- GRÁFICO ESTILO PROFESIONAL -----
    plt.figure(figsize=(9, 6))
    plt.plot(
        tamanos, tiempos,
        marker="o", color="tab:blue", linewidth=2,
        label="Tiempos reales (experimentales)"
    )
    plt.plot(
        tamanos, factorial_escalado,
        linestyle="--", color="tab:orange", linewidth=2,
        label="Crecimiento teórico O(n!)"
    )

    plt.xscale("log")
    plt.yscale("log")
    plt.grid(True, which="both", linestyle="--", alpha=0.6)
    plt.title("Comparación de rendimiento: Fuerza Bruta vs Complejidad Teórica", fontsize=12)
    plt.xlabel("Tamaño (n)")
    plt.ylabel("Tiempo (s)")
    plt.legend()
    plt.tight_layout()

    path = os.path.join("docs", nombre)
    plt.savefig(path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"📊 Gráfico guardado en {path}")


def test_fuerza_bruta_rendimiento():
    tamanos = [4, 5, 6, 7, 8, 9]
    resultados = []

    for n in tamanos:
        finca = generar_finca(n)
        t_prom, costo = medir_promedio(roFB, finca, repeticiones=3)
        resultados.append((n, round(t_prom, 6), costo))
        print(f"[FUERZA BRUTA] n={n:<4} | Tiempo promedio: {t_prom:.6f}s | Costo total: {costo}")
        assert t_prom >= 0

    guardar_resultados_csv(resultados)
    generar_grafico_comparacion(resultados)

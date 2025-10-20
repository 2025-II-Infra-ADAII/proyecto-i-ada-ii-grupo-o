import sys
import os
import time
import statistics
import pandas as pd
import matplotlib.pyplot as plt
import math

# Asegurar que se pueda importar desde src/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importar la versión dinámica
from src.dinamica import roPD


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
    Ejecuta 3 repeticiones del algoritmo dinámico con una finca de tamaño n.
    Devuelve el tamaño y el tiempo promedio.
    """
    finca = generar_finca_fija(n)
    tiempos = []

    for _ in range(3):
        costo, duracion = medir_tiempo(roPD, finca)
        tiempos.append(duracion)

        # Validaciones unitarias básicas
        orden, _ = roPD(finca)
        assert isinstance(orden, list)
        assert len(orden) == n
        assert isinstance(costo, (int, float))

    promedio = statistics.mean(tiempos)
    print(f"Tamaño {n:>6} | Promedio: {promedio:.6f}s")
    return n, promedio


def test_rendimiento_dinamica():
    """
    Prueba varios tamaños y genera el archivo CSV + gráfico PNG.
    """
    # Tamaños pequeños apropiados para programación dinámica
    tamanos = [4, 6, 8, 10, 12, 14, 16]
    resultados = []

    print("Iniciando pruebas de rendimiento para algoritmo dinámico...")
    
    for n in tamanos:
        n, promedio = probar_tamano(n)
        resultados.append({"Tamaño (n)": n, "Tiempo promedio (s)": promedio})

    # Crear DataFrame y guardar CSV
    docs_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'docs'))
    os.makedirs(docs_path, exist_ok=True)
    
    df = pd.DataFrame(resultados)
    
    # Definir rutas completas
    csv_path = os.path.join(docs_path, "resultados_dinamica.csv")
    png_path = os.path.join(docs_path, "grafico_dinamica.png")
    
    df.to_csv(csv_path, index=False)
    print(f"Archivo CSV guardado en: {csv_path}")
    
    # Verificar que el archivo se creó
    if os.path.exists(csv_path):
        print(f"✓ Archivo CSV creado exitosamente: {csv_path}")
    else:
        print(f"✗ Error: No se pudo crear el archivo CSV en: {csv_path}")

    # Calcular O(2^n) normalizado para comparación
    df["O(2^n)"] = [2**n / 1000000 for n in df["Tamaño (n)"]]

    # Graficar
    plt.figure(figsize=(10, 6))
    plt.plot(df["Tamaño (n)"], df["Tiempo promedio (s)"], marker='o', linewidth=2, 
             markersize=8, label="Tiempos reales (experimentales)", color='blue')
    plt.plot(df["Tamaño (n)"], df["O(2^n)"], linestyle="--", linewidth=2, 
             label="Crecimiento teórico O(2^n) (normalizado)", color='red')

    plt.xlabel("Tamaño de la finca (n)")
    plt.ylabel("Tiempo (segundos)")
    plt.title("Rendimiento del Algoritmo de Programación Dinámica")
    plt.legend()
    plt.grid(True, linestyle="--", linewidth=0.5, alpha=0.7)
    
    # Mejorar el formato del gráfico
    plt.tight_layout()

    # Guardar el gráfico
    plt.savefig(png_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"Gráfico PNG guardado en: {png_path}")
    
    # Verificar que el gráfico se creó
    if os.path.exists(png_path):
        print(f"✓ Archivo PNG creado exitosamente: {png_path}")
    else:
        print(f"✗ Error: No se pudo crear el archivo PNG en: {png_path}")
    
    # Mostrar resumen de resultados
    print("\nResumen de resultados:")
    print(df.to_string(index=False))
    
    # Mostrar directorio actual y contenido de docs
    print(f"\nDirectorio actual: {os.getcwd()}")
    print(f"Contenido de docs/:")
    if os.path.exists(docs_path):
        for file in os.listdir(docs_path):
            print(f"  - {file}")
    else:
        print("  La carpeta docs no existe")


if __name__ == "__main__":
    test_rendimiento_dinamica()
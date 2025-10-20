import pandas as pd
import matplotlib.pyplot as plt
import math
import os

# Cargar resultados guardados por las pruebas
path_csv = "docs/resultados_fuerza_bruta.csv"
if not os.path.exists(path_csv):
    raise FileNotFoundError("❌ No se encontró el archivo de resultados. Ejecuta primero test_fuerzaBruta.py")

df = pd.read_csv(path_csv, encoding="latin1")


# Calcular valores teóricos O(n!) y escalar para comparación visual
factorial = [math.factorial(n) for n in df["Tamaño (n)"]]
max_factorial = max(factorial)
max_tiempo = max(df["Tiempo promedio (s)"])
df["O(n!)"] = [f * (max_tiempo / max_factorial) for f in factorial]

# Graficar resultados experimentales
plt.figure(figsize=(8, 5))
plt.plot(df["Tamaño (n)"], df["Tiempo promedio (s)"], marker='o', color="tab:blue", label="Tiempos reales (experimentales)")
plt.plot(df["Tamaño (n)"], df["O(n!)"], linestyle="--", color="tab:orange", label="Crecimiento teórico O(n!)")

plt.xscale("log")
plt.yscale("log")
plt.xlabel("Tamaño (n)")
plt.ylabel("Tiempo (s)")
plt.title("Comparación de rendimiento: Fuerza Bruta vs Complejidad Teórica")
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.savefig("docs/grafico_fuerza_bruta.png")
plt.show()

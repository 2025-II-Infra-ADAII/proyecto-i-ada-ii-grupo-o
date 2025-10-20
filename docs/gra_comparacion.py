import pandas as pd
import matplotlib.pyplot as plt
import math

# Cargar resultados guardados por las pruebas
df = pd.read_csv("docs/resultados_voraz.csv")

# Calcular valores teóricos O(n log n)
df["O(n log n)"] = [n * math.log(n) / 100000 for n in df["Tamaño (n)"]]

# Graficar resultados experimentales
plt.figure(figsize=(8, 5))
plt.plot(df["Tamaño (n)"], df["Tiempo promedio (s)"], marker='o', label="Tiempos reales (experimentales)")
plt.plot(df["Tamaño (n)"], df["O(n log n)"], linestyle="--", label="Crecimiento teórico O(n log n)")

plt.xscale("log")
plt.yscale("log")
plt.xlabel("Tamaño (n)")
plt.ylabel("Tiempo (s)")
plt.title("Comparación de rendimiento: Voraz vs Complejidad Teórica")
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.savefig("docs/grafico_voraz.png")
plt.show()
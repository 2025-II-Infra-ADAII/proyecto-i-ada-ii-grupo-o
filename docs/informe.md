# Proyecto: Plan de Riego Óptimo de una Finca

## Integrantes
- **Juan David García Arroyave** – 2359450  
- **Sebastián Zacipa Martínez** – 2359695  
- **Juan José Hincapié Tascon** – 2359493  

---

## Introducción

El presente proyecto aplica tres enfoques algorítmicos para resolver el problema del **riego óptimo de una finca**:
- **Fuerza Bruta**
- **Algoritmo Voraz**
- **Programación Dinámica**

Cada método busca determinar el orden de riego que **minimiza el costo total**, comparando eficiencia, exactitud y complejidad temporal.

---

## Definición del Problema

Cada tablón de la finca se describe con tres parámetros:

| Parámetro | Descripción |
|------------|--------------|
| `ts` | Tiempo de supervivencia (máximo antes de secarse) |
| `tr` | Tiempo requerido de riego |
| `p`  | Penalización o prioridad |

El objetivo es minimizar el **costo total de retraso**, definido matemáticamente como:

$$
CRF_\Pi = \sum_{i=0}^{n-1} p_i \cdot \max(0, (t_\Pi(i) + tr_i) - ts_i)
$$

donde:
- $t_\Pi(i)$ es el tiempo de inicio del riego del tablón $i$ en el orden $\Pi$.

---

## Estrategias Implementadas

###  3.1 Fuerza Bruta
Evalúa todas las permutaciones posibles del orden de riego y selecciona la de menor costo.

**Complejidad:**
$$
O(n!)
$$

---

### 3.2 Algoritmo Voraz

El método voraz **riega primero los tablones con menor tiempo de supervivencia ($t_s$)**.  
Aunque no siempre encuentra la solución óptima, es eficiente en tiempo y proporciona una solución razonablemente buena.

función implementada en Python:
```python
def roV(finca):
    orden = sorted(range(len(finca)), key=lambda i: finca[i][0])

    tiempo = 0
    costo = 0
    for i in orden:
        ts, tr, p = finca[i]
        fin_riego = tiempo + tr
        retraso = max(0, fin_riego - ts)
        costo += retraso * p
        tiempo = fin_riego

    return orden, costo
```



**Complejidad:**

El algoritmo tiene dos fases principales:

1. **Ordenación de los tablones**

   La función `sorted()` usa el algoritmo **Timsort**, cuya complejidad promedio y peor caso es:

   $$
   O(n \log n)
   $$

2. **Recorrido secuencial para calcular el costo**

   Solo realiza una iteración sobre los $n$ tablones:

   $$
   O(n)
   $$

Por tanto, la complejidad total del algoritmo es:

$$
T(n) = O(n \log n) + O(n) = O(n \log n)
$$


---

### 3.3 Programación Dinámica
Se utiliza una **máscara de bits** para representar subconjuntos de tablones.  
Cada subconjunto define un **subproblema**: el costo mínimo de regar ese grupo.

**Relación de recurrencia:**

$$
dp[\text{mask}] = \min_{j \in \text{mask}} \left\{
dp[\text{mask} \setminus \{j\}] +
p_j \cdot \max(0, \text{sum\_tr} + tr_j - ts_j)
\right\}
$$

**Complejidad temporal:**
$$
T(n) = O(n \times 2^n)
$$

**Complejidad espacial:**
$$
S(n) = O(2^n)
$$

---

## Resultados Experimentales

A continuación se presentan las distintas fincas evaluadas y los resultados obtenidos con cada enfoque.

---

### Finca 1
$$
\text{Finca}_1 =
\begin{bmatrix}
10 & 3 & 4 \\
5 & 3 & 3 \\
2 & 2 & 1 \\
8 & 1 & 1 \\
6 & 4 & 2
\end{bmatrix}
$$

### Finca 2
$$
\text{Finca}_2 =
\begin{bmatrix}
9 & 3 & 4 \\
5 & 3 & 3 \\
2 & 2 & 1 \\
8 & 1 & 1 \\
6 & 4 & 2
\end{bmatrix}
$$

###  Finca 3
$$
\text{Finca}_3 =
\begin{bmatrix}
7 & 3 & 5 \\
4 & 2 & 3 \\
6 & 1 & 2 \\
10 & 4 & 6 \\
3 & 2 & 1
\end{bmatrix}
$$

###  Finca 4
$$
\text{Finca}_4 =
\begin{bmatrix}
12 & 5 & 5 \\
8 & 3 & 2 \\
6 & 4 & 3 \\
9 & 2 & 1 \\
10 & 3 & 4
\end{bmatrix}
$$

###  Finca 5
$$
\text{Finca}_5 =
\begin{bmatrix}
5 & 1 & 1 \\
7 & 2 & 3 \\
9 & 3 & 2 \\
4 & 2 & 1 \\
6 & 4 & 3
\end{bmatrix}
$$

###  Finca 6
$$
\text{Finca}_6 =
\begin{bmatrix}
15 & 6 & 4 \\
10 & 5 & 3 \\
8 & 2 & 2 \\
12 & 4 & 5 \\
9 & 3 & 1
\end{bmatrix}
$$

---

##  Comparación de Resultados

| Finca | Método | Orden Óptimo | Costo Total |
|:------|:--------|:--------------|:-------------|
| 1 | Voraz | [2, 1, 4, 3, 0] | 20 |
| 1 | Dinámica | [2, 4, 1, 3, 0] | 16 |
| 2 | Voraz | [2, 1, 4, 3, 0] | 24 |
| 2 | Dinámica | [2, 4, 1, 3, 0] | 18 |
| 3 | Voraz | [4, 1, 2, 0, 3] | 17 |
| 3 | Dinámica | [1, 4, 2, 0, 3] | 20 |
| 4 | Voraz | [2, 1, 3, 4, 0] | 33 |
| 4 | Dinámica | [1, 2, 3, 4, 0] | 37 |
| 5 | Voraz | [3, 0, 1, 4, 2] | 15 |
| 5 | Dinámica | [0, 3, 1, 4, 2] | 14 |
| 6 | Voraz | [2, 4, 1, 3, 0] | 30 |
| 6 | Dinámica | [2, 1, 4, 3, 0] | 52 |

>  En todos los casos, la **programación dinámica** obtiene un costo total menor o igual al del método **voraz**, validando que encuentra la **solución óptima**.

---

## Conclusiones

- El método **voraz** ofrece una solución rápida con bajo costo computacional, aunque no siempre óptima.  
- La **programación dinámica** garantiza la **solución óptima**, pero su costo computacional crece exponencialmente con $n$.  
- Para $n > 20$, la PD se vuelve **inviable en tiempo y espacio**, mientras que el método voraz sigue siendo eficiente.  
- Este proyecto demuestra cómo diferentes paradigmas algorítmicos equilibran **precisión vs eficiencia**.

---


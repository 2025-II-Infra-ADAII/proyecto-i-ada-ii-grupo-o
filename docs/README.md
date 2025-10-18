# Proyecto Integrador ADA II — Plan de Riego Óptimo de una Finca

## Integrantes

| Nombre | Código |
|:-----------------------------|:----------:|
| Juan David García Arroyave | 2359450 |
| Sebastián Zacipa Martínez | 2359695 |
| Juan José Hincapié Tascon | 2359493 |

---

## Descripción del Proyecto

Este proyecto desarrolla tres enfoques algorítmicos para resolver el **problema del riego óptimo de una finca**, buscando minimizar el costo total de retraso en el riego de los tablones.

Cada tablón está definido por tres parámetros:

- `ts`: tiempo de supervivencia  
- `tr`: tiempo de riego  
- `p`: penalización o prioridad  

El costo total se define como:

$$
CRF_\Pi = \sum_{i=0}^{n-1} p_i \cdot \max(0, (t_\Pi(i) + tr_i) - ts_i)
$$

---

## ⚙️ Métodos Implementados

### 🔹 Fuerza Bruta
Evalúa todas las permutaciones posibles del orden de riego y selecciona el de menor costo.  
**Complejidad:** $O(n!)$

### 🔹 Algoritmo Voraz
Riega primero los tablones con menor tiempo de supervivencia ($t_s$).  
**Complejidad:** $O(n \log n)$

### 🔹 Programación Dinámica
Usa máscaras de bits para evaluar todos los subconjuntos posibles de tablones.  
**Complejidad:** $O(n \times 2^n)$

---




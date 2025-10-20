[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/GxFB-nwe)

# Asignación: [Plan de Riego Óptimo de una Finca]

**Fecha:** [20/10/2025]
**Curso:** [ADA II]

---

## 👥 Integrantes del Grupo

| Nombre Completo             | Código  | Rol            | Correo Electrónico                          |
|-----------------------------|---------|----------------|---------------------------------------------|
| Juan David Garcia Arroyave  | 2359450 | [Líder/Colab.] | [juan.garcia.arroyave@correounivalle.edu.co]|
| Juan Jose Hincapie Tascon   | 2359695 | [Colaborador]  | [juan.hincapie.tascon@correounivalle.edu.co]|
| Sebastian Zacipa Martinez   | 2359493 | [Colaborador]  | [sebastian.zacipa@correounivalle.edu.co]    |    

---

## 📌 Descripción del Taller

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


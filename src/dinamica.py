import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from typing import List, Tuple
import math

def roPD(finca: List[Tuple[int, int, int]]) -> Tuple[List[int], int]:
    n = len(finca)
    if n == 0:
        return [], 0
    
    tiempos_siembra = [t[0] for t in finca]
    tiempos_riego = [t[1] for t in finca]
    penalizaciones = [t[2] for t in finca]
    
    return programacion_optima_dp(tiempos_siembra, tiempos_riego, penalizaciones)

def programacion_optima_dp(tiempos_siembra: List[int], tiempos_riego: List[int], penalizaciones: List[int]) -> Tuple[List[int], int]:
    n = len(tiempos_siembra)
    N = 1 << n
    
    suma_tiempos_riego = precalcular_suma_tr(tiempos_riego, n, N)
    
    dp = [float('inf')] * N
    padre = [-1] * N
    
    dp[0] = 0
    
    for mascara in range(1, N):
        for j in range(n):
            if mascara & (1 << j):
                mascara_anterior = mascara ^ (1 << j)
                tiempo_inicio = suma_tiempos_riego[mascara_anterior]
                tiempo_finalizacion = tiempo_inicio + tiempos_riego[j]
                
                tardanza = max(0, tiempo_finalizacion - tiempos_siembra[j])
                costo_adicional = penalizaciones[j] * tardanza
                
                if dp[mascara_anterior] + costo_adicional < dp[mascara]:
                    dp[mascara] = dp[mascara_anterior] + costo_adicional
                    padre[mascara] = j
    
    permutacion = reconstruir_solucion(padre, n, N)
    costo_total = dp[N - 1]
    
    return permutacion, costo_total

def precalcular_suma_tr(tiempos_riego: List[int], n: int, N: int) -> List[int]:
    suma_tr = [0] * N
    
    for mascara in range(1, N):
        for j in range(n):
            if mascara & (1 << j):
                mascara_anterior = mascara ^ (1 << j)
                suma_tr[mascara] = suma_tr[mascara_anterior] + tiempos_riego[j]
                break
    
    return suma_tr

def reconstruir_solucion(padre: List[int], n: int, N: int) -> List[int]:
    permutacion = []
    mascara_actual = N - 1
    
    while mascara_actual > 0:
        j = padre[mascara_actual]
        if j == -1:
            break
        permutacion.append(j)
        mascara_actual = mascara_actual ^ (1 << j)
    
    return permutacion[::-1]

def calcular_costo_programacion(finca: List[Tuple[int, int, int]], permutacion: List[int]) -> int:
    tiempos_siembra = [t[0] for t in finca]
    tiempos_riego = [t[1] for t in finca]
    penalizaciones = [t[2] for t in finca]
    
    tiempo_actual = 0
    costo_total = 0
    
    for idx in permutacion:
        tiempo_finalizacion = tiempo_actual + tiempos_riego[idx]
        tardanza = max(0, tiempo_finalizacion - tiempos_siembra[idx])
        costo = penalizaciones[idx] * tardanza
        costo_total += costo
        tiempo_actual = tiempo_finalizacion
    
    return costo_total
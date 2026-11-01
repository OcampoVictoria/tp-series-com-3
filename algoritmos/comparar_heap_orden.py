import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import time
import random
from serie import Serie
from estructuras.heap import HeapMaximos


def prioridad(serie):
    return serie.año


TAMAÑOS = [10_000, 100_000, 1_000_000]
N_TOP = 5
REPETICIONES = 10

print(f"{'N':>10} | {'Ordenar todo (ms)':>18} | {'Armar heap (ms)':>16} | {'Top 5 heap (ms)':>16}")

for n in TAMAÑOS:
    series = [Serie(f"serie{i}", "Creador", random.randint(1950, 2026), "Drama") for i in range(n)]

    # La heap se arma UNA sola vez
    inicio = time.perf_counter()
    heap = HeapMaximos.desde_lista(series, clave=prioridad)
    t_armar = (time.perf_counter() - inicio) * 1000

    # Estrategia 1: ordenar todo en cada consulta
    inicio = time.perf_counter()
    for _ in range(REPETICIONES):
        sorted(series, key=prioridad, reverse=True)[:N_TOP]
    t_ordenar = (time.perf_counter() - inicio) / REPETICIONES * 1000

    # Estrategia 2: consultar la heap ya armada
    inicio = time.perf_counter()
    for _ in range(REPETICIONES):
        heap.top_n(N_TOP)
    t_heap = (time.perf_counter() - inicio) / REPETICIONES * 1000

    print(f"{n:>10} | {t_ordenar:>18.4f} | {t_armar:>16.4f} | {t_heap:>16.4f}")

print("\nOrdenar todo: se repite en CADA consulta. Heap: se arma una vez y cada consulta cuesta O(k log n).")
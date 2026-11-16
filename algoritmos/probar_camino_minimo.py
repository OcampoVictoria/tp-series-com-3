import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from gestor_series import GestorSeries
from relaciones import construir_grafo_series, costo_arista
from algoritmos.recorridos import camino_mas_corto
from algoritmos.camino_minimo import camino_minimo

gestor = GestorSeries()
gestor.cargar_desde_json("series.json")
grafo = construir_grafo_series(gestor.listar())

casos = [
    ("Pinnochio", "W: Two Worlds"),
    ("Romance is a Bonus Book", "I Hear Your Voice"),
    ("Pinnochio", "Doctor Stranger"),
]

for origen, destino in casos:
    print(f"\n{origen} -> {destino}")
    print("  BFS (menos saltos):      ", camino_mas_corto(grafo, origen, destino))
    camino, costo = camino_minimo(grafo, origen, destino, costo_arista)
    costo = None if costo is None else round(costo, 2)
    print("  Dijkstra (más afinidad): ", camino, "| costo:", costo)
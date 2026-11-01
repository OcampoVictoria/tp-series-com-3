import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from gestor_series import GestorSeries
from relaciones import construir_grafo_series
from algoritmos.recorridos import bfs, dfs, camino_mas_corto

gestor = GestorSeries()
gestor.cargar_desde_json("series.json")
grafo = construir_grafo_series(gestor.listar())

origen = "Pinnochio"   # cambialo si en tu JSON se escribe distinto

print("--- BFS desde", origen, "---")
orden, distancias, _ = bfs(grafo, origen)
for serie in orden:
    print(f"  {serie}  (a {distancias[serie]} saltos)")

print("\n--- DFS desde", origen, "---")
for serie in dfs(grafo, origen):
    print("  ", serie)

print("\n--- Caso BFS: camino más corto ---")
print("  ", camino_mas_corto(grafo, "Pinnochio", "W: Two Worlds"))

print("\n--- Serie sin conexión con Pinnochio ---")
print("  ", camino_mas_corto(grafo, "Pinnochio", "Doctor Stranger"))
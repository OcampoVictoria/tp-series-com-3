import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from gestor_series import GestorSeries
from relaciones import construir_grafo_series

gestor = GestorSeries()
gestor.cargar_desde_json("series.json")
grafo = construir_grafo_series(gestor.listar())

print(f"Vértices: {grafo.cantidad_vertices()} | Aristas: {grafo.cantidad_aristas()}")

print("\n--- Lista de adyacencia ---")
for v in grafo.vertices():
    print(f"{v} (grado {grafo.grado(v)}): {grafo.vecinos(v)}")

print("\n--- Consulta 1: series relacionadas con Pinnochio (más relacionadas primero) ---")
for vecino, peso in sorted(grafo.vecinos("Pinnochio"), key=lambda x: x[1], reverse=True):
    print(f"  {vecino} (peso {peso})")

print("\n--- Consulta 2: la serie con más conexiones ---")
mas_conectada = max(grafo.vertices(), key=grafo.grado)
print(f"  {mas_conectada} (grado {grafo.grado(mas_conectada)})")

print("\n--- Consulta 3: ¿están relacionadas Pinnochio y W: Two Worlds? ---")
print("  ", grafo.existe_arista("Pinnochio", "W: Two Worlds"))
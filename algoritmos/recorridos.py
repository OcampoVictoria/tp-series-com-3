def bfs(grafo, origen):
    """Recorrido en anchura (BFS). Devuelve (orden_de_visita, distancias, padres).

    Usa una cola: se visita primero todo lo que está a 1 salto, después a 2, etc.
    La cola es una lista con un índice al frente, para no usar pop(0), que cuesta O(n).
    """
    if not grafo.existe_vertice(origen):
        return [], {}, {}

    distancias = {origen: 0}   # también sirve como "ya visitado"
    padres = {origen: None}
    cola = [origen]
    frente = 0

    while frente < len(cola):
        actual = cola[frente]
        frente += 1
        for vecino, _peso in grafo.vecinos(actual):
            if vecino not in distancias:
                distancias[vecino] = distancias[actual] + 1
                padres[vecino] = actual
                cola.append(vecino)

    return cola, distancias, padres


def camino_mas_corto(grafo, origen, destino):
   #Camino con menos saltos entre dos series, usando BFS. None si no hay.
    _, _, padres = bfs(grafo, origen)
    if destino not in padres:
        return None
    camino = []
    actual = destino
    while actual is not None:
        camino.append(actual)
        actual = padres[actual]
    camino.reverse()
    return camino


def dfs(grafo, origen):
    #Recorrido en profundidad (DFS), recursivo. Devuelve el orden de visita.
    #Se va por un camino hasta el fondo y recién ahí vuelve para probar otro.
    
    orden = []
    if grafo.existe_vertice(origen):
        _visitar(grafo, origen, {}, orden)
    return orden


def _visitar(grafo, vertice, visitados, orden):
    visitados[vertice] = True
    orden.append(vertice)
    for vecino, _peso in grafo.vecinos(vertice):
        if vecino not in visitados:
            _visitar(grafo, vecino, visitados, orden)
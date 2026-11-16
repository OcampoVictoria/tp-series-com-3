from estructuras.heap import HeapMaximos


def dijkstra(grafo, origen, costo):
    #Camino mínimo desde origen a todos los vértices alcanzables.
    #costo(peso)` convierte el peso de una arista en su costo (debe ser >= 0).
    #Devuelve (distancias, padres).
    #Complejidad con heap: O((V + E) log V).
    
    if not grafo.existe_vertice(origen):
        return {}, {}

    distancias = {origen: 0}
    padres = {origen: None}

    # Heap de máximos con clave negativa = saca primero la distancia MENOR
    pendientes = HeapMaximos(clave=lambda t: -t[0])
    pendientes.insertar((0, origen))

    while not pendientes.esta_vacia():
        d, actual = pendientes.extraer_maximo()
        if d > distancias[actual]:
            continue  # entrada vieja: ya se encontró un camino mejor
        for vecino, peso in grafo.vecinos(actual):
            nueva = d + costo(peso)
            if vecino not in distancias or nueva < distancias[vecino]:
                distancias[vecino] = nueva
                padres[vecino] = actual
                pendientes.insertar((nueva, vecino))

    return distancias, padres


def camino_minimo(grafo, origen, destino, costo):
    """Devuelve (camino, costo_total) o (None, None) si no hay conexión."""
    distancias, padres = dijkstra(grafo, origen, costo)
    if destino not in distancias:
        return None, None
    camino = []
    actual = destino
    while actual is not None:
        camino.append(actual)
        actual = padres[actual]
    camino.reverse()
    return camino, distancias[destino]
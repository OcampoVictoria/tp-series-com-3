class Grafo:
    """Grafo no dirigido y pesado, representado con lista de adyacencia.

    _adyacencia[u] = {v: peso, ...}  ->  vecinos de u con el peso de cada arista.
    Como es no dirigido, cada arista se guarda en las dos direcciones.
    """

    def __init__(self):
        self._adyacencia = {}

    def agregar_vertice(self, v):
        if v not in self._adyacencia:
            self._adyacencia[v] = {}

    def agregar_arista(self, u, v, peso=1):
        if u == v:
            return
        self.agregar_vertice(u)
        self.agregar_vertice(v)
        self._adyacencia[u][v] = peso
        self._adyacencia[v][u] = peso

    def existe_vertice(self, v):
        return v in self._adyacencia

    def existe_arista(self, u, v):
        return u in self._adyacencia and v in self._adyacencia[u]

    def peso(self, u, v):
        return self._adyacencia[u].get(v)

    def vecinos(self, v):
        #Devuelve los vecinos de v con su peso: [(vecino, peso), ...].
        if v not in self._adyacencia:
            return []
        return list(self._adyacencia[v].items())

    def grado(self, v):
        return len(self._adyacencia.get(v, {}))

    def vertices(self):
        return list(self._adyacencia.keys())

    def cantidad_vertices(self):
        return len(self._adyacencia)

    def cantidad_aristas(self):
        return sum(len(vecinos) for vecinos in self._adyacencia.values()) // 2
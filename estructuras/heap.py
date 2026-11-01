class HeapMaximos:
    """Heap binaria de máximos: el elemento de mayor prioridad está siempre arriba.

    Se guarda en una lista: para el nodo en la posición i,
    su hijo izquierdo está en 2*i+1, el derecho en 2*i+2 y su padre en (i-1)//2.
    `clave` es una función que devuelve la prioridad de un elemento.
    """

    def __init__(self, clave):
        self._datos = []
        self._clave = clave

    def __len__(self):
        return len(self._datos)

    def esta_vacia(self):
        return len(self._datos) == 0

    # INSERTAR: O(log n) 
    def insertar(self, elemento):
        self._datos.append(elemento)
        self._subir(len(self._datos) - 1)

    def _subir(self, i):
        while i > 0:
            padre = (i - 1) // 2
            if self._clave(self._datos[i]) > self._clave(self._datos[padre]):
                self._datos[i], self._datos[padre] = self._datos[padre], self._datos[i]
                i = padre
            else:
                break

    #  VER Y EXTRAER EL MÁXIMO 
    def ver_maximo(self):
        """Devuelve el de mayor prioridad sin sacarlo: O(1)."""
        return self._datos[0] if self._datos else None

    def extraer_maximo(self):
        """Saca y devuelve el de mayor prioridad: O(log n)."""
        if not self._datos:
            return None
        maximo = self._datos[0]
        ultimo = self._datos.pop()
        if self._datos:
            self._datos[0] = ultimo
            self._bajar(0)
        return maximo

    def _bajar(self, i):
        n = len(self._datos)
        while True:
            izq = 2 * i + 1
            der = 2 * i + 2
            mayor = i
            if izq < n and self._clave(self._datos[izq]) > self._clave(self._datos[mayor]):
                mayor = izq
            if der < n and self._clave(self._datos[der]) > self._clave(self._datos[mayor]):
                mayor = der
            if mayor == i:
                break
            self._datos[i], self._datos[mayor] = self._datos[mayor], self._datos[i]
            i = mayor

    # CONSTRUIR DESDE UNA LISTA: O(n)
    @classmethod
    def desde_lista(cls, lista, clave):
        heap = cls(clave)
        heap._datos = list(lista)
        for i in range(len(heap._datos) // 2 - 1, -1, -1):
            heap._bajar(i)
        return heap

    def top_n(self, n):
        #Devuelve los n de mayor prioridad. Costo: O(k log n), sin copiar la heap.
        extraidos = []
        for _ in range(min(n, len(self._datos))):
            extraidos.append(self.extraer_maximo())
        for elemento in extraidos:
            self.insertar(elemento)
        return extraidos
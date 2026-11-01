from estructuras.grafo import Grafo


def _generos(serie):
    return {g.strip().lower() for g in serie.genero.split("/")}


def coincidencias(a, b):
    """Peso de la relación: 1 si comparten creador + 1 por cada género compartido."""
    peso = 0
    if a.creador.lower() == b.creador.lower():
        peso += 1
    peso += len(_generos(a) & _generos(b))
    return peso


def construir_grafo_series(series):
    """Arma el grafo comparando todos los pares de series: O(n²)."""
    grafo = Grafo()
    for s in series:
        grafo.agregar_vertice(s.titulo)
    for i in range(len(series)):
        for j in range(i + 1, len(series)):
            peso = coincidencias(series[i], series[j])
            if peso > 0:
                grafo.agregar_arista(series[i].titulo, series[j].titulo, peso)
    return grafo


def agregar_serie_al_grafo(grafo, nueva, existentes):
    """Suma una serie nueva comparándola con las ya cargadas: O(n)."""
    grafo.agregar_vertice(nueva.titulo)
    for otra in existentes:
        peso = coincidencias(nueva, otra)
        if peso > 0:
            grafo.agregar_arista(nueva.titulo, otra.titulo, peso)
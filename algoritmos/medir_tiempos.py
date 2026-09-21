import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "_")))

from estructuras.arbol_binario import ArbolBST
from serie import Serie

def generar_series(n):
    """genera n series ficticias con titulos unicos, para medir con distintos tamaños"""
    generos = ["Romance", "Fantasia", "Melodrama", "Thriller"]
    series =[]
    for i in range(n):
        titulo = f"serie de prueba{i}"
        creador = f"Autor {i % 50}"
        año = 2000 + (i % 25)
        genero = generos[i % len(generos)]
        series.append(Serie(titulo, creador, año, genero))
    return series

def busqueda_secuencial(lista, titulo):
    #recorre la lista elemento por elemento buscando coincidencia exacta de titulo
    titulo = titulo.lower()
    for serie in lista:
        if serie.titulo.lower() == titulo:
            return Serie
    return None

def busqueda_binaria(lista_ordenada, titulo):
    #busca por titulo en una lista ya ordenada alfabeticamente, dividiendo el rango a la mitad
    titulo = titulo.lower()
    izquierda, derecha = 0, len(lista_ordenada) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        titulo_medio = lista_ordenada[medio].titulo.lower()
        if titulo_medio == titulo:
            return lista_ordenada[medio]
        elif titulo_medio < titulo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return None

def medir_secuencial(lista, titulo):
    inicio = time.time()
    busqueda_secuencial(lista, titulo)
    fin = time.time()
    return (fin - inicio) * 1000 #milisegundos

def medir_binaria(lista, titulo):
    #el ordenamiento se hace antes del cronometro, igual que la construccion del arbol
    lista_ordenada = sorted(lista, key=lambda e: e.titulo.lower())

    inicio =time.time()
    busqueda_binaria(lista_ordenada, titulo)
    fin =time.time()
    return (fin - inicio) *1000

def medir_arbol(lista, titulo):
 #mide solo la busqueda en arbol.
    arbol = ArbolBST()
    for serie in lista:
       arbol.insertar(serie, clave=lambda e: e.titulo.lower())

    inicio = time.time()
    arbol.buscar(titulo.lower(), clave=lambda e: e.titulo.lower())
    fin = time.time()
    return (fin - inicio) * 1000 # milisegundos

def main():
    tamaños = [100, 1000, 10000, 100000]
    print(f"{'N elementos' :>12} | {'Secuencial(ms)' :>16} | {'Binaria(ms)' :>14} | {'Arbol(ms)':>12}")
    print("-" * 62)

    for n in tamaños:
        lista = generar_series(n)
        titulo_buscado = lista[-1].titulo #peor caso:el ultimo elemnto

        t_secuencial = medir_secuencial(lista, titulo_buscado)
        t_binaria = medir_binaria(lista, titulo_buscado)
        t_arbol = medir_arbol(lista, titulo_buscado)

        print(f"{n:>12} | {t_secuencial:>16.4f} | {t_binaria:>14.4f} | {t_arbol:>12.4f}")

if __name__ == "__main__":
    main()
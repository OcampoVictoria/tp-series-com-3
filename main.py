from serie import Serie
from gestor_series import GestorSeries
from estructuras.avl import AVL
from estructuras.arbol_general import ArbolGeneral
from estructuras.heap import HeapMaximos
from relaciones import construir_grafo_series, agregar_serie_al_grafo #impor nuevo

def prioridad(serie):
    #mas reciente = mas prioridad (se ordena por año de estren)
    return serie.año

def construir_arbol_categorias(series):
    #armar la jerarquia decada, año, serie a partir de las series cargadas.
    arbol = ArbolGeneral()
    arbol.insertar_raiz("series")
    nodos_decada ={}
    nodos_año ={}

    for serie in series:
        decada = f"{(serie.año // 10)* 10}s"
        año = str(serie.año)

        if decada not in nodos_decada:
            nodos_decada[decada]= arbol.agregar_hijo(arbol.raiz, decada)

        clave_año=(decada, año)
        if clave_año not in nodos_año:
            nodos_año[clave_año]= arbol.agregar_hijo(nodos_decada[decada], año)

        arbol.agregar_hijo(nodos_año[clave_año], serie.titulo)

    return arbol

def mostrar_menu():
        print("\n=== Sistema de Recomendacion de Series ===")
        print("1. Agregar serie")
        print("2. Buscar serie")
        print("3. Listar series")
        print("4. Filtrar series")
        print("5. Explorar Categorias")
        print("6. Top N series mas recientes")
        print("7. Salir")

def main():
        gestor=GestorSeries()
        gestor.cargar_desde_json("series.json")

        avl= AVL()
        for serie in gestor.listar():
          avl.insertar(serie, clave=lambda e: e.titulo.lower())

        arbol_categorias = construir_arbol_categorias(gestor.listar())

        heap = HeapMaximos.desde_lista(gestor.listar(), clave=prioridad)

        grafo = construir_grafo_series(gestor.listar())

        while True:
          mostrar_menu()
          opcion=input("Elegir una Opcion: ")

          if opcion=="1":
             titulo=input("Titulo: ")
             creador=input("Creador: ")
             año=int(input("Año: "))
             genero=input("Genero: ")
             nueva_serie=Serie(titulo,creador, año, genero)
             agregar_serie_al_grafo(grafo, nueva_serie, gestor.listar())
             gestor.agregar(nueva_serie)
             avl.insertar(nueva_serie, clave=lambda e: e.titulo.lower())
             heap.insertar(nueva_serie)
             print("Serie agregada.")

          elif opcion=="2":
             texto=input("Buscar por titulo:")
             resultados=avl.buscar(texto.lower(), clave=lambda e: e.titulo.lower())
             if resultados:
              print(resultados)
             else:
                 print("No se encontro.")

          elif opcion=="3":
              for s in gestor.listar():
               print(s)

          elif opcion=="4":
             creador=input("Filtrar por creador (Enter para omitir): ") or None
             genero=input("Filtrar por genero (Enter para omitir): ") or None
             for s in gestor.filtrar(creador=creador, genero=genero):
               print(s)

          elif opcion=="5":
              print("\nCategorias por amplitud:")
              for categoria in arbol_categorias.amplitud():
                  print(f" - {categoria}")

          elif opcion=="6":
              n = int(input("¿Cuantas series queres ver?"))
              print(f"\nTOP {n}")
              for posicion, s in enumerate(heap.top_n(n), start=1):
                  print(f"{posicion}. {s.titulo:<25} {s.año}")

          elif opcion == "7":
              texto = input("¿Relacionadas con qué serie? ")
              serie = avl.buscar(texto.lower(), clave=lambda e: e.titulo.lower())
              if serie is None:
                  print("No se encontro esa serie.")
              else:
                   vecinos = sorted(grafo.vecinos(serie.titulo), key=lambda x: x[1], reverse=True)
                   if not vecinos:
                       print("No tiene series relacionadas.")
                   for titulo, peso in vecinos:
                       print(f" {titulo} (relacion {peso})")
         
          elif opcion =="8":
              print("¡Hasta luego!")
              break

          else:
              print("Opcion invalida.")

if __name__=="__main__":
    main()
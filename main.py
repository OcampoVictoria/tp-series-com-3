from serie import Serie
from gestor_series import GestorSeries
from estructuras.avl import AVL
from estructuras.arbol_general import ArbolGeneral

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
        print("6. Salir")

def main():
        gestor=GestorSeries()
        gestor.cargar_desde_json("series.json")

        avl= AVL()
        for serie in gestor.listar():
          avl.insertar(serie, clave=lambda e: e.titulo.lower())

        arbol_categorias = construir_arbol_categorias(gestor.listar())

        while True:
          mostrar_menu()
          opcion=input("Elegir una Opcion: ")

          if opcion=="1":
             titulo=input("Titulo: ")
             creador=input("Creador: ")
             año=int(input("Año: "))
             genero=input("Genero: ")
             nueva_serie=Serie(titulo,creador, año, genero)
             gestor.agregar(nueva_serie)
             avl.insertar(nueva_serie, clave=lambda e: e.titulo.lower())
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
              print("¡Hasta luego!")
              break

          else:
              print("Opcion invalida.")

if __name__=="__main__":
    main()
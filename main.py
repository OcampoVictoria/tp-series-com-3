from serie import Serie
from gestor_series import GestorSeries
from estructuras.arbol_binario import ArbolBST    #import nuevo

def mostrar_menu():
        print("\n=== Sistema de Recomendacion de Series ===")
        print("1. Agregar serie")
        print("2. Buscar serie")
        print("3. Listar series")
        print("4. Filtrar series")
        print("5. Salir")

def main():
        gestor=GestorSeries()
        gestor.cargar_desde_json("series.json")

        arbol = ArbolBST()
        for elemento in gestor.listar():
          arbol.insertar(elemento, clave=lambda e: e.titulo.lower())

        while True:
          mostrar_menu()
          opcion=input("Opcion a elegir: ")

          if opcion=="1":
             titulo=input("Titulo: ")
             creador=input("Creador: ")
             año=int(input("Año: "))
             genero=input("Genero: ")
             nueva_serie=Serie(titulo,creador, año, genero)
             gestor.agregar(nueva_serie)
             arbol.insertar(nueva_serie, clave=lambda e: e.titulo.lower())
             print("Serie agregada.")

          elif opcion=="2":
             texto=input("Buscar por titulo:")
             resultados=arbol.buscar(texto.lower(), clave=lambda e: e.titulo.lower())
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
              print("¡Hasta luego!")
              break

          else:
              print("Opcion invalida.")

if __name__=="__main__":
    main()
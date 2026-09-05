from serie import Serie
from gestor_series import GestorSeries

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

        while True:
          mostrar_menu()
          opcion=input("Opcion a elegir: ")

          if opcion=="1":
             titulo=input("Titulo: ")
             creador=input("Creador: ")
             año=int(input("Año: "))
             genero=input("Genero: ")
             gestor.agregar(Serie(titulo, creador, año, genero))
             print("Serie agregada.")

          elif opcion=="2":
             texto=input("Buscar por titulo:")
             resultados=gestor.buscar(texto)
             for s in resultados:
              print(s)

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
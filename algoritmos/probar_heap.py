import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from serie import Serie
from estructuras.heap import HeapMaximos


def prioridad(serie):
    return serie.año


def main():
    series = [
        Serie("I Hear Your Voice", "Park Hye-ryun", 2013, "Fantasía/Legal"),
        Serie("Pinocchio", "Park Hye-ryun", 2014, "Romance/Drama"),
        Serie("While You Were Sleeping", "Park Hye-ryun", 2017, "Fantasía/Romance"),
        Serie("W: Two Worlds", "Song Jae-jeong", 2016, "Fantasía/Thriller"),
        Serie("Doctor Stranger", "Park Jin-woo", 2014, "Melodrama/Médico"),
        Serie("Romance is a Bonus Book", "Jung Sun-young", 2019, "Romance"),
    ]

    # Se arman SIN orden; la heap deja arriba la de mayor prioridad
    heap = HeapMaximos.desde_lista(series, clave=prioridad)

    print("Máximo (sin sacarlo):", heap.ver_maximo())

    print("\n--- TOP 3 ---")
    for i, s in enumerate(heap.top_n(3), start=1):
        print(f"{i}. {s.titulo} ({s.año})")

    print("\n--- Inserto una serie más nueva ---")
    heap.insertar(Serie("Serie de prueba", "Alguien", 2026, "Drama"))
    print("Nuevo máximo:", heap.ver_maximo())

    print("\n--- Extraigo todo en orden ---")
    while not heap.esta_vacia():
        s = heap.extraer_maximo()
        print(f"  {s.titulo} ({s.año})")


if __name__ == "__main__":
    main()
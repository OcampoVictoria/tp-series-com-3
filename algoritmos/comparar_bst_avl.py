import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
 
import time
import threading
from serie import Serie
from estructuras.arboles import ArbolBST
from estructuras.avl import AVL

def ejecutar_comparacion():
    tamaños = [1_000, 10_000, 100_000]
    TAMAÑO_MAXIMO_BST = 10_000 # mas que esto, el BST degenerado tarda horas (O(n²))
    REPETICIONES = 200 
 
    print(f"{'N' :>8} | {'Altura BST' :>11} | {'Altura AVL' :>11} | {'Busq. BST (ms)' :>15} | {'Busq. AVL (ms)' :>15}")

    for n in tamaños:
        series = [Serie(f"serie{i:06d}", "Creador", 2010, "Drama") for i in range(n)]

        avl = AVL()
        for s in series:
           avl.insertar(s, clave=lambda e: e.titulo.lower())

        objetivo =series[-1].titulo.lower()

        inicio = time.perf_counter()
        for _ in range(REPETICIONES):
            avl.buscar(objetivo, clave=lambda e: e.titulo.lower())
        t_avl = (time.perf_counter() - inicio) / REPETICIONES * 1000

        if n<= TAMAÑO_MAXIMO_BST:
            bst =ArbolBST()
            for s in series:
                bst.insertar(s, clave=lambda e: e.titulo.lower())

            inicio = time.perf_counter()
            for _ in range(REPETICIONES):
                bst.buscar(objetivo, clave=lambda e: e.titulo.lower())
            t_bst = (time.perf_counter() - inicio) / REPETICIONES * 1000

            print(f"{n:>8} | {bst.altura():>11} | {avl.altura():>11} | {t_bst:>15.4f} | {t_avl:>15.4f}")
        else:
            print(f"{n:>8} | {'N/A':>11} | {avl.altura():>11} | {'inviable*':>15} | {t_avl:>15.4f}")

    print("\n* Con N=100.000, el BST degenerado requiere ~5.000 millones de operaciones")
    print("  para insertarse (O(n²) en el peor caso) — inviable en tiempo razonable.")
    print("  Esto demuestra en la práctica el problema que el AVL resuelve.")


if __name__== "__main__":
    sys.setrecursionlimit(50_000)
    threading.stack_size(64 * 1024 * 1024)
    hilo = threading.Thread(target=ejecutar_comparacion)
    hilo.start()
    hilo.join()
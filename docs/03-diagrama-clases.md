# Diagrama de clases — CrossVerse

## Diagrama

```mermaid
classDiagram
    class Serie {
        -titulo : str
        -creador : str
        -anio : int
        -genero : str
    }

    class GestorSeries {
        -series : list
        +agregar(serie)
        +cargar_desde_json(ruta)
        +buscar(titulo)
        +listar()
        +filtrar(creador, genero)
    }

    class NodoAVL {
        +dato
        +izquierdo
        +derecho
        +altura
    }
    class AVL {
        +raiz
        +insertar(dato, clave)
        +buscar(valor, clave)
        +inorder()
        +altura()
    }

    class NodoArbol {
        +dato
        +izquierdo
        +derecho
    }
    class ArbolBST {
        +raiz
        +insertar(dato, clave)
        +buscar(valor, clave)
        +inorder()
        +altura()
    }

    class NodoGeneral {
        +dato
        +hijos
    }
    class ArbolGeneral {
        +raiz
        +insertar_raiz(dato)
        +agregar_hijo(padre, dato)
        +buscar(valor)
        +amplitud()
        +profundidad_preorder()
    }

    class HeapMaximos {
        -datos : list
        -clave
        +insertar(elemento)
        +extraer_maximo()
        +ver_maximo()
        +desde_lista(lista, clave)
        +top_n(n)
    }

    class Grafo {
        -adyacencia : dict
        +agregar_vertice(v)
        +agregar_arista(u, v, peso)
        +vecinos(v)
        +grado(v)
        +existe_arista(u, v)
        +vertices()
    }

    class relaciones {
        <<module>>
        +coincidencias(a, b)
        +construir_grafo_series(series)
        +agregar_serie_al_grafo(grafo, nueva, existentes)
        +costo_arista(peso)
    }

    class recorridos {
        <<module>>
        +bfs(grafo, origen)
        +dfs(grafo, origen)
        +camino_mas_corto(grafo, origen, destino)
    }

    class camino_minimo {
        <<module>>
        +dijkstra(grafo, origen, costo)
        +camino_minimo(grafo, origen, destino, costo)
    }

    class main {
        <<module>>
        +prioridad(serie)
        +construir_arbol_categorias(series)
        +main()
    }

    GestorSeries "1" o-- "*" Serie : contiene
    AVL *-- NodoAVL
    ArbolBST *-- NodoArbol
    ArbolGeneral *-- NodoGeneral
    AVL ..> Serie : almacena
    HeapMaximos ..> Serie : ordena
    relaciones ..> Grafo : construye
    relaciones ..> Serie : compara
    recorridos ..> Grafo : recorre
    camino_minimo ..> Grafo : recorre
    camino_minimo ..> HeapMaximos : cola de prioridad
    main ..> GestorSeries
    main ..> AVL
    main ..> ArbolGeneral
    main ..> HeapMaximos
    main ..> relaciones
    main ..> recorridos
    main ..> camino_minimo
```

## Relaciones principales

| Relación | Tipo | Significado |
|---|---|---|
| `GestorSeries` — `Serie` | agregación | El gestor contiene la lista de series. |
| `AVL` — `NodoAVL`, `ArbolBST` — `NodoArbol`, `ArbolGeneral` — `NodoGeneral` | composición | Cada árbol está formado por sus nodos. |
| `AVL`, `HeapMaximos` → `Serie` | dependencia | Guardan y ordenan objetos `Serie` usando una función clave. |
| `Grafo` | independiente del dominio | Sus vértices son títulos; `relaciones` decide qué series se conectan y con qué peso. |
| `camino_minimo` → `HeapMaximos` | dependencia | Dijkstra usa la heap propia como cola de prioridad. |

## Notas

- `ArbolBST` quedó de la etapa del árbol binario y se conserva en el repositorio. El menú usa `AVL`.
- Los módulos `relaciones`, `recorridos` y `camino_minimo` contienen funciones, no clases.
- `Serie` expone sus atributos mediante propiedades de solo lectura (encapsulamiento).
# CrossVerse - Sistema de Recomendacion de Series

## Descripcion
Sistema que permite guardar, buscar, listar y filtrar series de un mismo universo narrativo (mismo creador / guionista), tomando como caso de estudio las series del actor Lee Jong-suk. Es el primer paso hacia un sitema de recomendaciones que relacione series entre si.

## Integrantes
Ocampo victoria, 
Arteaga Lautaro
  
## Estructura del proyecto 
  
```
├── main.py                  # menú de terminal
├── serie.py                 # clase Serie
├── gestor_series.py         # carga y operaciones sobre el catálogo
├── relaciones.py            # reglas de relación entre series y construcción del grafo
├── series.json              # datos de ejemplo
├── estructuras/
│   ├── arbol_binario.py     # árbol binario de búsqueda (etapa 3)
│   ├── arboles.py           # árbol binario de búsqueda usado por la comparación con el AVL
│   ├── avl.py               # árbol AVL
│   ├── arbol_general.py     # árbol general (n-ario)
│   ├── heap.py              # heap de máximos
│   └── grafo.py             # grafo con lista de adyacencia
├── algoritmos/
│   ├── recorridos.py        # BFS y DFS
│   ├── camino_minimo.py     # Dijkstra
│   └── ...                  # scripts de prueba y de medición de tiempos
├── docs/                    # documentación y análisis de cada etapa
└── README.md
```

## Como ejecutar 

1. Descarga o clonar el repositorio:
 ```https://github.com/OcampoVictoria/tp-series-com-3.git```
2. Ubicarse en la carpeta del proyecto.
3. Ejecutar:
 ```python main.py```
4. Elegir una opcion del menu escribiendo su numero. Los titulos se pueden escribir en mayusculas o minusculas, pero completos(por ejemplo, `pinnochio`, tal como figura en `series.json`).

## Menu
| Opcion | Funcion | Estructura o algoritmo |
|---|---|---|
| 1 | Agregar serie | actualiza lista, AVL, heap y grafo |
| 2 | Buscar serie por titulo | AVL |
| 3 | Listar series | lista |
| 4 | Filtrar por creador y/o genero | lista |
| 5 | Explorar categorias (decada → año → serie) | arbol general |
| 6 | Top N series mas recientes | heap de maximos |
| 7 | Series relacionadas | grafo |
| 8 | Camino con menos saltos entre dos series | BFS |
| 9 | Explorar el universo de una serie | DFS |
| 10 | Mejor camino de afinidad entre dos series | Dijkstra |
| 11 | Salir | |

## Documentación
 
- [Propuesta](docs/00-propuesta.md)
- [Requerimientos](docs/01-requerimientos.md)
- [Casos de uso](docs/02-casos-de-uso.md)
- [Diagrama de clases](docs/03-diagrama-clases.md)
- [Diagrama de datos](docs/04-diagrama-datos.md)
- [Análisis del árbol binario](docs/07-analisis-tp3.md)
- [Análisis de AVL y árbol general](docs/08-analisis-tp4-tp5.md)
- [Análisis de grafos y recorridos](docs/10-analisis-grafos-recorridos.md)
- [Análisis de optimización](docs/11-analisis-optimizacion.md)
   
## Estado actual
- [x] clase `Serie` con encapsulamiento
- [x] Clase `GestorSeries` para gestion de datos
- [x] Carga de datos desde JSON
- [x] Operaciones: agregar, buscar, listar, filtrar
- [x] Interfaz de terminal
- [x] Busqueda de arbol binario y AVL
- [x] Arbol general de categorias
- [x] Cola de prioridad (heap) y Top N
- [x] Grafo de relaciones entre series
- [x] Recorridos BFS y DFS
- [x] Camino de mayor afinidad con Dijkstra

## Limitaciones conocidas
- Las series agregadas desde el menu no se guardan en `series.json`.
- El arbol de categorias no incluye las series agregadas hasta reiniciar el programa.
- La busqueda por titulo es exacta, no parcial.

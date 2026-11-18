# Requerimientos — CrossVerse

CrossVerse es un sistema de recomendación de series por terminal. Guarda un catálogo de series,
las busca, las ordena, las relaciona entre sí (mismo creador o género) y recomienda a partir de
una serie dada.

## 1. Requerimientos funcionales

| ID | Requerimiento | Opción del menú |
|---|---|---|
| RF01 | El sistema debe cargar el catálogo de series desde un archivo JSON al iniciar. | (al iniciar) |
| RF02 | El sistema debe permitir agregar una serie nueva (título, creador, año, género) y dejarla disponible en la búsqueda, el Top N y las relaciones. | 1 |
| RF03 | El sistema debe permitir buscar una serie por título, sin distinguir mayúsculas de minúsculas. | 2 |
| RF04 | El sistema debe listar todas las series cargadas. | 3 |
| RF05 | El sistema debe filtrar las series por creador y/o género. | 4 |
| RF06 | El sistema debe permitir explorar el catálogo como una jerarquía década → año → serie. | 5 |
| RF07 | El sistema debe mostrar el Top N de series más recientes, con N elegido por el usuario. | 6 |
| RF08 | El sistema debe mostrar las series relacionadas con una dada, ordenadas de más a menos relacionada. | 7 |
| RF09 | El sistema debe encontrar el camino con menos saltos entre dos series, mostrando la secuencia completa de series intermedias. | 8 |
| RF10 | El sistema debe explorar en profundidad todas las series conectadas a una dada. | 9 |
| RF11 | El sistema debe encontrar el camino de mayor afinidad (menor costo) entre dos series, mostrando la secuencia y el costo total. | 10 |

## 2. Requerimientos no funcionales

| ID | Requerimiento | Cómo se cumple |
|---|---|---|
| RNF01 | La búsqueda por título debe resolverse en tiempo logarítmico. | AVL (árbol auto-balanceado). Con 10.000 series insertadas en orden, altura 14 y búsqueda de ~0,006 ms, contra altura 10.000 de un BST común. |
| RNF02 | El Top N no debe reordenar todo el catálogo en cada consulta. | Heap de máximos: se arma una vez y cada consulta cuesta O(k log n). Con 1.000.000 de series, Top 5 en ~0,065 ms. |
| RNF03 | Los recorridos del grafo deben costar O(V + E). | Grafo con lista de adyacencia; BFS y DFS. |
| RNF04 | El camino de menor costo debe resolverse con un algoritmo válido para las propiedades del grafo. | Dijkstra con heap, O((V + E) log V): costos positivos, grafo no dirigido y ralo. |
| RNF05 | El sistema debe ejecutarse desde terminal con Python 3.10 o superior, sin instalar librerías externas. | Solo biblioteca estándar. |
| RNF06 | Las estructuras de datos y los algoritmos deben estar implementados por el equipo. | Sin `heapq`, sin librerías de grafos. |
| RNF07 | La búsqueda desde el menú debe ser tolerante a mayúsculas y minúsculas. | El AVL compara el título normalizado a minúsculas. |
| RNF08 | Cada etapa debe conservar las funcionalidades de las etapas anteriores. | `main.py` integra todas las estructuras. |

## 3. Alcance

El sistema:
- trabaja con un catálogo de series cargado desde `series.json`;
- relaciona series por creador y género compartidos (peso = cantidad de coincidencias);
- ofrece todas sus funciones desde un menú de terminal.

## 4. Fuera de alcance

- Autenticación de usuarios ni perfiles personalizados.
- Recomendaciones basadas en puntuaciones o gustos de cada usuario.
- Persistencia de las series agregadas durante la ejecución: no se guardan de vuelta en el JSON.
- Interfaz gráfica o bot de Telegram.
- Ordenamiento topológico: el dominio no tiene dependencias entre series ("ver primero X").
# CrossVerse - Sistema de Recomendacion de Series

## Descripcion
Sistema que permite guardar, buscar, listar y filtrar series de un mismo universo narrativo (mismo creador / guionista), tomando como caso de estudio las series del actor Lee Jong-suk. Es el primer paso hacia un sitema de recomendaciones que relacione series entre si.

## Integrantes
Ocampo victoria (por ahora )
  
## Estructura del proyecto 
| crossverse |
|---|
| main.py # Punto de entrada, menu de terminal
| serie.py # Clase Serie
| gestor_series.py # Clase GestorSeries
| series.json # Datos de prueba(series de Lee Jomg-suk)
| README.md

## Como ejecutar 
1. Ubicarse en la carpeta del proyecto por terminal.
2. Ejecutar:
3. Usar el menu numerico para agregar, buscar, listar o filtrar series.
   
## Estado actual
- [x] clase `Serie` con encapsulamiento
- [x] Clase `GestorSeries` para gestiom de datos
- [x] Carga de datos desde JSON
- [x] Operaciones: agregar, buscar, listar, filtrar
- [x] Interfaz de terminal

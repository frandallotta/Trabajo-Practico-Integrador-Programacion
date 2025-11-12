# Sistema de Gestión de Datos de Países

## Descripción del Programa

Sistema desarrollado en Python 3.x que permite gestionar y analizar información sobre países del mundo. El programa trabaja con un dataset en formato CSV que contiene datos de nombre, población, superficie y continente de cada país.

La aplicación implementa funcionalidades completas de CRUD (Crear, Leer, Actualizar), junto con herramientas avanzadas de búsqueda, filtrado, ordenamiento y generación de estadísticas, permitiendo realizar análisis demográficos y geográficos de manera eficiente.

## Características Principales

- Carga y lectura de datos desde archivo CSV
- Agregar nuevos países con validación de datos
- Actualizar información de población y superficie
- Búsqueda de países por nombre (exacta o parcial)
- Filtrado por continente, rango de población y superficie
- Ordenamiento múltiple (nombre, población, superficie)
- Generación de estadísticas descriptivas
- Manejo robusto de errores y validaciones
- Interfaz de menú interactivo en consola

## Requisitos del Sistema

- Python 3.x
- Módulos estándar: csv, os, sys (incluidos en Python)
- Archivo CSV con estructura: nombre, poblacion, superficie, continente

## Estructura del Proyecto
```
proyecto/
│
├── main.py                 # Programa principal con menú
├── funciones.py           # Módulo de funciones auxiliares
├── paises.csv            # Dataset base de países
├── README.md             # Este archivo
└── docs/
    ├── marco_teorico.pdf
    ├── capturas/
    └── conclusiones.pdf
```

## Instrucciones de Uso

### 1. Instalación

Clone el repositorio:
```bash
git clone https://github.com/usuario/gestion-paises.git
cd gestion-paises
```

### 2. Ejecución

Ejecute el programa principal:
```bash
python main.py
```

### 3. Navegación por el Menú

Al iniciar, el programa muestra un menú con las siguientes opciones:
```
=== SISTEMA DE GESTIÓN DE PAÍSES ===
1. Cargar datos desde CSV
2. Agregar nuevo país
3. Actualizar datos de un país
4. Buscar país por nombre
5. Filtrar países
6. Ordenar países
7. Mostrar estadísticas
8. Listar todos los países
9. Guardar cambios
0. Salir
```

Ingrese el número correspondiente a la opción deseada y presione Enter.

## Ejemplos de Uso

### Ejemplo 1: Agregar un nuevo país
```
Seleccione opción: 2

--- Agregar Nuevo País ---
Nombre del país: Francia
Población: 67390000
Superficie (km²): 551695
Continente: Europa

País agregado exitosamente.
```

### Ejemplo 2: Buscar país por nombre
```
Seleccione opción: 4

--- Buscar País ---
Ingrese nombre (parcial o completo): arg

Resultados encontrados:
- Argentina | Población: 45,376,763 | Superficie: 2,780,400 km² | Continente: América
```

### Ejemplo 3: Filtrar por continente
```
Seleccione opción: 5

--- Filtrar Países ---
1. Por continente
2. Por rango de población
3. Por rango de superficie
Seleccione tipo de filtro: 1

Ingrese continente: Asia

Países en Asia:
- Japón | Población: 125,800,000 | Superficie: 377,975 km²
- China | Población: 1,411,750,000 | Superficie: 9,596,961 km²
Total: 2 países
```

### Ejemplo 4: Ordenar por población
```
Seleccione opción: 6

--- Ordenar Países ---
1. Por nombre
2. Por población
3. Por superficie
Seleccione criterio: 2

¿Orden ascendente? (s/n): n

Países ordenados por población (descendente):
1. China | Población: 1,411,750,000
2. India | Población: 1,393,409,038
3. Estados Unidos | Población: 331,893,745
...
```

### Ejemplo 5: Estadísticas generales
```
Seleccione opción: 7

=== ESTADÍSTICAS GENERALES ===

País con mayor población: China (1,411,750,000 habitantes)
País con menor población: Vaticano (825 habitantes)

Promedio de población: 38,456,231 habitantes
Promedio de superficie: 642,891 km²

--- Países por Continente ---
África: 54 países
América: 35 países
Asia: 48 países
Europa: 44 países
Oceanía: 14 países
```

## Validaciones Implementadas

- Campos obligatorios al agregar países (no se permiten valores vacíos)
- Validación de tipos de datos (población y superficie deben ser numéricos)
- Manejo de errores en lectura de archivos CSV
- Búsquedas sin resultados informadas claramente
- Prevención de duplicados al agregar países
- Validación de rangos numéricos en filtros

## Estructura del Archivo CSV

El archivo `paises.csv` debe seguir el siguiente formato:
```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
Brasil,213993437,8515767,América
Alemania,83149300,357022,Europa
```

## Participación de los Integrantes

### Franco Gasparin D'Allotta - Comisión 5
- Desarrollo del marco teórico completo
- Investigación y documentación de conceptos fundamentales
- Revisión exhaustiva del código
- Correcciones y optimizaciones del sistema
- Preparación de documentación técnica

### Lautaro German Lugones - Comisión 7
- Creación inicial del código y estructura del programa
- Implementación de funcionalidades principales
- Diseño y estructura del video tutorial
- Desarrollo de la lógica de procesamiento de datos

**Trabajo colaborativo:**
- Testing conjunto del sistema
- Preparación de ejemplos y casos de prueba
- Redacción de conclusiones grupales
- Integración final del proyecto

## Tecnologías Utilizadas

- Python 3.x
- Módulo csv para manejo de archivos
- Estructuras de datos: listas y diccionarios
- Funciones modulares para organización del código
- Control de flujo con condicionales y bucles

## Contacto y Soporte

Para consultas o reportar problemas:
- Repositorio: https://github.com/usuario/gestion-paises
- Issues: https://github.com/usuario/gestion-paises/issues

## Licencia

Proyecto académico desarrollado para Programación 1 - Tecnicatura Universitaria en Programación.

---

Última actualización: Noviembre 2025

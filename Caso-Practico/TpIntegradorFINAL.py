# funcion 1 AGREGAR PAISES
def agregar_pais(parametro_catalogo: list[dict[str,int]]):
    print("\n    Agregar pais    ")

    cantidad_paises = input("¿Cuántos paises desea ingresar? ")
    
    if not cantidad_paises.isdigit():
        print("Por favor, ingrese un número válido.")
        return

    int_cantidad_paises = int(cantidad_paises)
    if int_cantidad_paises <= 0:
        print("Debe ingresar al menos un pais.")
        return
       
    contador=0
    while contador < int_cantidad_paises:
        print(f"\nPais {contador+1} de {int_cantidad_paises}:")
        nombre_nuevo = input("Ingrese el nombre del pais: ").strip()
        poblacion_nueva = input("Ingrese la poblacion del pais: ").strip()

        if not poblacion_nueva.isdigit():
            print("poblacion inválida. Se omite este pais.")
            continue

        poblacion_int = int(poblacion_nueva)
        if poblacion_int < 0:
            print("La poblacion no puede ser negativa. Se omite este pais.")
            continue
        
        superficie_nueva = input("Ingrese la superficie del pais: km2 ").strip()
        
        if not superficie_nueva.isdigit():
            print("superficie inválida. Se omite este pais.")
            continue

        superficie_int = int(superficie_nueva)
        if superficie_int < 0:
            print("La superficie no puede ser negativa. Se omite este pais.")
            continue

        print("Seleccione el continente:")
        print("(A-AMERICA / E-EUROPA / AS-ASIA / O-OCEANIA / AF-AFRICA)")
        continente_codigo = input("Ingrese el código del continente: ").strip().upper()
        
        continentes = {
            "A": "America",
            "E": "Europa",
            "AS": "Asia",
            "O": "Oceania",
            "AF": "Africa"
        }
        
        if continente_codigo not in continentes:
            print("Código de continente inválido. Se omite este pais.")
            continue
        
        continente_nuevo = continentes[continente_codigo]

        parametro_catalogo.append({
            "nombre": nombre_nuevo,
            "poblacion": poblacion_int,
            "superficie": superficie_int,
            "continente": continente_nuevo
        })
        print("Pais agregado correctamente.")

        with open(file="paises.csv", mode="a", newline='') as archivo:
            catalogowriter = csv.writer(archivo)
            catalogowriter.writerow([nombre_nuevo,poblacion_int,superficie_int,continente_nuevo])

        contador+=1

    print(f"\nFinalizado. Paises agregagos al catalogo!")

# funcion 2 ACTUALIZAR DATOS
def actualizar_datos(parametro_catalogo: list[dict[str,int]]):
    print("\n    Actualizar datos    ")

    if not parametro_catalogo:
        print("El catálogo está vacío.")
        return

    operacion = input("Dato a modificar (P = poblacion / S = superficie): ").strip().lower()
    nombre_buscar = input("Ingrese el nombre del pais: ").strip()

    pais_encontrado = False

    contador=0
    while contador < len(parametro_catalogo):
        pais = parametro_catalogo[contador]

        if pais['nombre'].lower() != nombre_buscar.lower():
            contador+=1
            continue

        pais_encontrado = True
        if operacion == "p":
            if parametro_catalogo[contador]['poblacion'] > 0:
                poblacion_nueva = input("Ingrese la poblacion del pais: ").strip()
                if poblacion_nueva.isdigit():
                    poblacion_int = int(poblacion_nueva)
                    parametro_catalogo[contador]['poblacion'] = poblacion_int
                    print(f"Nueva poblacion de '{parametro_catalogo[contador]['nombre']}': {parametro_catalogo[contador]['poblacion']}")
                else:
                    print("Valor inválido.")
                    return   
            else:
                print(f"'{parametro_catalogo[contador]['nombre']}' No tiene poblacion")
                return

        elif operacion == "s":
            superficie_nueva = input("Ingrese la superficie del pais: ").strip()
            if superficie_nueva.isdigit():
                superficie_int = int(superficie_nueva)
                parametro_catalogo[contador]['superficie'] = superficie_int
                print(f"Nueva superficie de '{parametro_catalogo[contador]['nombre']}': {parametro_catalogo[contador]['superficie']}")
            else:
                print("Valor inválido.")
                return
        else:
            print("Operación inválida. Debe ingresar 'P' o 'S'.")
            return
        
        with open("paises.csv", "w", newline='') as archivo:   
            contador=0
            catalogowriter = csv.writer(archivo)
            catalogowriter.writerow(["nombre", "poblacion","superficie","continente"])
            while contador < len(parametro_catalogo):
                pais = parametro_catalogo[contador]
                catalogowriter.writerow([pais['nombre'],pais['poblacion'],pais['superficie'],pais['continente']])
                contador+=1

    if not pais_encontrado:
        print("El pais no se encontró en el catálogo.")

# funcion 3 BUSCAR PAIS
def buscar_pais(parametro_catalogo: list[dict[str,int]]):
    print("\n    Buscar país    ")
    termino = input("Ingrese nombre o parte del nombre: ").strip().lower()
    encontrados = []
    for pais in catalogo:
        if termino in pais["nombre"].lower():
            encontrados.append(pais)

    if len(encontrados) == 0:
        print("No se encontraron países.")
    else:
        print("Resultados:")
        for p in encontrados:
            print(f"- {p['nombre']} | Población: {p['poblacion']} | Superficie: {p['superficie']} | Continente: {p['continente']}")

# funcion 4 FILTRAR PAIS
def filtrar_pais(parametro_catalogo: list[dict[str,int]]):
    print("\nFiltrar país:")
    print("1 - Filtrar por continente")
    print("2 - Filtrar por rango de población")
    print("3 - Filtrar por rango de superficie")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("Seleccione el continente:")
        print("(A-AMERICA / E-EUROPA / AS-ASIA / O-OCEANIA / AF-AFRICA)")
        continente_codigo = input("Ingrese el código del continente: ").strip().upper()
        
        continentes = {
            "A": "america",
            "E": "europa",
            "AS": "asia",
            "O": "oceania",
            "AF": "africa"
        }
        
        if continente_codigo not in continentes:
            print("Código de continente inválido.")
            return

        continente_buscar = continentes[continente_codigo]

        print("\n    Resultados    ")
        encontrado = False
        for pais in parametro_catalogo:
            if pais["continente"].lower() == continente_buscar:
                print(f"{pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} | Continente: {pais['continente']}")
                encontrado = True

        if not encontrado:
            print("No se encontraron países en ese continente.")

    elif opcion == "2":
        minimo = int(input("Ingrese población mínima: "))
        maximo = int(input("Ingrese población máxima: "))

        print("\n    Resultados    ")
        encontrado = False
        for pais in parametro_catalogo:
            if minimo <= pais["poblacion"] <= maximo:
                print(f"{pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} | Continente: {pais['continente']}")
                encontrado = True

        if not encontrado:
            print("No se encontraron países dentro de ese rango de población.")

    elif opcion == "3":
        minimo = int(input("Ingrese superficie mínima: "))
        maximo = int(input("Ingrese superficie máxima: "))

        print("\n    Resultados    ")
        encontrado = False
        for pais in parametro_catalogo:
            if minimo <= pais["superficie"] <= maximo:
                print(f"{pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} | Continente: {pais['continente']}")
                encontrado = True

        if not encontrado:
            print("No se encontraron países en ese rango de superficie.")

    else:
        print("Opción inválida.")

# funcion 5 ORDENAR PAIS
def ordenar_pais(parametro_catalogo: list[dict[str,int]]):
    print("\nOrdenar países:")
    print("1 - Ordenar por nombre (A-Z)")
    print("2 - Ordenar por población (ascendente)")
    print("3 - Ordenar por superficie (ascendente o descendente)")

    opcion = input("Seleccione una opción: ")

    catalogo_ordenado = parametro_catalogo.copy()

    def burbuja(lista, clave, descendente=False):
        n = len(lista)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                a = lista[j][clave]
                b = lista[j + 1][clave]

                if not descendente and a > b:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]

                elif descendente and a < b:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]

    if opcion == "1":
        burbuja(catalogo_ordenado, "nombre")

    elif opcion == "2":
        burbuja(catalogo_ordenado, "poblacion")

    elif opcion == "3":
        modo = input("Ingrese 'A' para ascendente o 'D' para descendente: ").upper()
        if modo == "A":
            burbuja(catalogo_ordenado, "superficie", descendente=False)
        elif modo == "D":
            burbuja(catalogo_ordenado, "superficie", descendente=True)
        else:
            print("Modo inválido.")
            return

    else:
        print("Opción inválida.")
        return

    print("\n    Países ordenados:")
    for pais in catalogo_ordenado:
        print(f"{pais['nombre']} | Pob: {pais['poblacion']} | Sup: {pais['superficie']} | Cont: {pais['continente']}")

# funcion 6 MOSTRAR ESTADISTICAS
def obtener_poblacion(pais: dict):
    return pais["poblacion"]

def obtener_superficie(pais: dict):
    return pais["superficie"]

def mostrar_estadisticas(parametro_catalogo: list[dict[str,int]]):
    if len(parametro_catalogo) == 0:
        print("No hay datos cargados.")
        return

    print("\n    ESTADÍSTICAS ")

    pais_mayor_pob = max(parametro_catalogo, key=obtener_poblacion)
    pais_menor_pob = min(parametro_catalogo, key=obtener_poblacion)

    print(f"\nPaís con mayor población: {pais_mayor_pob['nombre']} ({pais_mayor_pob['poblacion']})")
    print(f"País con menor población: {pais_menor_pob['nombre']} ({pais_menor_pob['poblacion']})")

    total_poblacion = 0
    total_superficie = 0

    for pais in parametro_catalogo:
        total_poblacion += pais["poblacion"]
        total_superficie += pais["superficie"]

    promedio_poblacion = total_poblacion / len(parametro_catalogo)
    promedio_superficie = total_superficie / len(parametro_catalogo)

    print(f"\nPromedio de población: {promedio_poblacion:.2f}")
    print(f"Promedio de superficie: {promedio_superficie:.2f}")

    print("\nCantidad de países por continente:")

    continentes = {
        "AMERICA": 0,
        "EUROPA": 0,
        "ASIA": 0,
        "OCEANIA": 0,
        "AFRICA": 0
    }

    for pais in parametro_catalogo:
        cont = pais["continente"].upper()
        if cont in continentes:
            continentes[cont] += 1

    for cont, cantidad in continentes.items():
        print(f"  - {cont.capitalize()}: {cantidad}")


#INICIO DEL PROGRAMA

# VALIDAR SI EL ARCHIVO EXISTE, SINO CREARLO VACIO
import os
import csv

nombre_archivo = "paises.csv"

if not os.path.exists(nombre_archivo):
    
    with open(nombre_archivo, mode="w", newline='') as archivo:
        archivowriter = csv.writer(archivo)
        archivowriter.writerow(["nombre","poblacion","superficie","continente"])

    print(f"Archivo '{nombre_archivo}' creado correctamente.")
else:
    print(f"El archivo '{nombre_archivo}' ya existe.")


catalogo: list[dict[str,int]]= []

with open("paises.csv", newline="") as archivo:
    paisreader = csv.reader(archivo)
    next(paisreader)

    for nombre, poblacion, superficie, continente in paisreader:
        catalogo.append({
            "nombre": nombre,
            "poblacion": int(poblacion),
            "superficie": int(superficie),
            "continente": continente
        })

#menu
while True:
    print("\n MENÚ PRINCIPAL:")
    print("1. Agregar pais")
    print("2. Actualizar datos de un país")
    print("3. Buscar país por nombre")
    print("4. Filtrar países")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
    print("7. Salir")

    opcion = input("\nINGRESE OPCIÓN: ")

    match opcion:
        case "1":
            agregar_pais(catalogo)
        case "2":
            actualizar_datos(catalogo)
        case "3":
            buscar_pais(catalogo)
        case "4":
            filtrar_pais(catalogo)
        case "5":
            ordenar_pais(catalogo)
        case "6":
            mostrar_estadisticas(catalogo)
        case "7":
            print("\nSaliendo...")
            break
        case _:
            print("Opción inválida")
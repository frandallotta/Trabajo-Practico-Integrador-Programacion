
# Lista principal de países (cada país es un diccionario)
catalogo = []

# Cargar catálogo inicial (lista vacía en este caso)
def cargar_catalogo():
    # No se carga desde CSV, se inicia vacío.
    print("Catálogo de países inicializado vacío.")
    return []


# Agregar país al catálogo
def agregar_pais(catalogo):
    print("\n    Agregar país    ")
    nombre = input("Nombre: ").strip()
    poblacion = input("Población: ").strip()
    superficie = input("Superficie (km²): ").strip()
    continente = input("Continente: ").strip()

    if nombre == "" or poblacion == "" or superficie == "" or continente == "":
        print("Error: no se permiten campos vacíos.")
        return

    if not poblacion.isdigit() or not superficie.isdigit():
        print("Error: población y superficie deben ser números enteros.")
        return

    pais = {
        "nombre": nombre,
        "poblacion": int(poblacion),
        "superficie": int(superficie),
        "continente": continente
    }

    catalogo.append(pais)
    print(f"País '{nombre}' agregado correctamente.")


# Actualizar país existente
def actualizar_pais(catalogo):
    print("\n    Actualizar país    ")
    nombre = input("Ingrese el nombre del país a actualizar: ").strip()
    for pais in catalogo:
        if pais["nombre"].lower() == nombre.lower():
            nueva_poblacion = input("Nueva población: ").strip()
            nueva_superficie = input("Nueva superficie (km²): ").strip()

            if not nueva_poblacion.isdigit() or not nueva_superficie.isdigit():
                print("Error: los valores deben ser numéricos.")
                return

            pais["poblacion"] = int(nueva_poblacion)
            pais["superficie"] = int(nueva_superficie)
            print(f"País '{pais['nombre']}' actualizado correctamente.")
            return
    print("País no encontrado.")


# Buscar país por nombre (coincidencia parcial)
def buscar_pais(catalogo):
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


# Filtrar países
def filtrar_paises(catalogo):
    print("\n    Filtrar países    ")
    print("1. Por continente")
    print("2. Por rango de población")
    print("3. Por rango de superficie")
    opcion = input("Seleccione opción: ")

    filtrados = []

    if opcion == "1":
        cont = input("Ingrese continente: ").strip().lower()
        for p in catalogo:
            if p["continente"].lower() == cont:
                filtrados.append(p)

    elif opcion == "2":
        min_p = input("Población mínima: ").strip()
        max_p = input("Población máxima: ").strip()
        if min_p.isdigit() and max_p.isdigit():
            min_p = int(min_p)
            max_p = int(max_p)
            for p in catalogo:
                if min_p <= p["poblacion"] <= max_p:
                    filtrados.append(p)
        else:
            print("Error: deben ser valores numéricos.")
            return

    elif opcion == "3":
        min_s = input("Superficie mínima: ").strip()
        max_s = input("Superficie máxima: ").strip()
        if min_s.isdigit() and max_s.isdigit():
            min_s = int(min_s)
            max_s = int(max_s)
            for p in catalogo:
                if min_s <= p["superficie"] <= max_s:
                    filtrados.append(p)
        else:
            print("Error: deben ser valores numéricos.")
            return
    else:
        print("Opción inválida.")
        return

    if len(filtrados) == 0:
        print("No se encontraron países con ese criterio.")
    else:
        print("\nPaíses filtrados:")
        for p in filtrados:
            print(f"- {p['nombre']} | Población: {p['poblacion']} | Superficie: {p['superficie']} | Continente: {p['continente']}")


# Ordenar países
def ordenar_paises(catalogo):
    print("\n    Ordenar países    ")
    print("1. Por nombre")
    print("2. Por población")
    print("3. Por superficie")
    opcion = input("Seleccione opción: ")
    sentido = input("Orden ascendente (a) o descendente (d): ").strip().lower()

    ascendente = True
    if sentido == "d":
        ascendente = False

    if opcion == "1":
        catalogo.sort(key=lambda x: x["nombre"], reverse=not ascendente)
    elif opcion == "2":
        catalogo.sort(key=lambda x: x["poblacion"], reverse=not ascendente)
    elif opcion == "3":
        catalogo.sort(key=lambda x: x["superficie"], reverse=not ascendente)
    else:
        print("Opción inválida.")
        return

    print("Países ordenados correctamente!")


# Mostrar estadísticas
def mostrar_estadisticas(catalogo):
    print("\n--- Estadísticas ---")
    if len(catalogo) == 0:
        print("No hay países cargados!")
        return

    mayor_pob = catalogo[0]
    menor_pob = catalogo[0]
    total_pob = 0
    total_sup = 0
    continentes = {}

    for p in catalogo:
        total_pob += p["poblacion"]
        total_sup += p["superficie"]
        if p["poblacion"] > mayor_pob["poblacion"]:
            mayor_pob = p
        if p["poblacion"] < menor_pob["poblacion"]:
            menor_pob = p
        cont = p["continente"]
        if cont in continentes:
            continentes[cont] += 1
        else:
            continentes[cont] = 1

    prom_pob = total_pob / len(catalogo)
    prom_sup = total_sup / len(catalogo)

    print(f"País con mayor población: {mayor_pob['nombre']} ({mayor_pob['poblacion']})")
    print(f"País con menor población: {menor_pob['nombre']} ({menor_pob['poblacion']})")
    print(f"Población promedio: {prom_pob:.2f}")
    print(f"Superficie promedio: {prom_sup:.2f}")
    print("Cantidad de países por continente:")
    for cont, cant in continentes.items():
        print(f" - {cont}: {cant}")


# Mostrar todos los países cargados
def mostrar_todos(catalogo):
    print("\n    Países cargados    ")
    if len(catalogo) == 0:
        print("No hay países cargados.")
    else:
        for p in catalogo:
            print(f"- {p['nombre']} | Población: {p['poblacion']} | Superficie: {p['superficie']} | Continente: {p['continente']}")


# Programa principal
def menu_principal():
    catalogo = cargar_catalogo()

    while True:
        print("\n MENÚ PRINCIPAL:")
        print("1. Agregar país")
        print("2. Actualizar país")
        print("3. Buscar país")
        print("4. Filtrar países")
        print("5. Ordenar países")
        print("6. Mostrar estadísticas")
        print("7. Mostrar todos los países")
        print("8. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_pais(catalogo)
        elif opcion == "2":
            actualizar_pais(catalogo)
        elif opcion == "3":
            buscar_pais(catalogo)
        elif opcion == "4":
            filtrar_paises(catalogo)
        elif opcion == "5":
            ordenar_paises(catalogo)
        elif opcion == "6":
            mostrar_estadisticas(catalogo)
        elif opcion == "7":
            mostrar_todos(catalogo)
        elif opcion == "8":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Ejecución
menu_principal()

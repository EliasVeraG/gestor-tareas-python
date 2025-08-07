# ==============================================
#  Programa: Gestor de Tareas (To-Do List)
#  Descripción: Permite al usuario gestionar una lista de tareas
#               mediante un menú interactivo en consola.
#  Autor: Elias Alcides Vera Gauto
#  Fecha: 06 de Agosto del 2025
# ==============================================

print("==============================================")
print("         📋 GESTOR DE TAREAS - TO-DO LIST      ")
print("==============================================")

# Lista donde se almacenarán las tareas
# Cada tarea será una lista de dos elementos: [nombre, estado]
# Ejemplo: ["Estudiar Python", False]

tareas = []

# Bucle principal
while True:
    print("\nSeleccione una opción:\n")
    print("1 = Agregar una nueva tarea")
    print("2 = Mostrar todas las tareas")
    print("3 = Marcar una tarea como completada")
    print("4 = Eliminar una tarea")
    print("5 = Salir del programa")

    opcion = input("Ingrese qué quiere hacer: ")

    if not opcion.isdigit():
        print("⚠️ Entrada inválida. Por favor, ingrese un número.")
        continue
    opcion = int(opcion)

    if opcion < 1 or opcion > 5:
        print("⚠️ Opción fuera de rango. Intente de nuevo.")
        continue

    # ==========================
    # Opción 1: Agregar tarea
    # ==========================
    if opcion == 1:
        print("📝 Opción: Agregar tarea")
        nueva_tarea = input("Ingrese el nombre de la nueva tarea: ").strip()

        if nueva_tarea == "":
            print("⚠️ No se puede agregar una tarea vacía.")
        else:
            tareas.append([nueva_tarea, False])
            print("✅ Tarea agregada correctamente.")

    # ==========================
    # Opción 2: Mostrar tareas
    # ==========================
    elif opcion == 2:
        print("📋 Opción: Mostrar tareas")
        if len(tareas) == 0:
            print("⚠️ No hay tareas en la lista.")
        else:
            for i in range(len(tareas)):
                nombre = tareas[i][0]
                completada = tareas[i][1]
                estado = "✔️" if completada else "❌"
                print(f"{i + 1}. [{estado}] {nombre}")

    # ==========================
    # Opción 3: Marcar tarea como completada
    # ==========================
    elif opcion == 3:
        print("✅ Opción: Marcar tarea como completada")
        if len(tareas) == 0:
            print("⚠️ No hay tareas para marcar.")
        else:
            for i in range(len(tareas)):
                nombre = tareas[i][0]
                completada = tareas[i][1]
                estado = "✔️" if completada else "❌"
                print(f"{i + 1}. [{estado}] {nombre}")

            seleccion = input("Ingrese el número de la tarea que desea marcar como completada: ")

            if not seleccion.isdigit():
                print("⚠️ Entrada inválida.")
                continue

            seleccion = int(seleccion)

            if seleccion < 1 or seleccion > len(tareas):
                print("⚠️ Número fuera de rango.")
            else:
                if tareas[seleccion - 1][1] == True:
                    print("ℹ️ La tarea ya está marcada como completada.")
                else:
                    tareas[seleccion - 1][1] = True
                    print("✅ Tarea marcada como completada.")

    # ==========================
    # Opción 4: Eliminar tarea
    # ==========================
    elif opcion == 4:
        print("🗑️ Opción: Eliminar tarea")
        if len(tareas) == 0:
            print("⚠️ No hay tareas para eliminar.")
        else:
            for i in range(len(tareas)):
                nombre = tareas[i][0]
                completada = tareas[i][1]
                estado = "✔️" if completada else "❌"
                print(f"{i + 1}. [{estado}] {nombre}")

            seleccion = input("Ingrese el número de la tarea que desea eliminar: ")

            if not seleccion.isdigit():
                print("⚠️ Entrada inválida.")
                continue

            seleccion = int(seleccion)

            if seleccion < 1 or seleccion > len(tareas):
                print("⚠️ Número fuera de rango.")
            else:
                tarea_eliminada = tareas.pop(seleccion - 1)
                print(f"✅ Tarea eliminada: {tarea_eliminada[0]}")

    # ==========================
    # Opción 5: Salir
    # ==========================
    elif opcion == 5:
        print("\n👋 Gracias por usar el Gestor de Tareas.")
        print("Hasta luego.")
        break

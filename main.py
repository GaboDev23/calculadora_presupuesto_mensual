import manejar_archivos
import funciones
import prespuesto
import configuracion
from datetime import datetime

fecha_actual = datetime.now()

mes = fecha_actual.month
anio = fecha_actual.year

while True:
    datos = {}
    funciones.limpiar_consola()
    print("========== CALCULADORA DE PRESUPUESTO ==========")
    print("Introduce una opción:\n1. Crear nuevo presupuesto\n2. Ver presupuesto actual\n3. Modificar gastos\n4. Eliminar gasto\n5. Comparaciones\n6. Salir")
    opcion = input("========== ELIGE UNA OPCIÓN ==========\n")


    if not opcion.isdigit():
        print("Error, debe ser un número válido")
        continue

    opcion = int(opcion)

    if opcion == 1:
        funciones.limpiar_consola()
        print("========== CREAR UN NUEVO PRESUPUESTO ==========")

        nombre = input("Introduce tu nombre: ")

        datos = manejar_archivos.cargar_datos(nombre)

        if datos is None:
            print("No se encontró el historial, se creará uno nuevo")
            datos = {
                "nombre": nombre,
                "presupuestos": {}
                }
        else:
            print("Historial encontrado")

        ingresos = prespuesto.pedir_ingresos()

        categorias = ["Alquiler", "Comida", "Transporte"]
        gastos = []

        print("GASTOS MENSUALES")

        prespuesto.agregar_categorias_basicas(gastos)

        while True:
            mas_categorias = input(
            "¿Tienes más categorias de gastos? "
            "Introduce (si) para introducir categoría, "
            "y cualquier cosa para dejar de introducir categorías: "
        ).lower()

            if mas_categorias == "si":
                prespuesto.agregar_categoria(categorias, gastos)
            else:
                break

        manejar_archivos.crear_json(datos, f"{mes}-{anio}", ingresos, categorias, gastos)
    elif opcion == 2:
        funciones.limpiar_consola()
        print(f"{configuracion.CIAN}========== VER PRESUPUESTO ACTUAL =========={configuracion.RESET}")

        nombre, datos = prespuesto.pedir_datos()

        if datos is None:
            continue

        prespuesto.mostrar_datos(datos, nombre)

        if funciones.volver_menu():
            continue
    elif opcion == 3:
        funciones.limpiar_consola()
        print(f"{configuracion.CIAN}========== MODIFICAR GASTO =========={configuracion.RESET}")

        nombre, datos = prespuesto.pedir_datos()
        
        if datos is None:
            continue
        else:
            funciones.limpiar_consola()

            prespuesto.modificar_datos(datos)
            manejar_archivos.guardar_datos(datos)

            if funciones.volver_menu():
                continue

    elif opcion == 4:
        funciones.limpiar_consola()
        print(f"{configuracion.CIAN}========== ELIMINAR GASTO =========={configuracion.RESET}")
        nombre, datos = prespuesto.pedir_datos()

        if datos is None:
            continue
        else:
            funciones.limpiar_consola()

            prespuesto.eliminar_datos(datos)
            manejar_archivos.guardar_datos(datos)

            if funciones.volver_menu():
                continue
    elif opcion == 5:
        funciones.limpiar_consola()
        print(f"{configuracion.CIAN}========== COMPARAR PRESUPUESTO =========={configuracion.RESET}")
        nombre = input("Ingresa tu nombre: ")

        datos = manejar_archivos.cargar_datos(nombre)

        if datos is None:
            print("No se encontraron datos con el nombre")
            input()
            continue

        funciones.limpiar_consola()
        print(f"{configuracion.CIAN}========== INGRESOS =========={configuracion.RESET}")

        prespuesto.comparar_presupuestos(datos)

        input()
    elif opcion == 6:
        funciones.limpiar_consola()
        break
    else:
        print("¡OPCIÓN INCORRECTA!")

        if funciones.volver_menu():
            continue
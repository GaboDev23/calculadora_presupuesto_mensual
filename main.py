import funciones
import prespuesto
import configuracion

while True:
    funciones.limpiar_consola()
    print("========== CALCULADORA DE PRESUPUESTO ==========")
    print("Introduce una opción:\n1. Crear nuevo presupuesto\n2. Ver presupuesto actual\n3. Modificar gastos\n4. Eliminar gasto\n5. Salir")
    opcion = input("========== ELIGE UNA OPCIÓN ==========\n")


    if not opcion.isdigit():
        print("Error, debe ser un número válido")
        continue

    opcion = int(opcion)

    if opcion == 1:
        funciones.limpiar_consola()
        prespuesto.crear_categorias()
        print("========== CREAR UN NUEVO PRESUPUESTO ==========")
        nombre = input("Introduce tu nombre: ")
        edad = funciones.pedir_valor_int("Introduce tu edad: ", "Error, la edad debe ser un número entero")
        prespuesto.ingresos = prespuesto.pedir_ingresos()

        print("GASTOS MENSUALES")
        prespuesto.crear_categorias()
        prespuesto.agregar_categorias_basicas()
        
        while True:
            mas_categorias = input("¿Tienes más categorias de gastos? Introduce (si) para introducir categoría, y cualquier cosa para dejar de introducir categrías: ").lower()
            if mas_categorias == "si":
                prespuesto.agregar_categoria()
                continue
            else:
                break
        print("\n")
    elif opcion == 2:
        funciones.limpiar_consola()
        if not funciones.comprobar_gastos_vacios(prespuesto.categorias_nuevas["gastos_categorias_agregadas"]):
            if funciones.volver_menu():
                continue
        else:
            prespuesto.mostrar_datos(nombre, edad)

        if funciones.volver_menu():
            continue
    elif opcion == 3:
        funciones.limpiar_consola()
        print(f"{configuracion.CIAN}========== MODIFICAR GASTO =========={configuracion.RESET}")
        if not funciones.comprobar_gastos_vacios(prespuesto.categorias_nuevas["gastos_categorias_agregadas"]):
            if funciones.volver_menu():
                continue
        else:
            funciones.limpiar_consola()

            prespuesto.modificar_datos()

            if funciones.volver_menu():
                continue

    elif opcion == 4:
        funciones.limpiar_consola()
        print(f"{configuracion.CIAN}========== ELIMINAR GASTO =========={configuracion.RESET}")
        if not funciones.comprobar_gastos_vacios(prespuesto.categorias_nuevas["gastos_categorias_agregadas"]):
            if funciones.volver_menu():
                continue
        else:
            funciones.limpiar_consola()

            prespuesto.eliminar_datos()

            if funciones.volver_menu():
                continue
    elif opcion == 5:
        funciones.limpiar_consola()
        break
    else:
        print("¡OPCIÓN INCORRECTA!")

        if funciones.volver_menu():
            continue
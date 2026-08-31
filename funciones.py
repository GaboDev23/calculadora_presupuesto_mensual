import os
import configuracion

def pedir_valor_int(texto, error):
    while True:
        try:
            valor = int(input(texto))
            if valor <= 0:
                print(f"{configuracion.ROJO}Error, el número debe ser positivo mayor que 0{configuracion.RESET}")
                continue
            break
        except ValueError:
            print(f"{configuracion.ROJO}{error}{configuracion.RESET}")

    return valor

def pedir_valor_float(texto, error):
    while True:
        try:
            valor = float(input(texto))
            if valor < 0:
                print(f"{configuracion.ROJO}Error, el número debe ser positivo{configuracion.RESET}")
                continue
            break
        except ValueError:
            print(f"{configuracion.ROJO}{error}{configuracion.RESET}")

    return valor

def calcular_porcentaje(gastos_totales, ingresos):
    try:
        return gastos_totales / ingresos * 100
    except ZeroDivisionError:
        return None

def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")

def volver_menu():
    return input("Pulsa enter para salir...").lower() == ""

def comprobar_gastos_vacios(todos_los_gastos):
    if not todos_los_gastos:
        print("NO EXISTEN GASTOS")
        return False

    return True

def elegir_gasto(todas_las_categorias, todos_los_gastos):
    if comprobar_gastos_vacios(todos_los_gastos):
        mostrar_gastos = ""

        for i in range(len(todos_los_gastos)):
            mostrar_gastos += f"\n{i}. {todas_las_categorias[i]}: ${todos_los_gastos[i]}"

        print(mostrar_gastos)

        return comprobar_opcion(range(len(todas_las_categorias)))

def comprobar_opcion(opciones):
    while True:
        opcion = input("Elige una categoría según su número: ")

        if not opcion.isdigit():
            print("Error, debe ser un número válido")
            continue

        opcion = int(opcion)

        if opcion not in opciones:
            print(f"Error, {opcion} no está entre las opciones disponibles")
            continue

        return opcion
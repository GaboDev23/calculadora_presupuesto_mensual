import funciones
import configuracion

categorias_nuevas = {
    "categorias_agregadas": [
        "Alquiler",
        "Comida",
        "Transporte"
    ],
    "gastos_categorias_agregadas": []
}

ingresos = 0

def pedir_ingresos():
    return funciones.pedir_valor_float("Introduce tus ingresos mensuales: ", "Error, los ingresos son inválidos")


def calcular_dinero_restante(ingresos, todos_los_gastos):
    gastos_totales = sum(todos_los_gastos)
    dinero_restante = ingresos - gastos_totales

    return gastos_totales, dinero_restante

def crear_categorias():
    categorias_nuevas["categorias_agregadas"].clear()
    categorias_nuevas["categorias_agregadas"].extend(["Alquiler", "Comida", "Transporte"])
    categorias_nuevas["gastos_categorias_agregadas"].clear()

def agregar_categorias_basicas():
    alquiler = funciones.pedir_valor_float("¿Cuánto gastas en alquiler? ", "Error, los gastos de alquiler son inválidos")
    comida = funciones.pedir_valor_float("¿Cuánto gastas en comida? ", "Error, los gastos de comida son inválidos")
    transporte = funciones.pedir_valor_float("¿Cuánto gastas en transporte? ", "Error, los gastos de transporte son inválidos")

    categorias_nuevas["gastos_categorias_agregadas"].extend([alquiler, comida, transporte])

def agregar_categoria():
    nombre_categoria = input("Nombre de la categría: ").capitalize()

    if nombre_categoria not in categorias_nuevas["categorias_agregadas"]:
        categorias_nuevas["categorias_agregadas"].append(nombre_categoria)
        categoria = funciones.pedir_valor_float(f"¿Cuánto gastas en {nombre_categoria}? ", f"Error, los gastos de {nombre_categoria} son inválidos")
        categorias_nuevas["gastos_categorias_agregadas"].append(categoria)
    else:
        indice = categorias_nuevas["categorias_agregadas"].index(nombre_categoria)
        categorias_nuevas["gastos_categorias_agregadas"][indice] += funciones.pedir_valor_float(f"¿Cuánto gastas en {nombre_categoria}? ", f"Error, los gastos de {nombre_categoria} son inválidos")

def mostrar_datos(nombre, edad):
    print(f"{configuracion.CIAN}========== VER PRESUPUESTO ACTUAL =========={configuracion.RESET}")
    gastos_totales, dinero_restante = calcular_dinero_restante(ingresos, categorias_nuevas["gastos_categorias_agregadas"])
    print(f"NOMBRE: {nombre}")
    print(f"EDAD: {edad}")
    for i in range(len(categorias_nuevas["categorias_agregadas"])):
        print(f"{categorias_nuevas['categorias_agregadas'][i]}: ${categorias_nuevas['gastos_categorias_agregadas'][i]:.2f}")
    print(f"{configuracion.CIAN}========== RESUMEN =========={configuracion.RESET}")
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad} años")
    print("\n")
    print(f"Ingresos: ${ingresos:.2f}")
    print(f"Gastos totales: ${gastos_totales:.2f}")
    print(f"Dinero restante: ${dinero_restante:.2f}")
    porcentaje_gastado = funciones.calcular_porcentaje(gastos_totales, ingresos)
    if porcentaje_gastado is None:
        print(f"Porcentaje gastado: {porcentaje_gastado}")
    else:
        print(f"Porcentaje gastado: {porcentaje_gastado:.2f}%")
        print("\n")
        print(f"¡Te quedan ${dinero_restante:.2f} este mes!")
        print("\n")
    print("========== RESUMEN DE GASTOS ==========")
    if dinero_restante > 0:
        print(f"{configuracion.VERDE}Te ha sobrado: ${dinero_restante:.2f}{configuracion.RESET}")
    elif dinero_restante == 0:
        print(f"{configuracion.AMARILLO}Te has quedado en 0{configuracion.RESET}")
    else:
        print(f"{configuracion.ROJO}¡Cuidado has gastado más que tus ingreos!{configuracion.RESET}")
    print("\n")
    print("========== ANALISIS ==========")
    if porcentaje_gastado is None:
        print("No fue posible calcular el porcentaje de tus gastos")
    elif porcentaje_gastado == 0:
        print(f"{configuracion.VERDE}No has gastado nada{configuracion.RESET}")
    elif porcentaje_gastado < 50:
        print(f"{configuracion.VERDE}Has gastado menos de la mitad de tus ingresos{configuracion.RESET}")
    elif porcentaje_gastado == 50:
        print("Has gastado exactamente la mitad de tus ingresos")
    elif porcentaje_gastado < 100:
        print(f"{configuracion.AMARILLO}¡Cuidado, has utilizando una gran parte de tus ingresos!{configuracion.RESET}")
    elif porcentaje_gastado == 100:
        print(f"{configuracion.AMARILLO}¡Cuidado, has utilizado todos tus ingresos!{configuracion.RESET}")
    else:
        print(f"{configuracion.ROJO}¡CUIDADO, HAS EXCEDIDO LOS GASTOS DE TUS INGRESOS!{configuracion.RESET}")
    print("\n")
    print("========== ANALISIS DE CADA GASTO ==========")
    for i in range(len(categorias_nuevas["categorias_agregadas"])):
        porcentaje_categoria = funciones.calcular_porcentaje(categorias_nuevas["gastos_categorias_agregadas"][i], ingresos)

        print(f"{categorias_nuevas['categorias_agregadas'][i]} gastó {porcentaje_categoria:.2f}%")

def modificar_datos():
    opcion_categoria = funciones.elegir_gasto(categorias_nuevas["categorias_agregadas"], categorias_nuevas["gastos_categorias_agregadas"])
    
    categorias_nuevas["gastos_categorias_agregadas"][opcion_categoria] = funciones.pedir_valor_float(f"¿Cuánto gastas en {categorias_nuevas['categorias_agregadas'][opcion_categoria]}? ","Error, los gastos son inválidos")
    print("Gasto modificado correctamente")

def eliminar_datos():
    opcion_categoria = funciones.elegir_gasto(categorias_nuevas["categorias_agregadas"], categorias_nuevas["gastos_categorias_agregadas"])
    
    categorias_nuevas["categorias_agregadas"].pop(opcion_categoria)
    categorias_nuevas["gastos_categorias_agregadas"].pop(opcion_categoria)
    
    print("Gasto eliminado correctamente")
    
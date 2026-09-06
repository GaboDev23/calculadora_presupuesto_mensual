import funciones
import configuracion
import manejar_archivos

ingresos = 0

def pedir_datos():
    nombre = input("Introduce tu nombre: ")
    
    datos = manejar_archivos.cargar_datos(nombre)
    
    if datos is None:
        print("No se encontraron datos con el nombre")
        input()
        return nombre, None

    return nombre, datos

def pedir_ingresos():
    return funciones.pedir_valor_float("Introduce tus ingresos mensuales: ", "Error, los ingresos son inválidos")


def calcular_dinero_restante(ingresos, todos_los_gastos):
    gastos_totales = sum(todos_los_gastos)
    dinero_restante = ingresos - gastos_totales

    return gastos_totales, dinero_restante

def agregar_categoria(categorias, gastos):
    nombre_categoria = input("Nombre de la categoría: ").capitalize()

    if nombre_categoria not in categorias:
        categorias.append(nombre_categoria)

        gasto = funciones.pedir_valor_float(
            f"¿Cuánto gastas en {nombre_categoria}? ",
            f"Error, los gastos de {nombre_categoria} son inválidos"
        )

        gastos.append(gasto)

    else:
        indice = categorias.index(nombre_categoria)

        gastos[indice] += funciones.pedir_valor_float(
            f"¿Cuánto gastas en {nombre_categoria}? ",
            f"Error, los gastos de {nombre_categoria} son inválidos"
        )

def agregar_categorias_basicas(gastos):
    alquiler = funciones.pedir_valor_float(
        "¿Cuánto gastas en alquiler? ",
        "Error, los gastos de alquiler son inválidos"
    )

    comida = funciones.pedir_valor_float(
        "¿Cuánto gastas en comida? ",
        "Error, los gastos de comida son inválidos"
    )

    transporte = funciones.pedir_valor_float(
        "¿Cuánto gastas en transporte? ",
        "Error, los gastos de transporte son inválidos"
    )

    gastos.extend([alquiler, comida, transporte])

def mostrar_datos(datos, nombre):
    mes_actual = list(datos["presupuestos"].keys())[-1]
    presupuesto_actual = datos["presupuestos"][mes_actual]

    ingresos_actuales = presupuesto_actual["ingresos"]
    categorias = presupuesto_actual["categorias"]
    gastos = presupuesto_actual["gastos"]

    gastos_totales, dinero_restante = calcular_dinero_restante(
        ingresos_actuales,
        gastos
    )

    print(f"{configuracion.CIAN}========== VER PRESUPUESTO ACTUAL =========={configuracion.RESET}")
    print(f"NOMBRE: {nombre}")
    print(f"MES: {mes_actual}")
    print()

    for i in range(len(categorias)):
        print(f"{categorias[i]}: ${gastos[i]:.2f}")

    print(f"{configuracion.CIAN}========== RESUMEN =========={configuracion.RESET}")
    print()
    print(f"Ingresos: ${ingresos_actuales:.2f}")
    print(f"Gastos totales: ${gastos_totales:.2f}")
    print(f"Dinero restante: ${dinero_restante:.2f}")

    porcentaje_gastado = funciones.calcular_porcentaje(gastos_totales,ingresos_actuales)

    if porcentaje_gastado is None:
        print("Porcentaje gastado: No disponible")
    else:
        print(f"Porcentaje gastado: {porcentaje_gastado:.2f}%")
        print()
        print(f"¡Te quedan ${dinero_restante:.2f} este mes!")
        print()

    print("========== RESUMEN DE GASTOS ==========")

    if dinero_restante > 0:
        print(
            f"{configuracion.VERDE}"
            f"Te ha sobrado: ${dinero_restante:.2f}"
            f"{configuracion.RESET}"
        )

    elif dinero_restante == 0:
        print(
            f"{configuracion.AMARILLO}"
            f"Te has quedado en 0"
            f"{configuracion.RESET}"
        )

    else:
        print(
            f"{configuracion.ROJO}"
            f"¡Cuidado, has gastado más que tus ingresos!"
            f"{configuracion.RESET}"
        )

    print()
    print("========== ANALISIS ==========")

    if porcentaje_gastado is None:
        print("No fue posible calcular el porcentaje de tus gastos")

    elif porcentaje_gastado == 0:
        print(
            f"{configuracion.VERDE}"
            f"No has gastado nada"
            f"{configuracion.RESET}"
        )

    elif porcentaje_gastado < 50:
        print(
            f"{configuracion.VERDE}"
            f"Has gastado menos de la mitad de tus ingresos"
            f"{configuracion.RESET}"
        )

    elif porcentaje_gastado == 50:
        print("Has gastado exactamente la mitad de tus ingresos")

    elif porcentaje_gastado < 100:
        print(
            f"{configuracion.AMARILLO}"
            f"¡Cuidado, has utilizado una gran parte de tus ingresos!"
            f"{configuracion.RESET}"
        )

    elif porcentaje_gastado == 100:
        print(
            f"{configuracion.AMARILLO}"
            f"¡Cuidado, has utilizado todos tus ingresos!"
            f"{configuracion.RESET}"
        )

    else:
        print(
            f"{configuracion.ROJO}"
            f"¡CUIDADO, HAS EXCEDIDO LOS GASTOS DE TUS INGRESOS!"
            f"{configuracion.RESET}"
        )

    print()
    print("========== ANALISIS DE CADA GASTO ==========")

    for i in range(len(categorias)):
        porcentaje_categoria = funciones.calcular_porcentaje(gastos[i], ingresos_actuales)

        if porcentaje_categoria is None:
            print(f"{categorias[i]}: porcentaje no disponible")
        else:
            print(
                f"{categorias[i]} gastó "
                f"{porcentaje_categoria:.2f}%"
            )

def modificar_datos(datos):
    mes_actual = list(datos["presupuestos"].keys())[-1]
    presupuesto_actual = datos["presupuestos"][mes_actual]

    categorias = presupuesto_actual["categorias"]
    gastos = presupuesto_actual["gastos"]

    opcion_categoria = funciones.elegir_gasto(categorias, gastos)
    
    gastos[opcion_categoria] = funciones.pedir_valor_float(f"¿Cuánto gastas en {categorias[opcion_categoria]}? ", "Error, los gastos son inválidos")

    print("Gasto modificado correctamente")

def eliminar_datos(datos):
    mes_actual = list(datos["presupuestos"].keys())[-1]
    presupuesto_actual = datos["presupuestos"][mes_actual]

    categorias = presupuesto_actual["categorias"]
    gastos = presupuesto_actual["gastos"]

    opcion_categoria = funciones.elegir_gasto(categorias, gastos)
    
    categorias.pop(opcion_categoria)
    gastos.pop(opcion_categoria)
    
    print("Gasto eliminado correctamente")

def comparar_diferencia(actual, anterior):
    diferencia = actual - anterior

    if diferencia > 0:
        return f"+${diferencia:.2f}"
    elif diferencia < 0:
        return f"-${abs(diferencia):.2f}"
    else:
        return "$0.00"

def comparar_presupuestos(datos):
    if len(datos["presupuestos"]) < 2:
        print(f"{configuracion.ROJO}No hay suficientes meses para realizar la comparación{configuracion.RESET}")
        input()
        return
    
    mes_actual = list(datos["presupuestos"].keys())[-1]
    datos_mes_actual = datos["presupuestos"][mes_actual]

    mes_anterior = list(datos["presupuestos"].keys())[-2]
    datos_mes_anterior = datos["presupuestos"][mes_anterior]

    ingreso_actual = f"${datos_mes_actual['ingresos']:.2f}"
    ingreso_anterior = f"${datos_mes_anterior['ingresos']:.2f}"

    print(f"{'Mes actual:':<15} {ingreso_actual:>15}")
    print(f"{'Mes anterior:':<15} {ingreso_anterior:>15}")
    diferencia_ingresos = comparar_diferencia(datos_mes_actual["ingresos"], datos_mes_anterior["ingresos"])
    print(f"{'Diferencia:':<15} {diferencia_ingresos:>15}")

    print("="*80)
    print(f"{'CATEGORIA':<20} {mes_actual:>15} {mes_anterior:>15} {'DIFERENCIA':>15}")
    print("="*80)
    for i in range(len(datos_mes_actual["categorias"])):
        categoria_actual = datos_mes_actual["categorias"][i]

        if categoria_actual not in datos_mes_anterior["categorias"]:
            continue

        indice_anterior = datos_mes_anterior["categorias"].index(categoria_actual)

        gasto_actual = datos_mes_actual["gastos"][i]
        gasto_anterior = datos_mes_anterior["gastos"][indice_anterior]

        diferencia_gasto = comparar_diferencia(gasto_actual, gasto_anterior)

        gasto_actual_texto = f"${gasto_actual:.2f}"
        gasto_anterior_texto = f"${gasto_anterior:.2f}"
        print(
        f"{categoria_actual:<20} "
        f"{gasto_actual_texto:>15} "
        f"{gasto_anterior_texto:>15} "
        f"{diferencia_gasto:>15}"
        )

    print("-"*80)
    total_mes_actual, restante_mes_actual = calcular_dinero_restante(datos_mes_actual["ingresos"], datos_mes_actual["gastos"])
    total_mes_anterior, restante_mes_anterior = calcular_dinero_restante(datos_mes_anterior["ingresos"], datos_mes_anterior["gastos"])
    diferencia_total = comparar_diferencia(total_mes_actual, total_mes_anterior)
    print(f"{'TOTAL':<20} {f'${total_mes_actual}':>15} {f'${total_mes_anterior}':>15} {diferencia_total:>15}")

    print("="*80)
    diferencia_restantes = comparar_diferencia(restante_mes_actual, restante_mes_anterior)
    print(f"{'Restante mes actual:':<25} {f'${restante_mes_actual}':>15}")
    print(f"{'Restante mes anterior:':<25} {f'${restante_mes_anterior}':>15}")
    print(f"{'Diferencia de restantes:':<25} {diferencia_restantes:>15}")
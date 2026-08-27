RESET = "\033[0m"
ROJO = "\033[31m"
VERDE = "\033[32m"
AMARILLO = "\033[33m"
AZUL = "\033[34m"
CIAN = "\033[36m"

def pedir_valor_int(texto, error):
    while True:
        try:
            valor = int(input(texto))
            if valor <= 0:
                print(f"{ROJO}Error, el número debe ser positivo mayor que 0{RESET}")
                continue
            break
        except ValueError:
            print(f"{ROJO}{error}{RESET}")

    return valor

def pedir_valor_float(texto, error):
    while True:
        try:
            valor = float(input(texto))
            if valor < 0:
                print(f"{ROJO}Error, el número debe ser positivo{RESET}")
                continue
            break
        except ValueError:
            print(f"{ROJO}{error}{RESET}")

    return valor

nombre = input("Introduce tu nombre: ")
edad = pedir_valor_int("Introduce tu edad: ", "Error, la edad debe ser un número entero")
ingresos = pedir_valor_float("Introduce tus ingresos mensuales: ", "Error, los ingresos son inválidos")

print("GASTOS MENSUALES")
alquiler = pedir_valor_float("¿Cuánto gastas en alquiler? ", "Error, los gastos de alquiler son inválidos")
comida = pedir_valor_float("¿Cuánto gastas en comida? ", "Error, los gastos de comida son inválidos")
transporte = pedir_valor_float("¿Cuánto gastas en transporte? ", "Error, los gastos de transporte son inválidos")
categorias_nuevas = {
    "categorias_agregadas": [],
    "gastos_categorias_agregadas": []
}

while True:
    mas_categorias = input("¿Tienes más categorias de gastos? Introduce (si) para introducir categoría, y cualquier cosa para dejar de introducir categrías: ").lower()

    if mas_categorias == "si":
        nombre_categoria = input("Nombre de la categría: ")
        categorias_nuevas["categorias_agregadas"].append(nombre_categoria)
        categoria = pedir_valor_float(f"¿Cuánto gastas en {nombre_categoria}? ", f"Error, los gastos de {nombre_categoria} son inválidos")
        categorias_nuevas["gastos_categorias_agregadas"].append(categoria)
    else:
        break

gastos_totales = alquiler + comida + transporte

for i in categorias_nuevas["gastos_categorias_agregadas"]:
    gastos_totales += i

dinero_restante = ingresos - gastos_totales

try:
    porcentaje_gastado = gastos_totales / ingresos * 100
except ZeroDivisionError:
    porcentaje_gastado = None

print(f"{CIAN}========== GASTOS =========={RESET}")
print(f"Alquiler: ${alquiler:.2f}")
print(f"Comida: ${comida:.2f}")
print(f"Transporte: ${transporte:.2f}")
for i in range(len(categorias_nuevas["categorias_agregadas"])):
    print(f"{categorias_nuevas['categorias_agregadas'][i]}: ${categorias_nuevas['gastos_categorias_agregadas'][i]:.2f}")
print(f"{CIAN}========== RESUMEN =========={RESET}")
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print("\n")
print(f"Ingresos: ${ingresos:.2f}")
print(f"Gastos totales: ${gastos_totales:.2f}")
print(f"Dinero restante: ${dinero_restante:.2f}")
if porcentaje_gastado is None:
    print(f"Porcentaje gastado: {porcentaje_gastado}")
else:
    print(f"Porcentaje gastado: {porcentaje_gastado:.2f}%")
print("\n")
print(f"¡Te quedan ${dinero_restante:.2f} este mes!")
print("\n")
print("========== RESUMEN DE GASTOS ==========")
if dinero_restante > 0:
    print(f"{VERDE}Te ha sobrado: ${dinero_restante:.2f}{RESET}")
elif dinero_restante == 0:
    print(f"{AMARILLO}Te has quedado en 0{RESET}")
else:
    print(f"{ROJO}¡Cuidado has gastado más que tus ingreos!{RESET}")
print("\n")
print("========== ANALISIS ==========")
if porcentaje_gastado is None:
    print("No fue posible calcular el porcentaje de tus gastos")
elif porcentaje_gastado == 0:
    print(f"{VERDE}No has gastado nada{RESET}")
elif porcentaje_gastado < 50:
    print(f"{VERDE}Has gastado menos de la mitad de tus ingresos{RESET}")
elif porcentaje_gastado == 50:
    print("Has gastado exactamente la mitad de tus ingresos")
elif porcentaje_gastado < 100:
    print(f"{AMARILLO}¡Cuidado, has utilizando una gran parte de tus ingresos!{RESET}")
elif porcentaje_gastado == 100:
    print(f"{AMARILLO}¡Cuidado, has utilizado todos tus ingresos!{RESET}")
else:
    print(f"{ROJO}¡CUIDADO, HAS EXCEDIDO LOS GASTOS DE TUS INGRESOS!{RESET}")
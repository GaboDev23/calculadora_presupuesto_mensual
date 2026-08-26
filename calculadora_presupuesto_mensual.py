nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
ingresos = float(input("Introduce tus ingresos mensuales: "))

print("GASTOS MENSUALES")
alquiler = float(input("¿Cuánto gastas en alquiler? "))
comida = float(input("¿Cuánto gastas en comida? "))
transorte = float(input("¿Cuánto gastas en transporte? "))
otros = float(input("¿Cuánto gastas en otros gastos? "))

gastos_totales = alquiler + comida + transorte + otros
dinero_restante = ingresos - gastos_totales
porcentaje_gastado = round(gastos_totales / ingresos * 100)

print("========== RESUMEN ==========")
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print("\n")
print(f"Ingresos: ${ingresos:.2f}")
print(f"Gastos totales: ${gastos_totales:.2f}")
print(f"Dinero restante: ${dinero_restante:.2f}")
print(f"Porcentaje gastado: {porcentaje_gastado}%")
print("\n")
print(f"¡Te quedan ${dinero_restante:.2f} este mes!")
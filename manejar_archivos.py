import json
import os

def crear_json(datos, mes, ingresos, categorias, gastos):
    datos["presupuestos"][mes] = {
        "ingresos": ingresos,
        "categorias": categorias,
        "gastos": gastos
    }

    guardar_datos(datos)

def cargar_datos(nombre):
    directorio = os.path.dirname(__file__)

    nombre_archivo = f"presupuesto_{nombre.lower()}.json"

    ruta = os.path.join(directorio, f"datos/{nombre_archivo}")

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        return datos
    except FileNotFoundError:
        return None

def guardar_datos(datos):
    nombre_archivo = f"presupuesto_{datos['nombre'].lower()}.json"

    directorio = os.path.dirname(__file__)
    ruta = os.path.join(directorio, "datos", nombre_archivo)

    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)
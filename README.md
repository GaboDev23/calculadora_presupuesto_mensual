# 💰 Calculadora de Presupuesto Personal

Una aplicación de consola desarrollada en **Python** para gestionar presupuestos mensuales, registrar gastos por categorías, almacenar un historial financiero y comparar la evolución de ingresos y gastos entre diferentes meses.

El proyecto comenzó como una calculadora sencilla de ingresos y gastos y ha evolucionado progresivamente incorporando conceptos como **datos primitivos, operaciones matemáticas, F-Strings, funciones, estructuras de control, listas, diccionarios, manejo de errores, modularización, archivos JSON, persistencia de datos y comparación de información histórica**.

Actualmente, cada usuario puede disponer de su propio historial de presupuestos, almacenado permanentemente en archivos JSON.

---

# 🚀 Versión actual

**Versión 4**

La Versión 4 introduce un cambio importante en el funcionamiento del programa: los presupuestos ya no existen únicamente durante la ejecución.

Ahora la información se almacena en archivos `.json`, permitiendo conservar los datos después de cerrar el programa y mantener un historial organizado por meses.

Cada usuario posee su propio archivo:

```text
presupuesto_gabriel.json
presupuesto_maite.json
presupuesto_tomas.json
```

Dentro de cada archivo pueden almacenarse múltiples presupuestos mensuales.

---

# ✨ Características principales

* 💰 Registro de ingresos mensuales.
* 📂 Categorías básicas de gastos.
* ➕ Categorías personalizadas.
* ✏️ Modificación de gastos.
* 🗑️ Eliminación de gastos.
* 📊 Cálculo de gastos totales.
* 💵 Cálculo de dinero restante.
* 📈 Cálculo del porcentaje gastado.
* 🔍 Análisis individual de cada categoría.
* 🎨 Colores en consola.
* 🛡️ Validación de datos.
* 📁 Persistencia mediante archivos JSON.
* 👤 Historial independiente para cada usuario.
* 📅 Detección automática del mes y año.
* 🗃️ Historial de presupuestos mensuales.
* 🔄 Carga automática de presupuestos existentes.
* 💾 Guardado permanente de modificaciones.
* 📊 Comparación entre meses.
* 📉 Comparación de gastos por categoría.
* 💰 Comparación de ingresos.
* 💵 Comparación del dinero restante.
* 🧩 Código dividido en diferentes módulos.

---

# 🧠 Conceptos utilizados

Durante el desarrollo del proyecto se practican los siguientes conceptos de Python.

## Datos primitivos

* `str` para nombres, categorías y textos.
* `int` para valores como el mes y el año.
* `float` para ingresos y gastos.
* `None` para representar datos inexistentes o resultados que no pueden calcularse.

## Operaciones matemáticas

* Suma de gastos.
* Resta entre ingresos y gastos.
* Diferencia entre presupuestos.
* División y multiplicación para calcular porcentajes.

## Manipulación de números

* Conversión de datos mediante `int()` y `float()`.
* Formateo de cantidades monetarias utilizando `:.2f`.
* Cálculo de porcentajes.
* Cálculo de diferencias positivas y negativas.

## F-Strings

Se utilizan para:

* Insertar variables dentro de textos.
* Mostrar cantidades monetarias.
* Formatear números con dos decimales.
* Alinear columnas en las comparaciones.
* Crear nombres dinámicos de archivos.

Por ejemplo:

```python
nombre_archivo = f"presupuesto_{nombre.lower()}.json"
```

## Funciones

El programa utiliza funciones reutilizables para:

* Solicitar datos.
* Validar valores.
* Agregar categorías.
* Calcular gastos.
* Mostrar presupuestos.
* Modificar gastos.
* Eliminar gastos.
* Comparar presupuestos.
* Cargar archivos.
* Guardar archivos.

## Estructuras de control

Se utilizan:

* `if`
* `elif`
* `else`
* `while`
* `for`

Estas estructuras permiten controlar el menú, validar información, recorrer categorías y gestionar diferentes situaciones del presupuesto.

## Listas

Las listas almacenan las categorías y sus respectivos gastos.

Por ejemplo:

```python
categorias = [
    "Alquiler",
    "Comida",
    "Transporte"
]

gastos = [
    10000,
    2000,
    1700
]
```

Cada posición de `categorias` corresponde con la misma posición de `gastos`.

## Diccionarios

Los diccionarios permiten organizar la información de cada usuario y sus presupuestos.

Por ejemplo:

```python
datos = {
    "nombre": "Gabriel",
    "presupuestos": {}
}
```

## Manejo de errores

Se utilizan mecanismos como:

* `try/except`
* `ValueError`
* `FileNotFoundError`
* Validación de opciones.
* Validación de números negativos.
* Control de divisiones entre cero.
* Comprobación de historiales inexistentes.

## Archivos JSON

La Versión 4 incorpora archivos `.json` para almacenar permanentemente los presupuestos.

Se utilizan:

```python
json.load()
```

para cargar información y:

```python
json.dump()
```

para guardarla.

## Módulo `datetime`

Se utiliza `datetime` para detectar automáticamente la fecha actual:

```python
from datetime import datetime

fecha_actual = datetime.now()

mes = fecha_actual.month
anio = fecha_actual.year
```

Esto permite registrar automáticamente presupuestos con identificadores como:

```text
9-2026
10-2026
11-2026
```

sin solicitar el mes o el año al usuario.

## Modularización

El programa está dividido en diferentes archivos `.py`, separando responsabilidades y evitando concentrar toda la lógica en `main.py`.

---

# 📁 Estructura del proyecto

La Versión 4 utiliza la siguiente estructura:

```text
Calculadora-Presupuesto/
│
├── main.py
├── funciones.py
├── prespuesto.py
├── manejar_archivos.py
├── configuracion.py
│
└── datos/
    ├── presupuesto_gabriel.json
    ├── presupuesto_maite.json
    └── ...
```

## `main.py`

Contiene el flujo principal de la aplicación.

Se encarga de:

* Mostrar el menú.
* Recibir la opción seleccionada.
* Detectar automáticamente el mes y año actual.
* Coordinar las funciones de los demás módulos.
* Crear nuevos presupuestos.
* Cargar historiales existentes.
* Ejecutar las opciones de consulta, modificación, eliminación y comparación.

## `prespuesto.py`

Contiene la lógica principal relacionada con los presupuestos.

Se encarga de:

* Solicitar ingresos.
* Solicitar los datos de un usuario.
* Gestionar categorías.
* Registrar gastos.
* Mostrar el presupuesto actual.
* Modificar gastos.
* Eliminar gastos.
* Calcular gastos totales.
* Calcular dinero restante.
* Comparar presupuestos.
* Comparar diferencias entre valores.

## `funciones.py`

Contiene funciones reutilizables y utilidades generales.

Se encarga de:

* Validar números.
* Solicitar valores numéricos.
* Calcular porcentajes.
* Limpiar la consola.
* Seleccionar categorías.
* Validar opciones.
* Permitir regresar al menú principal.

## `manejar_archivos.py`

Nuevo módulo encargado de la persistencia de datos.

Se encarga de:

* Crear presupuestos dentro del historial.
* Cargar archivos JSON.
* Guardar archivos JSON.
* Actualizar información existente.
* Generar archivos independientes para cada usuario.
* Trabajar con la carpeta `datos/`.
* Manejar historiales inexistentes mediante `FileNotFoundError`.

## `configuracion.py`

Contiene las constantes utilizadas para los colores de la consola.

Los colores permiten diferenciar:

* Errores.
* Advertencias.
* Resultados positivos.
* Títulos.
* Secciones importantes.

---

# 🗃️ Estructura de los datos

Cada usuario dispone de su propio archivo JSON.

Por ejemplo:

```text
datos/presupuesto_gabriel.json
```

Su estructura puede ser:

```json
{
    "nombre": "Gabriel",
    "presupuestos": {
        "8-2026": {
            "ingresos": 30000.0,
            "categorias": [
                "Alquiler",
                "Comida",
                "Transporte",
                "Internet"
            ],
            "gastos": [
                10000.0,
                2500.0,
                1800.0,
                1500.0
            ]
        },
        "9-2026": {
            "ingresos": 32000.0,
            "categorias": [
                "Alquiler",
                "Comida",
                "Transporte",
                "Internet"
            ],
            "gastos": [
                10000.0,
                2000.0,
                1700.0,
                1500.0
            ]
        }
    }
}
```

De esta forma, un único archivo contiene todo el historial financiero del usuario.

---

# ⚙️ ¿Cómo funciona?

Al iniciar el programa aparece el menú principal:

```text
========== CALCULADORA DE PRESUPUESTO ==========

Introduce una opción:

1. Crear nuevo presupuesto
2. Ver presupuesto actual
3. Modificar gastos
4. Eliminar gasto
5. Comparaciones
6. Salir
```

---

# 1️⃣ Crear nuevo presupuesto

El programa solicita el nombre del usuario.

```text
========== CREAR UN NUEVO PRESUPUESTO ==========

Introduce tu nombre: Gabriel
```

A continuación intenta cargar:

```text
presupuesto_gabriel.json
```

Si el archivo no existe:

```text
No se encontró el historial, se creará uno nuevo
```

El programa crea una estructura nueva:

```python
{
    "nombre": "Gabriel",
    "presupuestos": {}
}
```

Si el archivo ya existe:

```text
Historial encontrado
```

y se cargan los presupuestos anteriores.

Esto permite agregar un nuevo mes sin eliminar el historial existente.

## Ingresos

El programa solicita:

```text
Introduce tus ingresos mensuales: 32000
```

## Categorías básicas

Todos los presupuestos comienzan con:

* Alquiler
* Comida
* Transporte

El usuario introduce el gasto correspondiente a cada una.

```text
¿Cuánto gastas en alquiler? 10000
¿Cuánto gastas en comida? 2000
¿Cuánto gastas en transporte? 1700
```

## Categorías adicionales

También pueden agregarse categorías personalizadas:

```text
¿Tienes más categorias de gastos? si

Nombre de la categoría: Internet

¿Cuánto gastas en Internet? 1500
```

Si la categoría ya existe, el nuevo importe se suma al gasto existente.

## Fecha automática

El usuario no necesita introducir el mes ni el año.

El programa obtiene automáticamente la fecha mediante `datetime`.

Por ejemplo, si se ejecuta durante septiembre de 2026:

```text
9-2026
```

El presupuesto se guarda dentro del historial utilizando esa clave.

---

# 2️⃣ Ver presupuesto actual

Esta opción solicita el nombre:

```text
========== VER PRESUPUESTO ACTUAL ==========

Introduce tu nombre: Gabriel
```

El programa carga el archivo correspondiente y obtiene el último presupuesto registrado.

Ejemplo:

```text
========== VER PRESUPUESTO ACTUAL ==========

NOMBRE: Gabriel
MES: 9-2026

Alquiler: $10000.00
Comida: $2000.00
Transporte: $1700.00
Internet: $1500.00

========== RESUMEN ==========

Ingresos: $32000.00
Gastos totales: $15200.00
Dinero restante: $16800.00
Porcentaje gastado: 47.50%

¡Te quedan $16800.00 este mes!

========== RESUMEN DE GASTOS ==========

Te ha sobrado: $16800.00

========== ANALISIS ==========

Has gastado menos de la mitad de tus ingresos

========== ANALISIS DE CADA GASTO ==========

Alquiler gastó 31.25%
Comida gastó 6.25%
Transporte gastó 5.31%
Internet gastó 4.69%
```

Los datos ya no dependen de variables temporales de la ejecución.

Son obtenidos directamente del historial almacenado.

---

# 3️⃣ Modificar gastos

El usuario introduce su nombre y el programa carga su historial.

Después se obtiene el último presupuesto registrado y se muestran sus categorías.

Por ejemplo:

```text
0. Alquiler: $10000.0
1. Comida: $2000.0
2. Transporte: $1700.0
3. Internet: $1500.0

Elige una categoría según su número: 1

¿Cuánto gastas en Comida? 1500

Gasto modificado correctamente
```

El valor anterior se sustituye:

```text
Comida: $2000
```

por:

```text
Comida: $1500
```

Después se utiliza `guardar_datos()` para escribir nuevamente el historial en el archivo JSON.

Por lo tanto, la modificación permanece incluso después de cerrar el programa.

---

# 4️⃣ Eliminar gasto

Esta opción también trabaja directamente sobre el presupuesto almacenado.

El usuario selecciona una categoría:

```text
0. Alquiler: $10000
1. Comida: $1500
2. Transporte: $1700
3. Internet: $1500

Elige una categoría según su número: 3
```

El programa elimina tanto:

```python
categorias.pop(opcion_categoria)
```

como:

```python
gastos.pop(opcion_categoria)
```

manteniendo ambas listas sincronizadas.

Después se guarda nuevamente el archivo JSON.

```text
Gasto eliminado correctamente
```

---

# 5️⃣ Comparaciones

La Versión 4 incorpora un sistema para comparar los dos últimos presupuestos registrados.

El usuario introduce su nombre:

```text
========== COMPARAR PRESUPUESTO ==========

Ingresa tu nombre: Gabriel
```

El programa carga el historial y obtiene:

* El último mes registrado.
* El mes inmediatamente anterior.

Por ejemplo:

```text
9-2026
8-2026
```

## Comparación de ingresos

```text
Mes actual:          $32000.00
Mes anterior:        $30000.00
Diferencia:          +$2000.00
```

Una diferencia positiva se representa mediante:

```text
+$2000.00
```

Una diferencia negativa:

```text
-$500.00
```

Y cuando no existe diferencia:

```text
$0.00
```

## Comparación por categorías

El programa compara las categorías presentes en ambos presupuestos.

No depende de que una categoría ocupe la misma posición en ambos meses.

Primero obtiene el nombre de la categoría y después busca su posición correspondiente en el presupuesto anterior.

Esto permite comparar correctamente estructuras como:

```text
Mes actual:
Alquiler
Comida
Transporte
Internet

Mes anterior:
Alquiler
Transporte
Comida
```

aunque las posiciones sean diferentes.

Las categorías que no existen en el presupuesto anterior actualmente no se incluyen en la comparación.

## Tabla comparativa

La información se presenta en forma de tabla:

```text
================================================================================
CATEGORIA                     9-2026          8-2026      DIFERENCIA
================================================================================
Alquiler                    $10000.00       $10000.00           $0.00
Comida                       $2000.00        $2500.00        -$500.00
Transporte                   $1700.00        $1800.00        -$100.00
--------------------------------------------------------------------------------
TOTAL                       $15200.00       $15800.00        -$600.00
================================================================================
```

## Comparación del dinero restante

También se compara cuánto dinero quedó disponible en cada mes:

```text
Restante mes actual:        $16800.00
Restante mes anterior:      $14200.00
Diferencia de restantes:     +$2600.00
```

Esto permite observar rápidamente si la situación financiera mejoró o empeoró respecto al mes anterior.

## Validación de meses

Para realizar una comparación deben existir al menos dos presupuestos.

Si solamente existe uno:

```text
No hay suficientes meses para realizar la comparación
```

De esta forma se evita intentar acceder a un mes anterior inexistente.

---

# 6️⃣ Salir

Finaliza la ejecución del programa y limpia la consola.

---

# 🧮 Cálculos realizados

## Gastos totales

```text
Gastos totales = suma de todos los gastos
```

En Python:

```python
gastos_totales = sum(todos_los_gastos)
```

## Dinero restante

```text
Dinero restante = ingresos - gastos totales
```

## Porcentaje gastado

```text
Porcentaje gastado = gastos totales / ingresos × 100
```

## Porcentaje por categoría

Cada gasto también se compara individualmente con los ingresos:

```text
Porcentaje de categoría = gasto de categoría / ingresos × 100
```

## Diferencia entre meses

```text
Diferencia = valor actual - valor anterior
```

Si el resultado es positivo:

```text
+$500.00
```

Si es negativo:

```text
-$500.00
```

Si ambos valores son iguales:

```text
$0.00
```

---

# 🛡️ Validación de datos

El programa valida diferentes situaciones para evitar errores durante la ejecución.

## Valores no numéricos

Si se introduce texto cuando se espera un número:

```text
Introduce tus ingresos mensuales: hola

Error, los ingresos son inválidos
```

El programa vuelve a solicitar el dato.

## Números negativos

No se permiten cantidades negativas para ingresos o gastos.

```text
¿Cuánto gastas en comida? -500

Error, el número debe ser positivo
```

## Usuario inexistente

Si se intenta consultar un usuario cuyo archivo no existe:

```text
Introduce tu nombre: Tomas

No se encontraron datos con el nombre
```

`cargar_datos()` captura `FileNotFoundError` y devuelve `None`.

## Ingresos iguales a cero

Cuando los ingresos son `0`, no puede calcularse correctamente un porcentaje.

En ese caso la función correspondiente devuelve `None`.

## Comparación sin historial suficiente

Si existen menos de dos meses:

```text
No hay suficientes meses para realizar la comparación
```

## Opciones incorrectas

El menú comprueba que la opción introducida sea numérica y corresponda con una opción disponible.

---

# 📊 Análisis de gastos

El programa analiza qué porcentaje de los ingresos se ha utilizado.

* **0%:** No se ha gastado nada.
* **Menos del 50%:** Se ha gastado menos de la mitad de los ingresos.
* **50%:** Se ha gastado exactamente la mitad.
* **Entre 50% y 100%:** Se muestra una advertencia.
* **100%:** Se han utilizado todos los ingresos.
* **Más del 100%:** Los gastos han superado los ingresos.

También informa si:

* Sobró dinero.
* El presupuesto terminó exactamente en `0`.
* Se gastó más dinero del disponible.

---

# 💾 Persistencia de datos

Una de las principales novedades de la Versión 4 es la persistencia.

Anteriormente, los datos solamente existían mientras el programa estaba ejecutándose.

Ahora el flujo es:

```text
Usuario introduce nombre
        ↓
Buscar archivo JSON
        ↓
¿Existe?
   ↓          ↓
  Sí          No
   ↓          ↓
Cargar      Crear historial
   ↓          ↓
Modificar datos
        ↓
Guardar JSON
```

Esto permite cerrar completamente el programa y recuperar posteriormente toda la información.

---

# 👤 Historial independiente por usuario

Cada persona dispone de un archivo separado.

Por ejemplo:

```text
datos/
│
├── presupuesto_gabriel.json
├── presupuesto_maite.json
├── presupuesto_tomas.json
└── presupuesto_lucia.json
```

Esto evita mezclar los presupuestos de diferentes usuarios.

---

# 📅 Historial mensual

Dentro de cada archivo, los presupuestos se organizan por mes y año:

```json
"presupuestos": {
    "7-2026": {},
    "8-2026": {},
    "9-2026": {}
}
```

Esto permite construir progresivamente un historial financiero sin eliminar los meses anteriores.

---

# 🧪 Pruebas realizadas

Durante el desarrollo se comprobaron diferentes situaciones:

* [x] Crear un presupuesto para un usuario nuevo.
* [x] Crear automáticamente su archivo JSON.
* [x] Detectar un historial existente.
* [x] Agregar un nuevo presupuesto al historial.
* [x] Mantener los presupuestos anteriores.
* [x] Detectar automáticamente el mes y año.
* [x] Crear categorías básicas.
* [x] Crear categorías adicionales.
* [x] Agregar gastos.
* [x] Visualizar el último presupuesto.
* [x] Cargar datos después de reiniciar el programa.
* [x] Modificar un gasto existente.
* [x] Guardar permanentemente una modificación.
* [x] Eliminar una categoría.
* [x] Eliminar su gasto correspondiente.
* [x] Guardar permanentemente una eliminación.
* [x] Consultar un usuario inexistente.
* [x] Comparar dos meses.
* [x] Comparar ingresos.
* [x] Comparar gastos por categoría.
* [x] Comparar categorías aunque tengan posiciones diferentes.
* [x] Calcular diferencias positivas.
* [x] Calcular diferencias negativas.
* [x] Comparar gastos totales.
* [x] Comparar dinero restante.
* [x] Intentar comparar un historial con menos de dos meses.
* [x] Validar entradas incorrectas.
* [x] Validar números negativos.
* [x] Validar opciones inexistentes del menú.

---

# 🗺️ Evolución del proyecto

## Versión 1

* [x] Solicitar ingresos.
* [x] Registrar gastos básicos.
* [x] Calcular gastos totales.
* [x] Calcular dinero restante.
* [x] Mostrar un resumen básico del presupuesto.

## Versión 2

* [x] Agregar validación de datos.
* [x] Evitar números negativos.
* [x] Manejar ingresos iguales a `0`.
* [x] Agregar categorías personalizadas.
* [x] Permitir acumular gastos en categorías existentes.
* [x] Crear funciones reutilizables.
* [x] Calcular porcentajes.
* [x] Analizar el porcentaje utilizado de los ingresos.
* [x] Agregar colores ANSI.
* [x] Mejorar la presentación de la consola.

## Versión 3

* [x] Crear un menú principal.
* [x] Permitir repetir operaciones sin reiniciar el programa.
* [x] Visualizar el presupuesto actual.
* [x] Modificar gastos.
* [x] Eliminar gastos.
* [x] Analizar individualmente cada categoría.
* [x] Separar el proyecto en módulos.
* [x] Crear `funciones.py`.
* [x] Crear `prespuesto.py`.
* [x] Crear `configuracion.py`.
* [x] Mejorar la organización de las funciones.
* [x] Validar las opciones del menú.

## Versión 4

* [x] Implementar persistencia de datos.
* [x] Utilizar archivos JSON.
* [x] Crear un archivo independiente por usuario.
* [x] Crear la carpeta `datos/`.
* [x] Crear `manejar_archivos.py`.
* [x] Cargar historiales existentes.
* [x] Crear automáticamente historiales nuevos.
* [x] Detectar automáticamente el mes y año.
* [x] Guardar múltiples meses por usuario.
* [x] Mantener los presupuestos anteriores.
* [x] Eliminar la edad al no ser necesaria.
* [x] Mostrar información directamente desde los datos almacenados.
* [x] Modificar gastos almacenados.
* [x] Guardar permanentemente las modificaciones.
* [x] Eliminar gastos almacenados.
* [x] Guardar permanentemente las eliminaciones.
* [x] Eliminar la dependencia de estructuras globales para categorías y gastos.
* [x] Agregar comparación entre meses.
* [x] Comparar ingresos.
* [x] Comparar categorías comunes.
* [x] Comparar gastos totales.
* [x] Comparar dinero restante.
* [x] Mostrar diferencias positivas y negativas.
* [x] Crear tablas comparativas en consola.
* [x] Validar que existan suficientes meses para comparar.
* [x] Mejorar la separación de responsabilidades entre módulos.

---

# 🔮 Futuras versiones

## Versión 5

* [ ] Permitir seleccionar manualmente los meses que se quieren comparar.
* [ ] Consultar cualquier mes almacenado en el historial.
* [ ] Mostrar categorías que existen únicamente en uno de los meses.
* [ ] Detectar la categoría con mayor y menor gasto.
* [ ] Calcular promedios mensuales.
* [ ] Calcular el promedio histórico de cada categoría.
* [ ] Crear estadísticas sobre la evolución financiera.
* [ ] Implementar límites de gasto por categoría.

## Versión 6

* [ ] Implementar metas de ahorro.
* [ ] Permitir establecer un objetivo mensual de ahorro.
* [ ] Analizar si el usuario está cumpliendo sus objetivos.
* [ ] Generar recomendaciones basadas en el historial.
* [ ] Detectar aumentos importantes de gastos.
* [ ] Detectar gastos recurrentes.
* [ ] Mejorar los reportes financieros.
* [ ] Incorporar diferentes monedas.

## Versión 7

* [ ] Implementar programación orientada a objetos.
* [ ] Crear clases para usuarios y presupuestos.
* [ ] Mejorar la arquitectura interna del proyecto.
* [ ] Crear gráficos de gastos.
* [ ] Crear gráficos de evolución mensual.
* [ ] Crear gráficos por categoría.
* [ ] Exportar reportes.
* [ ] Preparar el proyecto para una interfaz gráfica.

## Versión 8

* [ ] Crear una interfaz gráfica.
* [ ] Crear formularios para registrar presupuestos.
* [ ] Mostrar gráficos dentro de la aplicación.
* [ ] Crear una vista del historial.
* [ ] Crear un panel financiero.
* [ ] Permitir navegar entre diferentes meses.
* [ ] Mejorar la experiencia de usuario.
* [ ] Reducir la dependencia de la consola.

## Versión 9

* [ ] Convertir el proyecto en una aplicación web.
* [ ] Crear cuentas de usuario.
* [ ] Implementar autenticación.
* [ ] Utilizar una base de datos.
* [ ] Crear un dashboard financiero.
* [ ] Acceder al historial desde diferentes dispositivos.
* [ ] Generar reportes financieros desde la web.
* [ ] Convertir el proyecto en una aplicación de gestión financiera más completa.

---

# 📚 Objetivo del proyecto

El objetivo principal de **Calculadora de Presupuesto Personal** es aprender Python mediante el desarrollo progresivo de una aplicación real.

En lugar de limitarse a ejercicios aislados, cada versión introduce nuevos problemas y conceptos que requieren reorganizar y ampliar el código existente.

La **Versión 4** representa uno de los cambios más importantes del proyecto hasta el momento, incorporando:

* Persistencia mediante JSON.
* Historiales independientes por usuario.
* Presupuestos organizados por mes.
* Detección automática de fechas.
* Lectura y escritura de archivos.
* Modificación persistente de información.
* Comparación entre diferentes meses.
* Análisis de la evolución de ingresos y gastos.
* Una estructura modular con responsabilidades mejor separadas.

El proyecto sirve como base para continuar avanzando hacia conceptos más complejos como **programación orientada a objetos, estadísticas financieras, gráficos, bases de datos, interfaces gráficas y desarrollo web**.

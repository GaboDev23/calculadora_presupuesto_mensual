# 💰 Calculadora de Presupuesto Personal

Una aplicación de consola desarrollada en **Python** que permite gestionar un presupuesto mensual, registrar gastos por categorías y determinar cuánto dinero queda disponible después de cubrir los gastos.

El proyecto fue creado como práctica de los fundamentos de Python, incorporando progresivamente conceptos como **datos primitivos, operaciones matemáticas, manipulación de números, F-Strings, funciones, estructuras de control, listas, diccionarios, manejo de errores y modularización**.

---

## 🧠 Conceptos utilizados

Durante el desarrollo del proyecto se practican los siguientes conceptos:

* **Datos primitivos**

  * `str` para nombres y textos.
  * `int` para la edad.
  * `float` para ingresos y gastos.
  * `None` para representar un porcentaje que no puede calcularse.

* **Operaciones matemáticas**

  * Suma de gastos.
  * Resta entre ingresos y gastos.
  * División y multiplicación para calcular porcentajes.

* **Manipulación de números**

  * Conversión de datos utilizando `int()` y `float()`.
  * Formateo de cantidades monetarias utilizando `:.2f`.
  * Cálculo de porcentajes.

* **F-Strings**

  * Utilizadas para mostrar información de forma clara.
  * Inserción de variables dentro de textos.
  * Formateo de cantidades monetarias con dos decimales.

* **Funciones**

  * Funciones reutilizables para solicitar y validar valores.
  * Funciones para crear, modificar, eliminar y mostrar información.
  * Separación de responsabilidades mediante funciones.

* **Estructuras de control**

  * `if`, `elif` y `else` para tomar decisiones.
  * `while` para repetir solicitudes hasta obtener datos válidos.
  * `for` para recorrer categorías y gastos.

* **Listas y diccionarios**

  * Listas para almacenar categorías y sus respectivos gastos.
  * Diccionarios para organizar las categorías y gastos asociados.

* **Manejo de errores**

  * `try/except` para controlar entradas incorrectas.
  * Manejo de `ValueError`.
  * Manejo de `ZeroDivisionError`.
  * Validación de opciones introducidas por el usuario.

* **Colores en consola**

  * Uso de códigos ANSI para mejorar la presentación.
  * Rojo para errores y situaciones negativas.
  * Verde para resultados positivos.
  * Amarillo para advertencias.
  * Cian para títulos y secciones.

* **Modularización**

  * División del proyecto en diferentes módulos `.py`.
  * Separación de la lógica según su responsabilidad.
  * Uso de `import` para utilizar funciones y variables de otros módulos.

---

## 📁 Estructura del proyecto

La versión 3 divide el programa en diferentes módulos:

```text
Calculadora-Presupuesto/
│
├── main.py
├── funciones.py
├── prespuesto.py
└── configuracion.py
```

### `main.py`

Contiene el flujo principal de la aplicación y el menú de opciones.

Se encarga de:

* Mostrar el menú principal.
* Recibir la opción del usuario.
* Ejecutar las funciones correspondientes.
* Controlar el flujo general del programa.

### `prespuesto.py`

Contiene la lógica relacionada con el presupuesto.

Se encarga de:

* Almacenar los ingresos.
* Gestionar las categorías.
* Agregar categorías.
* Registrar gastos.
* Mostrar el presupuesto.
* Modificar gastos.
* Eliminar gastos.
* Calcular el dinero restante.

### `funciones.py`

Contiene funciones reutilizables y utilidades generales.

Se encarga de:

* Validar números enteros.
* Validar números decimales.
* Calcular porcentajes.
* Limpiar la consola.
* Comprobar si existen gastos.
* Validar opciones.
* Permitir volver al menú.

### `configuracion.py`

Contiene las constantes utilizadas para los colores de la consola.

---

## ⚙️ ¿Cómo funciona?

Al iniciar el programa se muestra un menú principal:

```text
========== CALCULADORA DE PRESUPUESTO ==========

Introduce una opción:
1. Crear nuevo presupuesto
2. Ver presupuesto actual
3. Modificar gastos
4. Eliminar gasto
5. Salir
```

### 1. Crear un nuevo presupuesto

Al seleccionar esta opción, el programa solicita:

1. Nombre.
2. Edad.
3. Ingresos mensuales.
4. Gastos de alquiler.
5. Gastos de comida.
6. Gastos de transporte.
7. Categorías adicionales de gastos.

Las tres categorías iniciales son:

* Alquiler
* Comida
* Transporte

También se pueden agregar categorías personalizadas.

Por ejemplo:

```text
¿Tienes más categorias de gastos? si

Nombre de la categoria: Internet

¿Cuánto gastas en Internet? 1500

¿Tienes más categorias de gastos? si

Nombre de la categoria: Gimnasio

¿Cuánto gastas en Gimnasio? 2000

¿Tienes más categorias de gastos? no
```

Si se introduce una categoría que ya existe, el programa suma el nuevo gasto al importe existente.

---

### 2. Ver presupuesto actual

Permite visualizar toda la información del presupuesto actual:

```text
========== VER PRESUPUESTO ACTUAL ==========

NOMBRE: Gabriel
EDAD: 27

Alquiler: $10000.00
Comida: $6000.00
Transporte: $2500.00
Internet: $1500.00

========== RESUMEN ==========

Ingresos: $35000.00
Gastos totales: $20000.00
Dinero restante: $15000.00
Porcentaje gastado: 57.14%
```

También muestra un análisis general de los gastos y el porcentaje que representa cada categoría respecto a los ingresos.

---

### 3. Modificar gastos

El usuario puede seleccionar una categoría existente y establecer un nuevo importe.

Por ejemplo:

```text
0. Alquiler: $10000
1. Comida: $6000
2. Transporte: $2500

Elige una categoría según su número: 1

¿Cuánto gastas en Comida? 7000

Gasto modificado correctamente
```

El gasto anterior se reemplaza por el nuevo valor.

---

### 4. Eliminar gastos

Permite seleccionar una categoría y eliminarla junto con su gasto correspondiente.

```text
0. Alquiler: $10000
1. Comida: $6000
2. Transporte: $2500

Elige una categoría según su número: 2

Gasto eliminado correctamente
```

Las categorías y los gastos se mantienen sincronizados para evitar errores al acceder a sus posiciones.

---

### 5. Salir

Finaliza la ejecución del programa y limpia la consola.

---

## 🧮 Cálculos realizados

### Gastos totales

```text
Gastos totales = suma de todos los gastos
```

Incluye las categorías básicas y todas las categorías adicionales.

### Dinero restante

```text
Dinero restante = ingresos - gastos totales
```

### Porcentaje gastado

```text
Porcentaje gastado = gastos totales / ingresos × 100
```

También se calcula el porcentaje que representa cada categoría individual respecto a los ingresos.

Si los ingresos son `0`, el porcentaje no puede calcularse y la función devuelve `None`.

---

## 🛡️ Validación de datos

El programa valida los datos introducidos por el usuario para evitar errores.

Si se introduce texto cuando se espera un número:

```text
Introduce tu edad: abc

Error, la edad debe ser un número entero
```

El programa vuelve a solicitar el dato hasta recibir un valor válido.

También se evita introducir valores negativos:

```text
¿Cuánto gastas en comida? -500

Error, el número debe ser positivo
```

La edad debe ser un número entero mayor que `0`, mientras que los ingresos y gastos pueden ser `0`.

Las opciones del menú también son validadas para impedir que el usuario introduzca valores que no correspondan a una opción disponible.

---

## 📊 Análisis de gastos

El programa analiza el porcentaje de ingresos utilizado y muestra diferentes mensajes según el resultado:

* **0%:** No se ha gastado nada.
* **Menos del 50%:** Se ha gastado menos de la mitad de los ingresos.
* **50%:** Se ha gastado exactamente la mitad.
* **Entre 50% y 100%:** Se muestra una advertencia.
* **100%:** Se han utilizado todos los ingresos.
* **Más del 100%:** Los gastos superan los ingresos.

También se informa si al usuario le sobra dinero, queda exactamente en `0` o ha gastado más de sus ingresos.

---

## 🖥️ Ejemplo de ejecución

```text
========== CALCULADORA DE PRESUPUESTO ==========

Introduce una opción:
1. Crear nuevo presupuesto
2. Ver presupuesto actual
3. Modificar gastos
4. Eliminar gasto
5. Salir

========== ELIGE UNA OPCIÓN ==========
1

========== CREAR UN NUEVO PRESUPUESTO ==========

Introduce tu nombre: Gabriel
Introduce tu edad: 27
Introduce tus ingresos mensuales: 35000

GASTOS MENSUALES

¿Cuánto gastas en alquiler? 10000
¿Cuánto gastas en comida? 6000
¿Cuánto gastas en transporte? 2500

¿Tienes más categorias de gastos? si

Nombre de la categoria: Internet
¿Cuánto gastas en Internet? 1500

¿Tienes más categorias de gastos? no
```

Posteriormente, al seleccionar **Ver presupuesto actual**:

```text
========== VER PRESUPUESTO ACTUAL ==========

NOMBRE: Gabriel
EDAD: 27

Alquiler: $10000.00
Comida: $6000.00
Transporte: $2500.00
Internet: $1500.00

========== RESUMEN ==========

Nombre: Gabriel
Edad: 27 años

Ingresos: $35000.00
Gastos totales: $20000.00
Dinero restante: $15000.00
Porcentaje gastado: 57.14%

========== RESUMEN DE GASTOS ==========

Te ha sobrado: $15000.00

========== ANALISIS ==========

¡Cuidado, has utilizado una gran parte de tus ingresos!

========== ANALISIS DE CADA GASTO ==========

Alquiler gastó 28.57%
Comida gastó 17.14%
Transporte gastó 7.14%
Internet gastó 4.29%
```

---

## 🧪 Pruebas realizadas

La versión 3 fue probada mediante diferentes casos de uso para comprobar el funcionamiento del programa.

Se ejecutaron correctamente **12 casos de prueba**:

* [x] Crear un presupuesto básico.
* [x] Crear un presupuesto con categorías adicionales.
* [x] Agregar una categoría existente.
* [x] Visualizar el presupuesto actual.
* [x] Modificar un gasto.
* [x] Eliminar un gasto.
* [x] Introducir datos inválidos.
* [x] Introducir números negativos.
* [x] Seleccionar una opción inexistente.
* [x] Salir del programa.
* [x] Intentar acceder al presupuesto antes de crear uno.
* [x] Eliminar todas las categorías y comprobar el funcionamiento posterior.

Todas las pruebas fueron ejecutadas correctamente.

---

## 🔮 Posibles mejoras y futuras versiones

### Versión 2

* [x] Agregar validación de datos para evitar errores cuando el usuario introduce texto donde debería introducir un número.
* [x] Evitar que se introduzcan valores negativos en ingresos o gastos.
* [x] Utilizar `if/else` para mostrar diferentes mensajes dependiendo del dinero restante.
* [x] Mejorar el formato visual de la consola.
* [x] Permitir introducir más categorías de gastos.
* [x] Mostrar las categorías adicionales junto con sus respectivos gastos.
* [x] Manejar el caso en que los ingresos sean `0`.
* [x] Analizar los gastos según el porcentaje de ingresos utilizado.
* [x] Crear funciones reutilizables para validar valores enteros y decimales.
* [x] Utilizar colores para diferenciar errores, advertencias y resultados positivos.

### Versión 3

* [x] Agregar un menú principal.
* [x] Permitir registrar varios gastos.
* [x] Separar los gastos en categorías.
* [x] Calcular qué porcentaje de los ingresos representa cada categoría.
* [x] Agregar una opción para modificar gastos.
* [x] Agregar una opción para eliminar gastos.
* [x] Permitir repetir los cálculos sin reiniciar el programa.
* [x] Mejorar la organización del código mediante funciones.
* [x] Separar el proyecto en diferentes módulos.
* [x] Crear un módulo para las funciones reutilizables.
* [x] Crear un módulo para la configuración de colores.
* [x] Crear un módulo dedicado a la gestión del presupuesto.
* [x] Validar las opciones introducidas en los menús.
* [x] Permitir crear nuevamente un presupuesto sin conservar los datos del anterior.

### Versión 4

* [ ] Guardar los datos en un archivo.
* [ ] Cargar los datos cuando se vuelva a iniciar el programa.
* [ ] Utilizar archivos `.json` para almacenar la información.
* [ ] Crear un historial de presupuestos mensuales.
* [ ] Comparar los gastos de diferentes meses.

### Futuras mejoras

* [ ] Implementar programación orientada a objetos.
* [ ] Crear gráficos para visualizar los gastos.
* [ ] Crear una interfaz gráfica.
* [ ] Convertir el proyecto en una aplicación web.
* [ ] Agregar diferentes monedas.
* [ ] Crear un sistema de metas de ahorro.
* [ ] Calcular cuánto dinero podría ahorrarse al mes.
* [ ] Crear recomendaciones basadas en los gastos del usuario.
* [ ] Permitir establecer límites de gasto por categoría.
* [ ] Mostrar las categorías que representan la mayor parte de los gastos.

---

## 📚 Objetivo del proyecto

El objetivo principal es practicar los fundamentos de Python mediante un proyecto sencillo y funcional, construyendo progresivamente nuevas versiones a medida que se aprenden conceptos más avanzados del lenguaje.

La **versión 3** incorpora un **menú principal, gestión completa de categorías y gastos, modificación y eliminación de gastos, análisis individual de categorías, validación de opciones, posibilidad de crear nuevos presupuestos y una estructura modular dividida en diferentes archivos Python**.

Este proyecto forma parte del proceso de aprendizaje y puede utilizarse como base para desarrollar posteriormente una aplicación de gestión financiera más completa.

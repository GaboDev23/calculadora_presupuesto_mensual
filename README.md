# 💰 Calculadora de Presupuesto Personal

Una pequeña aplicación de consola desarrollada en **Python** que permite calcular los gastos mensuales de una persona y determinar cuánto dinero le queda disponible después de cubrir sus gastos.

El proyecto fue creado como práctica de los fundamentos básicos de Python, especialmente **datos primitivos, operaciones matemáticas, manipulación de números, F-Strings, funciones, estructuras de control, listas, diccionarios y manejo de errores**.

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

  * Funciones reutilizables para solicitar y validar valores enteros y decimales.

* **Estructuras de control**

  * `if`, `elif` y `else` para tomar decisiones.
  * `while` para repetir solicitudes hasta obtener datos válidos.
  * `for` para recorrer categorías y gastos.

* **Listas y diccionarios**

  * Listas para almacenar categorías y sus respectivos gastos.
  * Diccionarios para organizar las categorías adicionales.

* **Manejo de errores**

  * `try/except` para controlar entradas incorrectas.
  * Manejo de `ValueError`.
  * Manejo de `ZeroDivisionError`.

* **Colores en consola**

  * Uso de códigos ANSI para mejorar la presentación.
  * Rojo para errores y situaciones negativas.
  * Verde para resultados positivos.
  * Amarillo para advertencias.
  * Cian para títulos y secciones.

## ⚙️ ¿Cómo funciona?

Al iniciar el programa, se solicita al usuario:

1. Nombre.
2. Edad.
3. Ingresos mensuales.
4. Gastos de alquiler.
5. Gastos de comida.
6. Gastos de transporte.
7. Categorías adicionales de gastos.

El usuario puede agregar tantas categorías adicionales como necesite.

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

Las categorías y sus respectivos gastos son almacenados y posteriormente incluidos en el cálculo de los gastos totales.

### Gastos totales

```text
Gastos totales = alquiler + comida + transporte + categorías adicionales
```

### Dinero restante

```text
Dinero restante = ingresos - gastos totales
```

### Porcentaje gastado

```text
Porcentaje gastado = gastos totales / ingresos × 100
```

Si los ingresos son `0`, el porcentaje no puede calcularse y el programa muestra que no está disponible.

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

## 📊 Análisis de gastos

El programa analiza el porcentaje de ingresos utilizado y muestra diferentes mensajes según el resultado:

* **0%:** No se ha gastado nada.
* **Menos del 50%:** Se ha gastado menos de la mitad de los ingresos.
* **50%:** Se ha gastado exactamente la mitad.
* **Entre 50% y 100%:** Se muestra una advertencia.
* **100%:** Se han utilizado todos los ingresos.
* **Más del 100%:** Los gastos superan los ingresos.

También se informa si al usuario le sobra dinero, queda exactamente en `0` o ha gastado más de sus ingresos.

## 🖥️ Ejemplo de ejecución

```text
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

========== GASTOS ==========

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

¡Te quedan $15000.00 este mes!

========== RESUMEN DE GASTOS ==========

Te ha sobrado: $15000.00

========== ANALISIS ==========

¡Cuidado, has utilizado una gran parte de tus ingresos!
```

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

* [ ] Agregar un menú principal.
* [ ] Permitir registrar varios gastos.
* [ ] Separar los gastos en categorías.
* [ ] Calcular qué porcentaje de los ingresos representa cada categoría.
* [ ] Agregar una opción para modificar gastos.
* [ ] Agregar una opción para eliminar gastos.
* [ ] Permitir repetir los cálculos sin reiniciar el programa.
* [ ] Mejorar la organización del código mediante funciones.

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

## 📚 Objetivo del proyecto

El objetivo principal es practicar los fundamentos de Python mediante un proyecto sencillo y funcional, construyendo progresivamente nuevas versiones a medida que se aprenden conceptos más avanzados del lenguaje.

La segunda versión incorpora **validación de datos, manejo de errores, funciones reutilizables, categorías personalizadas, análisis de gastos y una presentación visual mejorada**.

Este proyecto forma parte del proceso de aprendizaje y puede utilizarse como base para desarrollar posteriormente una aplicación de gestión financiera más completa.

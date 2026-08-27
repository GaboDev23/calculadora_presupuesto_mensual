# 💰 Calculadora de Presupuesto Personal

Una pequeña aplicación de consola desarrollada en **Python** que permite calcular los gastos mensuales de una persona y determinar cuánto dinero le queda disponible después de cubrir sus gastos.

El proyecto fue creado como práctica de los fundamentos básicos de Python, especialmente **datos primitivos, operaciones matemáticas, manipulación de números y F-Strings**.

## 🧠 Conceptos utilizados

Durante el desarrollo del proyecto se practican los siguientes conceptos:

* **Datos primitivos**

  * `str` para nombres y otros textos.
  * `int` para la edad.
  * `float` para ingresos y gastos.

* **Operaciones matemáticas**

  * Suma de los gastos.
  * Resta entre ingresos y gastos.
  * División y multiplicación para calcular el porcentaje gastado.

* **Manipulación de números**

  * Conversión de datos utilizando `int()` y `float()`.
  * Redondeo de resultados utilizando `round()`.
  * Formateo de números decimales.

* **F-Strings**

  * Utilizadas para mostrar los resultados de forma clara y ordenada.
  * Formateo de cantidades monetarias utilizando `:.2f`.

## ⚙️ ¿Cómo funciona?

Al iniciar el programa, se solicita al usuario:

1. Nombre.
2. Edad.
3. Ingresos mensuales.
4. Gastos de alquiler.
5. Gastos de comida.
6. Gastos de transporte.
7. Otros gastos.

Con estos datos, el programa calcula:

### Gastos totales

```text
Gastos totales = alquiler + comida + transporte + otros
```

### Dinero restante

```text
Dinero restante = ingresos - gastos totales
```

### Porcentaje gastado

```text
Porcentaje gastado = gastos totales / ingresos × 100
```

Finalmente, se muestra un resumen con toda la información.

## 🖥️ Ejemplo de ejecución

```text
Introduce tu nombre: Gabriel
Introduce tu edad: 27
Introduce tus ingresos mensuales: 35000

GASTOS MENSUALES

¿Cuánto gastas en alquiler? 10000
¿Cuánto gastas en comida? 6000
¿Cuánto gastas en transporte? 2500
¿Cuánto gastas en otros gastos? 3000

========== RESUMEN ==========

Nombre: Gabriel
Edad: 27 años

Ingresos: $35000.00
Gastos totales: $21500.00
Dinero restante: $13500.00
Porcentaje gastado: 61%

¡Te quedan $13500.00 este mes!
```
## 🔮 Posibles mejoras y futuras versiones

El proyecto puede evolucionar bastante a partir de esta primera versión.

### Versión 2

* [x] Agregar validación de datos para evitar errores cuando el usuario introduce texto donde debería introducir un número.
* [x] Evitar que se introduzcan valores negativos en ingresos o gastos.
* [x] Utilizar `if/else` para mostrar diferentes mensajes dependiendo del dinero restante.
* [x] Mejorar el formato visual de la consola.
* [ ] Permitir introducir más categorías de gastos.

### Versión 3

* [ ] Agregar un menú principal.
* [ ] Permitir registrar varios gastos.
* [ ] Separar los gastos en categorías.
* [ ] Calcular qué porcentaje de los ingresos representa cada categoría.
* [ ] Agregar una opción para modificar o eliminar gastos.
* [ ] Permitir repetir los cálculos sin reiniciar el programa.

### Versión 4

* [ ] Guardar los datos en un archivo.
* [ ] Cargar los datos cuando se vuelva a iniciar el programa.
* [ ] Utilizar archivos `.json` para almacenar la información.
* [ ] Crear un historial de presupuestos mensuales.
* [ ] Comparar los gastos de diferentes meses.

### Futuras mejoras

* [ ] Crear funciones para organizar mejor el código.
* [ ] Implementar programación orientada a objetos.
* [ ] Crear gráficos para visualizar los gastos.
* [ ] Crear una interfaz gráfica.
* [ ] Convertir el proyecto en una aplicación web.
* [ ] Agregar diferentes monedas.
* [ ] Crear un sistema de metas de ahorro.
* [ ] Calcular cuánto dinero podría ahorrarse al mes.
* [ ] Crear recomendaciones basadas en los gastos del usuario.

## 📚 Objetivo del proyecto

El objetivo principal es practicar los fundamentos de Python mediante un proyecto sencillo y funcional, construyendo progresivamente nuevas versiones a medida que se aprenden conceptos más avanzados del lenguaje.

Este proyecto forma parte del proceso de aprendizaje y puede utilizarse como base para desarrollar posteriormente una aplicación de gestión financiera más completa.

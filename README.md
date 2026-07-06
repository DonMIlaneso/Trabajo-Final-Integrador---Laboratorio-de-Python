# Trabajo Final Integrador - Python

## Escenario 9: Sistema de venta de entradas para recitales

Sistema por consola que permite administrar la venta de entradas para distintos recitales. La solucion contempla seleccion de evento, seleccion de sectores, calculo de importes, control de capacidad, aplicacion de promociones o descuentos, registro de ventas y estadisticas basicas de demanda.

## Integrantes

- Caballero Lara
- Hanke Valentin
- Lazcano Francisco
- Vallarino Daniel
- Vallejos Belinda

## Comision

AED 1.1

## Funcionalidades

- Visualizacion de eventos disponibles.
- Visualizacion de sectores disponibles por evento.
- Venta de entradas con datos del comprador.
- Seleccion del recital antes de elegir el sector.
- Bloqueo de compra si todavia no se selecciono un evento.
- Compra limitada al evento seleccionado, sin cambiar de recital durante la operacion.
- Validacion de DNI, evento, sector, cantidad, promocion y medio de pago.
- Control de capacidad por sector y por evento.
- Calculo de subtotal, descuento y total a pagar.
- Registro de ventas activas.
- Guardado de ventas en el archivo `ventas.json`.
- Recuperacion de ventas anteriores al volver a ejecutar el programa.
- Cancelacion de ventas con liberacion de cupos.
- Listado de ventas realizadas.
- Estadisticas de ventas, recaudacion, ocupacion y sector mas demandado por evento.


## Requisitos tecnicos aplicados

- Condicionales: validacion de opciones, confirmaciones y estados.
- Estructuras repetitivas: menus, solicitudes de datos y recorridos de ventas.
- Funciones: separacion de responsabilidades por operacion.
- Validaciones: ingreso numerico, DNI, cupos disponibles y promociones.
- Acumuladores y contadores: calculo de recaudacion, entradas vendidas y estadisticas.
- Modularizacion basica: funciones para menu, ventas, calculos y estadisticas.
- Manejo basico de errores: uso de `try/except` para entradas numericas invalidas y lectura del archivo de ventas.
- Archivos: uso de `ventas.json` para guardar y recuperar las ventas.

## Instrucciones de ejecucion

### Opcion 1: abrir en una ventana nueva

En Windows, hacer doble clic sobre:

```text
Ejecutable.bat
```

Ese archivo abre una nueva ventana de consola y ejecuta el sistema.

### Opcion 2: ejecutar desde una terminal

1. Abrir una terminal en la carpeta del proyecto.
2. Ejecutar:

```bash
python main.py
```

3. Utilizar el menu principal para operar el sistema.

## Archivo de ventas

Las ventas se guardan automaticamente en:

```text
ventas.json
```

Cuando se confirma una compra o se cancela una venta, el archivo se actualiza. Al iniciar nuevamente el programa, se cargan las ventas anteriores y se recalculan los cupos ocupados de cada sector.

## Uso de Inteligencia Artificial

Se utilizó Codex como herramienta de apoyo durante el desarrollo del proyecto. La IA fue utilizada para generar una estructura inicial del sistema, proponer funciones, organizar la modularización, revisar validaciones, mejorar mensajes al usuario y colaborar en la documentación del README.

El código final fue revisado, probado y adaptado por el grupo. Todos los integrantes deben comprender la lógica implementada, las funciones utilizadas, las validaciones realizadas, el manejo de errores, los acumuladores, los contadores y el funcionamiento general del sistema.
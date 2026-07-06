# Trabajo Final Integrador - Python

## Escenario 9: Sistema de venta de entradas para recitales

Sistema por consola que permite administrar la venta de entradas para un recital. La solucion contempla seleccion de sectores, calculo de importes, control de capacidad, aplicacion de promociones o descuentos, registro de ventas y estadisticas basicas de demanda.

## Integrantes

- Caballero Lara
- Hanke Valentin
- Lazcano Francisco
- 

## Comision

AED 1.1

## Funcionalidades

- Visualizacion de sectores disponibles.
- Venta de entradas con datos del comprador.
- Validacion de DNI, sector, cantidad, promocion y medio de pago.
- Control de capacidad por sector.
- Calculo de subtotal, descuento y total a pagar.
- Registro de ventas activas.
- Guardado de ventas en el archivo `ventas.json`.
- Recuperacion de ventas anteriores al volver a ejecutar el programa.
- Cancelacion de ventas con liberacion de cupos.
- Listado de ventas realizadas.
- Estadisticas de ventas, recaudacion, ocupacion y sector mas demandado.

## Requisitos tecnicos aplicados

- Condicionales: validacion de opciones, confirmaciones y estados.
- Estructuras repetitivas: menus, solicitudes de datos y recorridos de ventas.
- Funciones: separacion de responsabilidades por operacion.
- Validaciones: ingreso numerico, DNI, cupos disponibles y promociones.
- Acumuladores y contadores: calculo de recaudacion, entradas vendidas y estadisticas.
- Modularizacion basica: funciones para menu, ventas, calculos y estadisticas.
- Manejo basico de errores: uso de `try/except` para entradas numericas invalidas y lectura del archivo de ventas.
- Archivos: uso de `ventas.json` para guardar y recuperar las ventas.

<<<<<<< HEAD
## Instrucciones de ejecucion

### Opcion 1: abrir en una ventana nueva

En Windows, hacer doble clic sobre:

```text
ejecutar_en_ventana.bat
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

## Caso de prueba valido sugerido

1. Elegir la opcion `2. Comprar entradas`.
2. Ingresar un nombre y apellido valido.
3. Ingresar un DNI de 7 u 8 numeros.
4. Elegir el sector `CAMPO`.
5. Comprar `4` entradas.
6. Seleccionar la promocion `Grupo 4 o mas entradas`.
7. Elegir un medio de pago.
8. Confirmar la venta con `S`.
9. Verificar la venta en la opcion `3` y las estadisticas en la opcion `4`.
10. Cerrar el programa, volver a abrirlo y comprobar que la venta sigue apareciendo.

## Caso de prueba con validacion

1. Intentar ingresar texto cuando el sistema pide una opcion numerica.
2. Intentar comprar mas entradas que las disponibles en un sector.
3. Intentar usar la promocion de grupo comprando menos de 4 entradas.
4. Verificar que el sistema muestre mensajes de error y vuelva a solicitar el dato.
=======
>>>>>>> d59277e751420b4db8e0b9ed5c7f336f940493ee

## Uso de Inteligencia Artificial

Se utilizo asistencia de IA como apoyo para organizar la estructura del programa, revisar alternativas de validacion, proponer casos de prueba y mejorar la claridad del codigo. La logica final debe ser comprendida y defendida por todos los integrantes del grupo.

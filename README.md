# Trabajo Final Integrador - Python

## Escenario 9: Sistema de venta de entradas para recitales

Sistema por consola que permite administrar la venta de entradas para un recital. La solucion contempla seleccion de sectores, calculo de importes, control de capacidad, aplicacion de promociones o descuentos, registro de ventas y estadisticas basicas de demanda.

## Integrantes

- Completar integrante 1
- Completar integrante 2
- Completar integrante 3

## Comision

Completar comision.

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

## Modalidad de trabajo segun la consigna

- El trabajo se realiza en grupos de 3 a 5 integrantes.
- El sistema debe estar desarrollado en Python y ejecutarse por consola.
- El repositorio debe mostrar el proceso de trabajo mediante commits periodicos, no solamente una carga final.
- La entrega digital debe incluir enlace al repositorio, archivo README y video de demostracion.
- El video debe durar como maximo 5 minutos e incluir presentacion breve del grupo, explicacion general del sistema, un caso valido y un caso con validaciones o mensajes de error.
- El uso de IA esta permitido como apoyo, pero todos los integrantes deben comprender y poder justificar la solucion.

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

## Uso de Inteligencia Artificial

Se utilizo asistencia de IA como apoyo para organizar la estructura del programa, revisar alternativas de validacion, proponer casos de prueba y mejorar la claridad del codigo. La logica final debe ser comprendida y defendida por todos los integrantes del grupo.

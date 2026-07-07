"""
Trabajo Final Integrador - Escenario 9
Sistema de venta de entradas para recitales.

Programa de consola desarrollado con estructuras basicas de Python:
diccionarios, listas, funciones, condicionales, ciclos, acumuladores,
contadores y validaciones.
"""

import json
import os
from pathlib import Path
from datetime import datetime


os.system("")

ARCHIVO_VENTAS = Path(__file__).with_name("ventas.json")

RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"


def color_texto(texto, color):
    return f"{color}{texto}{RESET}"

EVENTOS = {
    "ROCK": {
        "nombre": "Noche de Rock Nacional",
        "fecha": "15/08/2026",
        "lugar": "Estadio Ciudad",
        "sectores": {
            "CAMPO": {"nombre": "Campo", "precio": 18000.0, "capacidad": 120, "vendidas": 0},
            "PLATEA": {"nombre": "Platea", "precio": 25000.0, "capacidad": 80, "vendidas": 0},
            "VIP": {"nombre": "VIP", "precio": 42000.0, "capacidad": 30, "vendidas": 0},
        },
    },
    "POP": {
        "nombre": "Festival Pop Latino",
        "fecha": "22/08/2026",
        "lugar": "Arena Central",
        "sectores": {
            "GENERAL": {"nombre": "General", "precio": 15000.0, "capacidad": 150, "vendidas": 0},
            "PLATEA": {"nombre": "Platea", "precio": 23000.0, "capacidad": 90, "vendidas": 0},
            "VIP": {"nombre": "VIP", "precio": 38000.0, "capacidad": 40, "vendidas": 0},
        },
    },
    "INDIE": {
        "nombre": "Indie Session",
        "fecha": "05/09/2026",
        "lugar": "Teatro Sur",
        "sectores": {
            "PULLMAN": {"nombre": "Pullman", "precio": 12000.0, "capacidad": 60, "vendidas": 0},
            "PLATEA": {"nombre": "Platea", "precio": 16000.0, "capacidad": 70, "vendidas": 0},
            "PALCO": {"nombre": "Palco", "precio": 28000.0, "capacidad": 20, "vendidas": 0},
        },
    },
}

PROMOCIONES = {
    "NINGUNA": {"nombre": "Sin promocion", "descuento": 0.0},
    "ESTUDIANTE": {"nombre": "Estudiante", "descuento": 0.10},
    "GRUPO": {"nombre": "Grupo 4 o mas entradas", "descuento": 0.15},
    "CLUB": {"nombre": "Socio club de fans", "descuento": 0.20},
}

MEDIOS_PAGO = ["EFECTIVO", "DEBITO", "CREDITO", "TRANSFERENCIA"]
ventas = []


def cargar_ventas():
    if not ARCHIVO_VENTAS.exists():
        return []

    try:
        with open(ARCHIVO_VENTAS, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            if isinstance(datos, list):
                return datos
            print("Aviso: el archivo de ventas no tiene el formato esperado.")
            return []
    except json.JSONDecodeError:
        print("Aviso: no se pudo leer ventas.json porque contiene datos invalidos.")
        return []
    except OSError:
        print("Aviso: no se pudo acceder al archivo de ventas.")
        return []


def guardar_ventas():
    try:
        with open(ARCHIVO_VENTAS, "w", encoding="utf-8") as archivo:
            json.dump(ventas, archivo, indent=4, ensure_ascii=False)
    except OSError:
        print("Aviso: no se pudieron guardar las ventas en el archivo.")


def actualizar_cupos_desde_ventas():
    for evento in EVENTOS.values():
        for sector in evento["sectores"].values():
            sector["vendidas"] = 0

    for venta in ventas:
        evento = venta.get("evento")
        sector = venta.get("sector")
        estado = venta.get("estado")
        cantidad = venta.get("cantidad", 0)
        if estado == "ACTIVA" and evento in EVENTOS and sector in EVENTOS[evento]["sectores"]:
            EVENTOS[evento]["sectores"][sector]["vendidas"] += cantidad


def mostrar_titulo():
    print(color_texto("\n" + "=" * 60, CYAN))
    print(color_texto("SISTEMA DE VENTA DE ENTRADAS PARA RECITALES", BOLD + CYAN))
    print(color_texto("=" * 60, CYAN))
    print(color_texto("Boleteria de eventos musicales", MAGENTA))


def mostrar_menu(codigo_evento_actual=None):
    print(color_texto("\nMenu principal", BOLD + BLUE))
    if codigo_evento_actual:
        evento = EVENTOS[codigo_evento_actual]
        print(color_texto(f"Evento seleccionado: {evento['nombre']} ({evento['fecha']})", GREEN))
    else:
        print(color_texto("Evento seleccionado: ninguno", YELLOW))
    print(color_texto("1. Seleccionar evento y ver sectores disponibles", CYAN))
    print(color_texto("2. Comprar entradas para el evento seleccionado", CYAN))
    print("3. Ver ventas realizadas")
    print("4. Ver estadisticas")
    print("5. Cancelar una venta")
    print("6. Salir")


def pedir_opcion(minimo, maximo, mensaje="Ingrese una opcion: "):
    while True:
        try:
            opcion = int(input(mensaje))
            if minimo <= opcion <= maximo:
                return opcion
            print(color_texto(f"Error: ingrese un numero entre {minimo} y {maximo}.", RED))
        except ValueError:
            print(color_texto("Error: debe ingresar un numero entero.", RED))


def pedir_texto(mensaje, minimo=2):
    while True:
        texto = input(mensaje).strip()
        if len(texto) >= minimo:
            return texto
        print(color_texto(f"Error: el texto debe tener al menos {minimo} caracteres.", RED))


def pedir_dni():
    while True:
        dni = input("DNI del comprador: ").strip()
        if dni.isdigit() and 7 <= len(dni) <= 8:
            return dni
        print(color_texto("Error: el DNI debe contener 7 u 8 numeros.", RED))


def mostrar_eventos():
    print(color_texto("\nEventos disponibles", BOLD + MAGENTA))
    print(color_texto("-" * 75, MAGENTA))
    print(color_texto(f"{'Codigo':<10}{'Evento':<28}{'Fecha':<14}{'Lugar':<20}", BOLD))
    print(color_texto("-" * 75, MAGENTA))
    for codigo, evento in EVENTOS.items():
        print(f"{codigo:<10}{evento['nombre']:<28}{evento['fecha']:<14}{evento['lugar']:<20}")


def elegir_evento():
    while True:
        mostrar_eventos()
        codigo = input("Ingrese codigo de evento: ").strip().upper()
        if codigo in EVENTOS:
            return codigo
        print(color_texto("Error: evento inexistente.", RED))


def mostrar_sectores(codigo_evento):
    evento = EVENTOS[codigo_evento]
    print(color_texto("\nSectores disponibles", BOLD + MAGENTA))
    print(color_texto(f"Evento: {evento['nombre']} | Fecha: {evento['fecha']} | Lugar: {evento['lugar']}", GREEN))
    print(color_texto("-" * 60, MAGENTA))
    print(color_texto(f"{'Codigo':<10}{'Sector':<15}{'Precio':<12}{'Libres':<10}", BOLD))
    print(color_texto("-" * 60, MAGENTA))
    for codigo, sector in evento["sectores"].items():
        libres = sector["capacidad"] - sector["vendidas"]
        print(f"{codigo:<10}{sector['nombre']:<15}${sector['precio']:<11.2f}{libres:<10}")


def elegir_sector(codigo_evento):
    while True:
        mostrar_sectores(codigo_evento)
        codigo = input("Ingrese codigo de sector: ").strip().upper()
        if codigo in EVENTOS[codigo_evento]["sectores"]:
            if lugares_disponibles(codigo_evento, codigo) > 0:
                return codigo
            print(color_texto("Error: ese sector no tiene lugares disponibles.", RED))
        else:
            print(color_texto("Error: sector inexistente.", RED))


def lugares_disponibles(codigo_evento, codigo_sector):
    sector = EVENTOS[codigo_evento]["sectores"][codigo_sector]
    return sector["capacidad"] - sector["vendidas"]


def pedir_cantidad(codigo_evento, codigo_sector):
    disponibles = lugares_disponibles(codigo_evento, codigo_sector)
    while True:
        try:
            cantidad = int(input(f"Cantidad de entradas (1 a {disponibles}): "))
            if 1 <= cantidad <= disponibles:
                return cantidad
            print(color_texto("Error: cantidad invalida o superior a la capacidad disponible.", RED))
        except ValueError:
            print(color_texto("Error: debe ingresar un numero entero.", RED))


def mostrar_promociones():
    print(color_texto("\nPromociones", BOLD + BLUE))
    codigos = list(PROMOCIONES.keys())
    for indice, codigo in enumerate(codigos, start=1):
        promo = PROMOCIONES[codigo]
        porcentaje = int(promo["descuento"] * 100)
        print(f"{indice}. {promo['nombre']} ({porcentaje}% descuento)")
    return codigos


def elegir_promocion(cantidad):
    codigos = mostrar_promociones()
    while True:
        opcion = pedir_opcion(1, len(codigos), "Seleccione promocion: ")
        codigo = codigos[opcion - 1]
        if codigo == "GRUPO" and cantidad < 4:
            print(color_texto("Error: la promocion de grupo requiere comprar 4 o mas entradas.", RED))
        else:
            return codigo


def elegir_medio_pago():
    print(color_texto("\nMedios de pago", BOLD + BLUE))
    for indice, medio in enumerate(MEDIOS_PAGO, start=1):
        print(f"{indice}. {medio.title()}")
    opcion = pedir_opcion(1, len(MEDIOS_PAGO), "Seleccione medio de pago: ")
    return MEDIOS_PAGO[opcion - 1]


def calcular_importes(codigo_evento, codigo_sector, cantidad, codigo_promocion):
    precio_unitario = EVENTOS[codigo_evento]["sectores"][codigo_sector]["precio"]
    subtotal = precio_unitario * cantidad
    descuento = subtotal * PROMOCIONES[codigo_promocion]["descuento"]
    total = subtotal - descuento
    return subtotal, descuento, total


def generar_codigo_venta():
    return f"V{len(ventas) + 1:04d}"


def comprar_entradas(codigo_evento):
    print(color_texto("\nNueva venta", BOLD + GREEN))
    evento = EVENTOS[codigo_evento]
    print(color_texto(f"Evento seleccionado: {evento['nombre']}", GREEN))
    print(color_texto(f"Fecha: {evento['fecha']} | Lugar: {evento['lugar']}", GREEN))
    comprador = pedir_texto("Nombre y apellido del comprador: ")
    dni = pedir_dni()
    codigo_sector = elegir_sector(codigo_evento)
    cantidad = pedir_cantidad(codigo_evento, codigo_sector)
    codigo_promocion = elegir_promocion(cantidad)
    medio_pago = elegir_medio_pago()

    subtotal, descuento, total = calcular_importes(codigo_evento, codigo_sector, cantidad, codigo_promocion)

    print(color_texto("\nResumen de compra", BOLD + YELLOW))
    print(f"Comprador: {comprador} | DNI: {dni}")
    print(f"Evento: {EVENTOS[codigo_evento]['nombre']}")
    print(f"Fecha: {EVENTOS[codigo_evento]['fecha']} | Lugar: {EVENTOS[codigo_evento]['lugar']}")
    print(f"Sector: {EVENTOS[codigo_evento]['sectores'][codigo_sector]['nombre']}")
    print(f"Cantidad: {cantidad}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Descuento: ${descuento:.2f}")
    print(f"Total a pagar: ${total:.2f}")

    confirmar = input("Confirmar venta? (S/N): ").strip().upper()
    if confirmar != "S":
        print(color_texto("Venta cancelada por el usuario.", YELLOW))
        return

    venta = {
        "codigo": generar_codigo_venta(),
        "fecha_hora": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "comprador": comprador,
        "dni": dni,
        "evento": codigo_evento,
        "sector": codigo_sector,
        "cantidad": cantidad,
        "promocion": codigo_promocion,
        "medio_pago": medio_pago,
        "subtotal": subtotal,
        "descuento": descuento,
        "total": total,
        "estado": "ACTIVA",
    }
    ventas.append(venta)
    EVENTOS[codigo_evento]["sectores"][codigo_sector]["vendidas"] += cantidad
    guardar_ventas()
    print(color_texto(f"Venta registrada correctamente. Codigo: {venta['codigo']}", GREEN))


def listar_ventas():
    print(color_texto("\nVentas realizadas", BOLD + BLUE))
    if not ventas:
        print(color_texto("No hay ventas registradas.", YELLOW))
        return

    for venta in ventas:
        codigo_evento = venta.get("evento")
        codigo_sector = venta.get("sector")
        evento = EVENTOS.get(codigo_evento, {"nombre": "Evento no disponible"})
        sectores = evento.get("sectores", {})
        sector = sectores.get(codigo_sector, {"nombre": "Sector no disponible"})["nombre"]
        promo = PROMOCIONES[venta["promocion"]]["nombre"]
        print("-" * 60)
        print(f"Codigo: {venta['codigo']} | Estado: {venta['estado']}")
        print(f"Fecha: {venta['fecha_hora']}")
        print(f"Comprador: {venta['comprador']} | DNI: {venta['dni']}")
        print(f"Evento: {evento['nombre']}")
        print(f"Sector: {sector} | Cantidad: {venta['cantidad']}")
        print(f"Promocion: {promo} | Pago: {venta['medio_pago'].title()}")
        print(f"Total: ${venta['total']:.2f}")


def cancelar_venta():
    if not ventas:
        print(color_texto("\nNo hay ventas para cancelar.", YELLOW))
        return

    listar_ventas()
    codigo = input("\nIngrese codigo de venta a cancelar: ").strip().upper()
    for venta in ventas:
        if venta["codigo"] == codigo:
            if venta["estado"] == "CANCELADA":
                print(color_texto("Error: esa venta ya estaba cancelada.", RED))
                return
            venta["estado"] = "CANCELADA"
            codigo_evento = venta.get("evento")
            codigo_sector = venta.get("sector")
            if codigo_evento in EVENTOS and codigo_sector in EVENTOS[codigo_evento]["sectores"]:
                EVENTOS[codigo_evento]["sectores"][codigo_sector]["vendidas"] -= venta["cantidad"]
            guardar_ventas()
            print(color_texto("Venta cancelada y cupos liberados correctamente.", GREEN))
            return
    print(color_texto("Error: no se encontro una venta con ese codigo.", RED))


def obtener_ventas_activas():
    return [venta for venta in ventas if venta["estado"] == "ACTIVA"]


def calcular_sector_mas_demandado(ventas_activas):
    cantidades = {}
    for codigo_evento, evento in EVENTOS.items():
        for codigo_sector in evento["sectores"]:
            cantidades[(codigo_evento, codigo_sector)] = 0

    for venta in ventas_activas:
        clave = (venta.get("evento"), venta.get("sector"))
        if clave in cantidades:
            cantidades[clave] += venta["cantidad"]

    clave_mayor = None
    mayor_cantidad = -1
    for clave, cantidad in cantidades.items():
        if cantidad > mayor_cantidad:
            clave_mayor = clave
            mayor_cantidad = cantidad
    return clave_mayor, mayor_cantidad


def mostrar_estadisticas():
    ventas_activas = obtener_ventas_activas()
    print(color_texto("\nEstadisticas de ventas", BOLD + BLUE))
    print(color_texto("-" * 60, BLUE))
    if not ventas_activas:
        print(color_texto("Todavia no hay ventas activas para analizar.", YELLOW))
        return

    entradas_vendidas = 0
    recaudacion_total = 0.0
    descuento_total = 0.0

    for venta in ventas_activas:
        entradas_vendidas += venta["cantidad"]
        recaudacion_total += venta["total"]
        descuento_total += venta["descuento"]

    capacidad_total = 0
    for evento in EVENTOS.values():
        for sector in evento["sectores"].values():
            capacidad_total += sector["capacidad"]

    porcentaje_ocupacion = entradas_vendidas * 100 / capacidad_total
    sector_mas_demandado, cantidad_sector = calcular_sector_mas_demandado(ventas_activas)
    codigo_evento_mayor, codigo_sector_mayor = sector_mas_demandado
    evento_mayor = EVENTOS[codigo_evento_mayor]
    sector_mayor = evento_mayor["sectores"][codigo_sector_mayor]

    print(f"Ventas activas: {len(ventas_activas)}")
    print(f"Entradas vendidas: {entradas_vendidas} de {capacidad_total}")
    print(f"Ocupacion total: {porcentaje_ocupacion:.2f}%")
    print(f"Recaudacion total: ${recaudacion_total:.2f}")
    print(f"Descuentos aplicados: ${descuento_total:.2f}")
    print(
        "Sector mas demandado: "
        f"{evento_mayor['nombre']} - {sector_mayor['nombre']} ({cantidad_sector} entradas)"
    )

    print(color_texto("\nDetalle por evento y sector", BOLD + MAGENTA))
    for evento in EVENTOS.values():
        print(color_texto(f"\n{evento['nombre']} ({evento['fecha']} - {evento['lugar']})", MAGENTA))
        for sector in evento["sectores"].values():
            vendidas = sector["vendidas"]
            libres = sector["capacidad"] - vendidas
            ocupacion = vendidas * 100 / sector["capacidad"]
            print(
                f"{sector['nombre']:<10} | Vendidas: {vendidas:<3} "
                f"| Libres: {libres:<3} | Ocupacion: {ocupacion:.2f}%"
            )


def ejecutar_sistema():
    ventas.extend(cargar_ventas())
    actualizar_cupos_desde_ventas()
    mostrar_titulo()
    print(f"Archivo de ventas: {ARCHIVO_VENTAS.name}")
    codigo_evento_actual = None
    while True:
        mostrar_menu(codigo_evento_actual)
        opcion = pedir_opcion(1, 6)

        if opcion == 1:
            codigo_evento_actual = elegir_evento()
            mostrar_sectores(codigo_evento_actual)
        elif opcion == 2:
            if codigo_evento_actual is None:
                print(color_texto("\nPrimero debe seleccionar un evento desde la opcion 1.", YELLOW))
            else:
                comprar_entradas(codigo_evento_actual)
        elif opcion == 3:
            listar_ventas()
        elif opcion == 4:
            mostrar_estadisticas()
        elif opcion == 5:
            cancelar_venta()
        elif opcion == 6:
            print(color_texto("Gracias por utilizar el sistema. Hasta luego.", GREEN))
            break


if __name__ == "__main__":
    ejecutar_sistema()

"""
Trabajo Final Integrador - Escenario 9
Sistema de venta de entradas para recitales.

Programa de consola desarrollado con estructuras basicas de Python:
diccionarios, listas, funciones, condicionales, ciclos, acumuladores,
contadores y validaciones.
"""

import json
from pathlib import Path
from datetime import datetime


ARCHIVO_VENTAS = Path(__file__).with_name("ventas.json")

EVENTO = {
    "nombre": "Noche de Rock Nacional",
    "fecha": "15/08/2026",
    "lugar": "Estadio Ciudad",
}

SECTORES = {
    "CAMPO": {"nombre": "Campo", "precio": 18000.0, "capacidad": 120, "vendidas": 0},
    "PLATEA": {"nombre": "Platea", "precio": 25000.0, "capacidad": 80, "vendidas": 0},
    "VIP": {"nombre": "VIP", "precio": 42000.0, "capacidad": 30, "vendidas": 0},
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
    for sector in SECTORES.values():
        sector["vendidas"] = 0

    for venta in ventas:
        sector = venta.get("sector")
        estado = venta.get("estado")
        cantidad = venta.get("cantidad", 0)
        if estado == "ACTIVA" and sector in SECTORES:
            SECTORES[sector]["vendidas"] += cantidad


def mostrar_titulo():
    print("\n" + "=" * 60)
    print("SISTEMA DE VENTA DE ENTRADAS PARA RECITALES")
    print("=" * 60)
    print(f"Evento: {EVENTO['nombre']}")
    print(f"Fecha: {EVENTO['fecha']} | Lugar: {EVENTO['lugar']}")


def mostrar_menu():
    print("\nMenu principal")
    print("1. Ver sectores disponibles")
    print("2. Comprar entradas")
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
            print(f"Error: ingrese un numero entre {minimo} y {maximo}.")
        except ValueError:
            print("Error: debe ingresar un numero entero.")


def pedir_texto(mensaje, minimo=2):
    while True:
        texto = input(mensaje).strip()
        if len(texto) >= minimo:
            return texto
        print(f"Error: el texto debe tener al menos {minimo} caracteres.")


def pedir_dni():
    while True:
        dni = input("DNI del comprador: ").strip()
        if dni.isdigit() and 7 <= len(dni) <= 8:
            return dni
        print("Error: el DNI debe contener 7 u 8 numeros.")


def mostrar_sectores():
    print("\nSectores disponibles")
    print("-" * 60)
    print(f"{'Codigo':<10}{'Sector':<15}{'Precio':<12}{'Libres':<10}")
    print("-" * 60)
    for codigo, sector in SECTORES.items():
        libres = sector["capacidad"] - sector["vendidas"]
        print(f"{codigo:<10}{sector['nombre']:<15}${sector['precio']:<11.2f}{libres:<10}")


def elegir_sector():
    while True:
        mostrar_sectores()
        codigo = input("Ingrese codigo de sector: ").strip().upper()
        if codigo in SECTORES:
            if lugares_disponibles(codigo) > 0:
                return codigo
            print("Error: ese sector no tiene lugares disponibles.")
        else:
            print("Error: sector inexistente.")


def lugares_disponibles(codigo_sector):
    sector = SECTORES[codigo_sector]
    return sector["capacidad"] - sector["vendidas"]


def pedir_cantidad(codigo_sector):
    disponibles = lugares_disponibles(codigo_sector)
    while True:
        try:
            cantidad = int(input(f"Cantidad de entradas (1 a {disponibles}): "))
            if 1 <= cantidad <= disponibles:
                return cantidad
            print("Error: cantidad invalida o superior a la capacidad disponible.")
        except ValueError:
            print("Error: debe ingresar un numero entero.")


def mostrar_promociones():
    print("\nPromociones")
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
            print("Error: la promocion de grupo requiere comprar 4 o mas entradas.")
        else:
            return codigo


def elegir_medio_pago():
    print("\nMedios de pago")
    for indice, medio in enumerate(MEDIOS_PAGO, start=1):
        print(f"{indice}. {medio.title()}")
    opcion = pedir_opcion(1, len(MEDIOS_PAGO), "Seleccione medio de pago: ")
    return MEDIOS_PAGO[opcion - 1]


def calcular_importes(codigo_sector, cantidad, codigo_promocion):
    precio_unitario = SECTORES[codigo_sector]["precio"]
    subtotal = precio_unitario * cantidad
    descuento = subtotal * PROMOCIONES[codigo_promocion]["descuento"]
    total = subtotal - descuento
    return subtotal, descuento, total


def generar_codigo_venta():
    return f"V{len(ventas) + 1:04d}"


def comprar_entradas():
    print("\nNueva venta")
    comprador = pedir_texto("Nombre y apellido del comprador: ")
    dni = pedir_dni()
    codigo_sector = elegir_sector()
    cantidad = pedir_cantidad(codigo_sector)
    codigo_promocion = elegir_promocion(cantidad)
    medio_pago = elegir_medio_pago()

    subtotal, descuento, total = calcular_importes(codigo_sector, cantidad, codigo_promocion)

    print("\nResumen de compra")
    print(f"Comprador: {comprador} | DNI: {dni}")
    print(f"Sector: {SECTORES[codigo_sector]['nombre']}")
    print(f"Cantidad: {cantidad}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Descuento: ${descuento:.2f}")
    print(f"Total a pagar: ${total:.2f}")

    confirmar = input("Confirmar venta? (S/N): ").strip().upper()
    if confirmar != "S":
        print("Venta cancelada por el usuario.")
        return

    venta = {
        "codigo": generar_codigo_venta(),
        "fecha_hora": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "comprador": comprador,
        "dni": dni,
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
    SECTORES[codigo_sector]["vendidas"] += cantidad
    guardar_ventas()
    print(f"Venta registrada correctamente. Codigo: {venta['codigo']}")


def listar_ventas():
    print("\nVentas realizadas")
    if not ventas:
        print("No hay ventas registradas.")
        return

    for venta in ventas:
        sector = SECTORES[venta["sector"]]["nombre"]
        promo = PROMOCIONES[venta["promocion"]]["nombre"]
        print("-" * 60)
        print(f"Codigo: {venta['codigo']} | Estado: {venta['estado']}")
        print(f"Fecha: {venta['fecha_hora']}")
        print(f"Comprador: {venta['comprador']} | DNI: {venta['dni']}")
        print(f"Sector: {sector} | Cantidad: {venta['cantidad']}")
        print(f"Promocion: {promo} | Pago: {venta['medio_pago'].title()}")
        print(f"Total: ${venta['total']:.2f}")


def cancelar_venta():
    if not ventas:
        print("\nNo hay ventas para cancelar.")
        return

    listar_ventas()
    codigo = input("\nIngrese codigo de venta a cancelar: ").strip().upper()
    for venta in ventas:
        if venta["codigo"] == codigo:
            if venta["estado"] == "CANCELADA":
                print("Error: esa venta ya estaba cancelada.")
                return
            venta["estado"] = "CANCELADA"
            SECTORES[venta["sector"]]["vendidas"] -= venta["cantidad"]
            guardar_ventas()
            print("Venta cancelada y cupos liberados correctamente.")
            return
    print("Error: no se encontro una venta con ese codigo.")


def obtener_ventas_activas():
    return [venta for venta in ventas if venta["estado"] == "ACTIVA"]


def calcular_sector_mas_demandado(ventas_activas):
    cantidades = {}
    for codigo in SECTORES:
        cantidades[codigo] = 0
    for venta in ventas_activas:
        cantidades[venta["sector"]] += venta["cantidad"]

    codigo_mayor = None
    mayor_cantidad = -1
    for codigo, cantidad in cantidades.items():
        if cantidad > mayor_cantidad:
            codigo_mayor = codigo
            mayor_cantidad = cantidad
    return codigo_mayor, mayor_cantidad


def mostrar_estadisticas():
    ventas_activas = obtener_ventas_activas()
    print("\nEstadisticas de ventas")
    print("-" * 60)
    if not ventas_activas:
        print("Todavia no hay ventas activas para analizar.")
        return

    entradas_vendidas = 0
    recaudacion_total = 0.0
    descuento_total = 0.0

    for venta in ventas_activas:
        entradas_vendidas += venta["cantidad"]
        recaudacion_total += venta["total"]
        descuento_total += venta["descuento"]

    capacidad_total = sum(sector["capacidad"] for sector in SECTORES.values())
    porcentaje_ocupacion = entradas_vendidas * 100 / capacidad_total
    sector_mas_demandado, cantidad_sector = calcular_sector_mas_demandado(ventas_activas)

    print(f"Ventas activas: {len(ventas_activas)}")
    print(f"Entradas vendidas: {entradas_vendidas} de {capacidad_total}")
    print(f"Ocupacion total: {porcentaje_ocupacion:.2f}%")
    print(f"Recaudacion total: ${recaudacion_total:.2f}")
    print(f"Descuentos aplicados: ${descuento_total:.2f}")
    print(
        "Sector mas demandado: "
        f"{SECTORES[sector_mas_demandado]['nombre']} ({cantidad_sector} entradas)"
    )

    print("\nDetalle por sector")
    for codigo, sector in SECTORES.items():
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
    while True:
        mostrar_menu()
        opcion = pedir_opcion(1, 6)

        if opcion == 1:
            mostrar_sectores()
        elif opcion == 2:
            comprar_entradas()
        elif opcion == 3:
            listar_ventas()
        elif opcion == 4:
            mostrar_estadisticas()
        elif opcion == 5:
            cancelar_venta()
        elif opcion == 6:
            print("Gracias por utilizar el sistema. Hasta luego.")
            break


if __name__ == "__main__":
    ejecutar_sistema()

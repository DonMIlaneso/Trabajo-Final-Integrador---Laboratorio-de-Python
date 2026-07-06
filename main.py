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
    print("\n" + "=" * 60)
    print("SISTEMA DE VENTA DE ENTRADAS PARA RECITALES")
    print("=" * 60)
    print("Boleteria de eventos musicales")


def mostrar_menu(codigo_evento_actual=None):
    print("\nMenu principal")
    if codigo_evento_actual:
        evento = EVENTOS[codigo_evento_actual]
        print(f"Evento seleccionado: {evento['nombre']} ({evento['fecha']})")
    else:
        print("Evento seleccionado: ninguno")
    print("1. Seleccionar evento y ver sectores disponibles")
    print("2. Comprar entradas para el evento seleccionado")
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


def mostrar_eventos():
    print("\nEventos disponibles")
    print("-" * 75)
    print(f"{'Codigo':<10}{'Evento':<28}{'Fecha':<14}{'Lugar':<20}")
    print("-" * 75)
    for codigo, evento in EVENTOS.items():
        print(f"{codigo:<10}{evento['nombre']:<28}{evento['fecha']:<14}{evento['lugar']:<20}")


def elegir_evento():
    while True:
        mostrar_eventos()
        codigo = input("Ingrese codigo de evento: ").strip().upper()
        if codigo in EVENTOS:
            return codigo
        print("Error: evento inexistente.")


def mostrar_sectores(codigo_evento):
    evento = EVENTOS[codigo_evento]
    print("\nSectores disponibles")
    print(f"Evento: {evento['nombre']} | Fecha: {evento['fecha']} | Lugar: {evento['lugar']}")
    print("-" * 60)
    print(f"{'Codigo':<10}{'Sector':<15}{'Precio':<12}{'Libres':<10}")
    print("-" * 60)
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
            print("Error: ese sector no tiene lugares disponibles.")
        else:
            print("Error: sector inexistente.")


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


def calcular_importes(codigo_evento, codigo_sector, cantidad, codigo_promocion):
    precio_unitario = EVENTOS[codigo_evento]["sectores"][codigo_sector]["precio"]
    subtotal = precio_unitario * cantidad
    descuento = subtotal * PROMOCIONES[codigo_promocion]["descuento"]
    total = subtotal - descuento
    return subtotal, descuento, total


def generar_codigo_venta():
    return f"V{len(ventas) + 1:04d}"


def comprar_entradas(codigo_evento):
    print("\nNueva venta")
    evento = EVENTOS[codigo_evento]
    print(f"Evento seleccionado: {evento['nombre']}")
    print(f"Fecha: {evento['fecha']} | Lugar: {evento['lugar']}")
    comprador = pedir_texto("Nombre y apellido del comprador: ")
    dni = pedir_dni()
    codigo_sector = elegir_sector(codigo_evento)
    cantidad = pedir_cantidad(codigo_evento, codigo_sector)
    codigo_promocion = elegir_promocion(cantidad)
    medio_pago = elegir_medio_pago()

    subtotal, descuento, total = calcular_importes(codigo_evento, codigo_sector, cantidad, codigo_promocion)

    print("\nResumen de compra")
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
        print("Venta cancelada por el usuario.")
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
    print(f"Venta registrada correctamente. Codigo: {venta['codigo']}")


def listar_ventas():
    print("\nVentas realizadas")
    if not ventas:
        print("No hay ventas registradas.")
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
            codigo_evento = venta.get("evento")
            codigo_sector = venta.get("sector")
            if codigo_evento in EVENTOS and codigo_sector in EVENTOS[codigo_evento]["sectores"]:
                EVENTOS[codigo_evento]["sectores"][codigo_sector]["vendidas"] -= venta["cantidad"]
            guardar_ventas()
            print("Venta cancelada y cupos liberados correctamente.")
            return
    print("Error: no se encontro una venta con ese codigo.")


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

    print("\nDetalle por evento y sector")
    for evento in EVENTOS.values():
        print(f"\n{evento['nombre']} ({evento['fecha']} - {evento['lugar']})")
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
                print("\nPrimero debe seleccionar un evento desde la opcion 1.")
            else:
                comprar_entradas(codigo_evento_actual)
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

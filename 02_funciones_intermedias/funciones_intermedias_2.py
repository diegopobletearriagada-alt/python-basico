# Lista de ventas original
ventas = [
    {"fecha": "2024-01-01", "producto": "Notebook", "cantidad": 2, "precio": 850000.0},
    {"fecha": "2024-01-01", "producto": "Mouse", "cantidad": 5, "precio": 12000.0},
    {"fecha": "2024-01-02", "producto": "Teclado", "cantidad": 3, "precio": 25000.0},
    {"fecha": "2024-01-02", "producto": "Mouse", "cantidad": 4, "precio": 12000.0},
    {"fecha": "2024-01-03", "producto": "Notebook", "cantidad": 1, "precio": 850000.0},
    {"fecha": "2024-01-03", "producto": "Monitor", "cantidad": 2, "precio": 180000.0}
]

# 1. Cálculo de ingresos totales
ingresos_totales = 0

for venta in ventas:
    ingresos_totales += venta["cantidad"] * venta["precio"]

# 2. Análisis del producto más vendido
ventas_por_producto = {}

for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]

    if producto in ventas_por_producto:
        ventas_por_producto[producto] += cantidad
    else:
        ventas_por_producto[producto] = cantidad

producto_mas_vendido = ""
cantidad_mas_vendida = 0

for producto in ventas_por_producto:
    if ventas_por_producto[producto] > cantidad_mas_vendida:
        producto_mas_vendido = producto
        cantidad_mas_vendida = ventas_por_producto[producto]

# 3. Promedio de precio por producto
precios_por_producto = {}

for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    precio = venta["precio"]

    suma_precios = precio * cantidad

    if producto in precios_por_producto:
        suma_actual, cantidad_actual = precios_por_producto[producto]
        precios_por_producto[producto] = (suma_actual + suma_precios, cantidad_actual + cantidad)
    else:
        precios_por_producto[producto] = (suma_precios, cantidad)

promedio_precio_por_producto = {}

for producto in precios_por_producto:
    suma_total, cantidad_total = precios_por_producto[producto]
    promedio_precio_por_producto[producto] = suma_total / cantidad_total

# 4. Ventas por día
ingresos_por_dia = {}

for venta in ventas:
    fecha = venta["fecha"]
    ingreso = venta["cantidad"] * venta["precio"]

    if fecha in ingresos_por_dia:
        ingresos_por_dia[fecha] += ingreso
    else:
        ingresos_por_dia[fecha] = ingreso

# 5. Resumen de ventas por producto
resumen_ventas = {}

for producto in ventas_por_producto:
    resumen_ventas[producto] = {
        "cantidad_total": ventas_por_producto[producto],
        "ingresos_totales": precios_por_producto[producto][0],
        "precio_promedio": promedio_precio_por_producto[producto]
    }

# Mostrar resultados
print("LISTA DE VENTAS ORIGINAL")
for venta in ventas:
    print(venta)

print("\nINGRESOS TOTALES GENERADOS")
print(ingresos_totales)

print("\nPRODUCTO MÁS VENDIDO Y SU CANTIDAD TOTAL VENDIDA")
print(producto_mas_vendido, "-", cantidad_mas_vendida)

print("\nPRECIO PROMEDIO DE VENTA POR PRODUCTO")
for producto in promedio_precio_por_producto:
    print(producto, "-", promedio_precio_por_producto[producto])

print("\nINGRESOS TOTALES POR DÍA")
for fecha in ingresos_por_dia:
    print(fecha, "-", ingresos_por_dia[fecha])

print("\nRESUMEN DE VENTAS POR PRODUCTO")
for producto in resumen_ventas:
    print(producto, "-", resumen_ventas[producto])
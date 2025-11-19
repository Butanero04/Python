
precio_articulo = float(input("Introduce el precio del artuculo: "))
precio_venta = float(input("Introduce el precio de venta real: "))

descuento = ((precio_articulo - precio_venta) / precio_articulo) * 100

print("El porcentaje de descuento realizado es:", descuento, "%")
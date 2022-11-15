# Escribir un programa que guarde en un diccionario los precios de los artículos de
# la tabla, pregunte al usuario por un artículo, un número de unidades y muestre por
# pantalla el precio de esa cantidad de producto.
# Si el producto no está en el diccionario debe mostrar un mensaje informando de ello.
productos_venta = {'pan':1.40, 'huevos':2.30, 'cebolla':0.85, 'aceite':4.35}
producto = input("indica el producto\n")
cantidad = float(input("cuantos compras\n"))
if producto in productos_venta:
    print(cantidad*productos_venta[producto])
else:
    print("ese producto no esta a la venta")
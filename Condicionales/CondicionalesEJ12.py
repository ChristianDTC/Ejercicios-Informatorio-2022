#12. Hacer un programa que imprima el nombre de un artículo, clave, precio original
#y su precio con descuento. El descuento lo hace en base a la clave, si la clave es
#01 el descuento es del 10% y si la clave es 02 el descuento en del 20% (solo
#existen dos claves).

print ("Ingrese el Nombre del Artículo: ")
nombrearticulo = input()

print ("Ingrese la Clave 01 - 02: ")
clave = input()

print ("Ingrese su Precio:")
preciooriginal = float ( input())

if clave == "01" or clave == "1":
    print (nombrearticulo.upper())
    print ("Clave: 01" )
    print (f"Precio Original ${preciooriginal}")
    print (f"Precio con Descuento {round(preciooriginal*(1-0.1),2)}")
elif clave == "02" or clave == "2":
    print (nombrearticulo.upper())
    print ("Clave: 02")
    print (f"Precio Original ${preciooriginal}")
    print (f"Precio con Descuento {round(preciooriginal*(1-0.2),2)}")


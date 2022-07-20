#Una distribuidora de libros vende a librerías y a particulares. Aplica
#bonificaciones por cantidad según el siguiente criterio:
#i. a librerías: hasta 24 unidades, el 20%; más de 24 unidades, el 25%.
#ii. a particulares: menos de 6 unidades, nada; desde 6 hasta 18
#unidades, el 5% y más de 18 unidades, el 10%.
#El tipo de cliente está codificado así: 'L' para librerías, 'P' para particular.
#Dado el importe bruto de una compra de libros, el tipo de cliente de que se
#trata y la cantidad total pedida por el mismo, determinar el importe bruto
#bonificado.


print ("Ingrese el Tipo de Cliente:")
print ("L = Librerira")
print ("P - Particular")
tipocliente = input()

print ("Ingrese la Cantidad de Libros a Comprar:")
cantidadlibros = int (input())

print ("Ingrese el Monto Total de la Compra:")
montocompra = float (input())

if tipocliente.upper() == "L":
    if cantidadlibros <=24:
        descuento = montocompra * 0.2
    elif cantidadlibros > 24:
        descuento = montocompra * 0.25

elif tipocliente.upper() == "P":
    if cantidadlibros <=18 and cantidadlibros >=6:
        descuento = montocompra * 0.05
    elif cantidadlibros > 18:
        descuento = montocompra * 0.1
    else:
        descuento = 0

print (f"El Precio a Pagar es de ${round(montocompra-descuento)}")
print (f"El Descuento Obtenido es de: ${round(descuento)}")

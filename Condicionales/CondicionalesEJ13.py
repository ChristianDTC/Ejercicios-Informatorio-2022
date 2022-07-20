#En un supermercado se hace una promoción, mediante la cual el cliente
#obtiene un descuento dependiendo de un número que se escoge al azar. Si el
#numero escogido es menor que 74 el descuento es del 15% sobre el total de la
#compra, si es mayor o igual a 74 el descuento es del 20%. Obtener cuánto
#dinero se le descuenta.

print ("Ingrese el Monto de la Compra:")
montocompra = float (input())

print ("Ingrese el Número Elegido por el Cliente:")
numeroelegido = int ( input())

if numeroelegido < 74:
    print (f"Se le Descontará ${round(montocompra*0.15)} del Total de la Compra")
elif numeroelegido >= 74:
    print (f"Se le Descontará ${round(montocompra*0.2)} del Total de la Compra")


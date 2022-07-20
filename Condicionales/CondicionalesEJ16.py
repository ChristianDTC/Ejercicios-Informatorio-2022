#16. Hacer un programa que calcule el total a pagar por la compra de camisas. Si se
#compran tres camisas o mas se aplica un descuento del 20% sobre el total de la
#compra y si son menos de tres camisas un descuento del 10%.


print ("Ingrese el Monto de la Compra:")
montocompra = float (input())

print ("Ingrese la Cantidad de Camisas a Comprar:")
cantidadcamisas = int ( input())

if cantidadcamisas < 3:
    print (f"El Total a Pagar es de: ${round(montocompra*(1-0.1),2)}")
elif cantidadcamisas >= 3:
    print (f"El Total a Pagar es de: ${round(montocompra*(1-0.2),2)}")


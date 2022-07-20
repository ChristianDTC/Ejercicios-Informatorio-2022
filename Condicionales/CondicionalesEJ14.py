#14. Leer 2 números; si son iguales que los multiplique, si el primero es mayor que
#el segundo que los reste y si no que los sume.

print ("Ingrese un Número:")
numero1 = float ( input())

print ("Ingrese un Número:")
numero2 = float ( input())

if numero1 == numero2:
    print ("Son Iguales")
    print (round(numero1 * numero2))
elif numero1 > numero2:
    print ("El Primero es Mayor que el Segundo")
    print (round(numero1 - numero2))
else:
    print ("Todos los Demás")
    print (round(numero1 + numero2))

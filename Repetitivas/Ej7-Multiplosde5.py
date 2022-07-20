#7) Realizar un programa que calcule y muestre la suma de los múltiplos de 5 
# comprendidos entre dos valores A y B. El programa no permitirá introducir valores negativos para A y B
# y verificará que A es menor que B. Si A es mayor que B, se deben intercambiar los valores.

import os
suma_multiplos_5 = 0

while (True): #solicito primer número

    print ("Ingrese un Número Posivito:")
    primer_numero = int(input())

    os.system("cls")

    if primer_numero > -1: #controlo que sea un número positivo
        break
    else:
        print ("NO PUEDE UTILIZAR NUMEROS NEGATIVOS") #sino se avisa y vuelve a pedir un número
        print()


while (True): #solicito primer número

    print ("Ingrese un Número Posivito:")
    segundo_numero = int(input())

    os.system("cls")

    if segundo_numero > -1: #controlo que sea un número positivo
        break
    else:
        print ("NO PUEDE UTILIZAR NUMEROS NEGATIVOS") #sino se avisa y vuelve a pedir un número
        print()


if primer_numero > segundo_numero: #controlo que el primer valor se el menor, sino los intercambio
    cambiar_valor = primer_numero
    primer_numero = segundo_numero
    segundo_numero = cambiar_valor

rango = segundo_numero - primer_numero

for x in range (rango+1): #recorro el rango dado buscando los multiplos de 5
    
    if (x + primer_numero) % 5 == 0 and (x + primer_numero) != 0:
        suma_multiplos_5 += (primer_numero + x)
        print(primer_numero + x)



print ("La Suma de los Números Multiplos de 5 en el Rango Brindado es de:")
print(suma_multiplos_5)

print()

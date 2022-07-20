#3) Diseñar un programa que permita obtener el producto entre A y Bmediante sumas sucesivas.

import os
multiplicacion = 0

print("Ingrese el Número a Multiplicar:")
numero1 = int(input())

print()

print("Ingrese el Número a Multiplicar:")
numero2 = int(input())

os.system("cls")

for x in range(numero2):
    multiplicacion += numero1

print(f"El Resultado de la Multiplicación de {numero1} por {numero2} es de :")
print(multiplicacion)

print()

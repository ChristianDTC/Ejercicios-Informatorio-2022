#2) Desarrollar una solución que calcule la suma de los cuadrados de los
# n primeros números naturales: 1 + 22 + 32 +… + n2.

import os
suma_cuadrados = 0

print ("Ingrese la Cantidad de Números Naturales que Quiere Sumar sus Cuadrados:")
cantidad_numeros = int(input())

for x in range(cantidad_numeros):
    suma_cuadrados += x**2

os.system("cls")

print (f"La Suma de los Cuadrados de los Primeros {cantidad_numeros} Números Naturales es de:")
print(suma_cuadrados)   

print()

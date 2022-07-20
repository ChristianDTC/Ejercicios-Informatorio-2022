#1) Determinar el número mayor de 10 números ingresados.

import os

numero_mayor = 0
numero_ingresado2 = []


for x in range(10):
    print ("Ingrese un Número:") #solicito los números
    numero_ingresado = float(input())

    #comparo los números y asigno el más grande
    numero_mayor = numero_ingresado if numero_ingresado > numero_mayor else numero_mayor
    
print(numero_mayor)
os.system("cls")


#################################################################################

for x in range(10):
    print ("Ingrese un Número:") #solicito los números
    numero_ingresado2.append(float(input()))

print(max(numero_ingresado2))
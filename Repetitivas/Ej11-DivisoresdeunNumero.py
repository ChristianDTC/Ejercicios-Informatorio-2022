#11) Hacer un programa que permita determinar todos los divisores de un número ingresado por el teclado.

import os


while (True):

    print ("Ingrese el Número que Desea Saber sus Divisores:")
    numero_elegido = int(input())

    os.system("cls")

    for x in range (numero_elegido +1):
        if x > 0 and numero_elegido % x == 0:
            print (f"{x} es Divisor de {numero_elegido}")
            print()


    while (True):

        print("¿Desea Seguir Cargando Números?\n1 = SI\n2 = NO")
        seguir_carga = input()

        if seguir_carga == "1":
            os.system("cls")
            break
        elif seguir_carga == "2":
            break
        else:
            print("Ingrese una Opción Válida")
            print()

    if seguir_carga == "2":
        break

os.system("cls")

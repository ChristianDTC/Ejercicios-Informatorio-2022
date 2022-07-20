#10) Mostrar los perímetros de varios triángulos ingresados sus lados porteclado, hasta que ya no desee.


import os

monto_total = 0

while (True):

    print ("Ingrese la Longitud del 1° lado del Triángulo:")
    primer_lado = float(input())

    print()

    print ("Ingrese la Longitud del 2° lado del Triángulo:")
    segundo_lado = float(input())

    print()

    print ("Ingrese la Longitud del 3° lado del Triángulo:")
    tercer_lado = float(input())

    os.system("cls")

    print("El Perímetro del Triángulo es de:")
    print (primer_lado + segundo_lado + tercer_lado)

    print()

    primer_lado = segundo_lado = tercer_lado = 0

    while (True):

        print("¿Desea Seguir Cargando Datos?\n1 = SI\n2 = NO")
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

print()
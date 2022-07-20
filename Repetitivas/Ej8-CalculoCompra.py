#8) Diseñar un programa que permita calcular el total de una compra,ingresando cantidad y precio de los productos. 
# El programa debe estar preparado para que el ingreso de los datos se produzca hasta que elusuario lo desee.


import os

monto_total = 0

while (True):

    print ("Ingrese la Cantidad de los Productos a Comprar:")
    cantidad_productos = int(input())

    print()

    print ("Ingrese el Precio de los Productos a Comprar:")
    precio_producto = float(input())

    os.system("cls")

    monto_total += (cantidad_productos * precio_producto)

    while (True):

        print("¿Desea Seguir Cargando Compras?\n1 = SI\n2 = NO")
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

print("El Monto Total de la Compra es de:")
print(f"${monto_total}")

print()
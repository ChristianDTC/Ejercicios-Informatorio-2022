#12) Calcular el monto a pagar por cada cliente y total recaudado en una estación de servicio.
#Debe diseñar un programa que permita montopor cliente y el total recaudado por la gasolinera, 
#tomando en cuentalo siguiente:
#• El precio del litro es para el Tipo A $50, para el Tipo B $ 55 y para elTipo C $60
#• El programa finaliza cuando se introduce una D como tipo degasolina.

import os

monto_total = 0

while (True):

    print ("Ingrese el Tipo de Gasolina a Cargar:")
    tipo_gasolina = input()

    os.system("cls")

    if tipo_gasolina.upper() == "D":
        break

    elif tipo_gasolina.upper() == "A" or tipo_gasolina.upper() == "B" or tipo_gasolina.upper() == "C":

        print ("Ingrese la Cantidad de Litros Cargados:")
        cantidad_litros_cargados = float(input())

        if tipo_gasolina.upper() == "A":
            precio_gasolina = 50
        elif tipo_gasolina.upper() == "B":
            precio_gasolina = 55
        elif tipo_gasolina.upper() == "C":
            precio_gasolina = 60

        monto_a_pagar_cliente = precio_gasolina * cantidad_litros_cargados
        
        os.system("cls")

        print ("El Monto a Pagar por el Cliente es de:")
        print (f"${monto_a_pagar_cliente}")

        monto_total += monto_a_pagar_cliente

        input()
        os.system("cls")

    else:
        print ("INGRESE UNA OPCION VALIDA")
        print()
    

print("El Monto Total Recaudado por la Estación de Servicio es de:")
print(f"${monto_total}")

print()
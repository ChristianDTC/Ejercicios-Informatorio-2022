#14) Una pizzería, vende sus pizzas en tres tamaños: pequeña, mediana; y grandes. 
#Una pizza puede ser sencilla (con sólo salsa y carne), o coningredientes extras, 
#tales como pepinillos, champiñones o cebollas. Desarrolle una solución que calcule 
#El precio de venta de una pizza, dándole el tamaño y el número de ingredientes extras.
#El precio de venta será 1.5 veces el costo total, que viene determinado por el tamaño, 
#más el número de ingredientes. En particular el costo total se calcula sumando:
#- un costo fijo de preparación. ($1000)
#- un costo variable que es proporcional al tamaño de la pizza.
#(0% pequeña - 10% medianda - 20% grande)
#- un costo adicional por cada ingrediente extra ($300)
#(por simplicidad sesupone que cada ingrediente extra tiene el mismo costo).

#precio de venta, tamaño, ingredientes extas


import os

def es_numero_entero (arg):

    while(True):        
        if arg.isdigit():
            return int(arg)
            break
        else:
            print ("INGRESE UN NUMERO VALIDO")
            arg = input()
            print()




print("BIENVENIDO A PIZZA INFO")
print()

print("Elija el Tamaño de su Pizza:\n1 = Pequeña\n2 = Mediana\n3 = Grande")
tamaño = es_numero_entero(input())

os.system("cls")

while(True):
    
    print("La Piza Sólo Contiene Salsa y Carne")
    print("¿Quiere Agregrar Ingredientes Extras?\n1 = SI\n2 = NO")
    sencilla = input()

    os.system("cls")

    if sencilla == "2":
        os.system("cls")
        break

    elif sencilla == "1":
        print("Puede Agregar uno o Todos los Ingredientes Extras:")
        print("1 = Pepinillos\n2 = Champiñones\n3 = Cebollas")
        eleccion_ingredientes =  input()
        print()

        if eleccion_ingredientes == 1 or eleccion_ingredientes ==
        break

    else:
        print("INGRESE UNA OPCION VALIDA")
        print()


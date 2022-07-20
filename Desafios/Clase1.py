x = 0
lista1 = []

while (x != 1):

    print ("Cuanto conoce sobre la contaminación del 1 al 10?: ")
    contaminacion = int(input())
    
    if contaminacion >= 1 and contaminacion <= 10:
        lista1.append(contaminacion)
    else:
        print("Valor incorrecto, por favor ingrese un numero del 1 al 10")
        print()

    while True:
        print("Desea seguir cargando mas datos?: 1= si 2=no")
        respuesta = int(input())
        if respuesta == 2:
            x = 1
            break
        elif respuesta == 1:
            print()
            break
        else:
            print("Por favor ingrese un valor valido: ")

print("La lista ordenada es: ")
print(sorted(lista1))
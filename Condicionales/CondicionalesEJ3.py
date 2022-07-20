#3. Determinar si el primero de un conjunto de tres números dados, es menor que
#los otros dos.

numero1 = int(input("Ingrese un Número: "))
numero2 = int(input("Ingrese un Número: "))
numero3 = int(input("Ingrese un Número: "))

if numero1 < numero2 and numero1 < numero3:
    print ("El Primer Número Ingresado es Menor que los 2 Números Siguientes.")
else:
    print ("El Primer Número Ingresado NO es Menor que los 2 Números Siguientes.")

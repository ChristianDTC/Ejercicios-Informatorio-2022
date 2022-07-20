#4. Realizar un programa que sea capaz de, habiéndose ingresado dos números m
#y n, determine si n es divisor de m.


numerom = int(input("Ingrese un Número: "))
numeron = int(input("Ingrese un Número: "))

if (numerom % numeron) == 0:
    print (f"{numeron} es Divisor de {numerom}")
else:
    print (f"{numeron} NO es Divisor de {numerom}")
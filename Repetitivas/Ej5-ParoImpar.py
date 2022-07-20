#5) Solicitar el ingreso de números al usuario y emitir un mensaje paradeterminar si es par o impar.
# El ciclo debe finalizar cuando el usuarioingresa 0.


import os


while(True):

    print("Ingrese un Número Entero:")
    numero_ingresado = int(input())

    if numero_ingresado == 0:
        break
    else:
        print()
    
    resultado = "El Número es Par" if (numero_ingresado % 2) == 0 else "El Número es Impar"
    print(resultado)

    print()
    input()
    os.system("cls")

print()
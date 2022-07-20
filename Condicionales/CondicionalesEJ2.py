#Desarrolle un programa que permita determinar si un número X ingresado es
#par o impar.


numeroingresado = int (input ("Ingrese el Número que Desea Saber si es Par o Impar: "))

if numeroingresado % 2 == 0:
    print (f"El Número {numeroingresado} es Par")
else:
    print (f"El Número {numeroingresado} es Impar")
#Desafío 2
#Realiza una función llamada relacion(a, b) que a partir de toneladas recicladas
#de dos ciudades se cumpla lo siguiente:
#Si el primer número es mayor que el segundo, debe devolver el nombre de la ciudad 1.
#Si el primer número es menor que el segundo, debe devolver el nombre de la ciudad 2.
#Si ambos números son iguales, debe devolver el nombre de ambas.


def relacion(toneladas1, toneladas2):
    if toneladas1 > toneladas2:
        print(ciudad1)
    elif toneladas1 < toneladas2:
        print(ciudad2)
    elif toneladas1 == toneladas2:
        print(ciudad1,",",ciudad2)

print("Ingrese el nombre de la ciudad: ")
ciudad1 = input()
print("Ingrese la cantidad de toneladas recicladas: ")
toneladas1 = int(input())

print("Ingrese el nombre de la ciudad: ")
ciudad2 = input()
print("Ingrese la cantidad de toneladas recicladas: ")
toneladas2 = int(input())
relacion(toneladas1, toneladas2)
#4) Diseñar un programa que imprima los números del 100 al 0 en ordendecreciente.


import os
x = 0

for x in range (101):
    print(100 - x)


input()
os.system("cls")


##############################################################

tupla = tuple(range(101))
print(tupla[::-1])

print()

lista = list(range(101))
print(lista[::-1])

input()
os.system("cls")
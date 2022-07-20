#Desafío 2
#Crea una tupla con los factores que más afectan a los mares. 
# Luego para jugar con niños y niñas, aprendiendo sobre contaminación del agua crea un programa que 
# pida números, si el numero esta entre 1 y la longitud máxima de la tupla, 
# muestra el contenido de esa posición sino muestra un mensaje de error.
#El programa termina cuando el usuario introduce un cero.

import os
factoresperjudicialesmares = ("Derrames de Petróleo", "Residuos Tóxicos", "Plaguicidas", "Herbicidas", "Fertilizantes", "Detergentes", "Productos Químicos", "Hidrocarburos", "Aguas Residuales", "Plásticos y Microplásticos", "Desechos Industriales", "Contaminación Acústica")

numero_elegido = 1

while numero_elegido != 0:
    print(f"Ingrese un Número entre 1 y {len(factoresperjudicialesmares)}:")
    numero_elegido = int(input())

    if numero_elegido != 0:
        if numero_elegido >=1 and numero_elegido <= len(factoresperjudicialesmares):
            print(factoresperjudicialesmares[numero_elegido - 1])
            print()
            
        else:
            print("ERROR, Eliga otro Número")
            print()
    else:
        break


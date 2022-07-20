#Desafío 4
#Escribir un programa que cargue una tupla con nombres de especie, y para cada nombre 
#de especie imprima el mensaje #Hola soy ......, cuidame.
#Modificá el programa anterior y dada una posición inicial p
#y una cantidad n, imprima el mensaje anterior para los n
#nombres que se encuentran a partir de la posición i.

import os

especiescargadas = []
especiesdeanimales = ("Mamíferos", "Aves", "Reptiles", "Ranas y Sapos", "Peces", "Cinepies y Milpies", "Arañas y Alacranes", "Insectos", "Cangrejos y Camarones", "Estrellas y Erizos", "Caracoles, Almejas y Pulpos", "Lombrices y Gusanos Marinos", "Rotíferos", "Gusanoes Planos", "Medusas y Corales", "ESponjas" )
indice = 0

for x in range (len(especiesdeanimales) -1):
    print (f"Hola soy {especiesdeanimales[x]} cuidame" )

input() #hago una pausa para que se lee la tupla

os.system ("cls") #limpio la pantalla



############################################################################


while (True):

    print ("Ingrese el Nombre de la Especie")
    especiescargadas.append(input())
    
    print()

    print (f"Hola soy {especiescargadas[indice]} cuidame")
    indice += 1 #hago1 un contador que uso de índice para saber la posicion del dato

    print()

    while (True): #bucle de control para finalizar el programa
            print ("¿Desea Seguir Cargando Especies de Animales? \n1 = SI\n2 = NO")
            seguircargandodatos = input()

            if seguircargandodatos == "1":
                os.system ("cls")
                break
            elif seguircargandodatos == "2":
                os.system ("cls")
                break
            else:
                print ("Ingrese una Opción Válida")
                print()

    if seguircargandodatos == "2": #finalizo el bucle principal
        break            


especiescargadas = tuple(especiescargadas)
print (f"Las Especies Cargadas son: {especiescargadas}")
print (type(especiescargadas))
input()

os.system ("cls")
#####################################################################################
#segunda parte

while (True): 

    print (f"Ingrese un Número entre 0 y {len(especiescargadas) }")
    numeroelegido = int (input())
    os.system ("cls")

    if numeroelegido > -1 and numeroelegido < (len(especiescargadas) +1):
        for x in  range ((len(especiescargadas) + 1) - numeroelegido):
            indice = x + (numeroelegido - 1)
            print (f"Hola soy {especiescargadas[indice]} cuidame" )
            print()
            
        break

    else:
        print ("Ingrese una Opción Válida")
        print()



#Desafío 2
#Crea una tupla con los factores que más afectan a los mares. 
# Luego para jugar con niños y niñas, aprendiendo sobre contaminación del agua crea un programa que 
# pida números, si el numero esta entre 1 y la longitud máxima de la tupla, 
# muestra el contenido de esa posición sino muestra un mensaje de error.
#El programa termina cuando el usuario introduce un cero.



from math import trunc
import os

factoresperjudicialesmares = ("Derrames de Petróleo", "Residuos Tóxicos", "Plaguicidas", "Herbicidas", "Fertilizantes", "Detergentes", "Productos Químicos", "Hidrocarburos", "Aguas Residuales", "Plásticos y Microplásticos", "Desechos Industriales", "Contaminación Acústica")


while (True):

    print ("Ingrese un Número")
    numeroelegido = float (input())
    print()
    
    os.system ("cls")

    if trunc(numeroelegido) >= 1 and trunc(numeroelegido) <= (len(factoresperjudicialesmares) -1):
        print ("Uno de los Factores que Afectan el Mar es:")
        print (factoresperjudicialesmares[trunc(numeroelegido)])
        
        print()

        while (True):
            print ("Desea Seguir Cargando Números: \n1 = SI\n2 = NO")
            seguircargandonumeros = input()

            if seguircargandonumeros == "1":
                print()
                break
            elif seguircargandonumeros == "2":
                break
            else:
                print ("Ingrese una Opción Válida")
                print()

        if seguircargandonumeros == "2":
            print()
            break
            

    else:
        print ("El Número Ingresado no es Válido, Prueve con Otro")
        print()



#Desafío 3
#Crea un diccionario donde la clave sea el nombre de biólogos y el valor sea el email (no es necesario validar)
#Tendrás que ir pidiendo contactos hasta el usuario diga que no quiere insertar mas. 
#No se podrán insertar nombres repetidos.

import os

diccionariobiologos = {}
seguircargandonumeros = 0

while (True):
    print ("Ingrese el Nombre Biólogo:")
    nombrebiologo = input()

    os.system ("cls")

    if nombrebiologo in diccionariobiologos:
        
        print ("El Biólogo ya esta Regisrado")
        print()

    else:
        
        print ("Ingrese el Email del Biólogo:")
        emailbiologo = input()
        print()

        diccionariobiologos[nombrebiologo] = emailbiologo

        os.system ("cls")

        while (True):
            print ("Desea Seguir Cargando Contactos: \n1 = SI\n2 = NO")
            seguircargandonumeros = input()

            if seguircargandonumeros == "1":
                os.system ("cls")
                break
            elif seguircargandonumeros == "2":
                break
            else:
                print ("Ingrese una Opción Válida")
                print()

    if seguircargandonumeros == "2":
        print()
        break

os.system ("cls")
print (diccionariobiologos)
print()
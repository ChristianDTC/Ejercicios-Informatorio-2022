#DESAFÍO 1
#Nos han pedido desarrollar una aplicación móvil para reducir comportamientos inadecuados 
#para el ambiente.
#a) Te toca escribir un programa que simule el proceso de Login. 
# Para ello el programa debe preguntar al usuario la contraseña, 
# y no le permita continuar hasta que la haya ingresado correctamente.
#b) Modificar el programa anterior para que solamente permita una cantidad fija de intentos.

#dado que no se brinda una contraseña invente una de ejemplo
#EJERCICIO A
contrasenia = ""
while contrasenia != "contraseñacorrecta": 
    print ("Ingrese la Contraseña: ")
    contrasenia = input()
    if contrasenia != "contraseñacorrecta":
        print ("¡¡¡ CONTRASEÑA INCORRECTA !!!")
        print ("")

print ("LOGUIN CORRECTO")


#EJERCICIO B
contrasenia = ""
for x in range (3): #ejemplo con 3 intentos
    print ("Ingrese la Contraseña: ")
    contrasenia = input()
    if contrasenia != "contraseñacorrecta":
        print ("¡¡¡ CONTRASEÑA INCORRECTA !!!")
        print (f"Le Quedan {2-x} Intentos")
    else:
        print ("LOGUIN CORRECTO")
        break



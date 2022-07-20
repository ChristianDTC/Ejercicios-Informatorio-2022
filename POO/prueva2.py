import os

def NumerosMayor0(arg, str1="SOLO SE PUEDE INGRESAR UN NUMERO ENTERO POSITIVO\n", str2="SOLO SE PUEDE INGRESAR UN NUMERO ENTERO POSITIVO\n"):
    while(True):
        try:
            arg = int(arg)
            if arg > 0:
                break
            else:
                os.system("cls")
                arg = input(str1)
        except:
            os.system("cls")
            arg = input(str2)
    os.system("cls")
    return arg


respuesta = input ("Ingrese solo numeros mayores a 0\n")
respuesta = NumerosMayor0(respuesta, "Tiene que ingresar un numero mayor a 0")
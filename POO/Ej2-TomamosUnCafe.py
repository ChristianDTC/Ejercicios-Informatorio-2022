"""
Desarrolla una clase cafetera con atributos 
_capacidadMaxima (la cantidad máxima de café que puede contener la cafetera)
y _cantidadActual (la cantidad actual de café que hay en la cafetera). 

Luego desarrollar los siguientes métodos:
llenarCafetera(): pues eso, hace que la cantidad actual sea igual a la capacidad.  

servirTaza(int): simula la acción de servir una taza con la capacidad indicada. 
    Si la cantidad actual de café “no alcanza” para llenar la taza, se sirve lo que quede.  

vaciarCafetera(): pone la cantidad de café actual en cero.  

agregarCafe(int): añade a la cafetera la cantidad de café indicada.

Cómo quedaría ese programa? Probalo.
"""

import os

class Cafetera:
    def __init__(self, capacidadMaxima, cantidadActual):
        self._capacidadMaxima = capacidadMaxima
        self._cantidadActual = cantidadActual

    def __str__(self):
        return f"Cantidad Actual de Café: {self._cantidadActual} ml,\nCapacidad Máxima Cafetera: {self._capacidadMaxima} ml\n"

    def llenar_cafetera(self):
        if self._cantidadActual < self._capacidadMaxima:
            self._cantidadActual = self._capacidadMaxima
            return "Se lleno la cafetera\n"
        else:
            return "La cafetera ya esta llena\n"

    def servir_taza(self, arg):
        if self._cantidadActual > 0:
            if arg > self._cantidadActual:
                arg = self._cantidadActual
                self._cantidadActual = 0
                return f"La taza se pudo cargar con {arg} ml de café\n"
            else:
                self._cantidadActual -= arg
                return "La taza se pudo llenar de café\n"                  
        else:
            return "No se puede cargar la taza. La cafetera esta vacia.\n"
            
    def vaciar_cafetera(self):
        if self._cantidadActual > 0:
            self._cantidadActual = 0
            return "Se vacio la cafetera.\n"
        else:
            return "La cafetera ya esta vacia.\n"

    def agregar_cafe (self, arg):
        if arg <= (self._capacidadMaxima - self._cantidadActual):
            self._cantidadActual += arg
            return f"Se agrego a la cafetera, {arg} ml de cafe.\n"
        else:
            return "La cantidad de café que desea agregar supera la capacidad máxima.\n"


def SoloNumeros(arg, str1="SOLO SE PUEDE INGRESAR UN NUMERO ENTERO POSITIVO\n"):
    while(True):
        try:
            arg = int(arg)
            if arg >= 0:
                break
            else:
                os.system("cls")
                arg = input(str1)
        except:
            os.system("cls")
            arg = input(str1)
    os.system("cls")
    return arg


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
#FUNSION PARA CONTROLAR EL VALOR INGRESADO QUE SEA UN NUMERO ENTERO Y POSITIVO

opciones_menu = "MENU DE OPCIONES:\n1 = Ver estado de la cafetera\n2 = Vaciar cafetera\n3 = Cargar cafetera\n4 = Llenar la cafetera\n5 = Servir taza\n6 = Salir\n"

def Menu():
    while(True):
        opcion_elegida = input("MENU DE OPCIONES:\n1 = Ver estado de la cafetera\n2 = Vaciar cafetera\n3 = Cargar cafetera\n4 = Llenar la cafetera\n5 = Servir taza\n6 = Salir\n")
        os.system("cls")
        opcion_elegida = NumerosMayor0(opcion_elegida, "INGRESE UNA OPCION VALIDA\n" + opciones_menu, "SOLO SE PUEDE INGRESAR UN NUMERO ENTERO POSITIVO\n" + opciones_menu)
        if opcion_elegida > 0 and opcion_elegida < 7:
            if opcion_elegida == 1:
                print(cafetera_ingresada)
            if opcion_elegida == 2:
                print (cafetera_ingresada.vaciar_cafetera())
            if opcion_elegida == 3:
                agregar_cafe = input ("Ingrese la cantidad de ml de cafe que desea agregar:\n")
                agregar_cafe = NumerosMayor0(agregar_cafe, "La cantidad de ml de cafe que desea agregar debe ser mayor a 0:\n")
                print (cafetera_ingresada.agregar_cafe(agregar_cafe))
            if opcion_elegida == 4:
                print (cafetera_ingresada.llenar_cafetera())
            if opcion_elegida == 5:
                taza = input("Ingrese la cantidad de ml que desea cargar en la taza:\n")
                taza = NumerosMayor0(taza, "La cantidad de ml que desea cargar en la taza debe ser mayor a 0\n")
                print (cafetera_ingresada.servir_taza(taza))
            if opcion_elegida == 6:
                print ("GRACIAS por utilizar nuestros servicios\nHASTA LUEGO\n")
                break
        else:
            print ("INGRESE UNA OPCION VALIDA\n")
            

capacidadMaxima = input("Ingrese la capacidad máxima de ml que tiene la cafetera\n")
capacidadMaxima = NumerosMayor0(capacidadMaxima,"La capacidad máxima de ml de la cafetera debe ser mayor a 0\n" )

cantidadActual = input("Ingrese la cantidad actual de ml que tiene la cafetera\n")
cantidadActual = SoloNumeros(cantidadActual)

os.system("cls")

cafetera_ingresada = Cafetera(capacidadMaxima, cantidadActual)
Menu()


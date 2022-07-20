"""
CASO 2
Crea al menos un objeto de cada subclase y añadelos a una lista llamada vehiculos.

Realiza una función llamada 
catalogar() que reciba la lista de vehículos y los recorra 
mostrando el nombre de su clase y sus atributos.

Modifica la función catalogar() para que reciba un argumento optativo ruedas, 
haciendo que muestre únicamente los que su número de ruedas concuerde con el valor del argumento. 
También debe mostrar un mensaje 
"Se han encontrado {} vehículos con {} ruedas:" 
únicamente si se envía el argumento ruedas. Ponla a prueba con 0, 2 y 4 ruedas como valor.
"""

import os

class Vehiculo:
    def __init__ (self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f"Mi color es {self.color}.\nTengo {self.ruedas} ruedas.\n"


class Coche(Vehiculo):
    def __init__ (self, color, ruedas, velocidad, cilindradas):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindradas = cilindradas

    def __str__(self):
        return Vehiculo.__str__(self) + f"Mi velocidad es de {self.velocidad}km/h.\nTengo {self.cilindradas} cm3.\n"
       

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindradas, carga):
        super().__init__ (color, ruedas, velocidad, cilindradas)
        self.carga = carga

    def __str__(self):
        return Coche.__str__(self) + f"La carga que puedo soportas es de {self.carga} kg.\n"


class Bicicleta(Vehiculo):
    def __init__ (self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
        
    def __str__(self):
        return Vehiculo.__str__(self) + f"Mi tipo es {self.tipo}\n"
        

class Motocicleta(Bicicleta):
    def __init__ (self, color, ruedas, tipo, velocidad, cilindradas):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindradas = cilindradas

    def __str__(self):
        return Bicicleta.__str__(self) + f"Mi velocidad es de {self.velocidad}km/h\nTengo {self.cilindradas} cm3.\n"


def catalogar(vehiculos, ruedas = 0):
  count = 0
  for vehiculo in vehiculos:
    if ruedas == vehiculo.ruedas:
        print(type(vehiculo).__name__)
        for k, v in vars(vehiculo).items():
          print('{}: {}'.format(k.capitalize(),v), end=' | ')
        count +=1
        print('\n')
  if ruedas > 1:
    print(f"Se han encontrado {count} con {ruedas} ruedas.\n")
  elif count == 0 or count == 1:
    print("El Vehículo tiene que tener más de 1 rueda.\n")



bmw = Vehiculo("negro", 5)
#print(bmw)
audi = Coche("Negro", 4, 300, 1500)
#print(audi)
ford = Camioneta("blanco", 4, 200, 1500, 400)
#print(ford)
honda = Bicicleta("Negra", 2, "deportiva")
#print(honda)
kawasaky = Motocicleta("Negra", 2, "deportiva", 300, 2000)
#print(kawasaky)

vehiculos = [bmw, audi, ford, honda, kawasaky]

catalogar(vehiculos, 4)
print("\n****************************\n")

catalogar(vehiculos, 2)
print("\n****************************\n")

catalogar(vehiculos, 5)
print("\n*******************************\n")

catalogar(vehiculos, 1)
print("\n**********************\n")

catalogar(vehiculos, 0)
print("\n**********************")


input()
os.system("cls")
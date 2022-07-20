"""
Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva 
clase CuantaJoven que deriva de lo que definas al resolver el problema Cuenta Electrónica. 

Cuando se crea esta nueva clase, además del titular y la cantidad 
se debe guardar una bonificación que estará expresada en tanto por ciento.

Construye los siguientes métodos para la clase:
En esta ocasión los titulares de este tipo de cuenta tienen que 
ser mayor de edad, por lo tanto hay que crear un método 
esTitularValido() que devuelve verdadero si el titular es mayor de edad0
pero menor de 25 años y falso en caso contrario.

Además la retirada de dinero sólo se podrá hacer si el titular es válido.

El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
"""

import os

class CuentaJoven:
  def __init__(self, titular, edad, cantidad, bonificacion):
    self.titular = titular
    self.edad = edad
    self.cantidad = cantidad
    self.bonificacion = bonificacion
  
  def __str__(self):
    return f"Titular: {self.titular}.\nEdad: {self.edad} años.\nCantidad: ${self.cantidad}.\nBonificación: {self.bonificacion}%\n"
  
  def mostrar(self):
    print(f"Cuenta Joven {self.bonificacion}")
  
  def esTitularValido(self):
      if self.edad >= 18 and self.edad <= 25:
        return True
      else:
        return False
  
  def retirarDinero(self, arg):
    if self.esTitularValido():
      if arg > self.cantidad:
        print("No puede retirar esa cantidad.\nSALDO INSUFISCIENTE\n")
      else:
        self.cantidad -= arg
        print(f"RETIRO EXITOSO.\nSALDO: ${self.cantidad}\n")
    else:
      print("Sólo el Titular puede retirar dinero.\n")
  
    
Christian = CuentaJoven("si", 36, 10000000, 25)
Cristian = CuentaJoven("si", 25, 10000000000000000000000, 15)

print(Christian)
print(Cristian)

Christian.retirarDinero(100)
Cristian.retirarDinero(100)

Christian.mostrar()
Cristian.mostrar()



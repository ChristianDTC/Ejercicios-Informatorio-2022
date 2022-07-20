
import os

class Vehiculo:
    def __init__ (self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def mostrarColor (self):
        return f"Mi color es {self.color}."
        
    def mostrarRuedas (self):
        return f"Tengo {self.ruedas} ruedas."
   
class Coche (Vehiculo):
    def __init__ (self, color, ruedas, velocidad, cilindradas):
        super().__init__ (color, ruedas)
        self.velocidad = velocidad
        self.cilindradas = cilindradas
   
    def mostrarVelocidad (self):
        return f"Mi velocidad es de {self.velocidad} km/h."
        
    def mostrarCilindradas (self):
        return f"Tengo {self.cilindradas} cm3."


def numerosMayor0(arg,titulo, str1="SOLO SE PUEDE INGRESAR UN NUMERO ENTERO POSITIVO\n", str2="SOLO SE PUEDE INGRESAR UN NUMERO ENTERO POSITIVO\n"):
    while(True):
        try:
            arg = int(arg)
            if arg > 1:
                break
            else:
                os.system("cls")
                arg = input(str1 + titulo)
        except:
            os.system("cls")
            arg = input(str2 + titulo)
    os.system("cls")
    return arg

def soloLetras(arg, titulo, str = "SOLO PUEDE INGRESAR LETRAS\n"):
    while(True):
        try:
            if arg.isalpha():
                break
            else:
                os.system("cls")
                arg = input(str + titulo)
        except:
            os.system("cls")
            arg = input(str + titulo)
    os.system("cls")
    return arg


pedir_color = "Ingrese el color del coche\n"
color = input(pedir_color)
color = soloLetras(color, pedir_color )

pedir_ruedas = "Ingrese la cantidad de ruedas del coche\n"
ruedas = input(pedir_ruedas)
ruedas = numerosMayor0(ruedas, pedir_ruedas, "La cantidad de ruedas deber ser mayor a 1\n" )

audi = Coche("negro", 4, 300, 1500)
bm = Vehiculo(color, ruedas)




print("ATRIBUTOS:")
print ( audi.color )
print ( audi.ruedas )
print ( audi.velocidad )
print ( audi.cilindradas )


print()

print("METODOS:")
print(bm.mostrarColor())
print(bm.mostrarRuedas())
print()
print(audi.mostrarColor())
print(audi.mostrarRuedas())
print(audi.mostrarVelocidad())
print(audi.mostrarCilindradas())
print()

input()
os.system("cls")
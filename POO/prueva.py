
class Coche:
    def __init__ (self, color, ruedas, velocidad, cilindradas):
        self.color = color
        self.ruedas = ruedas
        self.velocidad = velocidad
        self.cilindradas = cilindradas



bmw = Coche("negro", 5, 100, 1500)
#print(bmw)
audi = Coche("Negro", 4, 300, 1500)
#print(audi)
ford = Coche("blanco", 4, 200, 150)
#print(ford)
honda = Coche("Negra", 2, 150, 10)
#print(honda)
kawasaky = Coche("Negra", 2,  300, 2000)
#print(kawasaky)



vehiculos = [bmw, audi, ford, honda, kawasaky]

for w in vehiculos:
    for x, y in vars(w).items():
        #print(vars(x).get("color"))
        if x != "cilindradas":
            if x == "color":
                print(f"{x.capitalize()}: {y.upper()}", end= " - ")
            else:
                print(f"{x.capitalize()}: {y}", end= " - ")
        else:
            print(f"{x.capitalize()}: {y}")
    print()


#Desafío 1
#150 años es el tiempo que tarda una bolsa de plástico común en degradarse y una botella de PET
#puede tardar 1.000 años en desaparecer.
#Por otro lado los Envases de tetrabrik pueden tardar hasta 30 años en degradarse.
#Un trozo de chicle tarda 5 años en degradarse.
#Se solicita una función para que dado el ingreso de un elemento, 
#se solicite tipo: Bolsa de plástico, botella PET, envase tetrabrik o chicle, 
# e imprima la cantidad de años que tarda en degradarse.


def  tiempoDeDegradacion(tipo):

    BolsaDePlástico= 150
    botellaPet=1000
    envaseTetrabrik=30
    chicle=5

    
    if tipo == "1":
        print("el tiempo de degradacion es de", BolsaDePlástico, "años")
    elif tipo == "2":
        print("el tiempo de degradacion es de" , botellaPet, "años")
    elif tipo == "3":
        print("el tiempo de degradacion es de", envaseTetrabrik, "años")
    elif tipo == "4":
        print("el tiempo de degradacion es de", chicle, "años")
    else:
         print("el elemento ingresado no corresponde")

print ("Ingrese el Tipo de Elemento que desea Saber el Tiempo de Degradación:")
print ("1 = BOLSA DE PLASTICO\n2 = BOTELLA PET\n3 = ENVASES TETRABRIK\n4 = CHICLE")

tiempoDeDegradacion(input())
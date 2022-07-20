#17. Determinar y exhibir si la estatura de una persona adulta dada, es mayor que la
#estatura media de las personas adultas de su sexo, siendo:
#- estatura media de mujeres adultas: 1,65 m.
#- estatura media de varones adultos: 1,72 m.


print ("Ingrese el Sexo de la Persona (M - F):")
sexo = input()

print ("Ingrese la Estatura de la Persona en Centímetros:")
estatura = int (input())

if sexo.upper() == "M" and estatura > 172:
    print ("La Estatura de la Persona es Mayor que la Media")
elif sexo.upper() == "F" and estatura > 165:
    print ("La Estatura de la Persona es Mayor que la Media")
else:
    print ("La Estatura de la Persona NO es Mayor que la Media")


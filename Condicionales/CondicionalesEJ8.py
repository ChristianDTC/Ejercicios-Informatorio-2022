#8. Calcular el número de pulsaciones que una persona debe tener por cada 10
#segundos de ejercicio, si la fórmula es: Número de pulsaciones = (220 - edad)/10


print ("Ingrese la Edad de la Persona: ")
edad = int ( input ())

numeropulsaciones = (220 - edad) / 10


print ("Por cada 10 Segundo de Ejercicio, la Persona debe tener:")
print (f"{numeropulsaciones} Pulsaciones")

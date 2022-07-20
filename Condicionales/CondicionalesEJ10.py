#10. Tres personas deciden invertir su dinero para fundar una empresa. Cada una
#de ellas invierte una cantidad distinta. Obtener el porcentaje que cada quien
#invierte con respecto a la cantidad total invertida.


print ("Ingrese la Cantidad a Invertir de la 1° Persona: ")
inversion1 = float (input())

print ("Ingrese la Cantidad a Invertir de la 2° Persona: ")
inversion2 = float (input())

print ("Ingrese la Cantidad a Invertir de la 3° Persona: ")
inversion3 = float (input())

inversiontotal = inversion1 + inversion2 + inversion3

print (f"La 1° Persona Invirtio el {round((inversion1*100)/inversiontotal,2)}% del Monto Total")
print (f"La 2° Persona Invirtio el {round((inversion2*100)/inversiontotal,2)}% del Monto Total")
print (f"La 3° Persona Invirtio el {round((inversion3*100)/inversiontotal,2)}% del Monto Total")

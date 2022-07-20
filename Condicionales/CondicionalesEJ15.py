#15. Un obrero necesita calcular su salario semanal, el cual se obtiene de la
#siguiente manera:
#i. Si trabaja 40 horas o menos se le paga $16 por hora
#ii. Si trabaja más de 40 horas se le paga $16 por cada una de las primeras 40 horas
#y $20 por cada hora extra.

print ("Ingrese la Cantidad de Hora Trabajadas:")
horasemanal = int (input())

if horasemanal <= 40:
    print (f"El Salario Semanal es de: ${16*horasemanal}")
elif horasemanal > 40:
    horasextras = horasemanal - 40
    print (f"El Salario Semanal es de: ${16*40 + horasextras*20}")

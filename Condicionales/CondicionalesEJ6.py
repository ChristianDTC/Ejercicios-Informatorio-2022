#6. Un equipo de fútbol ha tenido una buena campaña y desea premiar a sus
#jugadores con un aumento del salario para la siguiente campaña. Los sueldos
#deben ajustarse de la siguiente forma:
#Sueldo Actual (en $) Aumento
#0 – 6000 15%
#6000 – 7900 10%
#7900 – 12000 6%
#Más de 12000 0%
#Diseñar un programa que lea el salario de un jugador, y que a
#continuación muestre el tanto por ciento de aumento, el sueldo actual y el
#sueldo aumentado.

salarioactual = float ( input ("Ingrese el Salario Actual del Jugador: "))

if salarioactual <= 6000:
    print ("El Aumento del Salario a Recibir es del 15%")
    print (f"El Sueldo Actual es de: ${salarioactual}")
    print (f"El Sueldo con el Aumento es de: ${salarioactual * 1.15}")

elif salarioactual > 6000 and salarioactual <= 7900:
    print ("El Aumento del Salario a Recibir es del 10%")
    print (f"El Sueldo Actual es de: ${salarioactual}")
    print (f"El Sueldo con el Aumento es de: ${salarioactual * 1.1}")

elif salarioactual > 7900 and salarioactual <= 12000:
    print ("El Aumento del Salario a Recibir es del 6%")
    print (f"El Sueldo Actual es de: ${salarioactual}")
    print (f"El Sueldo con el Aumento es de: ${salarioactual * 1.06}")

elif salarioactual > 12000:
    print ("No Recibe Aumento del Salario")
    print (f"El Sueldo Actual se mantiene en: ${salarioactual}")


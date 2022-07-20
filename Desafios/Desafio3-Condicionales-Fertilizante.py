#Desafío 3
#Para el uso de fertilizantes es necesario medir cuánto abarca un determinado compuesto
# en el suelo el cual debe existir en una cantidad de al menos 10% por hectárea, 
# y no debe existir vegetación del tipo MATORRAL. Escribir un programa que 
# determine si es factible la utilización de fertilizantes.



compuesto = float ( input ("Ingrese el Porcentaje del Compuesto que Abarca por Hectarea: "))

vegetacion = input ("Ingrese el Tipo de Vegetación que hay: ")


if compuesto >= 10 and vegetacion.upper() == "MATORRAL":
    print ("Es Factible la Utilización de Fertilizantes")

else:
    print ("NO Es Factible la Utilización de Fertilizantes")

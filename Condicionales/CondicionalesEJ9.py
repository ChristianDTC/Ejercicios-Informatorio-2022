#9. En un Centro Asistencial existen tres áreas: Pediatría, Traumatología y
#Kinesiología. El presupuesto anual del hospital se reparte conforme a la siguiente tabla:
#ÁREA PORCENTAJE
#Pediatría 60%
#Traumatología 20%
#Kinesiología 20%
#Obtener la cantidad de dinero que recibirá cada área, para cualquier
#monto presupuestal que se ingrese por teclado.


print ("Ingrese el Monto del Presupuesto Anual del Hospital")
montopresupuestoanual = float ( input())

print ("El Area de Pediatría Recibirá:")
print (f"${round(montopresupuestoanual*0.6)}")
print ("El Area de Traumatología Recibirá:")
print (f"${round(montopresupuestoanual*0.2)}")
print ("El Area de Kinesiología Recibirá:")
print (f"${round(montopresupuestoanual*0.2)}")

#7. Un comercio ofrece un descuento del 15% sobre el total de la compra si esta
#supera los $1000. Obtenga para determinado cliente cuánto deberá pagar
#finalmente por su compra y el descuento obtenido, si es que corresponde.
from cgi import print_arguments


compra = float ( input ("Ingrese el Monto de la Compra: $"))

if compra > 1000:
    print (f"El Cliente Deberá Pagar: ${round(compra,2)}")
    print (f"El Descuento Obtenido es del 15% = ${round(compra*0.15,2)}")
else:
    print (f"El Cliente Deberá Pagar: ${round(compra,2)}")


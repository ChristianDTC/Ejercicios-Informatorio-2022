#La ciudad esta dividida en 2 secciones de recolección sección A y B 
# de acuerdo al nombre de la barrio y el tipo del barrio (CÉNTRICO y NO CÉNTRICO)
#La sección A esta formada por los barrios céntricos cuyo nombre comienza con 
# una letra anterior a M y los barrios no céntricos con nombre posterior a la M, 
# y la sección B el resto.
#Debemos hacer un programa que dado el nombre del barrio y la ubicación, 
# nos informe en que sección se encuentra.


print ("Ingrese el Nombre del Barrio: ")
nombrebarrio = input ()

print("Ingrese Tipo de Barrio")
print ("1 Céntrico - 2 No Céntrico")
tipobarrio = int (input ())


if nombrebarrio.upper() < "M" and tipobarrio == 1:
    print (f"El Barrio {nombrebarrio} Pertenece a la Sección A")
elif nombrebarrio.upper() > "M" and tipobarrio == 2:
    print (f"El Barrio {nombrebarrio} Pertenece a la Sección A")
else:
    print (f"El Barrio {nombrebarrio} Pertenece a la Sección B")



#if nombrebarrio.upper() > "M":
#   if tipobarrio == 1:
        #print (f"El Barrio {nombrebarrio} Pertenece a la Sección A")
#   elif tipobarrio == 2:
        #print (f"El Barrio {nombrebarrio} Pertenece a la Sección A")
#else:
    #print (f"El Barrio {nombrebarrio} Pertenece a la Sección B")
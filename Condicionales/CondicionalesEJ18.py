#18. Se leen tres números que son las longitudes de los lados de un triángulo.
#determinar e informar si el mismo es equilátero (3 lados iguales), isósceles (2
#lados iguales) o escaleno (3 lados distintos).

l1 = int(input("Ingrese la Longitud de un Lado del Triángulo: \n"))
l2 = int(input("Ingrese la Longitud de un Lado del Triángulo: \n"))
l3 = int(input("Ingrese la Longitud de un Lado del Triángulo: \n"))


if l1 == l2 and l1 == l3:
    print ("Triángulo Equilátero (3 Lados Iguales)")
elif l1==l2 or l1==l3 or l2 == l3:
    print ("Triángulo Isósceles (2 Lados Iguales)")
else:
    print ("Triángulo Escaleno (3 Lados Distintos)")


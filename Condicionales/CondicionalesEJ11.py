#11. Determinar si un alumno aprueba a reprueba un curso, sabiendo que aprobara
#si su promedio de tres calificaciones es mayor o igual a 70; desaprueba en caso
#contrario.

print ("Ingrese la 1° Nota: ")
nota1 = float (input())

print ("Ingrese la 2° Nota: ")
nota2 = float (input())

print ("Ingrese la 3° Nota: ")
nota3 = float (input())

notatotal = (nota1 + nota2 + nota3)/3

if notatotal >= 70:
    print ("El Alumno Aprobó")
else:
    print ("El Alumno Desaprobó")


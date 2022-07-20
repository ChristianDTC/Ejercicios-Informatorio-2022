#13) Un grupo de 100 estudiantes presentan un exámen de Física. 
#Diseñe un diagrama que lea por cada estudiante la calificación obtenida y calcule e imprima:
#A.- La cantidad de estudiantes que obtuvieron una calificación menor a50.
#B.- La cantidad de estudiantes que obtuvieron una calificación de 50 omás pero menor que 80. 
#C.- La cantidad de estudiantes que obtuvieron una calificación de 70 omás pero menor que 80.
#D. La cantidad de estudiantes que obtuvieron una calificación de 80 omás.

#DADO QUE EN LA OPCION B, C COMPRENDEN EL MISMO RANGO DE 70 A 80 LO MODIFIQUE DE LA SIGUIENTE MANERA
#B más de 50 pero menor que 70.
#C más de 70 pero menor que 80.



import os

indice = calificacion_menor_50 = calificacion_entre_50_70 = calificacion_entre_70_80 = calificacion_mas_80 = 0


while (indice < 100):
        
    while(True):

        print (f"Ingrese la Nota del {indice+1}° Alumno (0 - 100):")
        nota_alumno = input()

        os.system("cls")

        if nota_alumno.isdigit(): #controlo si se cargo un valor entero
            
            nota_alumno = int(nota_alumno) #lo paso a número entero para hacer la comparación
            indice += 1 #control del bucle

            calificacion_menor_50 += 1 if nota_alumno < 50 else 0
            calificacion_entre_50_70 += 1 if nota_alumno >= 50 and nota_alumno < 70 else 0
            calificacion_entre_70_80 += 1 if nota_alumno >= 70 and nota_alumno < 80 else 0
            calificacion_mas_80 += 1 if nota_alumno >= 80 else 0
           
            break

        else:
            print ("INGRESE UN NUMERO ENTERO")
            print()

    
print ("La Cantidad de Estudiantes que Obtuvieron una Calificación Menor a 50 es de:")
print(calificacion_menor_50)

print()

print ("La Cantidad de Estudiantes que Obtuvieron una Calificación de 50 o más pero Menor que 70 es de:")
print(calificacion_entre_50_70)

print()

print ("La Cantidad de Estudiantes que Obtuvieron una Calificación de 70 o más pero Menor que 80 es de:")
print(calificacion_entre_70_80)

print()

print ("La Cantidad de Estudiantes que Obtuvieron una Calificación de 80 o más es de:")
print(calificacion_mas_80)

print()
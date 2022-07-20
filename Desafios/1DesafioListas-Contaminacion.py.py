#Desafío 1
#Escribir un programa que pregunte
#a diferentes personas cuánto conocen sobre contaminación del 1 al 10
#almacene estos valores en una lista
#y los muestre por pantalla ordenados de menor a mayor.

import os
finalizarcarga = True
listacalificacion = []


while finalizarcarga:
    print ("Ingrese Cuánto Conoce Sobre Contaminación del 1 al 10")
    calificacion = int (input())
    

    if calificacion >= 1 and calificacion <=10:
        
        listacalificacion.append (calificacion)
        print()

        respuestavalida = True    
        while respuestavalida:    
            print ("Desea Seguir Cargando Datos:\n1 = SI\n2 = NO")
            respuesta = input()

            if respuesta == "1":
                respuestavalida = False
                os.system ("cls")
            elif respuesta == "2":
                finalizarcarga = False
                respuestavalida = False
            else:
                print()
                print ("Ingrese Una Opción Valida")
                print()
    else:
        print()
        print ("Ingrese Una Opción Valida")
        print()

    
os.system ("cls")
print ("La Lista Ordenada de Menor a Mayor es:")
print (sorted(listacalificacion))
print()
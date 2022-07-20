#DESAFÍO 4
#Escriba un programa que permita imprimir un tablero Ecológico (verde y blanco) 
# de acuerdo al tamaño indicado. Por ejemplo el gráfico a la izquierda es el resultado 
# de un tamaño: 8x6

print ("Ingrese el Alto del Tablero:")
altotablero = int (input())

print ("Ingrese el Ancho del Tablero:")
anchotablero = int (input())

print()

for x in range (altotablero): 
    for y in range (anchotablero):
        
        if x % 2 == 0: #al ser par empiza con B
            if y % 2 == 0: #al ser par empieza con B
                color = "B " 
            else: #la segunda entrada pasa a ser impar y alterna el color
                color = "V "
            print (color, end="")

        else: #la segunda linea de la columna pasa a ser impar y altera los colores
            if y % 2 == 0:
                color = "V " 
            else:
                color = "B "
            print (color, end="")

        
    print()


print()


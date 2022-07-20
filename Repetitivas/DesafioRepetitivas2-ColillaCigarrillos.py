#DESAFÍO 2
#Se inicia una campaña de recolección de colillas de cigarrillos en los barrios.
#Realizá un programa que permita registrar cantidad de colillas recolectadas por 
# un número determinado de personas. Luego obtener estadísticas al respecto 
# informando porcentaje de personas que han encontrado menos de 100 colillas, 
# más de 100 y menos de 200, más de 200 colillas.

#dado que en el ultimo punto no esta considerado si junto 200 colillas 
#lo agrego al valor entre 100 y 200

cantidadcolillasmenosde100 = cantidadcolillasentre100y200 = cantidadcolillasmasde200 = 0

print ("Ingrese la Cantidad de Recolectores: ")
cantidadrecolectores = int (input())

for x in range (cantidadrecolectores):
    print ("Ingrese la Cantidad de Colillas Recolectadas")
    colillasrecolectadas = int ( input())

    if colillasrecolectadas <= 100:
        cantidadcolillasmenosde100 = cantidadcolillasmenosde100 + 1
    elif colillasrecolectadas <= 200 and colillasrecolectadas > 100:
        cantidadcolillasentre100y200 = cantidadcolillasentre100y200 + 1
    elif colillasrecolectadas > 200:
        cantidadcolillasmasde200 = cantidadcolillasmasde200 + 1
    
print ("")

print ("El Porcentaje de Personas que han Encontrado Menos de 100 Colillas es de:")
print (f"{round((cantidadcolillasmenosde100 * 100)/cantidadrecolectores)}%")
print ("")


print ("El Porcentaje de Personas que han Encontrado Entre 100 y 200 Colillas es de:")
print (f"{round((cantidadcolillasentre100y200 * 100)/cantidadrecolectores)}%")
print ("")


print ("El Porcentaje de Personas que han Encontrado Más de 200 Colillas es de:")
print (f"{round((cantidadcolillasmasde200 * 100)/cantidadrecolectores)}%")
print ("")

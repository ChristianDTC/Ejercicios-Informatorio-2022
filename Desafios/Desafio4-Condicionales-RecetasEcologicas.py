#Tenemos que decidir entre 2 recetas ecológicas. Los ingredientes para cada tipo de receta 
# aparecen a continuación.
#Ingredientes comunes: Verduras y berenjena.
#Ingredientes Receta 1: Lentejas y apio.
#Ingredientes Receta 2: Morrón y Cebolla..
#Escribir un programa que pregunte al usuario que tipo de receta desea, 
# y en función de su respuesta le muestre un menú con los ingredientes disponibles 
# para que elija. Solo se puede eligir 3 ingrediente (entre la receta elegida y los comunes.)
# y el tipo de receta. Al final se debe mostrar por pantalla la receta elegida 
# y todos los ingredientes.


print ("Seleccione el Número (1 o 2) de Receta que Desea: ")
print ("RECETA 1: Lentejas y Apio")
print ("RECETA 2: Morrón y Cebolla")
tipodereceta = int ( input ())

print ("Puede Agregar un Ingrediente más: ")
print ("1: Verduras")
print ("2: Berenjena")
ingredientes = int ( input ())


if tipodereceta == 1:
    print ("La Receta Elegia es la 1")
    if ingredientes == 1:
        print ("Los Ingredientes son: Lenteja, Apio y Verduras")
    elif ingredientes == 2:
        print ("Los Ingredientes son: Lenteja, Apio y Berenjena")

elif tipodereceta == 2:
    print ("La Receta Elegia es la 2")
    if ingredientes == 1:
        print ("Los Ingredientes son: Morrón, Cebolla y Verduras")
    elif ingredientes == 2:
        print ("Los Ingredientes son: Morrón, Cebolla y Berenjena")



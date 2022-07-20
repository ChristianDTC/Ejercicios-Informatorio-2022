#Realiza una función separar(lista) que tome una lista que tenga datos de 
#cantidad de árboles plantados en diferentes ciudades de Argentina durante la cuarentena. 
#Luego la función debe devolver dos listas ordenadas. 
#La primera con las cantidades que superen los 100 y la segunda con el resto.
#Qué cantidad de ciudades han plantado más de 100 árboles durante cuarentena.


cantArboles = [150, 65, 87, 556, 35, 498]

def separar(lista):
    mayor100 = []
    menor100 = [] 
    for x in lista:
        if x > 100:
            mayor100.append(x)
             
        else:
            menor100.append(x)

    mayor100.sort()
    menor100.sort()
    
    print(mayor100)
    print(menor100)
    print("Las ciudades que han plantado más de 100 árboles son: ",  len(mayor100))

separar(cantArboles)
#DESAFÍO 5
#Se está desarrollando un sistema de control de vehículos desde donde se han tirado restos 
#de basura a la vía pública.
#Para ello la ciudad cuenta con sistemas de monitoreo de patentes que devuelve 
#3 letras y un valor numérico de 5 dígitos a la Central con el siguiente significado:
#3 letras: Correspondientes a la patente.
#Del valor numérico:
#Los 3 primeros números corresponden a la patente
#El 4 número indica
#1- Tiró basura a la vía pública
#0 - No tiró basura a la vía pública
#El 5 número indica
#1- Ya había sido multado el vehículo
#0 - Vehículo sin multas.
#Deberás informar cantidad de vehículos observados, 
#cantidad de vehículos que han tirado basura y 
# porcentaje de éstos que ya habían sido multados.


cantidavehiculos = cantidavehiculosmultados = cantidavehiculostiraronbasura = 0
faltancodigos = "1"


while faltancodigos == "1":

    print ("Ingrese el Código Devuelto por el Sistema de Monitoreo:")
    codigosistemamonitoreo = input()
    print()

    if len(codigosistemamonitoreo) != 8:
        print ("El Código Devuelto por el Sistema de Monitoreo es de 8 Dígitos")
        print ("Ingrese un Código Valido")
       
    else: 
        cantidavehiculos = cantidavehiculos + 1

        if codigosistemamonitoreo[6] == "1":
            cantidavehiculostiraronbasura = cantidavehiculostiraronbasura + 1

        if codigosistemamonitoreo[7] == "1":
            cantidavehiculosmultados = cantidavehiculosmultados + 1 

        print()

        cargacorrecta = False
        while not cargacorrecta:
            print ("¿Faltan Códigos por Cargar?")
            print ("1 = SI \n2 = NO")
            faltancodigos = input()

            if faltancodigos == "1":
                cargacorrecta = True
            elif faltancodigos == "2":
                cargacorrecta = True
            else:
                print()
                print ("Ingrese un Código Correcto:")
                print()         

    print()


print (f"La Cantidad de Vehículos Observados es de: {cantidavehiculos}")
print()
print (f"La Cantidad de Vehículos que Han Tirado Basura es de: {cantidavehiculostiraronbasura}")
print()
print ("El Porcentaje de Vehículos que Han Tirado Basura")
print (f"Y ya Habían sido Multados es de: {round((cantidavehiculosmultados * 100)/cantidavehiculos)}%")
print()
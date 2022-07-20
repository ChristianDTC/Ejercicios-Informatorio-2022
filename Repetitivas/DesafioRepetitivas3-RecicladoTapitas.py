#DESAFÍO 3
#En una tienda de descuento por reciclado las personas que van a pagar el importe de su compra
#llegan a la caja y ofrecen tapitas para reciclar, de acuerdo a la cantidad que lleven en 
#la caja le entregan un código de descuento que se aplicará sobre el total de su compra. 
#Determinar la cantidad que pagara cada cliente desde que la tienda abre hasta que cierra.
#Se sabe que si el código de descuento es rojo se obtendrá un 40% de descuento; 
#si es amarilla un 25% y si es blanca no obtendrá descuento.

#bool de control while
tiendaabierta = codigocorrecto = opcionvalida = True
montodeldia = 0

while tiendaabierta: #control del bucle del proceso
    print ("Ingrese el Monto de la Compra:")
    montocompra = float (input())
    print("")

    codigocorrecto = True
    while codigocorrecto: #bucle para que ingrese un codigo válido
        print ("Ingrese el Código de Descuento: ")
        print ("1 = ROJO \n2 = AMARILLO \n3 = BLANCO")
        codigodescuento = input()

        if codigodescuento == "1":
            montocompra = montocompra * (1 - 0.4)
            codigocorrecto = False
        elif codigodescuento == "2":
            montocompra = montocompra * (1 - 0.25)
            codigocorrecto = False
        elif codigodescuento == "3":
            montocompra = montocompra
            codigocorrecto = False
        else:
            print ("Ingrese un Código Válido")
            codigocorrecto = True

        
    montodeldia = montodeldia + montocompra
    print("")
    print  (f"El Cliente Pagará:  ${round(montocompra,2)}")
    print("")

    opcionvalida = True
    while opcionvalida: #bucle para que ingrese un codigo válido
        print("La Tienda Sigue Abierta:")
        print("1 = SI \n2 = NO")
        tiendacerrada = input()
        
        print("")    

        if tiendacerrada == "1":
            tiendaabierta = True
            opcionvalida = False
        elif tiendacerrada == "2":
            tiendaabierta = False
            opcionvalida = False
        else:
            print ("Ingrese una Opción Valida")
            opcionvalida = True

print("")

#16) Escribir un programa el cual lea dos valores enteros. 
#Si el primero es menor que el segundo, que imprima el mensaje ``Arriba''.
#Si el segundoes menor que el primero, que imprima el mensaje ``Abajo''. 
#Si losnúmeros son iguales, que imprima el mensaje ``igual''. 
#Si alguno de los datos ingresados es igual a 0, que imprima un mensaje conteniendo la palabra ``Error''.


import os


while (True):
    
    print ("Ingrese un Número Entero:")
    primer_numero = input()
    
    os.system("cls")

    if primer_numero.isdigit(): #controlo si se cargo un valor entero
        
        primer_numero = int(primer_numero) #lo paso a número entero para hacer la comparación

        while (True):

            print ("Ingrese un Número Entero:")
            segundo_numero = input()

            os.system("cls")
        
            if segundo_numero.isdigit():
                segundo_numero = int(segundo_numero) 

                if primer_numero == 0 or segundo_numero == 0:
                    print ("ERROR")
                    print()
                    break

                elif primer_numero == segundo_numero:
                    print ("IGUAL")
                    print()
                    break

                elif primer_numero < segundo_numero:
                    print ("ARRIBA")
                    print()
                    break

                elif primer_numero > segundo_numero:
                    print ("ABAJO")
                    print()
                    break
            else:
                print ("INGRESE UN NUMERO ENTERO")
                print()

        break

    else:
        print ("INGRESE UN NUMERO ENTERO")
        print()



    
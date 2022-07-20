#  File     :   lists1.py
#  Author   :   José Agustín González
#  Date     :   10/06/2022
'''
Write a program that asks different people how much they know about pollution
from 1 to 10, stores these values in a list and displays them on the screen
ordered from lowest to highest.
'''

import mymodule as my   #  My module with its own code library


my.clean_the_screen()

print("Consulta sobre contaminación")
print("----------------------------")

try:
    #  My code
    list = []
    people_counter = 0
    
    while True:
        value = int(input(f"\tContamin. ({my.color.BLUE}0{my.color.END}=Fin):"+
                          f"\n\t\t({my.color.BLUE}1{my.color.END}=Nada y " +
                          f"{my.color.BLUE}10{my.color.END}=Muchísimo) : "))
        if value >=1 and value<=10:
            list.append(value)
            people_counter += 1
            print(f"\t\tPers.:{my.color.GREEN}{people_counter}{my.color.END}"+
                  f"\tConocimiento : {my.color.BLUE}{value}{my.color.END}")
        elif value == 0:
            break
        else:
            print(f"\t{my.color.RED}ERROR, opción incorrecta.{my.color.END}")

except Exception as e:
    #  Handle the error
    print(f"\t{my.color.RED}ERROR, {str(e)} ingresar números.{my.color.END}")

else:
    #  If no exception then will be executed

    #  Sort the list
    list.sort()
    
    #  Submit the report
    print(f"\t\t{my.color.UNDERLINE}INFORME:{my.color.END}")
    print(f"\t\t\tLista ordenada : {my.color.GREEN}{list}{my.color.END}")

finally:
    #  Always gets executed either exception is generated or not
    print("Fin.")


import os   #  Miscellaneous operating system interfaces
import time #  Miscellaneous operating system interfaces



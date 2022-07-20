#5. Diseñar un programa que lea las longitudes de los tres lados de un triángulo
#(L1,L2,L3) y determine qué tipo de triángulo es, de acuerdo a los siguientes
#casos. Suponiendo que A determina el A de los tres lados y B y C
#corresponden con los otros dos, entonces:
#1. Si A>=B + C à No se trata de un triángulo
#2. Si A = B + C à Es un triángulo rectángulo 2 2 2
#3. Si A > B + C à Es un triángulo obtusángulo 2 2 2
#4. Si A < B + C à Es un triángulo acutángulo

l1 = int(input("Ingrese la Longitud de un Lado del Triángulo: "))
l2 = int(input("Ingrese la Longitud de un Lado del Triángulo: "))
l3 = int(input("Ingrese la Longitud de un Lado del Triángulo: "))

#primero ordeno de mayor a menor las longitudes
if l1 >= l2 and l1 >= l3:
    A = l1
    if l2 >= l3:
        B = l2
        C = l3
    else:
        B = l3
        C = l2
elif l2 >= l3:
    A = l2
    if l1 >= l3:
        B = l1
        C = l3 
    else:
        B = l3
        C = l1
else:
    A = l3
    if l1 >= l2:
        B = l1
        C = l2
    else:
        B = l2
        C = l1

if A > B + C: #para poder mostrar todas las posibilidades saque el mayor o igual
    print ("No se trata de un Triángulo")
elif A == B + C:
    print ("Es un Triángulo Rectángulo")
elif A > B + C:
    print ("Es un Triángulo Obtusángulo")
elif A < B + C:
    print ("Es un Triángulo Acutángulo")



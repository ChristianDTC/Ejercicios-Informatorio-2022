#17) Calcular la utilidad que un trabajador recibe en el reparto anual de utilidades 
# si este se le asigna como un porcentaje de su salario mensual que depende de su antigüedad en la empresa 
# de acuerdo con la sig. tabla:
# Tiempo Utilidad Menos de 1 año 5% del salario
# Más de 1 año y hasta 2 años 7% del salario
# Más de 2 años y hasta 5 años 10% del salario
# Más de 10 años 20% del salario


def is_float (arg):
    if utilidad_anual.find("."):
        print ("Es Float")
    else:
        print ("No es Float")


utilidad_anual = input("Ingrese la Utilidad Anual:\n")
is_float(utilidad_anual)

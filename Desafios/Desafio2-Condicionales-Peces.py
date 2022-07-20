#Desafío 2
#La contaminación del agua es cualquier cambio químico, físico o biológico
#en la calidad del agua que tiene un efecto dañino en cualquier cosa viva 
# que consuma ese agua. Cuando seres humanos beben el agua contaminada tienen 
# a menudo problemas de salud.
#La contaminación del agua se detecta en los laboratorios, donde pequeñas muestras 
# de agua se analizan para diversos tipos de contaminantes. Los organismos vivos tales 
# como pescados se pueden también utilizar para la detección de la contaminación del agua. 
# Los cambios en su comportamiento o crecimiento nos demuestran, que el agua en la que viven 
# está contaminada.
#Para seguir colaborando en esta misión de salvar al planeta,necesitamos que elabores un
#programa en Python
#que dado el tamañode un pez indique si su organismo está contaminado. 
#Para ello tendremos 4 opciones:
#Tamaño Normal: Mensaje
#"Pez en buenas condiciones"
#Tamaño por debajo de lo Normal: Mensaje
#"Pez con problemas denutrición"
#Tamaño un poco por encima de lo Normal: Mensaje
#"Pez consíntomas de organismo contaminado"
#Tamaño sobredimensionado: Mensaje
#"Pez contaminado"

print ("Ingrese el Tamaño del Pez")
print ("1 - Tamaño Normal")
print ("2 - Tamaño por Debajo Normal")
print ("3 - Tamaño un Poco por Encima de lo Normal")
print ("4 - Tamaño Sobredimensionado")
tamanio = int ( input())

if tamanio == 1:
    print("Pez en Buenas Condiciones")
elif tamanio == 2:
    print ("Pez con Problemas de Nutrición")
elif tamanio == 3:
    print ("Pez con Síntomas de Organismo Contaminado")
elif tamanio ==4:
    print ("Pez contaminado")


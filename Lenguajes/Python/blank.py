 print(2 + 2)
print("Julian" * 5)
Toti = 1;
print(Toti)
Este programa me saluda y me pide mi nombre
print("Hola Mundo")
print("¿Cual es tu nombre?") #Pregunta por su nombre
myName = input() #Guarda en la variable myName lo que ingrese en la consola
print("Es un placer conocerte, " + myName) #Imprime una cadena y le agrega el contenido de la variable myName
print("La longitud de su nombre es: ") #Imprime el string
print(len(myName)) #Muestra la cantidad de caracteres en una variable
print("¿Cual es su edad?") #Pregunta por su edad
miAge = input() #Guarda en la variable miAge lo que ingrese en la consola
print("Usted será " +str(int(miAge) + 1) + " en un año.") #Imprime dos string con la edad sumandole un año
print(float("3.40")) #Muestra 3.4
print(float(6.50)) #Muestra 6.5

nombre = "Manuel"
clave = "41323167"
if nombre == "Manuel":
	print("Hola Manuel")
	if clave == "41323167":
		print("Concedido")
	else: print("Denegado")

import sys #importar modulo para usar sys.exit

print("Escriba exit para salir")
respuesta = input()
if respuesta == "salir": sys.exit()
print("Escribio " + respuesta + ".")

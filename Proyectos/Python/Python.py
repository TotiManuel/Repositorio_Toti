Numero = 1 #Asigno el valor de 1 a la variable Numero
ciudad = "Villa Maria" #Asigno la String de "Villa Maria" a la variable de ciudad
print("Hola " + ciudad) #Imprimo en consola "Hola " + el valor de la variable ciudad(Villa Maria)
print(Numero) #Imprimo en consola el valor de la variable Numero(1)
print(type(9)) #Imprimo en consola que tipo de dato es el valor. (9=int)


Usuario=["Julian", "Martin"]	#Este es un arreglo llamado Usuario que contiene las strings "julian y martin"
usuario=input()	#Espera datos de entrada y los almacena en la variable usuario
if(usuario.lower()=="julian" or usuario.lower()=="martin"):print("si"), exit()  #usuario.lower() es para ver si en el arreglo usuario existen esa string sin importar mayuculas o minusculas. y envia el mensaje si.
else:print("no"),exit()	#si no existen esas strings envia el mensaje no.

#Pequeño programa de prueba
print("Bienvenido Usuario!!!");
print("Este es el sistema de JMM");
print("Dime tu nombre de usuario por favor:");
Usuario=input();
print("Decime la clave " + Usuario + " Por favor");
Clave=input();
if(Usuario.lower()=="julian"):
	if(Clave=="41323167"):print("Acceso Concedido")
	else:print("Acceso Denegado"),exit()
else:print("Acceso Denegado"),exit()
print("Que deseas hacer? ")
Accion=input();

import random
import os
import math

print("Juego de Matematicas")
print("")
nombre=input("Dime Tu Nombre: >> ")
os.system("cls")

#a = arreglo=[[0,0,0],[0,1,1],[1,1,1]]
#b = arregl=[[0,0,0],[1,1,1],[1,0,1]]
#print(arreglo)
#print(b)
#print(c)

def suma():
    print("Suma")
    while True:
        os.system("cls")
        suma1=random.randint(0,10)
        suma2=random.randint(0,10)
        print("Envia 100 para terminar el Juego")
        print("")
        print(suma1, "+", suma2)
        resultado=int(input("Resultado? "))
        if resultado==suma1+suma2:
            print("Correcto")
            input()
        elif resultado==100:
            break
            os.system("cls")
        else:
            print("Incorrecto")
            input()

def resta():
    print("Resta")
    while True:
        os.system("cls")
        while True:
            resta1=random.randint(0,10)
            resta2=random.randint(0,10)
            if resta1>resta2:
                break
        print("Envia 100 para terminar el Juego")
        print("")
        print(resta1, "-", resta2)
        resultado=int(input("Resultado? "))
        if resultado==resta1-resta2:
            print("Correcto")
            input()
        elif resultado==100:
            break
            os.system("cls")
        else:
            print("Incorrecto")
            input()
      
def division():
    print("Division")
    while True:
        os.system("cls")
        while True:
            division1=random.randint(1,10)
            division2=random.randint(1,10)
            if division1>division2:
                break
        print("Envia 100 para terminar el Juego")
        print("")
        print(division1, "%", division2)
        resultado=int(input("Resultado? "))
        if resultado==math.trunc(division1/division2):
            print("Correcto")
            input()
        elif resultado==100:
            break
            os.system("cls")
        else:
            print("Incorrecto")
            input()
 
def multiplicar():
    print("Multiplicar")
    while True:
        os.system("cls")
        multi1=random.randint(0,10)
        multi2=random.randint(0,10)
        print("Envia 100 para terminar el Juego")
        print("")
        print(multi1, "x", multi2)
        resultado=int(input("Resultado? "))
        if resultado==multi1*multi2:
            print("Correcto")
            input()
        elif resultado==100:
            break
            os.system("cls")
        else:
            print("Incorrecto")
            input()

def menu():
    os.system("cls")
    print("")
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicacion")
    print("4) Division")
    print("Presiona cualquier tecla para salir")
    elector_juego=int(input("Hola " + nombre + " , Que Operacion queres aprender hoy? >> "))
    if elector_juego==1:
        suma()
    elif elector_juego==2:
        resta()
    elif elector_juego==3:
        multiplicar()
    elif elector_juego==4:
        division()
    else:
        print("Error")

while True:
    menu() 
  



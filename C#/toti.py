#!/usr/bin/env python
from tkinter import *
import time
import os
import sys
import sqlite3
import getpass

root=Tk()
root.geometry("300x150")
root.title("Biomagnetismo Medico PB")
frame=Frame(root)
frame.place()


usuario=Label(root, text="Usuario: ").place(x=35,y=10)
usuario_uno = Entry(root).place(x=100,y=10)
clave=Label(root, text="Contraseña: ").place(x=10,y=50)
clave_uno = Entry(root, show="*").place(x=100,y=50)
#iniciar_sesion=Button(root, text="Iniciar Sesion", command = openNewWindow).place(x=150,y=90)


root.mainloop()


#registeredUser = ('Julian','Paola','Invitado')
#registeredPW = ('41323167','paola')
#def login(usuario,passw):
#    if usuario in registeredUser:
#        if passw in registeredPW:
#            return 1
#        else:
#            print("\n\tPassword does not match...\n")
#    else:
#        return 2
#usuario=input('Usuario: ')
#passw = getpass.getpass('Contraseña: ')
#if login(usuario,passw)==1:
#    print('Bienvenido ',usuario)
#else:
#    print('ERROR! Usuario no encontrado.')
################################################################
from tkinter import *
from tkinter import messagebox, ttk

root=Tk()
root.geometry("300x150")
root.title("Biomagnetismo Medico PB")
frame=Frame(root)
frame.place()

#def openNewWindow(event=None):
#	if usuario_uno=="toti" and clave_uno=="123":
#		root.withdraw()
#		newWindow = Toplevel(root)
#		width= newWindow.winfo_screenwidth()  
#		height= newWindow.winfo_screenheight() 
#		newWindow.geometry("%dx%d" % (width, height)) 							#newWindow.attributes('-fullscreen', True)
#		newWindow.title("Biomagnetismo Medico PB")
#		menubar = Menu(newWindow)
#		newWindow.config(menu=menubar)
#
#		filemenu = Menu(menubar, tearoff=0)
#		filemenu.add_command(label="Nuevo")
#		filemenu.add_command(label="Abrir")
#		filemenu.add_command(label="Guardar")
#		filemenu.add_command(label="Cerrar")
#
#		filemenu.add_separator()
#		filemenu.add_command(label="Salir", command=root.quit)
#	
#		editmenu = Menu(menubar, tearoff=0)
#		editmenu.add_command(label="Cortar")
#		editmenu.add_command(label="Copiar")
#		editmenu.add_command(label="Pegar")
	
#		helpmenu = Menu(menubar, tearoff=0)
#		helpmenu.add_command(label="Ayuda")
#		helpmenu.add_separator()
#		helpmenu.add_command(label="Acerca de...")
#		menubar.add_cascade(label="Archivo", menu=filemenu)
#		menubar.add_cascade(label="Editar", menu=editmenu)
#		menubar.add_cascade(label="Ayuda", menu=helpmenu) 
#		Label(newWindow, text ="BIENVENIDA PAOLA!!").pack()
#	else:
#		print("nop")


usuario=Label(root, text="Usuario: ").place(x=35,y=10)
usuario_uno = Entry(root).place(x=100,y=10)
clave=Label(root, text="Contraseña: ").place(x=10,y=50)
clave_uno = Entry(root, show="*").place(x=100,y=50)
boton_inicio=Button(root, text="Iniciar Sesion", command = openNewWindow).place(x=150,y=90)


root.mainloop()

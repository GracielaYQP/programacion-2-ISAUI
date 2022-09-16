#Escribir una aplicación GUI (llamada Películas). 
# Su función será: al pulsar el botón Añadir, 
# agregará en el listWidget el contenido de lineEdit (Películas). 
# La aplicación lleva: 
# 1 - 2 Etiquetas (Escribe el título de una película y Películas) 
# 2 - Un lineEdit donde se escribirá el nombre de la película 
# 3 - Un listWidget que registra las películas añadidas 
# 4 - Un botón "Añadir"

from distutils.cmd import Command
from tkinter import *

ventana=Tk() 
ventana.title("Peliculas")
ventana.geometry('550x300')
ventana.config(bg="#E3FF93")

def limpiar():
    pelicula.set("")

def enviar():   
    listado.insert(END,pelicula.get())
    limpiar()

pelicula = StringVar()

etiqueta = Label(ventana,borderwidth = 3,relief="ridge",width = 25, height= 2, text = "Escribe el título de la película", font= ("arial rounded mt bold",12), bg ="#00FF99")
etiqueta.grid(row=2,column =0, sticky = "nsew", padx=7,pady=7,ipady = 5  ) 
pelis = Label(ventana,borderwidth = 3,relief="ridge",width = 25, height= 2, text = "Listado películas", font= ("arial rounded mt bold",12), bg ="#00FF99")
pelis.grid(row=2,column =1, sticky = "nsew", padx=7,pady=7,ipady = 5 ) 

titulo_peli = Entry(ventana, justify= "center",width=25, textvariable=pelicula, font= ("arial rounded mt bold",12),bg = "#00FF99")
titulo_peli.grid (row=3,column = 0, padx=5,pady=5,ipady=15)

listado = Listbox(ventana,width = 30 )
listado.grid (row=3,column = 1, padx=5,pady=5)  #creo el panel donde se van a ver el lsitado de peliculas     

boton_aniadir = Button(ventana, width = 10,height= 2, text = " Añadir ", font = ("arial rounded mt bold",12), command= enviar, bg = "#55ED55")
boton_aniadir.grid (row=7, column=0, sticky= "nsew",padx=5,pady=5)

ventana.mainloop()


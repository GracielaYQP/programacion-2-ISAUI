#Escribir una aplicación GUI (llamada ContCreciente) 
#como la que se ve en la figura. Cada vez que se haga
#  clic en el botón "+", el valor del contador se incrementa en 1.
# El programa lleva 3 componentes: 
# 1 - Una Etiqueta "Contador" 
# 2 - Un lineEdit no editable, que muestre el valor del contador 
# 3 - Un Botón "+"

from tkinter import *
import tkinter #se importa la libreria

def incrementar():
    valor = int(lineEdit ["text"])
    lineEdit ["text"] = f"{valor+1}"

ventana = Tk()   #se crea una ventana dentro de esa libreria
ventana.title("ContCreciente") #se da un titulo a esa ventana
ventana.geometry('300x200') #se configura el tamaño de la ventana
ventana.config(bg="#F9F967") # le da color al fondo de la ventana


etiqueta = Label(ventana,width = 10, borderwidth = 3,relief="ridge", text = "CONTADOR", font= ("arial",12), bg ="#66FFFF" )
etiqueta.place(x = 15, y = 80 )

lineEdit = Label(ventana,width = 10,text = "0" , font= ("arial",12), bg = "#FF9D5B")
lineEdit.place( x = 120, y = 80)


boton_incrementar = Button(ventana, width = 5, text = " + ", font = ("arial",16), command= incrementar, bg= "#0099FF")
boton_incrementar.place(x = 225, y = 70)

ventana.mainloop()
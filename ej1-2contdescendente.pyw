#Escribir una aplicación GUI (llamada ContDecreciente) 
# como la que se ve en la figura. 
# Cada vez que se haga clic en el botón "-", 
# al valor de contador se le resta 1. 
# El programa lleva 3 componentes: 
# 1 - Una Etiqueta "Contador" 
# 2 - Un lineEdit no editable, que muestre el valor de contador 
# y que inicie con el número 88 
# 3 - Un Botón "-"
from tkinter import * #se importa la libreria

def decrementar():
    valor = int(lineEdit ["text"])
    lineEdit ["text"] = f"{valor-1}"

ventana = Tk()   #se crea una ventana dentro de esa libreria
ventana.title("ContCreciente") #se da un titulo a esa ventana
ventana.geometry('300x200') #se configura el tamaño de la ventana
ventana.config(bg="#FFBC8F")
ventana.rowconfigure([0,1,2], minsize = 50, weight= 1)
ventana.columnconfigure([0,1,2],minsize = 50, weight= 1 )

etiqueta = Label(ventana,width = 15, text = "CONTADOR",borderwidth = 3,relief="ridge",font= ("arial bold",12), bg = "#FF9900", )
etiqueta.grid(row=1,column =0,sticky= "nsew" )

lineEdit = Label(ventana,width = 10, text = "88" , font= ("arial bold",12), bg = "white")
lineEdit.grid (row=1,column = 1,sticky= "nsew" )

boton_decrementar = Button(ventana, width = 10, text = " - ", font= ("arial bold",16), bg = "#FFC671",command= decrementar)
boton_decrementar.grid (row=1, column=2, sticky= "nsew")

ventana.mainloop()
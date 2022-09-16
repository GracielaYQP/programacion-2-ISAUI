#scribir una aplicación GUI (llamada Contador) 
# como la que se ve en la figura. 
# Con 3 botones (Count Up - Para incrementar, 
# Count Down - Para restar y Reset - Para comenzar de cero). 
# La aplicación lleva: 
# 1 - Una etiqueta "Contador" 
# 2 - Un lineEdit no editable, que muestre el contador y 
# que inicie en 0 3 - 
# 3 Botones
from tkinter import *
def incrementar():
    valor = int(lineEdit ["text"])
    lineEdit ["text"] = f"{valor+1}"

def decrementar():
    valor = int(lineEdit ["text"])
    lineEdit ["text"] = f"{valor-1}"

def delete():
    valor = int(lineEdit ["text"])
    lineEdit ["text"] = f"0"

ventana = Tk()   
ventana.title("Contador") 
ventana.geometry('600x250')
ventana.resizable(width=False, height=False)
ventana.config(bg="#BFCFEB")
ventana.rowconfigure([0,1,2], minsize = 50, weight= 1)
ventana.columnconfigure([0,1,2,3,4],minsize = 50, weight= 1 )

etiqueta = Label(ventana,width = 15, relief="ridge",text = "CONTADOR",font= ("Showcard Gothic",10), bg = "#507BC8" )
etiqueta.grid(row=1,column =0,sticky= "nsew", padx= 5, pady= 5, ipady=8 )

lineEdit = Label(ventana,width = 10, relief="ridge",text = "0" , font= ("Showcard Gothic",20), bg = "white",fg="black")
lineEdit.grid (row=1,column = 1,sticky= "nsew", padx= 5, pady= 5, ipady=8  )

boton_incrementar = Button(ventana, width = 15, text = " COUNT UP ", font = ("Showcard Gothic",10), command= incrementar, bg = "#7C9EFC")
boton_incrementar.grid (row=1, column=2, sticky= "nsew", padx= 5, pady= 5, ipady=8 )

boton_decrementar = Button(ventana, width = 15, text = "COUNT DOWN ", font= ("Showcard Gothic",10), command= decrementar,bg = "#7C9EFC")
boton_decrementar.grid (row=1, column=3, sticky= "nsew", padx= 5, pady= 5, ipady=8 )

boton_borrar = Button(ventana, width = 15, text = " RESET ", font= ("Showcard Gothic",10), command= delete, bg = "#F94D2B",fg= "black")
boton_borrar.grid (row=1, column=4, sticky= "nsew", padx= 5, pady= 5, ipady=8)

ventana.mainloop()
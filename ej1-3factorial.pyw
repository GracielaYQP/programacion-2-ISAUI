#Escribir una aplicación GUI (llamada Factorial) 
# como la que se ve en la figura. Cada ves que se 
# haga clic en el botón "Siguiente", debe calcular 
# el factorial del primer lineEdit y mostrarlo en el segundo. 
# Al dar siguiente (n se incrementa en 1) n = 2 con 
# su factorial correspondiente.
#La aplicación lleva: 
# 1 - Dos etiquetas: una para n y otra para Factorial (n) 
# 2 - Dos lineEdit no editables 
# 3 - Un botón siguiente

import math
from tkinter import *
 
def calcular():      
    calculo = int(numero.get())+1
    lbresultado.config(text= math.factorial(calculo))
    for i in range(calculo):
        numero.set(calculo)
   

ventana = Tk()   #se crea una ventana dentro de esa libreria
ventana.title("FACTORIAL") #se da un titulo a esa ventana
ventana.geometry('600x370') #se configura el tamaño de la ventana
ventana.resizable(width=False,height=False)
ventana.rowconfigure([0,1,2], minsize = 50, weight= 1)
ventana.columnconfigure([0,1,2,3],minsize = 50, weight= 1 )
ventana.config(bg="#66FFFF")

etiqueta = Label(ventana,width = 15, borderwidth = 3,relief="ridge",text = "n: ", font= ("Cooper Black",14), bg = "#FFDA3B")
etiqueta.grid(row=0,column =0,padx=7,pady=7, ipady = 10 )

numero=IntVar(value=0)                                                   
lineEdit = Entry(ventana,width=15,justify = "center", textvariable=numero,state= "readonly",font= ("Cooper Black",14),bg = "white")
lineEdit.grid (row=0,column = 1, padx=7,pady=7, ipady = 10)

etiqueta = Label(ventana,width = 15, borderwidth = 3,relief="ridge",text = " Factorial de n: ",font= ("Cooper Black",14), bg ="#FFDA3B" )
etiqueta.grid(row=1,column =0 )

lbresultado=Label(ventana,text="1", width = 15, font= ("Cooper Black",12),bg = "white" )
lbresultado.grid(row=1,column=1, padx=7,pady=7,ipady = 10)

boton = Button(ventana, width = 10, text = "Siguiente ", font= ("Cooper Black",14), command= calcular, bg = "#8AB446")
boton.grid (row=2, column=1, padx=7,pady=7, ipady = 10)

ventana.mainloop()
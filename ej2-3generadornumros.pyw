#Escribir una aplicación GUI (llamada Generador de números). 
# Su función será: al pulsar el botón Generar, 
# generará un número aleatorio en el rango de los 
# dos Spin Box. 
# La aplicación lleva: 
# 1 - 3 Etiquetas (Número 1, Número 2 y Número Generado) 
# 2 - 2 Spin Box 
# 3 - 1 lineEdit que no pueda ser modificado 
# 4 - 1 Botón "Generar"
from tkinter import *
import random
from tkinter import messagebox

def generar():
    a = numero1.get()
    b = numero2.get()
    if a<b:
        numero_aleatorio = random.randint(a+1,b-1)
        return numero_generado.set(numero_aleatorio)
    else:
        numero_aleatorio=0
        return messagebox.showwarning("Error","El primer número debe ser menor que el segundo")


ventana=Tk()
ventana.title("Generador de Aleatorios")
ventana.geometry('370x300')
ventana.config(bg="#F9F967")
        
numero1 = IntVar()
numero2 = IntVar()
numero_generado = IntVar()


etiqueta1 = Label(ventana,borderwidth = 3,relief="ridge",width = 15, text = "Número 1", font= ("Brittanic Bold",12), bg ="#FF9900").grid(row=1,column =0, padx = 20, pady = 20, sticky = "nsew" ) 
etiqueta2 = Label(ventana,borderwidth = 3,relief="ridge",width = 15, text = "Número 2", font= ("Brittanic Bold",12), bg ="#FF9900").grid(row=2,column =0, padx = 20, pady = 20, sticky = "nsew" )
etiqueta3 = Label(ventana,borderwidth = 3,relief="ridge",width = 15, text = "Número Generado", font= ("Brittanic Bold",12), bg ="#FF9900").grid(row=3,column =0, padx = 20, pady = 20, sticky = "nsew" )

spin_num1 = Spinbox(from_= -1000, to= 1000, textvariable= numero1). grid(row=1,column =1, padx = 20, pady = 20, sticky = "nsew" )
spin_num2 = Spinbox(from_= -1000, to= 1000,textvariable= numero2). grid(row=2,column =1, padx = 20, pady = 20, sticky = "nsew" )

resultado = Entry(ventana,justify= "center", state = "readonly", width=15,textvariable=numero_generado, font= ("Brittanic Bold",12),bg = "#59E55C").grid (row=3,column = 1, padx=20,pady=20,sticky = "nsew")

boton_generar = Button(ventana, width = 15, text = " Generar ", font = ("Brittanic Bold",12), command= generar, bg = "#1CB420").grid (row=4, column=1,padx=20,pady=20,sticky = "nsew")

ventana.mainloop()
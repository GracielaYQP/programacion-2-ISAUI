#Escribir una aplicación GUI (llamada Calculadora 2) 
# como la que se ve en la figura y que funcione 
# como una calculadora. 
# La aplicación lleva: 
# 1 - 4 Etiquetas (Valor 1, Valor 2, Resultado y Operaciones) 
# 2 - 4 radioButton (Sumar, Restar, Multiplicar y Dividir) 
# 3 - 3 lineEdit (el lineEdit Resultado no puede ser modificado) 
# 4 - 1 botón Calcular, que al ser presionado realice 
# la operación correspondiente.
from tkinter import *
from tkinter import messagebox
def validar():
    try:
        valor1=num1.get()
        valor2 = num2.get()
    except:
        messagebox.showwarning("Error","Debe ingresar dos valores numericos")

def limpiar():
    limpiar = ""
    return f"{(num1).set(limpiar),(num2).set(limpiar),(resultado).set(limpiar)}"

def calcular():
    if opcion.get() == 1:
        validar()
        resultado.set(num1.get() + num2.get())
    elif opcion.get() == 2:
        validar()
        resultado.set(num1.get() - num2.get())
    elif opcion.get() == 3:
        validar()
        resultado.set(num1.get() * num2.get())
    elif opcion.get() == 4:
        validar()
        if int(num2.get())!=0:
            resultado.set(num1.get() / num2.get())
        else:
            messagebox.showerror ("Error", "No es posible dividir por 0")
    
ventana=Tk()
ventana.title("Calculadora")
ventana.geometry('850x450')
ventana.config(bg="#66FF66")

#variables
num1 = IntVar()
num2 = IntVar()
resultado = DoubleVar()
opcion = IntVar()

#Etiquetas
valor1 = Label(ventana,borderwidth = 3,relief="ridge",width = 15, text = "Valor 1", font= ("Goudy stout",12), bg ="#FFFF66")
valor1.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "nsew" ) 
valor2 = Label(ventana,borderwidth = 3,relief="ridge",width = 15, text = "Valor 2", font= ("Goudy stout",12), bg ="#FFFF66")
valor2.grid(row=2,column =0, padx = 5, pady = 5, sticky = "nsew" )
numGenerado = Label(ventana,borderwidth = 3,relief="ridge",width = 15, text = "Número Generado", font= ("Goudy stout",12), bg ="#FFFF66")
numGenerado.grid(row=3,column =0, padx = 5, pady = 5, sticky = "nsew" )
operacion = Label(ventana,borderwidth = 3,relief="ridge",width = 15, text = "Operacion", font= ("Goudy stout",12), bg ="#FFFF66")
operacion.grid(row=1,column =2, padx = 5, pady = 5, sticky = "nsew" )


#Entrys
ingreso1 = Entry(ventana, textvariable=num1, justify= "center", width=15,font= ("arial bold",14),bg = "#66FFFF")
ingreso1.grid (row=1,column = 1, padx=5,pady=5,ipady=15)
ingreso2 = Entry(ventana, textvariable=num2, justify= "center", width=15, font= ("arial bold",14),bg = "#66FFFF")
ingreso2.grid (row=2,column = 1, padx=5,pady=5,ipady=15)
resp = Entry(ventana, textvariable=resultado, state = "readonly", justify= "center", width=15, font= ("arial bold",14), bg = "#66FFFF")
resp.grid (row=3,column = 1, padx=5,pady=5,ipady=15)


#Radiobuttons
rbsumar = Radiobutton(ventana, text="Sumar",value=1, variable = opcion,font= ("Goudy stout",10))
rbsumar.grid(row=2,column =2, padx = 5, pady = 5, ipady= 15, sticky= "w")
rbrestar = Radiobutton(ventana, text="Restar",value=2, variable = opcion,font= ("Goudy stout",10))
rbrestar.grid(row=3,column =2, padx = 5, pady = 5,ipady= 15, sticky= "w" )
rbmultiplicar = Radiobutton(ventana, text="Multiplicar",value=3, variable = opcion,font= ("Goudy stout",10))
rbmultiplicar.grid(row=4,column =2, padx = 5, pady = 5, ipady= 15, sticky= "w")
rbdividir = Radiobutton(ventana, text="Dividir",value=4, variable = opcion,font= ("Goudy stout",10))
rbdividir.grid(row=5,column =2, padx = 5, pady = 5, ipady= 15, sticky= "w")
#boton
boton_calcular = Button(ventana, command = calcular , text = " Calcular ", width = 10,  font = ("Goudy stout",12),  bg = "#FFFF66")
boton_calcular.grid (row=7, column=1,columnspan = 3, padx = 5, pady = 5, ipady= 10, sticky= "w")

ventana.mainloop()
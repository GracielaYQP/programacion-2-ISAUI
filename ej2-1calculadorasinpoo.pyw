
from tkinter import *
from tkinter import messagebox
def validar():
    try:
        valor1=numero1.get()
        valor2 = numero2.get()
    except:
        messagebox.showwarning("Error","Debe ingresar dos valores numericos")

def sumar():
    validar()
    sumar=numero1.get()+numero2.get()
    limpiar()
    return numero3.set(sumar)        
        
def restar():
    validar()
    restar=numero1.get()-numero2.get()
    limpiar()
    return numero3.set(restar)
        
def multiplicar():
    validar()
    multiplicar=numero1.get()*numero2.get()
    limpiar()
    return numero3.set(multiplicar)

def dividir():
    validar()
    if int(numero2.get())!=0:
        dividir=numero1.get()/numero2.get()
        return numero3.set(dividir)
    else:
        return messagebox.showerror ("Error", "No es posible dividir por 0")
    limpiar()
    
    
def porcentaje():
    validar()
    porcentaje=numero1.get()*numero2.get()/100
    limpiar()
    return numero3.set(porcentaje)
    
def limpiar():
    limpiar = ""
    return f"{(numero1).set(limpiar),(numero2).set(limpiar),(numero3).set(limpiar)}"

#otra forma de limmpiar
# def limpiar():
#    numero1.delete(0,END)
#    numero2.delete(0,END)
#    numero3.delete(0,END)

ventana=Tk()
ventana.title("Calculadora")
ventana.geometry('400x350')
ventana.config(bg="#F9F967")
        
numero1 = DoubleVar(value = "")
numero2 = DoubleVar(value = "")
numero3 = DoubleVar(value = "")
        
etiqueta1 = Label(ventana,borderwidth = 3,relief="ridge",width = 15, text = "Primer Número", font= ("Jokerman",12), bg ="#FF822D").grid(row=1,column =0, sticky = "nsew" ) 
ingreso1 = Entry(ventana, justify= "center",  width=20,textvariable=numero1, font= ("Arial Bold",12),bg = "#66FFFF").grid (row=1,column = 2, padx=5,pady=5,ipady=15)
etiqueta2  = Label(ventana,borderwidth = 3,relief="ridge",width = 15, text = "Segundo Número", font= ("Jokerman",12), bg ="#FF822D").grid(row=2,column =0, sticky = "nsew" )
ingreso2 = Entry(ventana, justify= "center",width=20,textvariable=numero2, font= ("Arial Bold",12),bg = "#66FFFF").grid (row=2,column = 2, padx=5,pady=5,ipady=15)
etiqueta3 = Label(ventana,borderwidth = 3,relief="ridge",width = 15, text = "RESULTADO", font= ("Jokerman",12), bg ="#FF822D").grid(row=3,column =0, sticky = "nsew" ) 
resultado = Entry(ventana,justify= "center", state = "readonly", width=20,textvariable=numero3, font= ("Arial Bold",12),bg = "#66FFFF").grid (row=3,column = 2, padx=5,pady=5,ipady=15)
        
boton_sumar = Button(ventana, width = 15, text = " + ", font = ("Jokerman",16), command= sumar, bg = "#55ED55").grid (row=7, column=0, sticky= "nsew")
boton_restar = Button(ventana, width = 15, text = " - ", font = ("Jokerman",16), command= restar, bg = "#55ED55").grid (row=7, column=2, sticky= "nsew")
boton_multiplicar = Button(ventana, width = 15, text = " * ", font = ("Jokerman",16), command= multiplicar, bg = "#55ED55").grid (row=9, column=0, sticky= "nsew")
boton_dividir = Button(ventana, width = 15, text = " / ", font = ("Jokerman",16), command= dividir, bg = "#55ED55").grid (row=9, column=2, sticky= "nsew")
boton_porcentaje = Button(ventana, width = 15, text = " % ", font = ("Jokerman",16), command= porcentaje, bg = "#55ED55").grid (row=11, column=0, sticky= "nsew")
boton_limpiar = Button(ventana, width = 15, text = " Clear ", font = ("Jokerman",16), command= limpiar, bg = "#55ED55").grid (row=11, column=2, sticky= "nsew")
        
ventana.mainloop()
    
    


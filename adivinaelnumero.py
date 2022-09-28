from tkinter import *
from tkinter import messagebox
def arranque():
    ventana0 = Tk()
    ventana0.title("ADIVINO LO QUE PENSAS!!!")
    width= ventana0.winfo_screenwidth() #toma el tamanio del ancho de ventana de la pantalla
    height= ventana0.winfo_screenheight() #toma el tamanio del alto de la pantalla
    ventana0.geometry("%dx%d" % (width, height))#le da a la ventana el tamanio de la pantalla
    ventana0.resizable(width=False, height=False) #fija el tamanio de la pantalla
    ventana0.config(bg="#F9F967")

    def iniciar():
        ventana0.withdraw()
        ventana = Tk()
        ventana.title("ADIVINO LO QUE PENSAS!!!")
        width= ventana.winfo_screenwidth() #toma el tamanio del ancho de ventana de la pantalla
        height= ventana.winfo_screenheight() #toma el tamanio del alto de la pantalla
        ventana.geometry("%dx%d" % (width, height))#le da a la ventana el tamanio de la pantalla
        ventana.resizable(width=False, height=False) #fija el tamanio de la pantalla
        ventana.config(bg="#F9F967")
        def volver_a_jugar():
            abrir_ventana2()
        def abrir_ventana2():
            ventana.withdraw() # borro la ventana anterior
            ventana2 = Toplevel() #creo la nueva ventana
            width= ventana2.winfo_screenwidth()
            height= ventana2.winfo_screenheight()
            ventana2.geometry("%dx%d" % (width, height))
            ventana2.resizable(width=False, height=False)
            ventana2.config(bg= "#F9F967")
            def ingles():
                ventana2.withdraw()
                ventana3 = Toplevel()
                width= ventana3.winfo_screenwidth()
                height= ventana3.winfo_screenheight()
                ventana3.geometry("%dx%d" % (width, height))
                ventana3.config(bg="#F9F967")
                def ordenar():
                    ventana3.withdraw()
                    ventana4 = Toplevel()
                    width= ventana4.winfo_screenwidth()
                    height= ventana4.winfo_screenheight()
                    ventana4.geometry("%dx%d" % (width, height))
                    ventana4.config(bg="#F9F967")
                    def mayor():
                        ventana4.withdraw()
                        ventana5 = Toplevel()
                        width= ventana5.winfo_screenwidth()
                        height= ventana5.winfo_screenheight()
                        ventana5.geometry("%dx%d" % (width, height))
                        ventana5.config(bg="#F9F967")
                        def validar_resta():
                                try:
                                    valor2 = res_resta.get()
                                    if valor2!="0" and valor2!= "" and valor2.isnumeric():
                                        return True
                                    else:
                                        messagebox.showwarning("Error","You must enter a numeric value")
                                        return False
                                except:
                                    messagebox.showwarning("Error","You must enter a numeric value")
                        def seguir():
                            if validar_resta():
                                ventana5.withdraw()
                                ventana6 = Toplevel()
                                width= ventana6.winfo_screenwidth()
                                height= ventana6.winfo_screenheight()
                                ventana6.geometry("%dx%d" % (width, height))
                                ventana6.config(bg="#F9F967")
                                def validar_suma():
                                    try:
                                        valor1 = res_suma.get()
                                        if valor1!="0" and valor1!= ""and valor1.isnumeric():
                                            return True
                                        else:
                                            messagebox.showwarning("Error","You must enter a numeric value")
                                            return False
                                    except:
                                        messagebox.showwarning("Error","You must enter a numeric value")
                                def adivinar():
                                    if validar_suma():
                                        ventana6.withdraw()
                                        ventana7 = Toplevel()
                                        width= ventana7.winfo_screenwidth()
                                        height= ventana7.winfo_screenheight()
                                        ventana7.geometry("%dx%d" % (width, height))
                                        ventana7.config(bg="#F9F967") 

                                        def salir():
                                            ventana7.withdraw()
                                            ventana8 = Toplevel()
                                            width= ventana8.winfo_screenwidth()
                                            height= ventana8.winfo_screenheight()
                                            ventana8.geometry("%dx%d" % (width, height))
                                            ventana8.config(bg="#F9F967")
                                            etiqueta_saludo = Label(ventana8,width = 30, height= 4, borderwidth = 4,relief="ridge", text = "thanks for playing!",anchor= 'center',font= ("Stencil",40), bg ="#66FFFF" )
                                            etiqueta_saludo.place(x=130, y= 200)
                                            boton_inicio = Button(ventana8, command = arranque, text = "RESTART", width = 15,font = ("Stencil",30),  bg = "#66FFFF")
                                            boton_inicio.place(x=800, y= 550)
                                            ventana8.mainloop()
                                        def numero_oculto():    
                                            k = int(res_resta.get())/9
                                            digito1 = (int(res_suma.get()) - k)/2
                                            digito2 = (int(res_suma.get()) + k)/ 2
                                            var = str(int(digito1))+str(int(digito2))
                                            return numero.set(var)
                                        etiqueta11 = Label(ventana7,width = 35, height= 2, borderwidth = 4,relief="ridge", text = "The number is...",anchor= 'center',font= ("Stencil",30), bg ="#66FFFF" )
                                        etiqueta11.place(x=200, y= 100)
                                        numero = IntVar(value="")
                                        etiqueta12 = Entry(ventana7,width = 15, textvariable= numero ,justify= "center",font= ("Stencil",50), bg ="#66FFFF", fg ="#FF0000" , state= "readonly" )
                                        etiqueta12.place(x=320, y= 300)
                                        boton_ver = Button(ventana7, command = numero_oculto, text = "Press to see it!!! ", width = 30,font = ("Stencil",30),  bg = "#66FFFF")
                                        boton_ver.place(x=300, y= 450)
                                        boton_jugar_nuevo = Button(ventana7, command = volver_a_jugar, text = "Play again", width = 15,font = ("Stencil",30),  bg = "#66FFFF")
                                        boton_jugar_nuevo.place(x=800, y= 550)
                                        boton_salir = Button(ventana7, command = salir, text = "Exit", width = 15,font = ("Stencil",30),  bg = "#66FFFF")
                                        boton_salir.place(x=150, y= 550)
                                        ventana7.mainloop()
                            
                                etiqueta8 = Label(ventana6,width = 35, height= 2, borderwidth = 4,relief="ridge", text = "Now add the numbers of the number \n you thought at the beginning. .",anchor= 'center',font= ("Stencil",28), bg ="#66FFFF" )
                                etiqueta8.place(x=250, y= 100)
                                etiqueta9 = Label(ventana6,width = 25, height= 2, borderwidth = 4,relief="ridge", text = "Write the result here:",anchor= 'center',font= ("Stencil",28), bg ="#66FFFF" )
                                etiqueta9.place(x=18, y= 300)
                                res_suma = Entry(ventana6, justify= "left",width=15, font= ("Stencil",30),bg = "#66FFFF")
                                res_suma.place(x = 700 , y = 320)
                                boton_adivinar = Button(ventana6, command = adivinar, text = "If you press here...\n I tell you what number you thought!!! ", width = 35,font = ("Stencil",30),  bg = "#66FFFF")
                                boton_adivinar.place(x=250, y= 450)
                                ventana6.mainloop()

                        etiqueta6 = Label(ventana5,width = 53, height= 2, borderwidth = 4,relief="ridge", text ="So, subtract from the new \n number the one you thought of.",anchor= 'center',font= ("Stencil",28), bg ="#66FFFF" )
                        etiqueta6.place(x=18, y= 100)
                        etiqueta7 = Label(ventana5,width = 25, height= 2, borderwidth = 4,relief="ridge", text = "Write the result here:",anchor= 'center',font= ("Stencil",28), bg ="#66FFFF" )
                        etiqueta7.place(x=18, y= 300)
                        res_resta = Entry(ventana5, justify= "left",width=15, font= ("Stencil",30),bg = "#66FFFF")
                        res_resta.place(x = 700 , y = 320)
                        boton_seguir = Button(ventana5, command = seguir, text = " CONTINUE ", width = 10,font = ("Stencil",30),  bg = "#66FFFF")
                        boton_seguir.place(x=500, y= 520)
                        ventana5.mainloop()

                    def menor():
                        ventana4.withdraw()
                        ventana8 = Toplevel()
                        width= ventana8.winfo_screenwidth()
                        height= ventana8.winfo_screenheight()
                        ventana8.geometry("%dx%d" % (width, height))
                        ventana8.config(bg="#F9F967")
                        def validar_resta():
                                try:
                                    valor2 = res_resta.get()
                                    if valor2!="0" and valor2!= ""and valor2.isnumeric():
                                        return True
                                    elif valor2 == "0":
                                            messagebox.showwarning("Error","You must enter a number other than zero")    
                                    else:    
                                        messagebox.showwarning("Error","You must enter a numeric value")
                                        return False
                                except:
                                    messagebox.showwarning("Error","You must enter a numeric value")
                        def seguir():
                            if validar_resta():
                                ventana8.withdraw()
                                ventana9 = Toplevel()
                                width= ventana9.winfo_screenwidth()
                                height= ventana9.winfo_screenheight()
                                ventana9.geometry("%dx%d" % (width, height))
                                ventana9.config(bg="#F9F967")
                                def validar_suma():
                                        try:
                                            valor1 = res_suma.get()
                                            if valor1!="0" and valor1!= ""and valor1.isnumeric():
                                                return True
                                            elif valor1 == "0":
                                                messagebox.showwarning("Error","You must enter a number other than zero")    
                                            else:    
                                                messagebox.showwarning("Error","You must enter a numeric value")
                                                return False
                                        except:
                                            messagebox.showwarning("Error","You must enter a numeric value")
                                def adivinar():
                                    if validar_suma():
                                        ventana9.withdraw()
                                        ventana10 = Toplevel()
                                        width= ventana10.winfo_screenwidth()
                                        height= ventana10.winfo_screenheight()
                                        ventana10.geometry("%dx%d" % (width, height))
                                        ventana10.config(bg="#F9F967")
                                        def salir():
                                            ventana10.withdraw()
                                            ventana11 = Toplevel()
                                            width= ventana11.winfo_screenwidth()
                                            height= ventana11.winfo_screenheight()
                                            ventana11.geometry("%dx%d" % (width, height))
                                            ventana11.config(bg="#F9F967")
                                            etiqueta_saludo = Label(ventana11,width = 30, height= 4, borderwidth = 4,relief="ridge", text = "thanks for playing!",anchor= 'center',font= ("Stencil",40), bg ="#66FFFF" )
                                            etiqueta_saludo.place(x=130, y= 200)
                                            boton_inicio = Button(ventana11, command = arranque, text = "RESTART", width = 15,font = ("Stencil",30),  bg = "#66FFFF")
                                            boton_inicio.place(x=800, y= 550)
                                            ventana11.mainloop()
                                        def numero_oculto():
                                            k = int(res_resta.get())/9
                                            digito1 = (int(res_suma.get()) + k)/2
                                            digito2 = (int(res_suma.get()) - k)/ 2
                                            var = str(int(digito1))+str(int(digito2))
                                            return numero.set(var)
                                        etiqueta_11 = Label(ventana10,width = 35, height= 2, borderwidth = 4,relief="ridge", text = "The number is...",anchor= 'center',font= ("Stencil",30), bg ="#66FFFF" )
                                        etiqueta_11.place(x=200, y= 100)
                                        numero = IntVar(value="")
                                        etiqueta_12 = Entry(ventana10,width = 15, textvariable= numero ,justify= "center",font= ("Stencil",50), bg ="#66FFFF", fg ="#FF0000" , state= "readonly" )
                                        etiqueta_12.place(x=320, y= 300)
                                        boton_ver = Button(ventana10, command = numero_oculto, text = "Press to see it!!! ", width = 30,font = ("Stencil",30),  bg = "#66FFFF")
                                        boton_ver.place(x=300, y= 450)
                                        boton_jugar_nuevo = Button(ventana10, command = volver_a_jugar, text = "Play again", width = 15,font = ("Stencil",30),  bg = "#66FFFF")
                                        boton_jugar_nuevo.place(x=800, y= 550)
                                        boton_salir = Button(ventana10, command = salir, text = "Exit", width = 15,font = ("Stencil",30),  bg = "#66FFFF")
                                        boton_salir.place(x=150, y= 550)
                                        ventana10.mainloop()
                                etiqueta_8 = Label(ventana9,width = 35, height= 2, borderwidth = 4,relief="ridge", text = "Now, add up the digits of the number \n you thought of at first.",anchor= 'center',font= ("Stencil",28), bg ="#66FFFF" )
                                etiqueta_8.place(x=250, y= 100)
                                etiqueta_9 = Label(ventana9,width = 25, height= 2, borderwidth = 4,relief="ridge", text = "Write the result here:",anchor= 'center',font= ("Stencil",28), bg ="#66FFFF" )
                                etiqueta_9.place(x=18, y= 300)
                                res_suma = Entry(ventana9, justify= "left",width=15, font= ("Stencil",30),bg = "#66FFFF")
                                res_suma.place(x = 700 , y = 320)
                                boton_adivinar = Button(ventana9, command = adivinar, text = "If you press here...\n I tell you what number you thought!!! ", width = 35,font = ("Stencil",30),  bg = "#66FFFF")
                                boton_adivinar.place(x=250, y= 450)
                                ventana9.mainloop()

                        etiqueta_6 = Label(ventana8,width = 53, height= 2, borderwidth = 4,relief="ridge", text = "So, subtract the number you \n thought first from the new number",anchor= 'center',font= ("Stencil",28), bg ="#66FFFF" )
                        etiqueta_6.place(x=18, y= 100)
                        etiqueta_7 = Label(ventana8,width = 25, height= 2, borderwidth = 4,relief="ridge", text = "Write the result here:",anchor= 'center',font= ("Stencil",28), bg ="#66FFFF" )
                        etiqueta_7.place(x=18, y= 300)
                        res_resta = Entry(ventana8, justify= "left",width=15, font= ("Stencil",30),bg = "#66FFFF")
                        res_resta.place(x = 700 , y = 320)
                        boton_seguir = Button(ventana8, command = seguir, text = " Continue ", width = 10,font = ("Stencil",30),  bg = "#66FFFF")
                        boton_seguir.place(x=500, y= 520)
                        ventana8.mainloop()

                    etiqueta_5 = Label(ventana4,width = 49, height= 2, borderwidth = 4,relief="ridge", text = "Now reverse the order of the figures",anchor= 'center',font= ("Stencil",30), bg ="#66FFFF" )
                    etiqueta_5.place(x=18, y= 40)            
                    etiqueta5a = Label(ventana4,width = 49, height= 2, borderwidth = 4,relief="ridge", text = "Is the new number higher or lower than the first?",anchor= 'center',font= ("Stencil",30), bg ="#66FFFF" )
                    etiqueta5a.place(x=18, y= 240)
                    boton_mayor = Button(ventana4, command = mayor, text = " Higher ", width = 10,font = ("Stencil",30),  bg = "#66FFFF")
                    boton_mayor.place(x=200, y= 450)
                    boton_menor = Button(ventana4, command = menor, text = " Lower ", width = 10,font = ("Stencil",30),  bg = "#66FFFF")
                    boton_menor.place(x=800, y= 450)
                    ventana4.mainloop()

                etiqueta3 = Label(ventana3,width = 48, height= 2, borderwidth = 4,relief="ridge", text = "Think of a two-digit number (not equal). ...",anchor= 'center',font= ("Stencil",30), bg ="#66FFFF" )
                etiqueta3.place(x=25, y= 100)
                etiqueta4 = Label(ventana3,width = 40, height= 2, borderwidth = 4,relief="ridge", text = "Ready???? Press continue!",anchor= 'center',font= ("Stencil",30), bg ="#66FFFF" )
                etiqueta4.place(x=150, y= 300)
                boton_siguiente = Button(ventana3, command = ordenar, text = " Continue ", width = 10,font = ("Stencil",30),  bg = "#66FFFF")
                boton_siguiente.place(x=500, y= 500)
                ventana3.mainloop()    
            def spanish():
                ventana2.withdraw()
                ventana3 = Toplevel()
                width= ventana3.winfo_screenwidth()
                height= ventana3.winfo_screenheight()
                ventana3.geometry("%dx%d" % (width, height))
                ventana3.config(bg="#F9F967")
                def ordenar():
                    ventana3.withdraw()
                    ventana4 = Toplevel()
                    width= ventana4.winfo_screenwidth()
                    height= ventana4.winfo_screenheight()
                    ventana4.geometry("%dx%d" % (width, height))
                    ventana4.config(bg="#F9F967")
                    def mayor():
                        ventana4.withdraw()
                        ventana5 = Toplevel()
                        width= ventana5.winfo_screenwidth()
                        height= ventana5.winfo_screenheight()
                        ventana5.geometry("%dx%d" % (width, height))
                        ventana5.config(bg="#F9F967")
                        def validar_resta():
                                try:
                                    valor2 = res_resta.get()
                                    if valor2!="0" and valor2!= ""and valor2.isnumeric():
                                        return True
                                    elif valor2 =="0":
                                        messagebox.showwarning("Error","Debe ingresar un número distinto de cero")
                                    else:
                                        messagebox.showwarning("Error","Debe ingresar un valor numérico")
                                        return False
                                except:
                                    messagebox.showwarning("Error","Debe ingresar un valor numérico")
                        def seguir():
                            if validar_resta():
                                ventana5.withdraw()
                                ventana6 = Toplevel()
                                width= ventana6.winfo_screenwidth()
                                height= ventana6.winfo_screenheight()
                                ventana6.geometry("%dx%d" % (width, height))
                                ventana6.config(bg="#F9F967")
                                def validar_suma():
                                    try:
                                        valor1 = res_suma.get()
                                        if valor1!="0" and valor1!= ""and valor1.isnumeric():
                                            return True
                                        elif valor1 =="0":
                                            messagebox.showwarning("Error","Debe ingresar un número distinto de cero")
                                        else:
                                            messagebox.showwarning("Error","Debe ingresar un valor numérico")
                                            return False
                                    except:
                                        messagebox.showwarning("Error","Debe ingresar un valor numérico")
                                def adivinar():
                                    if validar_suma():
                                        ventana6.withdraw()
                                        ventana7 = Toplevel()
                                        width= ventana7.winfo_screenwidth()
                                        height= ventana7.winfo_screenheight()
                                        ventana7.geometry("%dx%d" % (width, height))
                                        ventana7.config(bg="#F9F967") 
                                        def salir():
                                            ventana7.withdraw()
                                            ventana8 = Toplevel()
                                            width= ventana8.winfo_screenwidth()
                                            height= ventana8.winfo_screenheight()
                                            ventana8.geometry("%dx%d" % (width, height))
                                            ventana8.config(bg="#F9F967")
                                            etiqueta_saludo = Label(ventana8,width = 30, height= 4, borderwidth = 4,relief="ridge", text = "Gracias por jugar!!!",anchor= 'center',font= ("Stencil",40), bg ="#66FFFF" )
                                            etiqueta_saludo.place(x=130, y= 200)
                                            boton_inicio = Button(ventana8, command = arranque, text = "Reiniciar", width = 15,font = ("Stencil",30),  bg = "#66FFFF")
                                            boton_inicio.place(x=800, y= 550)
                                            ventana8.mainloop()

                                        def numero_oculto():    
                                            k = int(res_resta.get())/9
                                            digito1 = (int(res_suma.get()) - k)/2
                                            digito2 = (int(res_suma.get()) + k)/ 2
                                            var = str(int(digito1))+str(int(digito2))
                                            return numero.set(var)
                                        etiqueta11 = Label(ventana7,width = 35, height= 2, borderwidth = 4,relief="ridge", text = "El número es...",anchor= 'center',font= ("Stencil",30), bg ="#66FFFF" )
                                        etiqueta11.place(x=200, y= 80)
                                        numero = IntVar(value="")
                                        etiqueta12 = Entry(ventana7,width = 15, textvariable= numero ,justify= "center",font= ("Stencil",60), bg ="#66FFFF", fg ="#FF0000" , state= "readonly" )
                                        etiqueta12.place(x=320, y= 280)
                                        boton_ver = Button(ventana7, command = numero_oculto, text = "Presioná para verlo!!! ", width = 30,font = ("Stencil",30),  bg = "#66FFFF")
                                        boton_ver.place(x=300, y= 430)
                                        boton_jugar_nuevo = Button(ventana7, command = volver_a_jugar, text = "Volver a jugar", width = 15,font = ("Stencil",30),  bg = "#66FFFF")
                                        boton_jugar_nuevo.place(x=800, y= 550)
                                        boton_salir = Button(ventana7, command = salir, text = "salir", width = 15,font = ("Stencil",30),  bg = "#66FFFF")
                                        boton_salir.place(x=150, y= 550)
                                        ventana7.mainloop()
                                
                                etiqueta8 = Label(ventana6,width = 35, height= 2, borderwidth = 4,relief="ridge", text = "Ahora, sumá las cifras del número \n que pensaste al principio.",anchor= 'center',font= ("Stencil",28), bg ="#66FFFF" )
                                etiqueta8.place(x=250, y= 100)
                                etiqueta9 = Label(ventana6,width = 25, height= 2, borderwidth = 4,relief="ridge", text = "Escribí el resultado aquí:",anchor= 'center',font= ("Stencil",28), bg ="#66FFFF" )
                                etiqueta9.place(x=18, y= 300)
                                res_suma = Entry(ventana6, justify= "left",width=15, font= ("Stencil",30),bg = "#66FFFF")
                                res_suma.place(x = 700 , y = 320)
                                boton_adivinar = Button(ventana6, command = adivinar, text = "Si presionas aquí...\n te digo qué número pensaste!!! ", width = 30,font = ("Stencil",30),  bg = "#66FFFF")
                                boton_adivinar.place(x=300, y= 450)
                                ventana6.mainloop()

                        etiqueta6 = Label(ventana5,width = 53, height= 2, borderwidth = 4,relief="ridge", text = "Entonces, restale al nuevo número el que pensaste.",anchor= 'center',font= ("Stencil",28), bg ="#66FFFF" )
                        etiqueta6.place(x=18, y= 100)
                        etiqueta7 = Label(ventana5,width = 25, height= 2, borderwidth = 4,relief="ridge", text = "Escribí el resultado aquí:",anchor= 'center',font= ("Stencil",28), bg ="#66FFFF" )
                        etiqueta7.place(x=18, y= 300)
                        res_resta = Entry(ventana5, justify= "left",width=15, font= ("Stencil",30),bg = "#66FFFF")
                        res_resta.place(x = 700 , y = 320)
                        boton_seguir = Button(ventana5, command = seguir, text = " SEGUIR ", width = 10,font = ("Stencil",30),  bg = "#66FFFF")
                        boton_seguir.place(x=500, y= 520)
                        ventana5.mainloop()

                    def menor():
                        ventana4.withdraw()
                        ventana8 = Toplevel()
                        width= ventana8.winfo_screenwidth()
                        height= ventana8.winfo_screenheight()
                        ventana8.geometry("%dx%d" % (width, height))
                        ventana8.config(bg="#F9F967")
                        def validar_resta():
                                try:
                                    valor2 = res_resta.get()
                                    if valor2!="0" and valor2!= ""and valor2.isnumeric():
                                        return True
                                    elif valor2 =="0":
                                        messagebox.showwarning("Error","Debe ingresar un número distinto de cero")
                                    else:
                                        messagebox.showwarning("Error","Debe ingresar un valor numérico")
                                        return False
                                except:
                                    messagebox.showwarning("Error","Debe ingresar un valor numérico")
                        def seguir():
                            if validar_resta():
                                ventana8.withdraw()
                                ventana9 = Toplevel()
                                width= ventana9.winfo_screenwidth()
                                height= ventana9.winfo_screenheight()
                                ventana9.geometry("%dx%d" % (width, height))
                                ventana9.config(bg="#F9F967")
                                def validar_suma():
                                        try:
                                            valor1 = res_suma.get()
                                            if valor1!="0" and valor1!= ""and valor1.isnumeric():
                                                return True
                                            elif valor1 =="0":
                                                messagebox.showwarning("Error","Debe ingresar un número distinto de cero")
                                            else:
                                                messagebox.showwarning("Error","Debe ingresar un valor numérico")
                                                return False
                                        except:
                                            messagebox.showwarning("Error","Debe ingresar un valor numérico")
                                def adivinar():
                                    if validar_suma():
                                        ventana9.withdraw()
                                        ventana10 = Toplevel()
                                        width= ventana10.winfo_screenwidth()
                                        height= ventana10.winfo_screenheight()
                                        ventana10.geometry("%dx%d" % (width, height))
                                        ventana10.config(bg="#F9F967")
                                        def salir():
                                            ventana10.withdraw()
                                            ventana11 = Toplevel()
                                            width= ventana11.winfo_screenwidth()
                                            height= ventana11.winfo_screenheight()
                                            ventana11.geometry("%dx%d" % (width, height))
                                            ventana11.config(bg="#F9F967")
                                            etiqueta_saludo = Label(ventana11,width = 30, height= 4, borderwidth = 4,relief="ridge", text = "Gracias por jugar!!!",anchor= 'center',font= ("Stencil",40), bg ="#66FFFF" )
                                            etiqueta_saludo.place(x=130, y= 200)
                                            boton_inicio = Button(ventana11, command = arranque, text = "REINICIAR", width = 15,font = ("Stencil",30),  bg = "#66FFFF")
                                            boton_inicio.place(x=800, y= 550)
                                            ventana11.mainloop()
                                        def numero_oculto():
                                            k = int(res_resta.get())/9
                                            digito1 = (int(res_suma.get()) + k)/2
                                            digito2 = (int(res_suma.get()) - k)/ 2
                                            var = str(int(digito1))+str(int(digito2))
                                            return numero.set(var)
                                        etiqueta_11 = Label(ventana10,width = 35, height= 2, borderwidth = 4,relief="ridge", text = "El número es...",anchor= 'center',font= ("Stencil",30), bg ="#66FFFF" )
                                        etiqueta_11.place(x=200, y= 100)
                                        numero = IntVar(value="")
                                        etiqueta_12 = Entry(ventana10,width = 15, textvariable= numero ,justify= "center",font= ("Stencil",50), bg ="#66FFFF", fg ="#FF0000" , state= "readonly" )
                                        etiqueta_12.place(x=320, y= 300)
                                        boton_ver = Button(ventana10, command = numero_oculto, text = "Presioná para verlo!!! ", width = 30,font = ("Stencil",30),  bg = "#66FFFF")
                                        boton_ver.place(x=300, y= 450)
                                        boton_jugar_nuevo = Button(ventana10, command = volver_a_jugar, text = "Volver a jugar", width = 15,font = ("Stencil",30),  bg = "#66FFFF")
                                        boton_jugar_nuevo.place(x=800, y= 550)
                                        boton_salir = Button(ventana10, command = salir, text = "salir", width = 15,font = ("Stencil",30),  bg = "#66FFFF")
                                        boton_salir.place(x=150, y= 550)
                                        ventana10.mainloop()
                                etiqueta_8 = Label(ventana9,width = 35, height= 2, borderwidth = 4,relief="ridge", text = "Ahora, sumá las cifras del número \n que pensaste al principio.",anchor= 'center',font= ("Stencil",28), bg ="#66FFFF" )
                                etiqueta_8.place(x=250, y= 100)
                                etiqueta_9 = Label(ventana9,width = 25, height= 2, borderwidth = 4,relief="ridge", text = "Escribí el resultado aquí:",anchor= 'center',font= ("Stencil",28), bg ="#66FFFF" )
                                etiqueta_9.place(x=18, y= 300)
                                res_suma = Entry(ventana9, justify= "left",width=15, font= ("Stencil",30),bg = "#66FFFF")
                                res_suma.place(x = 700 , y = 320)
                                boton_adivinar = Button(ventana9, command = adivinar, text = "Si presionas aquí...\n te digo qué número pensaste!!! ", width = 30,font = ("Stencil",30),  bg = "#66FFFF")
                                boton_adivinar.place(x=300, y= 450)
                                ventana9.mainloop()

                        etiqueta_6 = Label(ventana8,width = 53, height= 2, borderwidth = 4,relief="ridge", text = "Entonces, restale al número que pensaste el nuevo número.",anchor= 'center',font= ("Stencil",28), bg ="#66FFFF" )
                        etiqueta_6.place(x=18, y= 100)
                        etiqueta_7 = Label(ventana8,width = 25, height= 2, borderwidth = 4,relief="ridge", text = "Escribí el resultado aquí:",anchor= 'center',font= ("Stencil",28), bg ="#66FFFF" )
                        etiqueta_7.place(x=18, y= 300)
                        res_resta = Entry(ventana8, justify= "left",width=15, font= ("Stencil",30),bg = "#66FFFF")
                        res_resta.place(x = 700 , y = 320)
                        boton_seguir = Button(ventana8, command = seguir, text = " SEGUIR ", width = 10,font = ("Stencil",30),  bg = "#66FFFF")
                        boton_seguir.place(x=500, y= 520)
                        ventana8.mainloop()

                    etiqueta_5 = Label(ventana4,width = 49, height= 2, borderwidth = 4,relief="ridge", text = "Invertí el orden de las cifras",anchor= 'center',font= ("Stencil",30), bg ="#66FFFF" )
                    etiqueta_5.place(x=18, y= 40)            
                    etiqueta5a = Label(ventana4,width = 49, height= 2, borderwidth = 4,relief="ridge", text = "El nuevo número es mayor o menor que el primero?",anchor= 'center',font= ("Stencil",30), bg ="#66FFFF" )
                    etiqueta5a.place(x=18, y= 240)
                    boton_mayor = Button(ventana4, command = mayor, text = " MAYOR ", width = 10,font = ("Stencil",30),  bg = "#66FFFF")
                    boton_mayor.place(x=200, y= 450)
                    boton_menor = Button(ventana4, command = menor, text = " MENOR ", width = 10,font = ("Stencil",30),  bg = "#66FFFF")
                    boton_menor.place(x=800, y= 450)
                    ventana4.mainloop()

                etiqueta3 = Label(ventana3,width = 48, height= 2, borderwidth = 4,relief="ridge", text = "Pensá un número de dos cifras (que no sean iguales)...",anchor= 'center',font= ("Stencil",30), bg ="#66FFFF" )
                etiqueta3.place(x=25, y= 100)
                etiqueta4 = Label(ventana3,width = 40, height= 2, borderwidth = 4,relief="ridge", text = "Listo???? Presioná SEGUIR!",anchor= 'center',font= ("Stencil",30), bg ="#66FFFF" )
                etiqueta4.place(x=150, y= 300)
                boton_siguiente = Button(ventana3, command = ordenar, text = " SEGUIR ", width = 10,font = ("Stencil",30),  bg = "#66FFFF")
                boton_siguiente.place(x=500, y= 500)
                ventana3.mainloop()

            etiqueta2 = Label(ventana2,width = 45, height= 2, borderwidth = 4,relief="ridge", text = "ELEGÍ EL IDIOMA CON EL QUE QUERÉS INTERACTUAR",anchor= 'center',font= ("Stencil",30), bg ="#66FFFF" )
            etiqueta2.place(x=80, y= 150)
            boton_ingles = Button(ventana2, command = ingles, text = " INGLES ", width = 10,font = ("Stencil",30),  bg = "#66FFFF")
            boton_ingles.place(x=800, y= 400)
            boton_spanish = Button(ventana2, command = spanish, text = " ESPAÑOL ", width = 10,font = ("Stencil",30),  bg = "#66FFFF")
            boton_spanish.place(x=200, y= 400)
            ventana2.mainloop()

        etiqueta = Label(ventana,width = 45, height= 2, borderwidth = 4,relief="ridge", text = "PUEDO ADIVINAR EL NÚMERO QUE ESTÁS PENSANDO...",anchor= 'center',font= ("Stencil",30), bg ="#66FFFF" )
        etiqueta.place(x=60, y= 100)
        etiqueta1 = Label(ventana,width = 45, height= 2, borderwidth = 4,relief="ridge", text = "Si querés jugar, presioná el boton",anchor= 'center',font= ("Stencil",30), bg ="#66FFFF" )
        etiqueta1.place(x=60, y= 300)
        boton_jugar = Button(ventana, command = abrir_ventana2, text = " JUGAR ", width = 10,font = ("Stencil",30),  bg = "#66FFFF")
        boton_jugar.place(x=500, y= 500)
        ventana.mainloop()
    etiqueta_bienvenido = Label(ventana0,width = 30, height= 4, borderwidth = 4,relief="ridge", text = "BIENVENIDOS!!!",anchor= 'center',font= ("Stencil",40), bg ="#66FFFF" )
    etiqueta_bienvenido.place(x=130, y= 200)
    boton_jugar_nuevo = Button(ventana0, command = iniciar, text = "Comenzar", width = 15,font = ("Stencil",30),  bg = "#66FFFF")
    boton_jugar_nuevo.place(x=800, y= 550)
    
    ventana0.mainloop()
arranque()
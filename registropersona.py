from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkcalendar import Calendar
from conexion import *

ventana = Tk()
ventana.title("REGISTRO")
width= ventana.winfo_screenwidth() 
height= ventana.winfo_screenheight() 
ventana.geometry("%dx%d" % (width, height))
ventana.resizable(width=False, height=False) 
ventana.config(bg="#B9FFE8")
def cargar_seleccion(event):
    selection = elegir_tipo_persona.get()
    messagebox.showinfo(title="Nuevo elemento seleccionado",message=selection)
    if selection =="Paciente":
        paciente()

frame1 = LabelFrame(ventana,font= ("arial",20),text = "Registro",bg="#B9FFE8" )
frame1.grid(row=0,column=0,padx=500,pady=300,ipadx= 5, ipady= 5,sticky=NSEW,columnspan=2)
frame1.config(width=40,height=40,relief="sunken",bd=3 )
tipo_persona = Label(frame1,width = 10 ,text = "REGISTRO", font= ("arial",18), bg ="#89FFD8"  )
tipo_persona.grid(row=0,column=0,padx=10,pady=10,ipadx= 5, ipady= 5)
elegir_tipo_persona = Combobox(frame1, font= ("arial",18), values=("Paciente", "Médico Solicitante","Técnico/Bioquímico"))
elegir_tipo_persona.grid(row=0,column=0,padx=10 ,pady=10,ipadx= 5, ipady= 5)
elegir_tipo_persona.bind("<<ComboboxSelected>>", cargar_seleccion)

def paciente():
    ventana.withdraw() 
    ventanaPaciente = Toplevel()
    width= ventana.winfo_screenwidth() 
    height= ventana.winfo_screenheight() 
    ventanaPaciente.geometry("%dx%d" % (width, height))
    ventanaPaciente.resizable(width=False, height=False) 
    ventanaPaciente.config(bg="#B9FFE8")
    
    frame1 = LabelFrame(ventanaPaciente,bg="#B9FFE8" )
    frame1.grid(row=0,column=0,padx=500,pady=10,ipadx= 5, ipady= 5,sticky=NSEW,columnspan=2)
    frame1.config(width=20,height=20,relief="sunken",bd=3 )
    tipo_persona = Label(frame1,width = 20 ,text = "DATOS DEL PACIENTE", font= ("arial",12), bg ="#B9FFE8"  )
    tipo_persona.grid(row=0,column=0,padx=10,pady=10,ipadx= 5, ipady= 5)
    
    frame2 = LabelFrame(ventanaPaciente,font= ("arial",13),text = "Datos personales",bg="#B9FFE8" )
    frame2.grid(row=1,column=0,padx=40,pady=10,ipadx= 15, ipady= 15,sticky=NW)
    frame2.config(width=450,height=300,relief="sunken",bd=3)
    def validar_apellido(self,apellido):
        while (apellido1.isspace() or len(apellido1) <= 2):
            messagebox.showerror(title="Opcion inválida",message="Mínimo de carácteres en Apellido: 2 y no debe comenzar con un espacio")
            self.apellido.set('')
            validar_apellido(apellido1)
        else:
            return True
    def validar_nombre(self,nombre):
        while (nombre1.isspace() or len(nombre1) <= 1):
            messagebox.showerror(title="Opcion inválida",message="Mínimo de carácteres en Nombre: 3 y no debe comenzar con un espacio")
            self.nombre.set('')
            validar_nombre(nombre1)
        else:
            return True
    def dni_numerico(self,dni):
        while len (dni1) not in range (6, 9) or any(num.isalpha() for num in dni1):
            messagebox.showerror(title="Opcion inválida",message="El campo DNI acepta sólo números.Mínimo de caracteres: 6 y máximo de caracteres: 9")
            self.dni.set('')
            dni_numerico(dni1)
        else:
            dniInt = int(dni)
            return True
    def cargar_seleccion_sexo(event):
        selection = elegir_sexo.get()
        messagebox.showinfo(title="Nuevo elemento seleccionado",message=selection)
    def cargar_seleccion_genero(event):
        selection = elegir_genero.get()
        messagebox.showinfo(title="Nuevo elemento seleccionado",message=selection)
    def elegir_fecha():  
        ventana_fecha = Tk()
        ventana_fecha.title("Fecha de nacimiento") 
        ventana_fecha.geometry("400x400") 
        cal = Calendar(ventana_fecha, selectmode = 'day', 
                    year = 2020, month = 5, 
                    day = 22)  
        cal.pack(pady = 20) 
        def grad_date(): 
            fecha.config(text = "La fecha seleccionada es: " + cal.get_date()) 
        fechaAGuardar= cal.get_date()
        Button(ventana_fecha, text = "Obtener fecha", 
            command = grad_date).pack(pady = 20) 
        fecha = Label(ventana_fecha, text = "") 
        fecha.pack(pady = 20) 
        ventana_fecha.mainloop()
    def limpiar_campos(self):
        self.dni1.set('')
        self.apellido1.set('')
        self.nombre1.set('')
        self.fecha_nacimiento2.set('')
        self.nacionalidad1.set('')
        self.cargar_seleccion_genero.set('')
        
    def limpio_Dni(self):
        self.dni.set('')

    dni = Label(frame2,width = 20,anchor="w", text = "DNI *", font= ("arial",12), bg ="#89FFD8"  )
    dni.grid(row=0,column=0,padx=10,pady=10,ipadx= 5, ipady= 5,sticky=W )
    dni1 = Entry(frame2,width = 30, font= ("arial",12), bg ="white"  )
    dni1.grid(row=0,column=1, padx=10,pady=10,ipadx= 5, ipady= 5)
    apellido = Label(frame2,width = 20, anchor="w",text = "APELLIDO *",  font= ("arial",12), bg ="#89FFD8"  )
    apellido.grid(row=1,column=0, padx=10,pady=10,ipadx= 5, ipady= 5)
    apellido1 = Entry(frame2,width = 30, font= ("arial",12), bg ="white"  )
    apellido1.grid(row=1,column=1,padx=10,pady=10,ipadx= 5, ipady= 5)
    nombre = Label(frame2,width = 20, anchor="w",text = "NOMBRE *", font= ("arial",12), bg ="#89FFD8"  )
    nombre.grid(row=2,column=0,padx=10,pady=10,ipadx= 5, ipady= 5,sticky=W)
    nombre1 = Entry(frame2,width = 30, font= ("arial",12), bg ="white"  )
    nombre1.grid(row=2,column=1,padx=10,pady=10,ipadx= 5, ipady= 5)
    fecha_nacimiento = Label(frame2,width = 20,anchor="w", text = "FECHA DE NACIMIENTO *", font= ("arial",12), bg ="#89FFD8"  )
    fecha_nacimiento.grid(row=3,column=0,padx=10,pady=10,ipadx= 5, ipady= 5)
    fecha_nacimiento1 = Button(frame2,width = 30, font= ("arial",12), text = "Seleccionar fecha",command = elegir_fecha, bg ="white"  )
    fecha_nacimiento1.grid(row=3,column=1,padx=10,pady=10,ipadx= 5, ipady= 5)
    #fecha_nacimiento2 = Entry(frame2,width = 30, font= ("arial",12),textvariable= fechaAGuardar, bg ="white"  )
    #fecha_nacimiento2.grid(row=3,column=1,padx=10,pady=10,ipadx= 5, ipady= 5)
    nacionalidad = Label(frame2,width = 20, anchor="w",text = "NACIONALIDAD *", font= ("arial",12), bg ="#89FFD8"  )
    nacionalidad.grid(row=4,column=0,padx=10,pady=10,ipadx= 5, ipady= 5)
    nacionalidad1 = Entry(frame2,width = 30, font= ("arial",12), bg ="white"  )
    nacionalidad1.grid(row=4,column=1,padx=10,pady=10,ipadx= 5, ipady= 5)
    genero = Label(frame2,width = 20, anchor="w",text = "GÉNERO *", font= ("arial",12), bg ="#89FFD8"  )
    genero.grid(row=5,column=0,padx=10,pady=10,ipadx= 5, ipady= 5)
    elegir_genero= Combobox(frame2, font= ("arial",12), values=["Femenino", "Masculino", "No Binario", "Otro"])
    elegir_genero.grid(row=5,column=1,padx=10 ,pady=10,ipadx= 5, ipady= 5)
    elegir_genero.bind("<<ComboboxSelected>>", cargar_seleccion_genero)
    sexo = Label(frame2,width = 20, anchor="w",text = "SEXO *", font= ("arial",12), bg ="#89FFD8"  )
    sexo.grid(row=6,column=0,padx=10,pady=10,ipadx= 5, ipady= 5)
    elegir_sexo= Combobox(frame2, font= ("arial",12), values=["Masculino", "Femenino", "Intersex"])
    elegir_sexo.grid(row=6,column=1,padx=10 ,pady=10,ipadx= 5, ipady= 5)
    elegir_sexo.bind("<<ComboboxSelected>>", cargar_seleccion_sexo)


    frame3 = LabelFrame(ventanaPaciente,font= ("arial",13),text = "Datos de Contacto",bg="#B9FFE8" )
    frame3.grid(row=1,column=1,padx=40,pady=10,ipadx= 15, ipady= 15,sticky=NW)
    frame3.config(width=450,height=300,relief="sunken",bd=3)
    def validar_calle(self,calle):
        while (calle1.isspace() or len(calle1) <= 2):
            messagebox.showerror(title="Opcion inválida",message="Mínimo de carácteres en Calle: 2 y no debe comenzar con un espacio")
            self.calle.set('')
            validar_calle(calle1)
        else:
            return True
    def altura_numero(self,altura):
        while len (altura1) not in range (1, 6) or any(num.isalpha() for num in altura1):
            messagebox.showerror(title="Opcion inválida",message="El campo Altura acepta sólo números.Mínimo de caracteres: 1 y máximo de caracteres: 6")
            self.altura.set('')
            altura_numero(altura1)
        else:
            altura1Int = int(altura1)
            return True
    def validar_nombre_barrio(self,barrio):
        while (barrio.isspace() or len(barrio) <= 1):
            messagebox.showerror(title="Opcion inválida",message="Mínimo de carácteres en Barrio: 3 y no debe comenzar con un espacio")
            self.barrio.set('')
            validar_nombre_barrio(barrio)
        else:
            return True
    def telefono1(self,telefono_1):  #? ver nombre que acompania al self
        while len (telefono_11) not in range (1, 12) or any(num.isalpha() for num in telefono_11):
            messagebox.showerror(title="Opcion inválida",message="El campo Telefono 1 acepta sólo números.Mínimo de caracteres: 1 y máximo de caracteres: 12")
            self.telefono_1.set('')
            altura_numero(telefono_11)
        else:
            telefono1Int = int(telefono1)
            return True
    def telefono2(self,telefono_2):
        while len (telefono_21) not in range (1, 12) or any(num.isalpha() for num in telefono_21):
            messagebox.showerror(title="Opcion inválida",message="El campo Telefono 2 acepta sólo números.Mínimo de caracteres: 1 y máximo de caracteres: 12")
            self.telefono_2.set('')
            altura_numero(telefono_21)
        else:
            telefono2Int = int(telefono2)
            return True    
    domicilio = Label(frame3,width = 20, anchor="w",text = "DOMICILIO *", font= ("arial",12), bg ="#89FFD8"  )
    domicilio.grid(row=0,column=0,padx=10,pady=10,ipadx= 5, ipady= 5)
    calle = Label(frame3,width = 20, anchor="w",text = "CALLE *", font= ("arial",12), bg ="#89FFD8"  )
    calle.grid(row=1,column=0,padx=10,pady=10,ipadx= 5, ipady= 5)
    calle1 = Entry(frame3,width = 30, font= ("arial",12), bg ="white"  )
    calle1.grid(row=1,column=1,padx=10,pady=10,ipadx= 5, ipady= 5)
    altura = Label(frame3,width = 20, anchor="w",text = "ALTURA *", font= ("arial",12), bg ="#89FFD8"  )
    altura.grid(row=2,column=0,padx=10,pady=10,ipadx= 5, ipady= 5)
    altura1 = Entry(frame3,width = 30, font= ("arial",12), bg ="white"  )
    altura1.grid(row=2,column=1,padx=10,pady=10,ipadx= 5, ipady= 5)
    departamento = Label(frame3,width = 20, anchor="w",text = "PISO/DPTO", font= ("arial",12), bg ="#89FFD8"  )
    departamento.grid(row=3,column=0,padx=10,pady=10,ipadx= 5, ipady= 5)
    departamento1 = Entry(frame3,width = 30, font= ("arial",12), bg ="white"  )
    departamento1.grid(row=3,column=1,padx=10,pady=10,ipadx= 5, ipady= 5)
    barrio = Label(frame3,width = 20, anchor="w",text = "BARRIO *", font= ("arial",12), bg ="#89FFD8"  )
    barrio.grid(row=4,column=0,padx=10,pady=10,ipadx= 5, ipady= 5)
    barrio = Entry(frame3,width = 30, font= ("arial",12), bg ="white"  )
    barrio.grid(row=4,column=1,padx=10,pady=10,ipadx= 5, ipady= 5)
    telefono_1 = Label(frame3,width = 20, anchor="w",text = "TELEFONO 1 *", font= ("arial",12), bg ="#89FFD8"  )
    telefono_1.grid(row=5,column=0,padx=10,pady=10,ipadx= 5, ipady= 5)
    telefono_11 = Entry(frame3,width = 30, font= ("arial",12), bg ="white"  )
    telefono_11.grid(row=5,column=1,padx=10,pady=10,ipadx= 5, ipady= 5)
    telefono_2 = Label(frame3,width = 20, anchor="w",text = "TELEFONO 2", font= ("arial",12), bg ="#89FFD8"  )
    telefono_2.grid(row=6,column=0,padx=10,pady=10,ipadx= 5, ipady= 5)
    telefono_21 = Entry(frame3,width = 30, font= ("arial",12), bg ="white"  )
    telefono_21.grid(row=6,column=1,padx=10,pady=10,ipadx= 5, ipady= 5)
    email = Label(frame3,width = 20, anchor="w",text = "E-MAIL", font= ("arial",12), bg ="#89FFD8"  )
    email.grid(row=7,column=0,padx=10,pady=10,ipadx= 5, ipady= 5)
    email1 = Entry(frame3,width = 30, font= ("arial",12), bg ="white"  )
    email1.grid(row=7,column=1,padx=10,pady=10,ipadx= 5, ipady= 5)

    def guardar():
        pass
    campo_obligatorio = Label(ventanaPaciente,width = 20, anchor="w",text = "( * ) Campo obligatorio", font= ("arial",12), bg ="#B9FFE8"  )
    campo_obligatorio.place(x = 50 , y = 620)
    boton_guardar = Button(ventanaPaciente, width = 15,height= 2, text = " REGISTRAR ", font = ("arial bold",12), command= guardar, bg = "#00E800")
    boton_guardar.place (x = 680, y = 620)
    def cancelar():
        pass
    boton_cancelar = Button(ventanaPaciente, width = 15,height= 2, text = " CANCELAR ", font = ("arial bold",12), command= cancelar, bg = "#0066FF")
    boton_cancelar.place (x = 900, y = 620)
    ventanaPaciente.mainloop()

ventana.mainloop()




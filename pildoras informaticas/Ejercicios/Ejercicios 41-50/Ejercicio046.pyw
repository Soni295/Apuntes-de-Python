from tkinter import *

raiz=Tk()

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

#osea que esta variable va a ser una
# cadena de caracteres
miNombre=StringVar()
# aca asocion el cuadro nombre a la variable mi nombre
cuadroNombre=Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=0, column=1)

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=1, column=1)
cuadroPass.config(show="*")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2, column=1)

cuadroDireccón=Entry(miFrame)
cuadroDireccón.grid(row=3, column=1)

# aca le agrege el texto
textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=4, column=1, sticky="w", padx=10, pady=10) 

# aca especifico el contenedo padre
# en command es con quien interactua
# y que lo mueve de manera vertical
# el sticky lo utiliso para que se adapte al widdet
scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=4, column=2, sticky="nsew")
#esto es para que la barra siga nuestra posicion
textoComentario.config(yscrollcommand=scrollVert.set)

#-------------------------------------------------------

nombreLabel=Label(miFrame,  text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky="w", padx=10, pady=10)

passLabel=Label(miFrame, text="Contraseña:")
passLabel.grid(row=1, column=0, sticky="w", padx=10, pady=10)

apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=2, column=0, sticky="w", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Dirección:")
direccionLabel.grid(row=3, column=0, sticky="w", padx=10, pady=10)

comentariosLabel=Label(miFrame, text="Dirección:")
comentariosLabel.grid(row=4, column=0, sticky="w", padx=10, pady=10)

def codigoBoton():
  #aca voy a morificar una variable que esta por arriba
  miNombre.set("Juan")

# creo un boton con su funcion
botonEnvio=Button(raiz,text="Enviar", command=codigoBoton)

botonEnvio.pack()
raiz.mainloop()
from tkinter import *

raiz=Tk()

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

#aca estoy posicionando los elementos
cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=0, column=1)

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1, column=1)

cuadroDireccón=Entry(miFrame)
cuadroDireccón.grid(row=2, column=1)

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=3, column=1)
# esto se utiliza para tapar la contraseña
cuadroPass.config(show="*")

nombreLabel=Label(miFrame,  text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky="w", padx=10, pady=10)

apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=1, column=0, sticky="w", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Dirección:")
direccionLabel.grid(row=2, column=0, sticky="w", padx=10, pady=10)

passLabel=Label(miFrame, text="Contraseña:")
passLabel.grid(row=3, column=0, sticky="w", padx=10, pady=10)



# con .config(fg="red", justify="center")
# en los Entry podria poner los textos en rojo
# y centrados cuando se escriben 

# el pading es la distancia que hay entre el contenedor
# y el contenido esa se puede modificar como pady y padx

#sticky permite posicionar el texto del label n,s,e,w
# y combinaciones ne nw ejemplo
raiz.mainloop()
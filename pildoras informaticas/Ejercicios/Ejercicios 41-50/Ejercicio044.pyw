from tkinter import Tk, Frame, Label, PhotoImage

root=Tk()

miFrame=Frame(root, width=500, height=400)

miFrame.pack()

# Creo el label
#fg es el color del texto
# font es para el tipo y tamaño del texto
miLabel=Label(miFrame,font=(18) ,text="Hola en python" , fg="red")

# asi se coloca una imagen en un label
#miImagen=PhotoImage(file="nombreDelArchivo.png")
# como no lo voy a seguir modificando al label
# no hace falta que lo meta en una variable
#Label(miFrame, Image=miImagen).place(x=100,y=100)

# cuando empaquetamos el label se adapta a las
# dimensiones del label
#miLabel.pack()
# por eso se usa place para ubicar el label
# sin que modifique el tamaño
miLabel.place(x=100, y=200)




root.mainloop()

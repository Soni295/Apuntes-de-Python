from tkinter import *

root=Tk()
root.title("Ejemplo")

frame=Frame(root)
frame.pack()

playa=IntVar()
montana=IntVar()
turismoRural=IntVar()

def opcionesViaje():

  opcionEscogida=""

  if(playa.get()==1):
    opcionEscogida+= " Playa"

  if(montana.get()==1):
    opcionEscogida+= " Montaña"

  if(turismoRural.get()==1):
    opcionEscogida+= " Turismo rural"

  textoFinal.config(text=opcionEscogida)


Label(frame, text="Elije destinos:", width="50").pack()

Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Montaña", variable=montana, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Turismo rural", variable=turismoRural, onvalue=1, offvalue=0, command=opcionesViaje).pack()

#foto=PhotoImage(file="hi.png")
#Label(root, image=foto).pack()

textoFinal=Label(frame)
textoFinal.pack()

root.mainloop()

# es una app donde te dice donde vas a ir segun
# el check boton que oprimis
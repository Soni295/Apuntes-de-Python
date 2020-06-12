from tkinter import Tk, IntVar, Label, Radiobutton

root=Tk()

varOpcion=IntVar()

def imprimir():
  #print(varOpcion.get())
  if varOpcion.get()==1:
    etiqueta.config(text="Has elegido masculino")
  elif varOpcion.get()==2:
    etiqueta.config(text="Has elegido femenino")
  else:
    etiqueta.config(text="Has otra opcion")

Label(root, text="Genero:").pack()
# queo dos radiosbutton que cuando se selecciona
# uno se deselecciona el otro
# cada uno tiene un valor que se lo pasa a la variable VarOpcion
# y activa la funcion que imprime su valor
# luego lo comente y imprime abajo un texto segun lo que uno elija
Radiobutton(root, variable=varOpcion, value=1, command=imprimir, text="Masculino").pack()
Radiobutton(root, variable=varOpcion, value=2, command=imprimir, text="Femenino").pack()
Radiobutton(root, variable=varOpcion, value=3, command=imprimir, text="Otra opcion").pack()
 
etiqueta=Label(root)
etiqueta.pack()

root.mainloop()
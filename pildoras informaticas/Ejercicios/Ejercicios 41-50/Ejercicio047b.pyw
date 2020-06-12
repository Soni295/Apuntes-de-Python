from tkinter import Tk, Frame, StringVar, Entry, Button

raiz=Tk()

miFrame=Frame(raiz)
miFrame.pack()

#----------------------Variables----------------------

resultado=0
operacion=""
mirror=StringVar()

#----------------------pantalla----------------------

pantalla=Entry(miFrame, textvariable=mirror)                         
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(bg="black", fg="white", justify="right")

#----------------------funciones----------------------

def botonInsertar(texto):
  global operacion
  
  if(operacion!=""):
    mirror.set(texto)
    operacion=""
  else:
    valor=mirror.get()
    mirror.set(valor +str(texto))  

def cuenta(texto):
  global resultado
  global operacion
  operacion=texto

  if(texto=="+"):
    resultado+=int(mirror.get())

  elif(texto=="-"):
    resultado-=int(mirror.get())

  elif(texto=="*"):
    resultado*=int(mirror.get())

  elif(texto=="/"):
    resultado=int(mirror.get())

  mirror.set(resultado)



#----------------------clase boton----------------------

class Boton():
  def __init__(self,texto,row,column,funcion=botonInsertar):
    self.texto=texto
    self.row=row
    self.column=column
    Button(miFrame, text=self.texto, width=3, command=lambda:funcion(self.texto)).grid(row=self.row,  column=self.column)

#---fila1

boton7=Boton(7,2,1)
boton8=Boton(8,2,2)
boton9=Boton(9,2,3)
botonDiv=Boton("/",2,4,cuenta)

#---fila2

boton4=Boton(4,3,1)
boton5=Boton(5,3,2)
boton6=Boton(6,3,3)
botonMult=Boton("*",3,4,cuenta)

#---fila3

boton1=Boton(1,4,1)
boton2=Boton(2,4,2)
boton3=Boton(3,4,3)
botonMenos=Boton("-",4,4,cuenta)

#---fila4

boton0=Boton(0,5,1)
botonComa=Boton(",",5,2)
botonIgual=Boton("=",5,3)
botonSuma=Boton("+",5,4,cuenta)

raiz.mainloop()
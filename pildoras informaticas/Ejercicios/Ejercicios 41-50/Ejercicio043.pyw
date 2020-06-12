from tkinter import *

raiz=Tk()

raiz.title("Ventana de pruebas")

raiz.resizable(1,1)

raiz.geometry("650x350")

raiz.config(bg="blue")

# aca creo mi primer frame
miFrame=Frame()

# aca lo empaqueto en la raiz
# con side lo pongo a la izquierda
# y con anchor a arriba
# con fill="y" rellena horizontalmente
# y fill="both", expand="True" para que
# se adapte al contenedor
miFrame.pack(side="left", anchor="n")

# le cambio el color al frame
# pero para verlo tiene que tener un tamaño
miFrame.config(bg="red")

# Le doy un tamaño al frame
# con relief="sunken" le pone relieve
miFrame.config(width="650",height="350")

miFrame.config(cursor="hand2")

raiz.mainloop()
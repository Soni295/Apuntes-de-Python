from tkinter import Tk, Button
# necesito otra importacion
from tkinter import filedialog


root=Tk()

def abreFichero():
  # initiad sirve para que nos coloque en x carpeta al iniciar
  # la busqueda
  # con files typ me pide una tupla en el primer parametro pongo el 
  # mensaje y en el segundo la terminacion del archivo
  fichero=filedialog.askopenfilename(title="Abrir", initialdir="C:",filetypes=(("Ficheros de excel","*.xlsx"),
  ("Ficheros de texto", "*.txt"), ("Todos los ficheros","*.*")))

  print(fichero)# esto nos devuelve la ruta del archivo


Button(root, text="Abrir fichero", command=abreFichero).pack()

root.mainloop()
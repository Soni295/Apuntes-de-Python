from tkinter import Tk, Menu
#aca importo otro libreria de tk
# para poder hacer las ventanas emergentes
from tkinter import messagebox



root=Tk()
# voy a poner le ventana emergente en acerca de
# en el menu de ayuda

def infoAdicional():
  # por defecto funciona como una ventana de error pero eso
  # se puede modificar
  messagebox.showinfo("Procesador de sion","Procesador de textos version 2020")

def avisoLicencia():
    messagebox.showwarning("Licencia", "Producto bajo licencia GNU")

def salirAplicacion():
  # devuelve un valor
  valor= messagebox.askquestion("Salir", "Deseas salir de la aplicación")

  if valor=="yes":
    root.destroy()

def cerrarDocumento():
  valor=messagebox.askretrycancel("Reintentar","No es posible cerrar documente bloqueado")
  if valor==False:
    root.destroy()

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)
#el tear es una barra que aparece en el menu
archivoMenu=Menu(barraMenu, tearoff=0)#menu
archivoMenu.add_command(label="Nuevo")#submenu
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar Como")
archivoMenu.add_separator()#esto agregar un separador
archivoMenu.add_command(label="Cerrar",command=cerrarDocumento)
archivoMenu.add_command(label="Salir", command=salirAplicacion)

archivoEdicion=Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas=Menu(barraMenu, tearoff=0)

archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de...", command=infoAdicional)

# agrego el menu al la barra
barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edición", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

root.mainloop()
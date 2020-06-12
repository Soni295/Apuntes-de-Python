from tkinter import Tk, Menu

root=Tk()

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)
#el tear es una barra que aparece en el menu
archivoMenu=Menu(barraMenu, tearoff=0)#menu
archivoMenu.add_command(label="Nuevo")#submenu
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar Como")
archivoMenu.add_separator()#esto agregar un separador
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_command(label="Salir")



archivoEdicion=Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")


archivoHerramientas=Menu(barraMenu, tearoff=0)

archivoAyuda=Menu(barraMenu, tearoff=0)

archivoAyuda.add_command(label="Licencia")
archivoAyuda.add_command(label="Acerca de...")







# agrego el menu al la barra
barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edición", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)


root.mainloop()
from tkinter import Tk

# con esto creo a aplicacion
raiz=Tk()

# Esto le pone el titulo a la app
raiz.title("Ventana de pruebas")

# acepta en los parametros booleanos
# el primer parametro corresponde al ancho
# y el segundo corresponde al alt
# el 0 significa que no se puede cambiar el tamaño
raiz.resizable(0,0)

# para cambiarle el icono tiene q se ext .ico
# raiz.iconbitmap("icono.ico")

#Esto es para darle los tamaños por defecto
raiz.geometry("650x350")

# este metodo permite modificar un monton de cosas
# bg es background
raiz.config(bg="blue")

# y con esto creo un bucle para abrirla
# el metodo mainloop siempre debe estar en ultimo lugar
raiz.mainloop()
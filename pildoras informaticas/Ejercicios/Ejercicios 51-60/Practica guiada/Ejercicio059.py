from tkinter import *
from tkinter import messagebox
import sqlite3

#--Funciones------------------------------------------------

def conexionBBDD():
  miConexion=sqlite3.connect("Usuarios")
  miCursor=miConexion.cursor()

  try:
    miCursor.execute('''
      CREATE TABLE DATOSUSUARIOS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE_USUARIO VARCHAR(50),
        PASSWORD VARCHAR(50),
        APELLIDO VARCHAR(10),
        DIRECCION VARCHAR(50),
        COMENTARIOS VARCHAR(100))
    ''')

    messagebox.showinfo("BBDD","BBDD creada con éxito.")

  except:
    messagebox.showwarning("¡Atención!","La BBDD ya existe.")

def salirAplicacion():
  valor=messagebox.askquestion("Salir","¿Desea salir de la aplicación?")

  if valor=="yes":
    root.destroy()

def limpiarCampos():
  miID.set("")  
  miNombre.set("")
  miApellido.set("")
  miPass.set("")
  miDireccion.set("")
  # asi se borra en el Text usando delete
  textoComentario.delete(1.0,END)

def crear():
  miConexion=sqlite3.connect("Usuarios")
  miCursor=miConexion.cursor()

  datos=[
    miNombre.get(),  
    miPass.get(), 
    miApellido.get(), 
    miDireccion.get(),
    textoComentario.get("1.0",END)
  ]

  miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL, ?, ?, ?, ?, ? )",(datos))
  """
  miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL, '{}', '{}', '{}', '{}', '{}')".format(
    miNombre.get(),
    miPass.get(), 
    miApellido.get(), 
    miDireccion.get(),
    textoComentario.get("1.0",END)))"""

  miConexion.commit()

  messagebox.showinfo("BBDD","Registro insertado con éxito.")

def leer():
  miConexion=sqlite3.connect("Usuarios")
  miCursor=miConexion.cursor()

  miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID = ?",miID.get())

  elUsuario=miCursor.fetchall()
  elUsuario=elUsuario[0]

  miID.set(elUsuario[0])
  miNombre.set(elUsuario[1])
  miApellido.set(elUsuario[2])
  miPass.set(elUsuario[3])
  miDireccion.set(elUsuario[4])
  textoComentario.insert(1.0,elUsuario[5])

  miConexion.commit()

def actualizar():
  miConexion=sqlite3.connect("Usuarios")
  miCursor=miConexion.cursor()  
  
  datos=[
    miNombre.get(),  
    miPass.get(), 
    miApellido.get(), 
    miDireccion.get(),
    textoComentario.get("1.0",END)
  ]

  miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO = ?, PASSWORD = ?, APELLIDO = ?, DIRECCION = ?, COMENTARIOS = ? "+
  "WHERE ID= "+ miID.get(),(datos))
  
  """
  miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO = '{}', PASSWORD = '{}', APELLIDO = '{}', DIRECCION = '{}', COMENTARIOS = '{}' WHERE ID ={}".format(
    miNombre.get(),
    miPass.get(), 
    miApellido.get(), 
    miDireccion.get(),
    textoComentario.get("1.0",END),
    miID.get()))
  """

  miConexion.commit()

  messagebox.showinfo("BBDD","Registro actualizado con éxito.")



def eliminar():
  miConexion=sqlite3.connect("Usuarios")
  miCursor=miConexion.cursor()
  miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID="+ miID.get())
  miConexion.commit()
  messagebox.showinfo("BBDD","Registro Borrado con éxito.")


#--Aplicacion-----------------------------------------------
root=Tk()

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300,height=300)

bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir", command=salirAplicacion)

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos",command=limpiarCampos)

crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear", command=crear)
crudMenu.add_command(label="Leer", command=leer)
crudMenu.add_command(label="Actualizar", command=actualizar)
crudMenu.add_command(label="Borrar", command=eliminar)

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

#--Comienzo de campos------------------------------------------------

miFrame=Frame(root)
miFrame.pack()

miID=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miPass=StringVar()
miDireccion=StringVar()

cuadroID=Entry(miFrame, textvariable=miID)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

cuadroNombre=Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red",justify="right")

cuadroPass=Entry(miFrame, textvariable=miPass)
cuadroPass.grid(row=2, column=1, padx=10, pady=10)
cuadroPass.config(show="?")

cuadroApellido=Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame, textvariable=miDireccion)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

textoComentario=Text(miFrame,width=16, height=5)
textoComentario.grid(row=5, column=1, padx=10, pady=10)
scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")
textoComentario.config(yscrollcommand=scrollVert.set)

#--Labels--------------------------------------------------------

idLabel=Label(miFrame, text="Id:")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

passLabel=Label(miFrame, text="Password:")
passLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Dirección:")
direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

comentarioLabel=Label(miFrame, text="Comentario:")
comentarioLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

#--Botones---------------------------------------------------------

miFrame2=Frame(root)
miFrame2.pack()

botonCrear=Button(miFrame2, text="Create", command=crear)
botonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

botonLeer=Button(miFrame2, text="Read", command=leer)
botonLeer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

botonActualizar=Button(miFrame2, text="Update", command=actualizar)
botonActualizar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

botonBorrar=Button(miFrame2, text="Delete", command=eliminar)
botonBorrar.grid(row=1, column=3, sticky="e", padx=10, pady=10)

root.mainloop()
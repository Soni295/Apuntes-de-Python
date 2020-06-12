import sqlite3
from tkinter import Tk, Frame, StringVar, Button, Label, Entry, Text, Scrollbar, Menu
from tkinter import messagebox
#------------------Base de datos funciones--------------------

# Abrer ejecuta la funcion que le es pasada por parametro
# y a esta funcion le pasa el cursor
def conexionBD(funcion):
  miConexion=sqlite3.connect("BaseDeDatosPractica")
  miCursor=miConexion.cursor()
  
  funcion(miCursor)

  miConexion.commit()
  miConexion.close()

# Esta funcion Crea la base de datos
def crearBD(cursor):
  try:
    cursor.execute('''
      CREATE TABLE USUARIOS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE_USUARIO VARCHAR(50),
        PASSWORD VARCHAR(50),
        APELLIDO VARCHAR(10),
        DIRECCION VARCHAR(50),
        COMENTARIOS VARCHAR(100)
      )
    ''')
    messagebox.showinfo("Base de datos","La base de datos ha sido creada exitosamente.")
  except:
    messagebox.showinfo("Base de datos","La base de datos ya existe.")

def salida():
  valor= messagebox.askquestion("Salir", "Deseas salir de la aplicación.")

  if valor=="yes":
    raiz.destroy()

# Esta funcion inserta datos dentro de la base de datos
def insertar(cursor):
  lista=(nombre.get(), password.get(), apellido.get(), direccion.get(), textoComentario.get(0.0,"end")) 
  cursor.execute("INSERT INTO USUARIOS VALUES(NULL, ?, ?, ?, ?, ?)", lista)
  messagebox.showinfo("Creación de usuario","La creacion fue exitosa.")
  limpiar()
  
#limpia todos las lineas de texto
def limpiar():
  idUsuario.set("")
  nombre.set("")
  password.set("")
  apellido.set("")
  direccion.set("")
  comentarios.set("")
  textoComentario.delete(0.0,"end")

# Esta funcion busca en la base de datos segun el id
# y devuelve todos los datos
def buscar(cursor):
  try:
    cursor.execute("SELECT * FROM USUARIOS WHERE ID = {}".format(idUsuario.get()))
    limpiar()
    print(idUsuario.get())
    dato=cursor.fetchall()
    idUsuario.set(dato[0][0])
    nombre.set(dato[0][1])
    password.set(dato[0][2])
    apellido.set(dato[0][3])
    direccion.set(dato[0][4])
    textoComentario.insert(0.0,dato[0][5])    
  except:
    messagebox.showwarning("Busqueda","Ese ID no existe.")

# Esta modifica una tabla en la base de datos usando
# el id como referencia
def modificar(cursor):
  try:
    cursor.execute("""
      UPDATE USUARIOS SET
      NOMBRE_USUARIO = ?, 
      PASSWORD = ?, APELLIDO = ?, 
      DIRECCION = ?, COMENTARIOS = ?
      Where ID = ?
      """,[nombre.get(),
      password.get(),
      apellido.get(), 
      direccion.get(), 
      textoComentario.get(0.0,"end"),
      idUsuario.get()])
    messagebox.showinfo("Modificación","La Modificación fue exitosa.")
  except:
    messagebox.showwarning("Modificación","Hubo un problema con la modificacion\npuede que no exita ese id")

# Esta borra una tabla usando el id como referencia
def borrarUsuario(cursor):
  valor=messagebox.askyesno("Borrar usuario.","¿Esta seguro que quiere\nborrar este usuario?")
  print(valor)
  if(valor):
    cursor.execute("DELETE FROM USUARIOS WHERE ID=?",[idUsuario.get()])
    messagebox.showinfo("Borrar","El usuario {} fue borrado exitosamente.".format(idUsuario.get()))
    limpiar()

def licenciaApp():
  messagebox.showinfo("Licencia 2020","Totalmente gratuito")

def acercaDe():
  messagebox.showinfo("Acerca De..","Creado por Sión")

#------------------------Aplicación----------------------------

raiz=Tk()
raiz.title("Prueba de Aplicación")

#------------------------Frames----------------------------

miFrame1=Frame(raiz)
miFrame1.pack()
miFrame2=Frame(raiz)
miFrame2.pack()

#------------------------Menus----------------------------

barraDeMenus=Menu(raiz)
raiz.config(menu=barraDeMenus)
barraDeMenus.config(bg="red")


baseDeDatos=Menu(barraDeMenus,tearoff=0)
baseDeDatos.add_command(label="Conectar",command=lambda:conexionBD(crearBD))
baseDeDatos.add_command(label="Salir", command=salida)


borrar=Menu(barraDeMenus,tearoff=0)
borrar.add_command(label="Borrar campos",command=limpiar)


crud=Menu(barraDeMenus,tearoff=0)
crud.add_command(label="Create",command=lambda:conexionBD(insertar))
crud.add_command(label="Read",command=lambda:conexionBD(buscar))
crud.add_command(label="Update",command=lambda:conexionBD(modificar))
crud.add_command(label="Delete",command=lambda:conexionBD(borrarUsuario))


ayuda=Menu(barraDeMenus,tearoff=0)
ayuda.add_command(label="Licencia", command=licenciaApp)
ayuda.add_command(label="Acerca de...")


barraDeMenus.add_cascade(label="BBDD", menu=baseDeDatos)
barraDeMenus.add_cascade(label="Borrar", menu=borrar)
barraDeMenus.add_cascade(label="CRUD", menu=crud)
barraDeMenus.add_cascade(label="Ayuda", menu=ayuda)

#------------------------Variables----------------------------
                                      
idUsuario=StringVar()
nombre=StringVar()
password=StringVar()
apellido=StringVar()
direccion=StringVar()
comentarios=StringVar()

#------------------------Clases------------------------------

class Boton():
  def __init__(self, texto, row, column, funcion):
    self.texto=texto
    self.row=row
    self.column=column
    Button(miFrame2, font=(16), text=self.texto, width=5, height=2,padx=10, command=lambda:conexionBD(funcion)).grid(row=self.row, column=self.column)

class ElLabel():
  def __init__(self, texto, row, column):
    self.texto=texto
    self.row=row
    self.column=column
    Label(miFrame1, font=(16), padx=10,pady=8,text=self.texto).grid(row=self.row, column=self.column)

class ElEntry():
  def __init__(self, var, row, column,show="",color="black"):
    self.var=var
    self.row=row
    self.column=column
    Entry(miFrame1, font=(16),textvariable=var,show=show,fg=color).grid(row=self.row, column=self.column)

#------------------------Labels------------------------------

idLabel=ElLabel("id:",0,0)
nombreLabel=ElLabel("Nombre:",1,0)
passwordLabel=ElLabel("Password:",2,0)
apellidoLabel=ElLabel("Apellido:",3,0)
direccionLabel=ElLabel("Dirección:",4,0)
comentariosLabel=ElLabel("Comentarios:",5,0)

#------------------------Entrys------------------------------

idEntry=ElEntry(idUsuario,0,1)
nombreEntry=ElEntry(nombre,1,1,color="red")
passwordEntry=ElEntry(password,2,1,"?")
apellidoEntry=ElEntry(apellido,3,1)
direccionEntry=ElEntry(direccion,4,1)

#------------------------Comentario------------------------------

textoComentario=Text(miFrame1, width=23, height=5)
textoComentario.grid(row=5, column=1, sticky="w", padx=0, pady=10) 

scrollVert=Scrollbar(miFrame1, command=textoComentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")
textoComentario.config(yscrollcommand=scrollVert.set)

#------------------------Botones------------------------------

create=Boton("Create",0,0,insertar)
read=Boton("Read",0,1,buscar)
update=Boton("Update",0,2,modificar)
delete=Boton("Delete",0,3,borrarUsuario)

raiz.mainloop()
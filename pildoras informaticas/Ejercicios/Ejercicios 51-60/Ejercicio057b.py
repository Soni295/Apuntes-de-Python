import sqlite3

miConexion=sqlite3.connect("GestionProductos2")
miCursor=miConexion.cursor()
# En esta version voy a poner la
# clave primaria que sea autoincremental

# cambie el primer campo a id y a integer Y AUTOINCREMT
miCursor.execute('''
  CREATE TABLE PRODUCTOS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50),
    PRECIO INTEGER,
    SECCION VARCHAR(20))
''')

# aca le quite el primer valor a cada elemento
# por que este se va a generar solo
productos=[
  ("pelota", 20, "juguetería"),
  ("pantalón", 15, "confección"),
  ("destornillador", 25, "ferretería"),
  ("jarrón", 45, "cerámica"),
]
# y en la ultima parte pongo la palabra
# reservada NULL
miCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)", productos)

miConexion.commit()

miConexion.close()
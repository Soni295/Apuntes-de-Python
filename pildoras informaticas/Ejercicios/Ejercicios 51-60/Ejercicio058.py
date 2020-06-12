import sqlite3

miConexion=sqlite3.connect("GestionProductos3")
miCursor=miConexion.cursor()

# UNIQUE sirve para hacer que un campo no se pueda repetir
miCursor.execute('''
  CREATE TABLE PRODUCTOS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
    PRECIO INTEGER,
    SECCION VARCHAR(20))
''')



productos=[
  ("pelota", 20, "juguetería"),
  ("pantalón", 15, "confección"),
  ("destornillador", 25, "ferretería"),
  ("jarrón", 45, "cerámica"),
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)", productos)

miConexion.commit()

miConexion.close()
import sqlite3

miConexion=sqlite3.connect("GestionProductos")
miCursor=miConexion.cursor()

# cuando creo una tabla en este ejemplo
# la creo con una clave primaria
# esta no se puede repetir
miCursor.execute('''
  CREATE TABLE PRODUCTOS (
    CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
    NOMBRE_ARTICULO VARCHAR(50),
    PRECIO INTEGER,
    SECCION VARCHAR(20))
''')
# codigo articulo nunca se puede repetir
# (AR0x) por que la clave es unica
productos=[
  ("AR01", "pelota", 20, "juguetería"),
  ("AR02", "pantalón", 15, "confección"),
  ("AR03", "destornillador", 25, "ferretería"),
  ("AR04", "jarrón", 45, "cerámica"),
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?,?)", productos)

miConexion.commit()

miConexion.close()
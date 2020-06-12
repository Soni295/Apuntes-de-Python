import sqlite3
# inicio la conexion
miConexion=sqlite3.connect("PrimeraBase")

# creo el cursor
miCursor=miConexion.cursor()

# aca se mete la intruccion sql de crear tabla
#-miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

# aca inserto valores en la tabla creada
#-miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON', 15, 'DEPORTES')")

# esto es para decir que aceptamos los cambios
# que se le hicieron a la tabla

variosProductos=[
  ("Camiseta", 10, "Deportes"),
  ("Jarrón", 90, "Cerámica"),
  ("Camión", 20, "Jueguetería")
]
# aca le pido al servidor todos los productos
# de la tabla PRODUCTOS
miCursor.execute("SELECT * FROM PRODUCTOS")

# este metodo devuelve una lista con todos los registros
# de la intruccion sql
variableProductos=miCursor.fetchall()

# aca imprime la respuesta

for producto in variableProductos:
  print("Nombre Articulo:", producto[0],
  "\nPrecio:", producto[1],
  "\nCategoria:", producto[2])


# esto es para ingresar varios valores
# al mismo tiempo 
# se tiene que poner tantos interrogantes
# como valores de tablas se quieran poner
#-miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)

miConexion.commit()

# cierro la conexion
miConexion.close()

# para ver la base de datos se puede descargar el visor sqlite
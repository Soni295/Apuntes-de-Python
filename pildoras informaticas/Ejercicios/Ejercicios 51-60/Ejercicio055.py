import sqlite3
# inicio la conexion
miConexion=sqlite3.connect("PrimeraBase")

# creo el cursor
miCursor=miConexion.cursor()

# aca se mete la intruccion sql de crear tabla
#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

# aca inserto valores en la tabla creada
miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON', 15, 'DEPORTES')")

# esto es para decir que aceptamos los cambios
# que se le hicieron a la tabla
miConexion.commit()


# cierro la conexion
miConexion.close()

# para ver la base de datos se puede descargar el visor sqlite
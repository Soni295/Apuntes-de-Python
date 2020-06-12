import sqlite3

miConexion=sqlite3.connect("GestionProductos3")
miCursor=miConexion.cursor()

# Esto seria el read
miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='confección'")
productos=miCursor.fetchall()
print(productos)

# Esto seria el Update
miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='pelota'")

# Esto seria el Delete 
# es importante nunca olvidar el where
# por que una vez echa la peticion podes borrar
# toda la base de datos
miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=4")

miConexion.commit()

miConexion.close()
# importo el open para abrir archivos
# tambien puedo usarlo sin importar
from io import open

# los archivos se pueden abrir en modo
# lectura, escritura o agregar

# el primer parametro es el nombre
# del archivo y el segundo parametro es
# el modo de abrir, w es de write

archivo_texto=open("archivo.txt", "w")

# creo un str
frase="\
Es un estupendo dia para estudiar Python\
\nel miercoles"

# aca le inserto el texto que deseo escribir
archivo_texto.write(frase)

archivo_texto.close()

# lo borror
del archivo_texto 

#--------------------------------------

# lo abro en modo lectura
archivo_texto=open("archivo.txt", "r")

#almaceno lo que esta en el archivo
texto=archivo_texto.read()

archivo_texto.close()

del archivo_texto

print(texto)

#------------------------------

archivo_texto=open("archivo.txt", "r")

# lee linea por linea y las guarda como listas
lineas_texto=archivo_texto.readlines()

archivo_texto.close()

del archivo_texto

print(lineas_texto)

#------------------------
# aca voy a agregar lineas de texto
# con append agregamos a lo que teniamos

archivo_texto=open("archivo.txt", "a")

# aca se lo agrega al final del archivo
archivo_texto.write("\nsiempre es una buena oportunidad para estudiar\nPython")

archivo_texto.close()
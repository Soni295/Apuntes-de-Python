
from io import open

archivo_texto=open("archivo.txt", "w")

frase="\
Es un estupendo dia para estudiar Python\
\nel miercoles"

archivo_texto.write(frase)

archivo_texto.close()
from io import open

def salto(mensaje):
  print(f"---------------------------\n{mensaje}\n---------------------------")
# en Python el cursor esta al comienzo del archivo
# pero cuando leemos el archivo el cursor se mueve
# al final
# osea que si lo leemos otra vez no va a mostrar nada
# por que el cursor se mueve al final del archivo
# con el metodo seek(numero de posicion) podemos
# elegir donde colocar el puntero
archivo_texto=open("archivo.txt", "r")

archivo_texto

print(archivo_texto.read())

# aca lo vuelvo a poner en el comienzo del archivo
archivo_texto.seek(0)
salto("Vuelvo al comienzo")

print(archivo_texto.read())

#Posiciono el cursor en el caracter 10 
salto("\
Arranco de la posision 10 \
y termnio en la 20")
archivo_texto.seek(10)

# y cuando a read le paso por parametro
# 20 significar que leera hasta ese caracter
print(archivo_texto.read(20))

archivo_texto.seek(0)

salto("arranco de la mitad para adelante")
archivo_texto.seek(len(archivo_texto.read())/2)

print(archivo_texto.read())
salto("-")
archivo_texto.close()

del archivo_texto

# cuando lo abro con r+ eso me permite leer y escribir el archivo
# al abrirlo me voy a encontrar en la posicion 0 del archivo
# pero me sobre escribe las lineas por eso hacer con cuidado
archivo_texto=open("archivo.txt", "r+")

linea_texto=archivo_texto.readlines()

# aca inserto un str a principio de la lista
linea_texto.insert(0,"El comienzo del texto\n")

nuevo_texto=""

#aca lo tranformo en mensaje
for i in linea_texto:
  nuevo_texto += i

archivo_texto.seek(0)
archivo_texto.write(nuevo_texto)

linea_texto[5]="Y este es el final del archivo"

archivo_texto.seek(0)

#esto acepta listas es como el opuesto a readlines
archivo_texto.writelines(linea_texto)
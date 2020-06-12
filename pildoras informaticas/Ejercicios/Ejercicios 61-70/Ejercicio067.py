import re

nombre1="Sandra López"
nombre2="Antonio Gómez"
nombre3="María López"
nombre4="Lara Gonzales"
nombre5="Mara Hernestina"

nombre6="Lara Gonzales"
nombre7="5654656121"
nombre8="a265465413"



# match busca si hay coincidencias dentro de un
# patron en una cadena de texto al principio
# ignore case es para q no distinga entre mayuscula y minuscula
if re.match("Sandra", nombre1, re.IGNORECASE):
  print("Hemos encontrado el nombre")

else:
  print("No lo hemos encontramos")


# El punto vale como comodin para un unico caracter
if re.match(".ara", nombre4, re.IGNORECASE):
  print("Hemos encontrado el nombre")

else:
  print("No lo hemos encontramos")


# la \d esto busca si una cadena comienza por un numero o no
if re.match("\d", nombre7):
  print("Hemos encontrado el numero")

else:
  print("No lo hemos encontramos")

#la diferencia es que match solo busca al comienzo y search busca en toda la cadena


if re.search("López", nombre3):
  print("Hemos encontrado el a lopez")

else:
  print("No lo hemos encontramos")

 
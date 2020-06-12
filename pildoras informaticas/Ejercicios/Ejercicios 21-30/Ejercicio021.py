# el asteristico en los parametros
# significa que no voy a saber cuantos
# parametros voy a recibir
def devuelve_ciudades(*ciudades):
  for elemento in ciudades:
    for subElemento in elemento:
      yield subElemento
#es lo mismo que el anterior
def devuelve_ciudades2(*ciudades):
  for elemento in ciudades:
      yield from elemento

ciudades_devueltas=devuelve_ciudades("Madrid","Barcelona","Bilbao","Valencia")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))
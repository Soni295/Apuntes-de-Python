# imprime hola 3 veces(imprime por la cantidad de elementos)
for i in [1, 2, 3]:
  print("hola")

"""
 imprimira cada elemento por cada vuelta
 primavera
 verano
 otonio
 invierno
"""
for i in ["primavera", "verano","otonio","invierno"]:
  print(i)

# el end en un print determina la finalizacion
# de lo que se imprime
# hola hola hola
# cuando el elemento a recorrer es un str
# el bucle se ejecuta por cada characte en
# el incluyendo los espacio
for i in "hola me llamo juan":
  print("hola",end=" ")
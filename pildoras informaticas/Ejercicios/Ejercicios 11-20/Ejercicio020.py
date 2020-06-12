# aca genero la lista con una funcion
# normal
def generaPares(limite):
  num=1
  miLista=[]

  while num<limite:
    miLista.append(num*2)

    num+=1
  
  return miLista

print(generaPares(10))


# aca hago lo mismo pero con yield
# y me los genera de uno en uno
def generaPares2(limite):
  num=1
    
  while num<limite:
    
    yield num*2

    num+=1
  
devuelvePares=generaPares2(10)

print(next(devuelvePares))

print("linea de codigo")

print(next(devuelvePares))

print("otra linea de codigo")

print(next(devuelvePares))
# me genera un numero cada vez que la llamo
# sin generar la lista completa
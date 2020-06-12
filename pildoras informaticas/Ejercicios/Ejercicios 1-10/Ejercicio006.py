miTupla=("juan", 13, 1, 1995)

#imprime 1
print(miTupla[2])

miLista=list(miTupla)

# imprime ['juan', 13, 1, 1995] 
# los corchetes son de lista
print(miLista)

miTupla2=tuple(miLista)

# imprime ('juan', 13, 1, 1995)
# los parentecis son de tupla
print(miTupla2)

#me da true por que existe en la tupla
print("juan" in miTupla2)

#me devolvera 1 por que solo existe 1 vez
print(miTupla2.count(13))

#devuelve la cantidad de elementos
#de la tuplas 4
print(len(miTupla2))

#empaquetado de tupla
miTupla3= "Hernesto", 14, 9, 1995

#me devuelve <class 'tuple'>
print(type(miTupla3))

#desempaquetado de tupla
nombre, dia, mes, agno =miTupla3

print("el nombre es:", nombre)
print("el dia es:", dia)
print("el mes es:", mes)
print("el ano es:", agno)

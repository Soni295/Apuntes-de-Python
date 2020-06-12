miDiccionario={"Alemania":"Berlin","Francia":"Paris","Reino Unido":"Londres","Espana":"Madrid"}

#muestra todo el diccionario
print(miDiccionario)

#muestra el valor de Alemania "Berlin"
print(miDiccionario["Alemania"])

#Agrego la clave Rusia con el valor Moscu
miDiccionario["Rusia"]="San Petersburgo"

# {'Alemania': 'Berlin', 'Francia': 'Paris', 
# 'Reino Unido': 'Londres',
# 'Espana': 'Madrid', 'Rusia': 'San Petersburgo'}
print(miDiccionario)

#le modifico el valor a la clave Rusia
miDiccionario["Rusia"]="Moscu"

# {'Alemania': 'Berlin', 'Francia': 'Paris', 
# 'Reino Unido': 'Londres',
# 'Espana': 'Madrid', 'Rusia': 'Moscu'}
print(miDiccionario)

#del es para eliminar 
del miDiccionario["Reino Unido"]

#{'Alemania': 'Berlin',
# 'Francia': 'Paris', 
# 'Espana': 'Madrid', 
# 'Rusia': 'Moscu'}
print(miDiccionario)

miDiccionario2={"Alemana":"Berlin",23:"Jordan","Mosqueteros":3}

#{'Alemana': 'Berlin', 23: 'Jordan', 'Mosqueteros': 3}
print(miDiccionario2)

miTupla=["Espana", "Francia", "Reino Unido", "Alemania"]

miDiccionario3={miTupla[0]:"Madrid",miTupla[1]:"Paris",miTupla[2]:"Londres",miTupla[3]:"Berlin"}


#{'Espana': 'Madrid', 
# 'Francia': 'Paris', 
# 'Reino Unido': 'Londres', 
# 'Alemania': 'Berlin'}
print(miDiccionario3)

miDiccionario4={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","anillos":[1991,1992,1993,1996,1997,1998]}

#[1991, 1992, 1993, 1996, 1997, 1998]
print(miDiccionario4["anillos"])
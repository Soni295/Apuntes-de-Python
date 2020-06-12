miLista = ["Maria","Pepe","Marta","Antonio"]

#lista completa
print(miLista)

#primer elemento "Maria"
print(miLista[0])

#primer elemento empezando desde el ultimo "Antonio"
print(miLista[-1])

miLista2 = ["a","b","c","d","f","g","h","i"]

#con esto va a imprimir una porcion arrancando del 0
#y terminando antes del 3 -> ["a","b","c"] 
print(miLista2[0:3])

#es igual que el anterio
print(miLista2[:3])

#arranca del 2 hasta el final 
#["c","d","f","g","h","i"]
print(miLista2[2:])

#antes de agregar ["a","b","c","d","f","g","h","i"]
print(miLista2)

#despues ["a","b","c","d","f","g","h","i","j"]
miLista2.append("j")
print(miLista2)

#despues ["k","a","b","c","d","f","g","h","i","j"]
miLista2.insert(0,"k")
print(miLista2)

#['k', 'a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 
# 'Maria', 'Pepe', 'Marta', 'Antonio']
miLista2.extend(miLista)
print(miLista2)

#remuevo Maria
miLista2.remove('Maria')
print(miLista2)

#remueve el ultimo elemento de la lista 'Antonio'
miLista2.pop()
print(miLista2)


#11 es el indice de pepe
print(miLista2.index("Pepe"))

#true por que pepe existe
print("Pepe" in miLista2)

#false por que no existe
print("z" in miLista2)
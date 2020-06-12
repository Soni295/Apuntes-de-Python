import pickle 

lista_nombres=["Pedro", "Ana", "Maria", "Isabel"]

# wb es cuando va a ser de escritura binaria
ficheto_binario=open("lista_nombres.txt","wb")

# esto es para volcar todo lo del fichero
# el primer parametro la informacion que se quiere
# volcar
# el segundo es el fichero
pickle.dump(lista_nombres, ficheto_binario)

ficheto_binario.close()

del ficheto_binario

#-------------------------------------

#rb es de read binary
fichero=open("lista_nombres.txt","rb")

# aca abro el fichero
lista=pickle.load(fichero)

print(lista)
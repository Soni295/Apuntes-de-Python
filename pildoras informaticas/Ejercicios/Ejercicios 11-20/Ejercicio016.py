# crea un lista de 5 elementos
# empezando desde 0
# imprime 0 1 2 3 4
for i in range(5):
  print(i)

# con la f en print se activan funciones
# especiales
# imprimira valor de la variable
# valor de la variable 0
# valor de la variable 1
# valor de la variable 2
for i in range(3):
  print(f"valor de la variable {i}")

# cuando tiene dos parametros range
# el primero es donde empieza y el segundo
# es donde temrina sin incluirlo
# 5 6 7 8 9 
for i in range(5,10):
  print(i)

# cuando tiene 3 parametros
# el 1ro es donde inicia el 2do donde termina
# el 3ro es el salto que hace entre cada uno
#25 35 45 55 65 75 85 95
for i in range(25, 100, 10):
  print(i)


valido=False

email=input("Introduce tu email:\n")

#len(email) devolvera la cantidad de caracteres
for i in range(len(email)):
  if email[i]=="@":
    valido=True

if valido:
  print("El email es correcto")
else:
  print("El email es incorrecto")
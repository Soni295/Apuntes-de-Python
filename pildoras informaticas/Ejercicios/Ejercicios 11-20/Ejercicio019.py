# con continue se salte todo lo de abajo 
# y pasa a la siguien vuelta del bucle
for letra in "Python":

  if letra=="h":
    continue

  print(f"viendo la letra: {letra}")


nombre="Pildoras informaticas"
contador=0

# aca lo uso para contar los caracteres
# evitando los espacios
for letra in nombre:
  if letra ==" ":
    continue
  contador+=1

print(contador)

# se usa para mantener el programa ocupado 
# hasta que el usuario se salga
while True:
  pass

email=input("Escriba aqui su email:\n")

for i in email:
  if i=="@":
    arroba=True
    break
# este else le pertenece al bucle, 
# y se ejecuta cuando termina el bucle
# (cuando ya no puede recorrer mas)
# pero si se uso break se saltea directamente
else:
  arroba=False

print(arroba)
# El booleano false se escribe
# con la primera en mayuscula
email=False

# ejecuta el bucle por cada character
# que tenga y si el caracter es igual
# al arroba pasa email a True
for i in "Juan@hotmail.com.es":
  if(i=="@"):
    email=True


# cuando pongo solo la variable el if
# asume automaticamente su valor true o false
# si es False lo saltea y si es True
# lo ejecuta
if email:
  print("\nEl email es correcto", )
else:
  print("\nEl email no es correcto")


print("------------------------")
print("Introduce tu direccion de email: ")

contador=0
miEmail=input()
email=False

for i in miEmail:
  if( i=="@" or i=="."):
    contador+=1

if contador==2:
  print("\nEl email es correcto", )
else:
  print("\nEl email no es correcto")
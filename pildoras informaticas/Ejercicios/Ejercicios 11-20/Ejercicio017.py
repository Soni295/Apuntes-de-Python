i=1
# aca veo la sintaxis en accion
# mientras i sea menor igual
# a 10 se ejecutara el codigo
while i<=10:
  print("Ejecucion numero "+ str(i))
  i+=1

print("Ejecucion terminada")

edad=int(input("Introduce la edad:\n"))

# se va a ejecutar siempre que ponga un valor
# en edad menor a 5 o mayor a 100
while edad<5 or edad>100:
  print("has introducido una edad erronea. Vuelve a intentarlo.")
  edad=int(input("Introduce la edad:\n"))

print("Gracias por colaborar")
import math

print("Programa de calculo de raiz cuadrada")
numero=int(input("Introduce un numero:\n"))

intentos=0

while numero<0:
  print("no se puede hallar la raiz de un numero negativo")

  if intentos==2:
    print("Has consumido demaciados intentos. Programa finalizado")
    break

  numero=int(input("Introduce un numero:\n"))

  if numero<0:
    intentos+=1

if intentos<2:
  solucion=math.sqrt(numero)
  print("La raiz cuadrada de" + str(numero) + " es " + str(solucion))
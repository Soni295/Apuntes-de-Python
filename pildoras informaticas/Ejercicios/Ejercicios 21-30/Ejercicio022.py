# 4 funciones para sumar, restar, multiplicar y dividir
def sumar(num1, num2):
  return num1 + num2

def restar(num1, num2):
  return num1 - num2

def multiplicar(num1, num2):
  return num1 * num2

#captura de excepcion si no se puede
#dividi se captura y se ejecuta el except
def dividir(num1, num2):

  try:
    return num1 / num2
    
  except ZeroDivisionError:
    print("No se puede divivir entre 0")
    return "Operacion erronea"

# el usuario le puede pasar los valores
# pero si pasa un str este sera captudaro
while True:
  try:
    numero1=int(input("Introduce tu primer numero:\n")) 
    numero2=int(input("Introduce tu segundo numero:\n"))
    break
  except ValueError:
    print("Los valores introducidos no son correctos. Intentalo de nuevo")


operacion=input("introduce la operacion a realizar\n(Suma, Resta, Multiplica, Divide):\n")

# pasa todo a minusculas por si aparece alguna mayuscula
operacion=operacion.lower()

if operacion=="suma":
  print(sumar(numero1, numero2))

elif operacion=="resta":
  print(restar(numero1, numero2))

elif operacion=="multiplica":
  print(multiplicar(numero1, numero2))

elif operacion=="divide":
  print(dividir(numero1, numero2))

else:
  print("Operacion no contemplada")

print("Operacion ejecutada. Continua la ejecucion del programa")
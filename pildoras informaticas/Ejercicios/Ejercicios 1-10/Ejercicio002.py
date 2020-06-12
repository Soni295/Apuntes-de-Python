print(5+6)#11
print(10%3)#1 devuelve el resto
print(5**3)#125 = 5*5*5
print(9//2)#4 =4.5 pero solo muestra el entero

nombre=5
print(type(nombre))#<class 'int'>

nombre='Juan'
print(type(nombre))#<class 'str'>

nombre=5.2
print(type(nombre))#<class 'float'>

mensaje="""Esto es un mensaje
con tres saltos 
de linea"""

print(mensaje)
#Esto es un mensaje
#con tres saltos 
#de linea

numero1=5
numero2=2

if numero1>numero2:
  print("el numero 1 es mayor")
#si el numero 1 es mayor que el numero dos se imprime en pantalla

else:
  print("el numero 2 es mayor")
#si no se cumple lo del if pasara lo del else
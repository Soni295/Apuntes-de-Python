"""
Se Evaluará :
la distancia menor a 40km
el numero de hermanos mayor a dos
salario familiar menor igual a 20000
"""

print("Programa de becas anio 2017")
distancia=int(input("Introduce la distacia a la escuela en km: "))

cant_hermanos=int(input("Introduce el numero de hermanos: "))
 
salario_familiar=int(input("Introduce el salario anual bruto: "))

print(
"Su casa esta a " + 
str(distancia) + 
"Km. del colegio, tiene " +
str(cant_hermanos) + 
" hermanos y su salario familiar es de $"+str(salario_familiar)+" anuales"
)

"""
El operador logico and pide que se cumplas ambas condiciones
para cumplir con la ejecucion
El operador logico or pide que se cumpla almenos una de las condiciones
para cumplir con la ejecucion
"""
if distancia>40 and cant_hermanos>2 or salario_familiar<=20000:
  print("Puedes recibir la beca")
else:
  print("No puede recibir la beca")

  
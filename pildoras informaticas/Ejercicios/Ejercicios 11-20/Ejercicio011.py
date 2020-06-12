#comparando salarios

salario_presidente=int(input("Introduce el salario del presidente: "))
print("El salario del presidente es $" + str(salario_presidente))

salario_director=int(input("Introduce el salario del director: "))
print("El salario del director es $" + str(salario_director))

salario_jefe_area=int(input("Introduce el salario del jefe area:"))
print("El salario del jefe area es $" + str(salario_jefe_area))

salario_administrativo=int(input("Introduce el salario del administrativo: "))
print("El salario del administrativo es $" + str(salario_administrativo))

"""
Mientras sigan este orden
(presidente,director, jefe de area, administrativo) 
de mayor a menor los salarios
imprimira "Todo funciona correctamente"
caso contrario
"Algo anda mal"
"""

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
  print("Todo funciona correctamente")
else:
  print("Algo anda mal")
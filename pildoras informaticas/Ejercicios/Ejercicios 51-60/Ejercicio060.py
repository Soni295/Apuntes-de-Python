# funcion normal
'''
def area_triangulo( base, altura ):
  return (base*altura)/2

triangulo1=area_triangulo(5,7)
triangulo2=area_triangulo(9,6)

print(triangulo1)

print(triangulo2)
'''
# funcion lambda
# tambien se les llama funciones "on the go", "on demand" o "online"
"""
area_triangulo = lambda base, altura: (base*altura)/2

triangulo1=area_triangulo(5,7)
triangulo2=area_triangulo(9,6)

print(triangulo1)

print(triangulo2)
"""
"""
al_cubo=lambda numero: pow(numero,3)
al_cubo2=lambda numero: numero**3

print(al_cubo(13))
print(al_cubo2(13))
"""

destacar_valor=lambda comision: "¡{} €!".format(comision)

comision_Ana=15585

print(destacar_valor(comision_Ana))
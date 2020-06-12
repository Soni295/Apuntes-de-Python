"""
def numero_par(num):
  if num%2==0:
    return True
"""
numeros=[17,24,7,39,8,51,92]

# la funcion filter requiere 2 argumentos
# el primero la funcion a llama
# y el segundo la lista que se llama
# lo que nos devuelve es un objeto
#--print(list(filter(numero_par, numeros)))
print(list(filter(lambda numero: numero%2==0, numeros)))
#[24,8,92]
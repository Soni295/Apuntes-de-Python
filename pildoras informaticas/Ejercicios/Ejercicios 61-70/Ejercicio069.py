def funcion_decoradora(funcion_parametro):
  # el *args significa que recibira multiples parametros
  # el **kawargs significa argumentos con keywords
  def funcion_interior(*args,**kwargs):
    
    # Acciones adicionales que decoran
    
    print("vamos a realizar un cálculo: ")
    
    funcion_parametro(*args,**kwargs)
    
    # Acciones adicionales que decoran

    print("Hemos terminado el cálculo") 

  return funcion_interior


# con esto hacemos que cuando se llame suma seria
# algo como funcion_decoradora(suma)
@funcion_decoradora
def suma(num1, num2, num3):
  print(num1+num2+num3)

@funcion_decoradora
def resta(num1,num2):
  print(num1-num2)

@funcion_decoradora
def potencia(base,exponente):
  print(pow(base,exponente))



suma(7,5,8)
resta(12,10)

potencia(base=5,exponente=3)
def funcion_decoradora(funcion_parametro):
  
  def funcion_interior():
    
    # Acciones adicionales que decoran
    
    print("vamos a realizar un cálculo: ")
    
    funcion_parametro()
    
    # Acciones adicionales que decoran

    print("Hemos terminado el cálculo") 

  return funcion_interior


# con esto hacemos que cuando se llame suma seria
# algo como funcion_decoradora(suma)
@funcion_decoradora
def suma():
  print(15+20)

@funcion_decoradora
def resta():
  print(30-10)


suma()
resta()

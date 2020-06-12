class Areas:

  """Esta clase calcula areas"""

  def areaCuadrado(lado):
    
    """Calcula el area de un cuadrado\
    \nelevado al cuadrado del lado pasado por parametro"""

    return "El área del cuadrado es: " + str(lado*lado)

  def areaTriangulo(base,altura):
    """Calcula el area de un triangulo utilizando los parametros base y altura"""

    return "El área del triangulo es: " +str((base*altura)/2)


print(Areas.areaCuadrado(5))
# esto devuelve la documentacion
print(Areas.areaCuadrado.__doc__)
# devuelve lo mismo pero mas detallado
help(Areas.areaCuadrado)
help(Areas.areaTriangulo)
help(Areas)
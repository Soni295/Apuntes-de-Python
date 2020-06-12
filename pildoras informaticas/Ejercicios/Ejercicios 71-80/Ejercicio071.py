def areaTriangulo(base, altura):
  """
  Calcula el área de un triangulo dado

  >>> areaTriangulo(3,6)
  'El area del triangulo es: 9.0'
  
  >>> areaTriangulo(4,5)
  'El area del triangulo es: 10.0'

  >>> areaTriangulo(9,3)
  'El area del triangulo es: 13.5'

  >>> areaTriangulo(8,5)
  'El area del triangulo es: 20.0'

  """
  
  return "El area del triangulo es: " +str((base*altura)/2)

import doctest

doctest.testmod()#no debe aparecer nada si la documentacion esta bien

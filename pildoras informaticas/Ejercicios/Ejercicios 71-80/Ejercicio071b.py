def compruebaMail(mailUsuario):
  """
  La función evalua un email
  recibido en busca de la @. si tiene una@
  es correcto, si tiene más de una @ es incorrecto
  y si la tiene al final tambien es incorrecto
  
  >>> compruebaMail('juan@cursos.es')
  True
  >>> compruebaMail('juancursos.es@')
  False
  >>> compruebaMail('juan@curs@os.es')
  False
  
  """

  arroba=mailUsuario.count("@")
  if (arroba != 1 or mailUsuario.rfind("@") ==(len(mailUsuario)-1) or mailUsuario.find("@")==0):
    return False
  else:
    return True

import doctest

doctest.testmod()#no debe aparecer nada si la documentacion esta bien

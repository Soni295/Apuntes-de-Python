import re

cadena="Vamos a aprender expreciones regulares en Python. Python es un lenguaje de sintaxis sensilla"

# search() busca un string y muestra donde coincide
# pide como parametro primero lo q se buscar y luego el texto
# devuelve un obj si esta y un none si no esta

#--print(re.search("aprender",cadena))
#<re.Match object; span=(8, 16), match='aprender'>

textoBuscado="aprender"
textoBuscado2="Python"



# busca todas las veces que se repite
# y te imprime repetidas veces la parabra
print(re.findall(textoBuscado2,cadena))
# ['Python', 'Python']

textoEncontrado=re.search(textoBuscado,cadena)

# esto dice en que cararte empieza a aparece
# lo encontrado
print(textoEncontrado.start())

# Lo mismo que el start pero donde termina
print(textoEncontrado.end())

# muestra de donde arranca a donde termina
print(textoEncontrado.span())

'''
if re.search(textoBuscado,cadena) is not None:
  print("He encontrado el texto")
else:
  print("No he encontrado el texto")

'''
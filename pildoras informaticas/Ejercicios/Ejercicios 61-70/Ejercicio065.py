import re

lista_nombres=[
  'Ana Gómez',
  'Sandra Aguirre',
  'María Martín',
  'Sandra López',
  'Sandra Fernandez',
  'Santiago Martín'
]
# El acento circunfejo ^ funciona como un comodin
# en este caso va a buscar todos los que comienzen por sandra

for elemento in lista_nombres:
  if re.findall('^Sandra', elemento):
    print(elemento)


# El metacaracter que es para buscar los que terminan
# es el dolar
for elemento in lista_nombres:
  if re.findall('Martín$', elemento):
    print(elemento)

lista_nombres2=[
  'http://informaticaespaña.es',
  'http://pildorasinformaticas.es',
  'http://pildorasinformaticas.com'
]

# asi cuando se quieren buscar 1 caracter o varios
for elemento in lista_nombres2:
  if re.findall('[ñ]', elemento):
    print(elemento)


lista_nombres2=[
  'hombres',
  'mujeres',
  'mascotas',
  'niños',
  'niñas'
]

#esto me buscara niñ y si lleva "o" o "a" antes de la "s"
for elemento in lista_nombres2:
  if re.findall('niñ[oa]s', elemento):
    print(elemento)

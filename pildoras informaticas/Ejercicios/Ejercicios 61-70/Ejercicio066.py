import re

lista_nombres=[
  'Ana',
  'Pedro',
  'María',
  'Rosa',
  'Sandra',
  'Celia'
]

# [o-t] es para que busque las palabras entre el rango
# de la o a la t
# ^[o-t] es para todos los que comienzen con ese rango
# [o-t]$ es para todos lo que terminen con ese rango
for elemento in lista_nombres:
  if re.findall('[o-t]', elemento):
    print(elemento)
  

lista_nombres2=[
  'Ma1',
  'Se1',
  'Ma2',
  'Ba1',
  'Ma3',
  'Va1',
  'Va2',
  'Ma4',
  'MaA',
  'Ma5',
  'MaB',
  'MaC',
]
#imprime todo los que sean Ma y que vayan
# del 0 al 3
# pero si ponemos Ma[^0-3] Imprime los Ma
# que no vayan de 0 al 3 osea Ma4
for elemento in lista_nombres2:
  if re.findall('Ma[0-3]', elemento):
    print(elemento)



# asi se puede agregar tambien el A al B

for elemento in lista_nombres2:
  if re.findall('Ma[0-3A-B]', elemento):
    print(elemento)

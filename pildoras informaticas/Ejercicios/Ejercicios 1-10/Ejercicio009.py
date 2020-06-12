print("Verificacion de acceso")

#aca ingresara el dato introducido
#por consola a la variable edad_usuario
edad_usuario=int(input("Introduce tu edad, por favor: "))

# si edad_usuario es menor que 18
# imprimira "No puedes pasar"
# si es mayor que 100 dira "Edad equivocada"
# pero si es mayor o igual que 18
# dira "Puedes pasar"
if edad_usuario < 18:
  print("No puedes pasar")
elif edad_usuario> 100:
  print("Edad equivocada")

else:
  print("Puedes pasar")

print("el programa ha finalizado")

print("  ")
print("  ")
alumno=int(input("Escribe la nota del alumno: "))

if alumno < 5:
  print("Insuficiente")
elif alumno < 6:
  print("Suficiente")
elif alumno < 7:
  print("Bien")
elif alumno < 9:
  print("Exelente")
else:
  print("Sobresaliente")
  
"""
Si alumno es menor que 5 ""
Si la anterior es falsa y alumno es menor que 6 "Insuficiente"
Si la anterior es falsa y alumno es menor que 7 "Suficiente"
Si la anterior es falsa y alumno es menor que 8 "Bien"
Si la anterior es falsa y alumno es menor que 9 "Exelente"
Si todas las anteriores son falsas "Sobresaliente"
"""
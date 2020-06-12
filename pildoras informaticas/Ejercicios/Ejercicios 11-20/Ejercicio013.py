print("Asignaturas Optativas anio 2020")
print("Informatica - Pruebas de software - Usabilidad y accesibilidad")

#almaceno el input
opcion=input("Escribe la asignatura elegida aqui: \n")

#transformo todo a minusculas
asignatura = opcion.lower()

#in es para comparar con cada uno de los valores
if asignatura in ("informatica", "pruebas de software", "usabilidad y accesibilidad"):  
  print("Asignatura elegida es " + asignatura)

else:
  print("La asignatura elegida no esta contemplada")
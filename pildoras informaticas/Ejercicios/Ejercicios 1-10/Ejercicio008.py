print("programa de evaluacion de notas de alumnos")

#input toma como str todo dato adentro
nota_alumno=input()

def evaluacion(nota):
  valoracion="aprobado"

  if nota<5:
    valoracion="suspenso"
  
  return valoracion

#si la nota es mayo que 5 responde aprobado en caso contrario suspenso
print("el alumno esta:", evaluacion(int(nota_alumno)))
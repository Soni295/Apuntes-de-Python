def divide():
  try:
    op1=float(input("Introduce el primer numero:\n"))
    op2=float(input("Introduce el segundo numero:\n"))

    print("La division es:" + str(op1/op2))
  
  except ValueError:
    print("El valor introducido es erroneo")
  
  except ZeroDivisionError:
    print("No se puede divivir por 0")
    
  # finally se ejecutara habiendo o no error
  finally:
    print("Calculo finalizado")

divide()
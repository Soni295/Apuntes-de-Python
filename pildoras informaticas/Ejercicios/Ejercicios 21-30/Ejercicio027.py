class Coche():
  # constructor de clase
  def __init__(self):  
    # encapsulo las variables
    self.__largoChasis=250
    self.__anchoChasis=120
    self.__enMarcha=False
    self.__ruedas=4
    
  def arrancar(self,arrancar):
    # le cambio para lo que le pase por parametro
    # se lo va a insertar como valor en arrancar
    self.__enMarcha=arrancar

    # y aca que devuelva un mensaje si el auto da
    # true o no
    if(self.__enMarcha):
      return "El coche esta en marcha"
    
    else:
      return "El coche esta parado"

  def estado(self):
    print(f"El coche tiene {self.__ruedas} ruedas, un ancho de {self.__anchoChasis} y un largo de {self.__largoChasis}.")

miCoche=Coche()

print(miCoche.arrancar(True))

miCoche.estado()

print("\n----A continuacion creamos el segundo objeto----\n")

miCoche2=Coche()

print(miCoche.arrancar(False))

miCoche2.estado()
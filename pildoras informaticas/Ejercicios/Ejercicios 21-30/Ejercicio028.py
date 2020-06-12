class Coche():

  def __init__(self):  
    self.__largoChasis=250
    self.__anchoChasis=120
    self.__enMarcha=False
    self.__ruedas=4
    
  def arrancar(self,arrancar):
    self.__enMarcha=arrancar

    if (self.__enMarcha):
      chequeo=self.__chequeo_interno()

    if(self.__enMarcha and chequeo):
      return "El coche esta en marcha"
    elif(self.__enMarcha and chequeo==False):
      return "Algo ha ido mal en el chequeo no podemos arrancar"
    else:
      return "El coche esta parado"

  def estado(self):
    print(f"El coche tiene {self.__ruedas} ruedas, un ancho de {self.__anchoChasis} y un largo de {self.__largoChasis}.")

  # encapsulo el metodo chequeo interno
  def __chequeo_interno(self):
    print("Estoy realizando el chequeo interno")

    self.gasolina="ok"
    self.aceite="ok"
    self.puertas="cerradas"

    if(self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas" ):
      return True
    else:
      return False


miCoche=Coche()

print(miCoche.arrancar(True))

miCoche.estado()

print("\n----A continuacion creamos el segundo objeto----\n")

miCoche2=Coche()

print(miCoche.arrancar(False))

miCoche2.estado()
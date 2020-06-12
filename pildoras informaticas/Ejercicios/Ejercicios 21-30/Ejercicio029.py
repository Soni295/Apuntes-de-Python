class Vehiculos():
  
  def __init__(self, marca, modelo):
    self.marca=marca
    self.modelo=modelo
    self.enMarcha=False
    self.acelera=False
    self.frena=False

  def arrancar(self):
    self.enMarcha=True

  def acelerar(self):
    self.acelera=True
  
  def frenar(self):
    self.frena=True

  def estado(self):
    print(f"Marca: {self.marca}.\nModelo: {self.modelo}",
    f"\nEn marcha: {self.enMarcha}. \nAcelerando: {self.acelera}.",
    f"\nFrenando: {self.frena}")

# aca esta heredando Vehiculos
class Moto(Vehiculos):
  pass

# Aca creo un objeto de la clase moto
# que tiene los mismos metodos y propiedades
# que la clase vehiculos
miMoto=Moto("Honda","CBR")

miMoto.estado()
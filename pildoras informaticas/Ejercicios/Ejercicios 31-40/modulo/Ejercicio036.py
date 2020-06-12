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


class Furgoneta(Vehiculos):
  
  def carga(self, cargar):
    self.cargado=cargar

    if(self.cargado):
      return "La furgoneta esta cargada"
    else:
      return "La furgoneta no esta cargada"


class Moto(Vehiculos):
  
  hcaballito="no estoy haciendo caballito"

  # esta funcion cambia el valor de la variable
  def caballito(self):
    self.hcaballito="Voy haciendo el caballito"
  
  def estado(self):
    print(f"Marca: {self.marca}.\nModelo: {self.modelo}",
    f"\nEn marcha: {self.enMarcha}. \nAcelerando: {self.acelera}.",
    f"\nFrenando: {self.frena}. \n{self.hcaballito}")


class VElectricos(Vehiculos):
  def __init__(self, marca, modelo):
    super().__init__(marca, modelo)

    self.autonomia=100

  def cargarEnergia(self):
    self.cargando=True


class BicicletaElectrica(VElectricos, Vehiculos):
  pass
"""
miBici=BicicletaElectrica("Orbea","hj")
miBici.estado()

print("\n----Otro vehiculo----\n")

miMoto=Moto("Honda","CBR")
miMoto.caballito()
miMoto.estado()

print("\n----Otro vehiculo----\n")

miFurgoneta=Furgoneta("Renault", "Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

"""
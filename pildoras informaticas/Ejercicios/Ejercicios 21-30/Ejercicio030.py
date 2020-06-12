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
  
  # al tener el mismo nombre que el metodo de la clase padre
  # este sobreescribe el anterior
  # en el caso de esta clase tener un hijo
  # el heredaria el estado de esta clase y no de vehiculos
  def estado(self):
    print(f"Marca: {self.marca}.\nModelo: {self.modelo}",
    f"\nEn marcha: {self.enMarcha}. \nAcelerando: {self.acelera}.",
    f"\nFrenando: {self.frena}. \n{self.hcaballito}")



class VElectricos():
  def __init__(self):
    self.autonomia=100

  def cargarEnergia(self):
    self.cargando=True

# Cuando hay herencia multiple
# se le da preferencia al primero que se usa
# como parametro
class BicicletaElectrica(VElectricos, Vehiculos):
  pass

miBici=BicicletaElectrica()

print("\n----Otro vehiculo----\n")

miMoto=Moto("Honda","CBR")
miMoto.caballito()
miMoto.estado()

print("\n----Otro vehiculo----\n")

miFurgoneta=Furgoneta("Renault", "Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))
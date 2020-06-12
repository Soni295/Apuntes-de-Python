import pickle

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


coche1=Vehiculos("Mazda","MX5")

coche2=Vehiculos("Seat","leon")

coche3=Vehiculos("Renault","Megane")

coches=[coche1, coche2, coche3]

fichero= open("losCoches","wb")
# guardo los autos en el fichero
pickle.dump(coches, fichero)

fichero.close()

del fichero

ficheroApertura=open("losCoches","rb")
# los copio para leerlos del fichero
misCoches=pickle.load(ficheroApertura)

ficheroApertura.close()

for i in misCoches:
  
  i.estado()
  print("\n")
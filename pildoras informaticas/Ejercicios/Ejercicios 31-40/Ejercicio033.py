class Coche():
  def desplazamiento(self):
    print("Me desplazo utilizando 4 ruedas")

class Moto():
  def desplazamiento(self):
    print("Me desplazo utilizando 2 ruedas")

class Camion():
  def desplazamiento(self):
    print("Me desplazo utilizando 6 ruedas")

# esta seria la forma sin polimorfismo
miVehiculo=Moto()
miVehiculo.desplazamiento()

miVehiculo2=Coche()
miVehiculo2.desplazamiento()

miVehiculo3=Camion()
miVehiculo3.desplazamiento()


# esta seria la forma con polimorfismo

# hago una funcion que llame al metodo vehiculo
def desplazamientoVehiculo(vehiculo):
  vehiculo.desplazamiento()

miVehiculo4=Camion()

miVehiculo5=Moto()

miVehiculo6=Coche()

desplazamientoVehiculo(miVehiculo4)
desplazamientoVehiculo(miVehiculo5)
desplazamientoVehiculo(miVehiculo6)

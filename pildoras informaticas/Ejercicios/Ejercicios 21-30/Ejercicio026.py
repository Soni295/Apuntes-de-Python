# clase
class Coche():
  
  # propiedades
  largoChasis=250
  anchoChasis=120
  ruedas=4
  enMarcha=False

  # comportamiento(metodos)
    
    # self hace referencia al objeto
    # que pertenece a la clase en si
  def arrancar(self):
    # el self. se refiere a la propiedad
    # del objeto 
    self.enMarcha=True

  def estado(self):
    
    if(self.enMarcha):
      return "El auto esta en marcha"
    
    else:
      return "El coche esta parado"

# Creo un objeto(intanciar una clase)
miCoche=Coche()

# Con esto puedo imprimir el largo chasis
print("El largo del coche es:", miCoche.largoChasis)

# Lo mismo que antes pero con las ruedas
print("El coche tiene", miCoche.ruedas, "ruedas")

# el coche cuando se crea esta en false
# por eso devuelve "El coche esta parado"
print(miCoche.estado())

# con esto cambio el estado de enMarcha
# de false a True
miCoche.arrancar()

# como el estado enMarchar es true
# imprimira "el auto esta en marcha"
print(miCoche.estado())



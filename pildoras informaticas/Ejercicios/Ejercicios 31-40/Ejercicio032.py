class Persona():
  def __init__(self, nombre, edad, lugar_de_residencia):
    self.nombre=nombre
    self.edad=edad
    self.lugar_de_residencia=lugar_de_residencia

  def descripcion(self):
    print(
      f"Nombre: {self.nombre}",
      f"\nEdad: {self.edad}",
      f"\nLugar de recidencia: {self.lugar_de_residencia}")


class Empleado(Persona):
  
  def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, recidencia_empleado):
    
    # Esto llama al metodo init de la clase padre
    # y se ejecutara como tal
    # y le agrege valores de mas que va a pedir
    super().__init__(nombre_empleado, edad_empleado, recidencia_empleado)
    
    self.salario=salario
    self.antiguedad=antiguedad

  def descripcion(self):
    
    # utiliza el metodo del padre
    super().descripcion()    

    print(f"El salario: {self.salario}")
    print(f"antiguedad: {self.antiguedad}")


Antonio=Empleado(1500, 15, "Antonio", 55,"España")
Antonio.descripcion()

# isinstace indica de que clase es un objeto si
# es de esa clase da true caso contrario false

print(isinstance(Antonio, Empleado))

print(isinstance(Antonio, Persona))
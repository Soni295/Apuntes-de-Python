import pickle

class Persona():
  def __init__(self, nombre, genero, edad):
    self.nombre = nombre 
    self.genero = genero 
    self.edad = edad
    print(f"Se ha creado una persona nueva con el nombre de {self.nombre}")
  
  # sirve para convertir en cadena de texto
  # la informacion de un objeto
  def __str__(self):
    return "{} {} {}".format(self.nombre, self.genero, self.edad)


class ListaPersonas():
  personas=[]

  def __init__(self):# para agregar informacion binaria
    listaDePersonas=open("ficheroExternoPersonas", "ab+")
    listaDePersonas.seek(0)

    # aca le digo que diga la cantidad de personas que guardo
    # pero si no guardo a nadie que pase a la execpcion
    try:
      self.personas=pickle.load(listaDePersonas)
      print("Se cargaron {} personas del fichero correspondiente".format(len(self.personas)))
    except:
      print("El fichero esta vacio")
    finally:
      listaDePersonas.close()
      del (listaDePersonas)

  def agregarPersonas(self, persona):
    # con esto agrego personas a la lista
    self.personas.append(persona)
  
  def mostrarPersonas(self):
    for persona in self.personas:
      print(persona)

  def guardarPersonasEnFicheroExterno(self):
    listaDePersonas=open("ficheroExternoPersonas", "wb")
    pickle.dump(self.personas, listaDePersonas)
    listaDePersonas.close()
    del (listaDePersonas) 
  
  def mostrarInfoFicheroExterno(self):
    print("La informacion del fichero externo es la siguiente:")
    for persona in self.personas:
      print(persona) 

miLista=ListaPersonas()

p=Persona("Sandra", "Femenino", 29)
p2=Persona("Antonio", "Masculino", 39)
p3=Persona("Ana", "Femenino", 19)

miLista.agregarPersonas(p)
miLista.agregarPersonas(p2)
miLista.agregarPersonas(p3)
miLista.guardarPersonasEnFicheroExterno()
miLista.mostrarInfoFicheroExterno()
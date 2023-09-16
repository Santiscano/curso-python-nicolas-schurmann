# el polimorfismo consiste en la tecnica de crear diferentes entidades con los mismos metodos aunque hagan diferentes cosas 
# y crear una funcion que ejecute el metodo que tienen en comun las entidades 
# en este caso la funcion guardar ejecuta los metodos guardar de las entidades que le entrego en un array 
from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def guardar(self):
        pass


# el DUCK TYPING es la posibilidad de python para trabajar tipado dinamico, lo que permitiria que no se necesite tener herencia de model para que estos metodos funcionen 
# ya que son metodos definidos internamente y en la funcion guardar solo necesita 2 considiciones para no fallar. 
# 1- recibir una coleccion. 
# 2- que cada clase de la coleccion tenga el metodo guardar.
class Usuario(Model):
    def guardar(self):
        print("guardado en BBDD")

class Session(Model):
    def guardar(self):
        print("guardado en archivo")

def guardar(entitys):
    for entity in entitys:
        entity.guardar()

usuario = Usuario()
sesion = Session()

guardar([usuario, sesion])
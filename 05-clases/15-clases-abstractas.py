# antes de explicar lo que se hace en esta clase se plantea la problematica y es la sigueinte:
# si yo instancio un objeto de la clase Model tendria un gran problema porque  tabla es False asi que cada que se cree un objeto se debe poner obligatorio el tener que definir la tabla a la que se va a acceder con esa instancia o clase heredera
# a lo que inicialmente se importan estos modulos con el objetivo de ....
from abc import ABC, abstractmethod #abc viene de abstrabclass
# despues de hacer heredar la clase principal con ABC debemos indicar que elementos son obligatorios para la creacion de esta clase
class Model(ABC):
    # tabla = False   # se comenta ya que tabla sera el metodo abstracto y siempre sera obliugatorio para los herederos

# ya no se necesita el constructor porque dicha validacion ya se puede evitar
    # def __init__(self):
    #     if not self.tabla:
    #         print("Error, tienes que definir una tabla")

# estos 2 decoradores no van a permitir que se pueda crear una instancia de Model, 
# asi que siempre se tendra que instanciar es desde las clases que hereden esta clase
    @property
    @abstractmethod
    def tabla(self):
        pass

    @property
    @abstractmethod
    def save(self):
        # print(f"Guardando {self.tabla} en BBDD") # ya no uso esto sino que se hara en el heredero
        pass

    @classmethod
    def search_with_id(self, _id):
        print(f"Buscando por id = {_id} en la tabla ${self.tabla}")


class Usuario(Model):
    tabla = "Usuario"

    def save(self):
        print(f"Guardando {self.tabla} en BBDD")



usuario = Usuario()
usuario.save()
Usuario.search_with_id(951) # recordar que @classmethod crea instancias es util para eso
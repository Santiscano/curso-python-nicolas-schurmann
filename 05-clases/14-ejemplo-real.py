class Model():
    tabla = False

    def __init__(self):
        if not self.tabla:
            print("Error, tienes que definir una tabla")

    def save(self):
        print(f"Guardando {self.tabla} en BBDD")

    @classmethod
    def search_with_id(self, _id):
        print(f"Buscando por id = {_id} en la tabla ${self.tabla}")

class Usuario(Model):
    tabla = "Usuario"

usuario = Usuario()
usuario.save()
Usuario.search_with_id(951) # recordar que @classmethod crea instancias es util para eso
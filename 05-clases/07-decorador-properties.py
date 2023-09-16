# para validar que no se escriba un nombre como por ejemplo un boolean o string vacio o diccionarios, etc
# una opcion seria hacer una funcion que valide y asigne el nombre desde una propiedad privada y en el constructor ejecutarla
# sin embargo esto tiene unos peros y es que se mostrarian mas metodos de los que realmente se deben usar pues solo deberia ser el constructor hasta lo que esta hecho aqui
class Perro:
    def __init__(self, nombre):
        self.set_nombre(nombre)
    
    def set_nombre(self, nombre):
        if nombre.strip():
            self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

perro = Perro('choclo')


# ahora la recomendacion de pytho es con el property y estos solo se usan para elementos que devuelven valores es decir getters
class PerroProperties():
    def __init__(self, nombre):
        self.nombre = nombre
    
    @property   # se pone en lo que sera el getter y el automaticamente crea un setter com el mismo nombre en este caso "nombre"
    def nombre(self):
        print('pasando por getter')
        return self.__nombre
    
    @nombre.setter  #este es el setiador y ambos estan ocultos
    def nombre(self, nombre):
        print('pasando por setter')
        if nombre.strip():
            self.__nombre = nombre

perroProperties = PerroProperties("Cuiquitingo")
print(perroProperties.nombre)

#





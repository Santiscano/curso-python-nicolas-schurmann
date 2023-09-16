class Perro:
    # __ con los 2 guiones bajos se define que es privado
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def habla(self):
        print(f"{self.__nombre} dice: Woof")
    @classmethod
    def factory(cls):
        return cls("chanchito feliz", 4)

perro1 = Perro.factory()
# print(perro1.__nombre) # esto genera error
# print(perro1.get_nombre())

# __dic__ es un diccionario que contiene todas las propiedades que tiene una instancia de un objeto
# las propiedades privadas estan nombradas como _nombreClase__nombrePropiedad en este caso los ejemplos serian
# _Perro__nombre
# asi que si quiero verlas puedo hacer lo siguiente
print(perro1.__dict__) # aqui vere los nombres

perro1._Perro__nombre = 'chanchito privado modificado' # aqui modifique una propiedad privada

print(perro1.__dict__)


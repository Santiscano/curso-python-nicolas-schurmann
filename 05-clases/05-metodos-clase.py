# el decorador @classmethod es util para crear instancias definiendo otras utilidades o formas por ejemplo 
# definiendo directamente la edad y nombre del perro o tambien creando una logica que haga el proceso como este caso de calculo de edad
import datetime

class Perro:
    patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} dice: Woof")

    # aqui estamos creando la instancia definiendole el nombre y edad
    @classmethod
    def factory(cls):
        return cls('chanchito feliz', 5) 

    # aqui haremos un calculo para definir la edad
    @classmethod
    def fromBirth(cls, nombre, año_nacimiento):
        edad = datetime.datetime.now().year - año_nacimiento # resta para calcular edad
        return cls(nombre, edad)

sami = Perro("sami", 3)
print(sami.habla())
print(sami.edad)

kiara = Perro.fromBirth("Kiara", 2019)
print(kiara.habla())
print(kiara.edad)


perro3 = Perro.factory()
print(perro3.habla())
print(perro3.edad)





class Perro:
    # __init__ es la forma como se define el constructor
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre # los que son self se refieren a las variables y metodos de la clase los otros son parametros
        self.edad = edad

    
    def habla(self):
        print(f"{self.nombre} dice: Woof")


mi_perro = Perro("sami", 3) # instancia 1
perro_stiven = Perro("kiara", 4) # instancia 2
print(mi_perro.nombre)
print(perro_stiven.nombre)
mi_perro.habla()
perro_stiven.habla()
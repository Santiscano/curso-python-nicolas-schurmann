class Perro:
    patas = 4 # propiedad de la clase
    
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} dice: Woof")

Perro.patas = 3 # cambiamos el valor de la propiedad de la CLASE
mi_perro = Perro("sami", 3)
mi_perro.patas = 5 # cambia el valor de la propiedad de la INSTANCIA
mi_perro2 = Perro("kiara", 4)
print(Perro.patas) #3
print(mi_perro.patas) #5
print(mi_perro2.patas) #3





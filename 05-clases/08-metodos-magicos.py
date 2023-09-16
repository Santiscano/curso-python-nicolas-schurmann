# son metodos que se ejecutan aun cuando no se han llamado, el primero de ellos es el constructor __init__
# todos los metodos magicos inician y terminan con 2 guines bajos por ejemplo __str__ , __init__
# documentacion de metodos magicos  https://rszalski.github.io/magicmethods/
class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f"clase perro: {self.nombre}"

    def habla(self):
        print(f"{self.nombre} dice: Woof")
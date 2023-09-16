class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __del__(self):
        print(f"chao {self.nombre} siempre te recordare")

    # se llama cuando tratemos de imprimir la clase
    def __str__(self):
        return f"Clase Perro: {self.nombre}"

    def habla(self):
        print(f"{self.nombre} dice: Woof")

perro1 = Perro('sami', 3)
perro1.habla()
# creamos una variable donde se guardara en string la instancia de perro, pero este tambien llamara al metodo __str__
texto = str(perro1)
del perro1



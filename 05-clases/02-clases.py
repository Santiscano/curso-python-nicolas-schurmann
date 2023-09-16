# self SIEMPRE debe ser el primer argumento en cada uno de los metodos 
# el nombre de la clase siempre debe iniciar en mayuscula
class Perro:
    def habla(self):
        print("Woof")


mi_perro = Perro() # esto es instanciar
mi_perro.habla() # ejecuta el metodo

print(type(mi_perro)) # vemos el tipo class

# boolean para decir si es una instancia
print(isinstance(mi_perro, Perro)) #True
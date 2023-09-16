class Animal:
    def comer(self):
        print('comiendo')

# la herencia se hace poniendolo dentro de parentecis
class Perro(Animal):
    def pasear(self):
        print("Paseando")

perro = Perro() # instanciamos el objeto perro, que es una clase hija del animal.
perro.comer()

# Herencia multinivel "recomendado no hacerlo mas de 2 niveles"
# chanchito hereda todo lo que tenga animal y tambien lo que tenga perro
class Chanchito(Perro):
    def programar(self):
        print ("Programando en Python")

chanchito=Chanchito()
chanchito.programar()
chanchito.pasear()



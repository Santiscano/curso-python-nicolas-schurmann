class Animal:
    def comer(self):
        print('comiendo')

    def pasear(self):
        print("Paseando al animal")

class Perro:
    def pasear(self):
        print("Paseando al perro")

# esta es la herencia multiple se hace por medio de las comas
class Chanchito(Perro, Animal):
    def programar(self):
        print ("Programando en Python")

# en este caso se presenta la prioblematica de tener el mismo metodo pasear con minimas diferencias
# asi que lo que hara python es escribir primero los metodos de animal y si encuentra un metodo en Perro 
# que tenga el mismo nombre lo sobre escribira es decir quedara el de pasear perro

chanchito = Chanchito()
chanchito.pasear() # paseando al perro

# para esto un mejor ejemplo del correcto usoo seria el siguiente
class Caminador: 
    def caminar(self) :
        print ('caminando')
    
class Volador:
    def volar (self) :
        print("volando")

class Nadador:
    def nadar (self) :
        print("nadando")

# aqui podemos ver como una clase puede extenderse varias veces sin problemas ya que no hay ambiguedades
class Aves(Caminador ,Volador ):
    pass

# pero tambien podemos hacerlo de otra manera
class Mamifero(Nadador ,Caminador ) :
    pass


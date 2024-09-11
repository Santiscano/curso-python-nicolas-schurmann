# la anulacion de metodos refiere a que se puede redefinir un metodo de la clase padre en la clase hija
class Ave:
    def __init__(self) -> None:
        self.volador = True

    def vuela(self):
        print("Estoy volando")


class Pato(Ave):
    def __init__(self):
        self.nadador = True
        super().__init__()

    def vuela(self): # aqui estamos redefiniendo el metodo vuela asi que este sera el que se muestre
        print("vuela pato")
        super().vuela() # super me entrega todos los metodos del padre

pato = Pato()
pato.vuela()
print(pato.volador, pato.nadador)
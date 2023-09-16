class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self) :
        return f"Producto: {self.nombre} -Precio: {self.precio}"


class Categoria:
    productos = []

    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos

    def agregar(self, producto):
        self.productos.append(producto)

    def imprimir(self):
        for producto in self.productos:
            print(producto)
    

kayak = Producto("kayak", 1000)
bicicleta = Producto('bicicleta', 500)
camiseta = Producto ('camiseta',234 )

deporters = Categoria("deportes", [kayak, bicicleta])

deporters.agregar(camiseta)
deporters.imprimir()








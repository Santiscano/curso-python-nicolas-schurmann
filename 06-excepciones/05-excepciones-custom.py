class MyError(Exception):
    "Esta clase es para representar mi error personalizado"

    def __init__(self, mensaje, codigo):
        self.mensaje = mensaje
        self.codigo = codigo
    
    def __str__(self):
        return f"{self.mensaje} - codigo: {self.codigo}"


def division(n=0):
    if n == 0:
        raise MyError("No es posible dividir por cero", 805)
    return 5 / n

try:
    division()
except MyError as err:
    print('Ocurrio un Error:',err.codigo, err.mensaje) # podemos acceder a lo que se crea en el constructor
    print(err) # este por su parte imprime el metodo magico __str__
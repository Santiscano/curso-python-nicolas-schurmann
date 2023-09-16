# https://docs.python.org/3/library/exceptions.html
# documentacion de exceptions en python

def division(n=0):
    if n == 0:
        raise ZeroDivisionError("No es posible dividir por cero")
    return 5 / n

# la operacion simplemente genera error porque matematicamente no es posible dividir entre 0
try:
    division()
except ZeroDivisionError as err:
    print('Ocurrio un Error:',err)
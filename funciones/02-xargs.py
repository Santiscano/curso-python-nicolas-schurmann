def suma(a, b, c):
    print(a + b + c)

suma(2,5,3)
# esto limita a que siempre deba entregar 3 argumentos, para poder hacer esto de manera dinamica se utiliza el xargs
def suma1(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print("El resultado es:", resultado)

suma1(2,4,8,4,6,4,9)
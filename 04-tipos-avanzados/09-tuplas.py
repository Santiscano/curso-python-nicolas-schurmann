# son lo mismo que una lista, solo que no se pueden modificar
# pero si se pueden crear nuevas en base a las existentes
numeros = (1,2,3, 4, 5, 6, 7, 8, 9)
print(type(numeros))
print(numeros)

# crear tuplas en base a listados
puntos = tuple([1, 2]) # las tuplas reciben cualquier tipo de dato que sea iterable

menosNumeros = numeros[:2] # se puede crear unevas tuplas
print(menosNumeros)
primero, segundo, *otros = numeros
print(primero, segundo, otros)

# se pueden iterar
for numero in numeros:
    print(numero)

# numeros[0] = 5 # esto da ERROR
# si es que necesito manipular informacion debo crear una lista con la tupla y esa si se usara

listaCreadaDeTupla = list(numeros)

listaCreadaDeTupla[0] = "Chanchito cambiado"
print(listaCreadaDeTupla)
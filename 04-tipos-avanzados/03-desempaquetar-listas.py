numeros = [1, 2, 3]

# feo!
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]

# bonito
primero, segundo, tercero = numeros

masNumeros = [1,2,3,4,5,6,7,8,9]
soloprimero, segundo, *otros, penultimo, ultimo = masNumeros # 1, 2 [3,4,5,6,7], 8, 9
print(soloprimero, segundo, penultimo, ultimo)
print(otros)
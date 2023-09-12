# iterar lista de elementos
buscar = 3

for numero in range(5): # range regresa una secuencia de numeros 0,1,2,3,4
    if numero == buscar:
        print("El numero que buscas es: ", numero)
        break
    else:
        print(numero)
else:
    print('No se encontro el elemento')


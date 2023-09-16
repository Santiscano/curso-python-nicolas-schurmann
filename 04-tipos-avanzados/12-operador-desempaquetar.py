lista = [1,2,3,4]
print(*lista)

listTupla = (1,2,3,4)
print(*listTupla)

lista2 = [5,6]

# para listas se utiliza 1 asterisco
listCombinada = [ *lista, *lista2 ]
print(listCombinada)

# para diccionarios se utilizan 2
punto1 = {'x': 19}
punto2 = {'y': 15}

unionPuntos = { **punto1, **punto2 }
print(unionPuntos)

# si ya existe la clave en uno de los lados que se convinara

punto3 = {'x': 19, 'y': 'soy el original'}
union1y3 = { **punto3, **punto2 }
# la dinamica consiste en que inicia de derecha a izquierda, 
# entonces primero observa las propiedades de punto2 y si existen en punto3 la remplazara como es el caso de y
# si no existe entonces la asignara a punto3
# es decir el diccionario final es el de la izquierda pero el valor que quedara si es que existen llaves iguales son las llaves que mas a la derecha esten









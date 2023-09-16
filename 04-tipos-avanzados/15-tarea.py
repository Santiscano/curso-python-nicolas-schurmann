from pprint import pprint
# 1. eliminar los espacios en blanco de un string y devolver una lista con los caracteres restantes
# 2. contar en un diccionario cuanto se repiten los caracteres de un string
# 3. ordenar las llaves de un diccionario por el valor que tienen y devolver una lista que contiene tuplas [("a",3), ("b",2), ("c",4), ("d",4)]
# 4. de un listado de tuplas, devolver las que tengan el mayor valor. [("a",3), ("b",2), ("c",4), ("d",4)] -> [("c",4), ("d",4)]
# 5. crear un mensaje que diga: los caracteres que mas se repiten con x repeticiones son: -C -D 

# 6. Juntar la solucion de los ejercicios anteriores para encontrar los caracteres que mas se repiten de un string.


# 1.
string = "hola este es mi string"
def delete_space(text):
    return[ char for char in text if char != " "]

with_out_space = delete_space(string)
print(with_out_space)

# 2.
def count_characthers(list):
    chars_dict = {}

    for char in list :
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    
    return chars_dict

counting = count_characthers(with_out_space)
pprint(counting, width=1)


# 3.
def toOrder(dict):
    return sorted(
        dict.items(),
        key=lambda key: key[1],
        reverse=True
    )

isOrder = toOrder(counting)
print(isOrder)


# 4.
def max_tuplas(list):
    maxNumer = list[0][1] #accedemos al numero de la primer tupla
    response = {} # creamos el nuevo diccionario
    
    for order in list:
        if maxNumer > order[1]:
            break
        response[order[0]] = order[1]
    
    return response

maxValues = max_tuplas(isOrder)
print(maxValues)

# 5.
def create_message(dict):
    message = "Los que mas se repiten son: \n"

    for key, value in dict.items():
        message += f"- {key} con {value} repeticiones \n"
    
    return message

final_message = create_message(maxValues)
print(final_message)


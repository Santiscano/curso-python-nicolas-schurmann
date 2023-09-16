mascotas = [
    "Wolfgang",
    "pelusa", 
    "pulga", 
    "santiago", 
    "pulga",
    "chanchito feliz"
]

# quiero agregar despues de wolfgan es decir en la posicion 1
mascotas.insert(1, "melvin agregado") # agrego indicando en que posicion
mascotas.append("chanchito triste") # agrega en ultima posicion

mascotas.remove("pulga") # elimina solo la primer ocurrencia
mascotas.pop() # elimina la ultima posicion
mascotas.pop(1) # si paso index elimina esa posicion
del mascotas[2] # lo mismo de eliminar por index
mascotas.clear() #limpia todo lo deja vacio

print(mascotas)


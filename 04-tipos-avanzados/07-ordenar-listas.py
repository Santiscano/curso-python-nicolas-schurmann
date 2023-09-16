numeros = [4, 54, 12, 7, 1, 9, 23, 21]

# numeros.sort(reverse=True) # modifica el array
ordenados = sorted(numeros, reverse=True) # esta funcion devuelve una nueva lista
print(numeros)
print(ordenados)

usuarios = [[3, "kelly"], [12, "stefa"], [1, "yenny"]]
usuarios.sort()
print(usuarios)

usuariosNombre = [["stefa", 12], ["yenny", 1], ["kelly", 3],]
usuariosNombre.sort() # aqui los ordeno por nombre no por numero
print(usuariosNombre)

#el intenta ordenar en base al primer criterio de cada elemento en este caso de los iterables

# pero si se requiere en base a otro elemento se tendra que buscar otra opcion por ejemplo en este segundo se quiere seguir ordenando por numero
# una forma de solucionar seria entregandole una funcion que devuelva dicha key
def ordena(element):
    return element[1]

usuariosNombre.sort(key=ordena, reverse=True)
print(usuariosNombre)

# pero una mas adecuada seria usar una funcion lamdba "anonima"
usuariosNombre.sort(key=(lambda el:el[1]))# la lambda es una function anonima
print(usuariosNombre)








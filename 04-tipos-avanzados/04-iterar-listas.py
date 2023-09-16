# listas - strings - range son iterables
mascotas = ["pelusa", "pulga", "santiago", "chanchito feliz"]

# enumerate es una funcion que regresa una tupla con el indice y el valor
# una tupla es algo como esto ('0', 'pelusa') y se accede igual que las listas con []
# for mascota in enumerate(mascotas):
#     print(mascota, mascota[0], mascota[1])
for indice, mascota in enumerate(mascotas):
    print(indice, mascota)




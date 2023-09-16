# el ejercicio es dentro de la nueva lista nombres agregar solo los nombres de la lista usuarios
usuarios = [["stefa", 12], ["yenny", 1], ["kelly", 3],]

nombres = []

for usuario in usuarios:
    nombres.append(usuario[0])

print(nombres)

# este for que hice se puede resumir en 1 linea
# nombres = [expresion for item in items]
names = [usuario[0] for usuario in usuarios] # esto es como map
print("names", names)

# filtrar
# namesFilters = [expresion for item in items]
# namesFilters = [usuario for usuario in usuarios if usuario[1] > 2] # aqui devuelve cada lista completa que cumpla
# namesFilters = [usuario[0] for usuario in usuarios if usuario[1] > 2] # aqui solo devuelve la primer posicion de cada una que cumpla

# methods
namesMethods = list(map(lambda usuario: usuario[0], usuarios))
print("map", namesMethods)

filterMethods = list(filter(lambda usuario: usuario[1] > 2, usuarios))
nameFilterMethods = [usuario[0] for usuario in filter(lambda usuario: usuario[1] > 2, usuarios)]

print("filter", filterMethods)
print("filter", nameFilterMethods)

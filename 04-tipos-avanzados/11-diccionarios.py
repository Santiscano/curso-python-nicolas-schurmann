# son coleccion de datos agrupados por llave y valor
# nombre = "hola mundo"

# solo acepta string en la llave, cualquier tipo de dato en valor
punto = {
    'x': 10,
    'y': 50
}
print(punto)
print(punto['x']) #en javascript se usa el punto aqui se usa es las llaves
print(punto['y'])

punto['z'] = 45
print(punto)

if 'lala' in punto:
    print(punto['lala']) #este no se ejecuta porque no existe

print('accediendo con .get()',punto.get('x'))

# tambien recibimos un segundo argumento para asignar un valor si no existe
print('accediendo con .get()',punto.get('lala'), 97)

# si quiero eliminar una llave con su valor
del punto['x']
del(punto['y'])

print('despues de eliminar', punto)

punto['x'] = 25

# iterar las llaves con su valor se puede con for
for valor in punto:
    print(punto[valor])

for valor in punto.items():
    print(valor)

for llave, valor in punto.items():
    print(llave, valor)


# uso real ejemplo

usuarios = [
    {'id': 1, 'nombre': "chanchito feliz"},
    {'id': 2, 'nombre': "chanchito triste"},
    {'id': 3, 'nombre': "santiago"},
]

for usuario in usuarios:
    print(usuario['nombre'])
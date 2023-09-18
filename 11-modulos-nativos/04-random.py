import random

lista = [1,2,3,4,5,6,7,8]
random.shuffle(lista)

lista2 = [1,2,3,4,5,6,7,8]
print(
    random.random(), # devuelve un numero entre 0 y 1
    random.randint(1, 10), #defino el rango entre los que quiero el numero
    lista, # cambia el orden de la lista
    random.choice(lista2), # nos entrega un valor aleatorio de la lista
    random.choices(lista2, k=3), # si quiero 3, 4, o la mitad, el segundo argumento indico la cantidad
    random.choices("abcdefghi", k=3), # tambien funciona con strings
    "".join(random.choices("abcdefghi", k=3)), # asi lo uno con cualquier otro string
)

# python tiene un modulo que ya constiene todos los caracteres en mayus, minus y numeros
import string

chars = string.ascii_letters # mayusculas y minusculas
digitos = string.digits # numeros
seleccion = random.choices(chars + digitos, k=16)
print('seleccion',seleccion)
constrasena = "".join(seleccion)
print ('contrasena generada:', constrasena )



# python no recomienda el uso de variables globales y el uso del mismo nombre de variable lo instancia como otra variable distinta
# la forma de poder usar una variable global es utilizando la palabra reservada global y ahi si se esta asignando la variable global
saludo = "Hola global"

def saludar():
    global saludo
    saludo = "Hola global modificada"

def saludaChanchito():
    saludo = '¡Hola chanchitos!'
    print(saludo)

print(saludo)
saludar()
saludaChanchito()
print(saludo)
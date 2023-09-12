def hola(nombre, apellido=" "): # usamos palabra reservada, nombre de la funcion, parentesis y :
    # print("Hola mundo a una funcion")
    print(f"Bienvenido {nombre} {apellido}")


hola("Santiago","Sierra")
hola("Estefany")
hola("Chanchito", "Feliz")

hola(apellido="Cano", nombre="Maria") #enviar los argumentos en desordern "argumentos nombrados"


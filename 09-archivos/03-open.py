from io import open

# escritura
# texto = " hola mundo!"

# archivo = open("09-archivos/hola-mundo.txt", "w")
# archivo.write(texto) # la funcion open siempre despues de abrirlo hay que cerrarlo sino seguira ocupando memoria
# archivo.close()


# lectura
# archivo = open("09-archivos/hola-mundo.txt", "r") # "r" es el valor por defecto si se quiere no se debe poner
# texto = archivo.read()
# archivo.close()
# print(texto)


# lectura como lista
# archivo = open("09-archivos/hola-mundo.txt", "r") # "r"  
# texto = archivo.readlines() # lee todas las lineas y las separa en un listado y las entrega a la variable de texto
# archivo.close()
# print(texto)


# metodos magicos
# with cierra automaticamente el archivo sin indicarlo - with podria ser un remplazo de try - except
# archivo.__enter__   => se ejecuta cuando se abra el archivo
# archivo.__exit__    => se ejecuta cuando termina todo lo que esta dentro del bloque de with
# PUNTERO = cuando se abre un archivo cuentan con un puntero que lo que hace es ir linea por linea y no regresar , es decir que si necesitamos que regrese a una linea especifica debemos indicarseo
# la indicacion de mover el puntero se hace con la funcion seek()
# en este caso readlines recorrera todo, seek lo reinicia a 0 y el for nuevamente lo recorre desde el 0

# with open("09-archivos/hola-mundo.txt", "r") as archivo:
#     print(archivo.readlines()) # este carga todo el archivo en memoria
#     archivo.seek(0) 
#     for linea in archivo: # en este caso solo carga 1 linea a la vez 
#         print(linea)


# agregar
# archivo = open("archivos/hola-mundo.txt", "a+")
# archivo.write("mensaje agregado")
# archivo.close()

# lectura y escritura
with open('09-archivos/hola-mundo2.txt', 'r+') as archivo: # 'r+' es para indicar lectura escritura
    texto = archivo.readlines() # escribe cada linea en una lista, pero tambien mueve el puntero hasta el final
    archivo.seek(0)
    texto[0] = "Chanchito feliz"
    archivo.writelines(texto) # nos permite escribir una lista dentro del archivo

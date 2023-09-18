from pathlib import Path
import csv


archivo = Path("09-archivos/archivo-prueba.txt")

# texto = archivo.read_text() # asi puedo leer el archivo
texto = archivo.read_text("utf-8").split("\n") # con split estoy indicando que cree una lista y le indico el caracter por el cual se dividira
print(texto)
# inserto en la posicion 0 el hola mundo, porque en este momento texto es un array
texto.insert(0, "hola mundo!")
# write solo recibe string asi que debo convertirlo primero en string antes de entregarlo
archivo.write_text("\n".join(texto), "utf-8")


# metodo 2 lectura - escritura ---mas complicada--- seria la del ejemplo de 03-open.py






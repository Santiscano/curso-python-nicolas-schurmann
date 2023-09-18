import sqlite3

conexion = sqlite3.connect("10-sqlite/app.db") #intentara conectarse con el archivo, sino existe python lo intentara crear
# cada vez que nos conectemos con una base de datos hay que cerrarla sino no se puede volver a escribir en la base de datos
conexion.close()
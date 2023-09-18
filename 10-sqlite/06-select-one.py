import sqlite3

with sqlite3.connect("10-sqlite/app.db") as conexion:
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuarios") # no estoy creando una variable para tomar el valor que devuelve sino que queda almacenado dentro del cursor y con fetchone se observa
    print(cursor.fetchone()) # solo nos mostrara el primer registro
import sqlite3


with sqlite3.connect("10-sqlite/app.db") as conexion:
    cursor = conexion.cursor()
    cursor.execute(
        "insert into usuarios values(?, ?)",
        [1, "hola mundo"]
    )

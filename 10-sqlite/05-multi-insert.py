import sqlite3

# multiples inserts
with sqlite3.connect("10-sqlite/app.db") as conexion:
    cursor = conexion.cursor()
    usuarios = [
        (2, "Juan"),
        (78965,"Pedro")
    ]
    cursor.executemany(
        "insert into usuarios values(?, ?)",
        usuarios
    )
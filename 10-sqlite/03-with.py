import sqlite3

# cuando se usa el operador with el llamara los metodos magicos de __exit__ por eso no hay necesidad de cerrar la conexion
# y si no hay errores llama a commit asi que no se necesita
with sqlite3.connect("10-sqlite/app.db") as conexion:
    cursor = conexion.cursor()

    cursor.execute(
        """
        CREATE TABLE if not exists usuarios
        (id INTEGER primary key, nombre VARCHAR(50));
        """
    )

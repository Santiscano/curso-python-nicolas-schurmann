import sqlite3

conexion = sqlite3.connect("10-sqlite/app.db")

# para realizar consultas se debe crear un objeto llamado cursor y se crea apartir de la conexion
# es un intermediario entre la libreria sqlite 3 y nosotros 
cursor = conexion.cursor()

# asi solo no se EJECUTARA
cursor.execute(
    """
    CREATE TABLE if not exists usuarios
    (id INTEGER primary key, nombre VARCHAR(50));
    """
)

# el metodo commit es el que comprometen los cambios a que se guarde la informacion
conexion.commit()
conexion.close()
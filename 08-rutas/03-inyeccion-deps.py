# import Correa # para dar mayor posibilidades entregamos este import por parametros

# class Perro:
#     def __init__(self, Correa):
#         self.correa = Correa()

# -----------------------#
# aqui se estan dando 2 ejemplos el primero sin inyeccion de dependencias y el segundo con inyeccion
# las diferencias y ventajas son las siguientes:
# sin inyeccion estas obligando y limitando a que el metodo guardar solo pueda guardar 1 tipo de imformacion, por ejemplo solo fotos
import usuario

def guardar():
    usuario.gardar()

# mientras que en este ejemplo a inyectar la dependencia yo puedo definir si lo que guardo son fotos, videos, audios, etc
def guardar(entidad):
    entidad.guardar()

# -------------------------------------------#
from pathlib import Path
import db
import api
import graphql

path = Path()
paths = [p for p in path.iterdir if p.is_dir()]

dependencias = {
    "db": db,
    "api":api,
    "graphql":graphql
}

def load(p):
    paquete = __import__(str(p).replace("/", "."))
    try:
        paquete.init(**dependencias)
    except: 
        print("el paquete no tiene el metodo init")

list(map(load, paths))


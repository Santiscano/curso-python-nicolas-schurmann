# el estandar de python para nombrar archivos es con guion bajo _ ejemplo user_taks
# NUNCA IMPORTAR CON * 
# PAQUETES se refiere a carétas, MODULOS refieren a archivos
# para indicarle a python que una carpeta es un paquete se debe crear un archivo __init__.py
# la invocacion seria PAQUETE.MODULO

from usuarios.usuario_impuestos import guardar, pagar_impuestos

guardar()
pagar_impuestos()

# LA SEGUNDA FORMA SERIA 
from usuarios import usuario_impuestos

usuario_impuestos.guardar()
usuario_impuestos.pagar_impuestos()

# esta es la forma de importar subpaquetes
from usuarios.admin.utilidades import cobrar

cobrar()

# ---------------------------dir-------------#
# import usuarios
# build, chache, doc, file, loader, name, package, path, spec
# print(dir(usuarios))
# print(usuarios.__name__)
# print(usuarios.__package__)
# print(usuarios.__path__)
# print(usuarios.__file__)
# esto mismo se podria hacer con los subpaquetes
# print(usuarios.admin.__init__)
# ..........

# --------------------------nombres dinamicos------------#
print(__name__)
# la importacion siempre se llama main desde donde se ejecute, y eso podria ser util para el ejemplo del archivo utilidades.py

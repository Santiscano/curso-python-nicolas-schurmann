from pathlib import Path
from time import ctime

archivo = Path("09-archivos/archivo-prueba.txt")
# archivo.exists() # validar si existe
# archivo.rename() # renombrar el archivo
# archivo.unlink() # eliminar el archivo

print(archivo.stat()) # entrega estadisticas como el tamaño, fecha de acceso, modificacion, otros

# ctime es para formatear la fecha
print('acceso',ctime(archivo.stat().st_atime)) # st_atime es fecha de acceso al archivo y lo entrega en timestamp
print('creacion',ctime(archivo.stat().st_ctime))
print('modificacion',ctime(archivo.stat().st_mtime))





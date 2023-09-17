from pathlib import Path

# path = Path("directorio")

# path.exists() #pregunta si existe
# path.mkdir() # crear directorio
# path.rmdir() # eliminar directorio - tiene la condicion de que debe estar vacio
# path.rename("chanchito-feliz") #cambiar nombre al directorio



# ------------------------------------------------------#

path = Path("08-rutas")

# for p in path.iterdir():
#     print(p) #muestra los directorios y archivos de este directorio

archivos = [p for p in path.iterdir() if not p.is_dir()] # condicion para solo archivos
archivosSuffix = [p for p in path.glob("*.py")] # mostrar todos los que tengan extencion .py
mkdirSuffix = [p for p in path.glob("**/*.py")] # dentro de todas las carpetas de rutas todos los archivos de .py 
mkdirSuffix = [p for p in path.rglob("*.py")] # r de recursivo = es lo mismo que la anterior con otra forma de sintaxis 

# print(archivos)
# print(archivosSuffix)
print(mkdirSuffix)
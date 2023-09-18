from pathlib import Path
from zipfile import ZipFile

# Escribir archivos comprimidos
# with ZipFile("09-archivos/comprimidos.zip", "w") as zip:
#     for path in Path().rglob("*.*"): # los asteriscos significan cualquier nombre . cualquier extension incluido carpetas
#         print(path) 
#         if str(path) != "09-archivos/comprimidos.zip":
#             zip.write(path)


# leer archivos comprimidos
with ZipFile("09-archivos/comprimidos.zip") as zip:
    # print(zip.namelist()) # indica todo lo que se encuentra dentro del archivo comprimido
    info = zip.getinfo("09-archivos/06-comprimidos.py") # acceder a la info de un archivo
    print(
        info.file_size,
        info.compress_size
    )
    zip.extractall("09-archivos/descomprimidos") # extraer todo lo que este en el archivo comprimido, aqui indique la carpeta



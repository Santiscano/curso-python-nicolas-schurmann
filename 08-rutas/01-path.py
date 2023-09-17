from pathlib import Path

# Path(r"C:\Archivos_de_programa\Minecraf")#esto se llama raw dtring y se usa para que no considere los \ "back-slash" como un caracter de escape
# Path("/usr/bin")
# Path()
# Path.home()
# Path("one/__init__.py")

path = Path("hola-mundo/mi-archivo.py")
path.is_file()
path.is_dir()
path.exists()


print(
    path.name, #nombre_del_archivo.py
    path.stem, #nombre del archivo sin extension
    path.suffix, #extension del archivo
    path.parent, #directorio padre
    path.absolute() #ruta completa de donde esta este archivo
)

p = path.with_name("chanchito.js") # nos permite cambiar el nombre del archivo incluido la extension
print(p)
p = path.with_suffix(".exe")
print(p)
p = path.with_stem("feliz")
print(p)
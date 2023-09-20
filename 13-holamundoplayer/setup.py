import setuptools
from pathlib import Path

long_desc = Path("README.md").read_text()

#los argumentos deben ser nombrados
setuptools.setup(
    name="holamundoplayer", # nombre del paque te que tendra dentro de pypi
    version="0.0.1",
    long_description=long_desc, # descripcion que aparecera dentro de pypi, lo que hacemos es importar lo que se escribio dentro de readme.md
    packages=setuptools.find_packages(
        exclude=["mocks", "tests"] # indicamos que carpetas no incluir
    ), # indicamos donde se encuentran los paquetes
)
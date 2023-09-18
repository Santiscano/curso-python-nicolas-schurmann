import os
from pathlib import Path
import sys

# print(sys.argv) #argumentos del cli

def cli(args):
    if len(args) == 1:
        print("No hay argumentos")
        return
    
    if len(args) != 3:
        print('se necesitan 2 argumentos')
        return
    
    origen = args[1]
    o = Path(origen)
    if not o.exists():
        print('Origen no existe')
        return

    destino = args[2]
    d = Path(destino)
    if d.exists():
        print('el destino ya existe')
        return

    os.rename(str(origen), str(destino))
    print("Archivo renombrado con exito")

# a la funcion le puse cli, no es nativo, fue el nombre que le di
cli(sys.argv)

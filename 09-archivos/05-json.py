import json
from pathlib import Path


# # escribir json
# productos = [
#     {"id": 1, "name": "Surfboard"},
#     {"id": 2, "name": "Bicicleta"},
#     {"id": 3, "name": "Skaate"},
# ]

# data = json.dumps(productos)

# Path("09-archivos/productos.json").write_text(data)


# leer json
data = Path("09-archivos/productos.json").read_text(encoding="utf-8")
productos = json.loads(data)
print(productos)

with open('09-archivos/productos.json') as f:
    data = json.load(f)
    print('open',data)


# modificar json
productos[0]["name"] = "Chanchito feliz"
Path("09-archivos/productos.json").write_text(json.dumps(productos))

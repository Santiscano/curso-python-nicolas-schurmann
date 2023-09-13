# kwargs => keyword arguments
def get_products(**datos): #cuando van los 2 asteriscos al llamarla debe tener el nombre del parametro
    # print(datos)
    print(datos["id"], datos["name"], datos["des"]) # dentro de [] ponemos nombre del parametro

get_products(id="id",
             name="iphone",
             des="Esto es un iphone")

# {"id": 'id', "name": "iphone", "desc": "Esto es...."}
# parametro: argumento
# ESTO SE LLAMA DICCIONARIO
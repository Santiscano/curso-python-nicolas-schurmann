animal = "chanCHito feliz"
print(animal.upper())
print(animal.lower())
print(animal.capitalize()) # toma solo la primera en mayuscula
print(animal.title()) # mayuscula cada primer letra de cada palabra
print(animal.strip()) # remueve espacios a la izquierda y derecha
print(animal.rstrip()) # remueve rigth
print(animal.lstrip()) # remueve left
print(animal.find("CH")) #devuelve la posicion donde lo encuentra si devuelve -1 es que no lo encontro
print(animal.replace("nCH", "j")) # si la encuentra lo cambia el primero por el 2do
print("nCH" in animal) # devuelve un booleano si existe o no
print("nCH" not in animal) # devuelve un booleano si existe o no



"""methodos_de_strings"""

nombre_curso = "Ultimate python"
descripcion_curso = """
Ultimate python,
este curso completa todos los detalles que necesitas
aprender para encontrar un trabajo como programador
"""
print(len(nombre_curso))
print(nombre_curso[0]) #aqui accedemos al primer caracter
print(nombre_curso[:]) # izquierda donde inicia - derecha donde termina
print(nombre_curso[0:8]) # inicia 0 hasta el 8vo caracter
print(nombre_curso[9:]) # inicia desde el caracter 9 hasta el final
print(nombre_curso[:8]) # desde el inicio hasta el 8

nombre = "Santiago"
apellido = "Sierra"

nombre_completo = nombre + " " + apellido
nombre_completo_correcto = f"{nombre} {apellido}"
nombre_producto = f"{nombre[0]}-{79632}"

print(nombre_completo)
print(nombre_completo_correcto)
print(nombre_producto)



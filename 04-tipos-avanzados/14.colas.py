# pila es una algo encima de otro, como por ejemplo una moneda encima de otra
# last in, first out
pila = []
pila.append(1)
pila.append(2)
pila.append(3)
print(pila)

# si quiero eliminar en la pila
last = pila.pop() # regresa el ultimo elemento y lo borra del final
print("ultimo: ", last)

pila.pop()
pila.pop()
if not pila:
    print('pila vacia')
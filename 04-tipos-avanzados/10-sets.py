# set significa grupo o conjunto
# coleccion de datos que no se puede repetir ni esta ordenada
primer = {1,1,2,2,3,4}
print(primer) # {1,2,3,4}

primer.add(5)
primer.remove(1)
print("primer", primer)

segundo = [4,5,6,7]
segundo = set(segundo)
print("segundo", segundo)

# operadores de set
print("| = union",primer | segundo) # toma todos de todos y elimina repetidos
print("& = intercepcion",primer & segundo) # toma solo los iguales
print("- = diferencia", primer - segundo) #los que son unicos del primer y no en el segundo
print("^ = diferencia simetrica", primer ^ segundo) #los que son unicos de los 2

# no se puede acceder a los elementos de este
# lo que si se puede hacer es preguntar si existe
if 5 in segundo:
    print('si valido si existe')

mascotas = ["wolfgang", "pelusa", "pulga", "copito"]
print(mascotas[0]) # acceder a la posicion

mascotas[0] = "Bicho" #cambia el valor de esa posicion
print(mascotas)

print(mascotas)[0:3] # trae desde el elemento 0 y trae 3 "si no se uno de los valores lo toma como el inicial o final respectivamente"
print(mascotas)[2:] #trae desde el 2 hassta el final
print(mascotas)[-1] # va al final
print(mascotas)[::2] # toma el primero salta el segundo, toma el 3 etc....
print(mascotas)[1::2] # inicia desde "pelusa" salta pulga toma copito


numeros = list(range(21))
print(numeros[::2]) # trae pares
print(numeros[1::2]) # trae inpares
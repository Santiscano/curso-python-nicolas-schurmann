lista = list([1,2,3])

lista.append(4) #agrega de ultimo

lista.insert(0, 0)

print(lista)


# ---------------------------------------------------------------------------------------------#

class Lista(list):
    def prepend (self , item ):
        self.insert(0, item)


list = Lista([1,2,3])
list.append(4)
list.prepend(0)
print(list)
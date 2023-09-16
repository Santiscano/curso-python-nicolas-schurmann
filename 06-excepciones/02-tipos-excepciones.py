try:
    ni = int(input("ingrese numero"))
# except Exception as err: # esto entrega el tipo del error
except ValueError as err :  # esta indica el valor del error
    print ("error", type(err), err)

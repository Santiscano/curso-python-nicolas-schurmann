try:
    ni = int(input("ingrese numero"))
except Exception as err: 
    print ("ocurrio un error", type(err), err)
else: # este se ejecuta siempre y cuando no existan errores
    print ("no ocurrio ningun error")
finally: # este siempre se ejecuta, con o sin errores
    print('se ejecuta siempre finally')
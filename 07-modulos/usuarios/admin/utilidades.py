# cada punto me lleva atras y puedo seleccionar tanto carpetas como archivos
# from ..usuario_impuestos import guardar

# print(__name__)

# def cobrar():
#     print("pagame")

# guardar()

# esto solo se ejecutara cuando se ejecute directamente este archivo, no cuando se este importando de otro archivo
# if __name__ == "__main__":
#     print("tarea de mantenimiento")




#  para cuando se quiere ejecutar condicionalmente si es importado o local se podria hacer lo siguiente
if __name__ != "__main__":
    from ..usuario_impuestos import guardar # import relativo
    from usuarios.usuario_impuestos import guardar # import absoluto
    
    print(__name__)

    def cobrar():
        print("pagame")

if __name__ == "__main__":
    print("tarea de mantenimiento")

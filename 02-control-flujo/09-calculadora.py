print("Bienvenido a la calculadora")
print("para salir escribe 'salir'")
print("Las operaciones son sum, res, mul, div")

resultado = ""
while True:
    if not resultado:
        resultado = input("Ingrese numero: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("Ingresa operacion: ")
    if op.lower() == "salir":
        break
    n2 = input("ingresa siguiente numero ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "sum":
        resultado += n2
    elif op.lower() == "res":
        resultado -= n2
    elif op.lower() == "mul":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    else: 
        print("Operación no valida")
        break
    
    print(f"El resultado es {resultado}")

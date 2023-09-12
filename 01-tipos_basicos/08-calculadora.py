n1 = input("ingresa el primer numero")
n2 = input("ingresa el segundo numero")

n1 = int(n1)
n2 = int(n2)

sum = n1 + n2
res = n1 - n2
mul = n1 * n2
div = n1 / n2

mesagge = f"""
para los numeros {n1} y {n2}
el resultado para la suma es {sum}
el resultado para la resta es {res}
el resultado para la multiplicacion es {mul}
el resultado para la division es {div}
"""

print(mesagge)
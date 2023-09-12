# and. or, not

gas = False
encendido = True
edad = 18

if gas and encendido:
    print("puedes avanzar 1")

if gas or encendido:
    print("puedes avanzar 2")

if not gas and encendido and edad > 17: 
    print("puedes avanzar 3")

if gas or (encendido and not edad < 17): 
    print("puedes avanzar 4")


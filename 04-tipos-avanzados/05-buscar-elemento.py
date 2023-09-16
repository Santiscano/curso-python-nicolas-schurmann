mascotas = ["pelusa", "pulga", "santiago", "chanchito feliz"]

print(mascotas.index("pulga")) # 1
# print(mascotas.index("wolfgang")) # error, para evitar hay que validar

if "Wolfgang" in mascotas:
    print(mascotas.index("Wolfgang"))

print(mascotas.count("pelusa"))


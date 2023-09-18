# import time

# print(time.time()) # fecha en timestamp 1-enero-1970 UTC



# https://docs.python.org/3/library/datetime.html

from datetime import datetime

fecha = datetime(2023, 9, 18)
fecha2 = datetime(2023, 2, 18)
print(fecha)

ahora = datetime.now()
print(ahora)

# fechas apartir de strings
fechaStr = datetime.strptime("2023-01-03", "%Y-%m-%d") # tambien pueden ser / en vez de -
print('string a fecha',fechaStr)

# string apartir de una fecha
print("fecha a string",fecha.strftime("%Y/%m/%d"))

# comparar fechas
print(fecha > fecha2) # True

# propiedades de fecha
print(
    "propiedades",
    fecha.year,
    fecha.month,
    fecha.day,
    fecha.hour,
    fecha.minute,
)

from datetime import datetime, timedelta

# timedelta en este caso lo uso para agregar 1 semana a la operacion de una forma mas pragmatica, e igualmente se pueden sumar otro datos que recibe como parametro
# lo recomendable es definir los parametros nombrados
fecha1 = datetime(2023,1,1) + timedelta(weeks=1)
fecha2 = datetime(2023,2,1)

# restamos las fechas y tomamos la diferencia de tiempo
delta = fecha2 - fecha1
print(delta)
print("dias", delta.days)
print("segundos", delta.seconds)
print("microsegundos", delta.microseconds)
print("total_seconds()", delta.total_seconds())




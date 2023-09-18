import csv
import os

# escribir
# with open("09-archivos/archivo.csv", "w") as archivo: #"w" es write
#     writer = csv.writer(archivo)
#     writer.writerow(["twit_id", "user_id", "text"])
#     writer.writerow([100, 1, "mensaje 1"])
#     writer.writerow([101, 2, "mensaje 2"])


# leer
# with open("09-archivos/archivo.csv") as archivo:
#     reader = csv.reader(archivo)
#     print(list(reader))
#     archivo.seek(0)
#     for linea in reader:
#         print(linea)

# help(open)

# leer y escribir "actualizar"
with open("09-archivos/archivo.csv") as r, open("09-archivos/archivo_temp.csv", "w+") as w:
    reader = csv.reader(r)
    writer = csv.writer(w)
    
    for row in reader:
        if len(row) > 0:
            if row[0] == "100":
                writer.writerow([100, 1, "texto modificado"])
                print('entro')
            else:
                writer.writerow(row)
    
# os.remove('09-archivos/archivo.csv')
# os.rename('09-archivos/archivo_temp.csv', '09-archivos/archivo.csv')


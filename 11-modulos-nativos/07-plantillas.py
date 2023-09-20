# https://myaccount.google.com/u/1/lesssecureapps
# en esta url hay que desabilitar la opcion

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email.mime.image import MIMEImage
from pathlib import Path # para capturar las rutas
from string import Template # crea la plantilla string 


# plantilla = """
#     <b>Hola mundo! $usuario</b>
# """

plantilla = Path("11-modulos-nativos/plantilla.html").read_text("utf-8") # indicmos el archivo html
template = Template(plantilla) # lo conviere en plantilla

# cambiamos las variables que definimos
# body_template = template.substitute(usuario="Chanchito feliz")
body_template = template.substitute({ "usuario": "Chanchito feliz"}) #si se tiene el diccionario aparte solo se le entrega y listo

path = Path("11-modulos-nativos/Strategy.png") # agregamos la imagen
mime_image = MIMEImage(path.read_bytes()) # configuramos imagen para email
mensaje = MIMEMultipart() # instancia de mensaje
mensaje["from"] = "santiscano@gmail.com"
mensaje["to"] = "stefacs14@gmail.com"
mensaje["subject"] = "este es el asunto del mensaje"
body = MIMEText(body_template, "html")
mensaje.attach(body) # anexamos el texto
mensaje.attach(mime_image) # anexmos imagenes

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smpt:
    smpt.ehlo() # esto nos permite identificarnos con el servidor smtp e identificar el nombre del dominio
    smpt.starttls() # transport layer security "tls"

    smpt.login("santiscano@gmail.com", "123") # usuario y contraseña
    smpt.send_message(mensaje) # enviamos mensaje
    print("mensaje enviado") # confirmamos que salio exitoso



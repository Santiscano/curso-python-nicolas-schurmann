# https://myaccount.google.com/u/1/lesssecureapps
# en esta url hay que desabilitar la opcion

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email.mime.image import MIMEImage
from pathlib import Path


path = Path("11-modulos-nativos/Strategy.png")
mime_image = MIMEImage(path.read_bytes())
mensaje = MIMEMultipart()
mensaje["from"] = "santiscano@gmail.com"
mensaje["to"] = "stefacs14@gmail.com"
mensaje["subject"] = "este es el asunto del mensaje"
body = MIMEText("cuerpo del mensaje", "html")
mensaje.attach(body)
mensaje.attach(mime_image)

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smpt:
    smpt.ehlo() # esto nos permite identificarnos con el servidor smtp e identificar el nombre del dominio
    smpt.starttls() # transport layer security

    smpt.login("santiscano@gmail.com", "123")
    smpt.send_message(mensaje)
    print("mensaje enviado")



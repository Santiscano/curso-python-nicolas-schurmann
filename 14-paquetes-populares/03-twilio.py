import os
from twilio.rest import Client # importacion para conectar con el cliente

sid = os.environ.get("TWILIO_SID")
token = os.environ.get("TWILIO_TOKEN")
numero = os.environ.get("TWILIO_N")

cliente = Client(sid, token)
mensaje = cliente.messages.create(
    body="Hola mundo!", #cuerpo
    from_= numero, #mi numero de donde enviare el mensaje
    to="+1" # destino
)


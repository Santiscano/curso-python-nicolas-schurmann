import os
from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient

email = os.environ.get("SENDGRID_EMAIL")

mensaje = Mail(
    from_email=email,
    to_emails=email,
    subject="correo de prueba",
    html_content="curso de  <b>Ultimate python</b>"
)

try:
    apikey = os.environ.get("SENDGRID_API_KEY") #api key
    sg = SendGridAPIClient(apikey) # crea el servidor y conecta
    response = sg.send(mensaje)
    print(
        response.status_code,
        response.body,
        response.headers,
    )
except Exception as e:
    print(e)
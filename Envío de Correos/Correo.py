#Martin Gabriel 
#Mejia Hurtado
#2086046

#Librerias
import smtplib, ssl
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

#Correos y contraseña
correo = input("Inserte su correo: ")
destinatario = input("Inserte destinatario: ")
password = input("Inserte contraseña: ")

mensaje = MIMEMultipart("alternative")
mensaje["Subject"] = "Prueba de envio (script Python) - 2086046"
mensaje["From"] = correo
mensaje["To"] = destinatario

#html del mensaje
html = """\
<html>
  <body>
        <p><h1>Practica 12 </h1><br>
        Ejercicio de la practica 12 para envios de correos.<br>
       <b>Alumno:</b> Martin Gabriel Mejia Hurtado. <br>
       <b>Matricula:</b> 2086046
    </p>
  </body>
</html>
"""
part1 = MIMEText(html, "html")
mensaje.attach(part1)

#IMAGEN
archivo = "fcfm.png"
with open(archivo, "rb") as adjunto:
    contenido_adjunto = MIMEBase("applicatioin", "octet-stream")
    contenido_adjunto.set_payload(adjunto.read())

encoders.encode_base64(contenido_adjunto)

contenido_adjunto.add_header( 
  "Content-Disposition",
  f"attachment; filename= {archivo}",
  )

mensaje.attach(contenido_adjunto)

#Login y envíar el email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login('<correo>', 'coxb cmco bczf vsro')
    server.sendmail(
        correo, destinatario, mensaje.as_string()
    )

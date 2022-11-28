import requests # Para hacer un request a un sitio
import base64 # Para Encode/decode en base 64
from requests import Response
#
# 02/27/22 - Martin Gabriel Mejia Hurtado
# Script encode_imgur.py 
#
## Para descargar la imagen del sitio
#
if __name__ == '__main__':
    url = 'https://i.imgur.com/XC5djWQ.jpeg'

    Response: Response = requests.get(url, stream=True)
    with open('cat.jpg','wb') as file_down:
        for chunk in Response.iter_content(): # Descargando contenido
            file_down.write(chunk)
    Response.close()
#
## Para codificar la imagen
#
with open('cat.jpg','rb') as bynary_file:
    bynary_file_data = bynary_file.read()
    base64_encoded_data =  base64.b64encode(bynary_file_data)
    base64_message = base64_encoded_data.decode('utf-8')
    
    print(base64_message)

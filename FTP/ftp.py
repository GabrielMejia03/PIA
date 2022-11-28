# Script para transferencia FTP
# Objetivo: Conectarse a servidor ftp y hacer un upload de un archivo
# 24/10/22
#
#Importando modulo ftp
from ftplib import FTP

#Estableciendo conexion a servidor
ftp = FTP(<ip>)

# Iniciar sesion
ftp.login('johnny','2086046')

# Cambiar directorio
ftp.cwd('upload')

# Listar directorio
ftp.retrlines('LIST')

#Cargar el archivo ADVERTENCIA.txt y subirlo
ftp.storlines('STOR ADVERTENCIA.txt', open('ADVERTENCIA.txt', 'rb'))

# Salida
ftp.quit()

# 02/10/22 - Martin Gabriel Mejia Hurtado
# Script codipo.ps1
Clear-Host
Write-Host "Bienvenido a un ejemplo de codificacion / decodificacion base64 usando powershell"-ForegroundColor Green
Write-Host "Codificando un archivo de texto"
#
# Se va a leer el contenido del archivo de texto
#
$inputfile = "C:\Users\marti\Desktop\Script\secret.txt"
$fc = Get-Content $inputfile
$GB = [System.Text.Encoding]::UTF8.GetBytes($fc)
$etext = [System.convert]::ToBase64String($GB)
Write-Host "El contenido del archivo CODIFICADO es:" $etext -ForegroundColor Green
#
# Decodificando contento de un archivo
#
Write-Host "DECODIFICANDO el texto previo:"
[System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String($etext)) | Out-File -Encoding "ASCII" C:\Users\marti\Desktop\Script\secret.txt
$outfile12 = Get-Content C:\Users\marti\Desktop\Script\secret.txt
Write-Host "El texto decodificado es el siguiente:" -ForegroundColor Green
Write-Host "DECODIFICADO:" $outfile12

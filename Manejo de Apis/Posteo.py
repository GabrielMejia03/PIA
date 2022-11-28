import requests
import json
# Nombre: Martin Gabriel Mejia Hurtado
# Matricula: 2086046
if __name__ == '__main__':
	url = "http://httpbin.org/post"
	argumentos = {'nombre':'Gabriel','Matricula':'2086046', 'Curso':'Laboratorio de Programacion para Ciberseguridad'}
	
	response = requests.post(url, params=argumentos)

	if response.status_code == 200:
		print(response.content)

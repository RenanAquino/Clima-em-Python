import requests
import json

#Buscar informações
cidade = str(input('Qual a cidade? ')).title()
key = "a830c08c52313dc49d1efa86f97940ff"
lingua = "pt_br"
api = requests.get("https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&lang={}&units=metric".format(cidade, key, lingua))
api = api.json()
#Selecionando informações
cidade = api['name']
pais = api['sys']['country']
temp = api['main']['temp']
temp_men = api['main']['temp_min']
temp_mai = api['main']['temp_max']
desc = api['weather'][0]['description']
umidade = api['main']['humidity']
vel_vento = api['wind']['speed']
#Apresentação
print("="*72)
print(f'Cidade: {cidade}')
print(f'País: {pais}')
print(f'Descrição: {desc}')
print(f'Umidade do ar: {umidade}%')
print(f'Temperatura: {temp:.2f}º')
print(f'Temperatura miníma: {temp_men:.2f}º')
print(f'Temperatura máxima: {temp_mai:.2f}º')
print(f'Velocidade do vento: {vel_vento}')
print("="*72)
#print(api)

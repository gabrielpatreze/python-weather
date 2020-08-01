import requests
import json

cidade = input('Escreva a cidade: ')

requisicao = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + cidade + ',&appid=hereyourappid')
#adicionar o input da cidade espaço + cidade + espaço ',

tempo = json.loads(requisicao.text)
#transformou json em python dicionario

#print(tempo) geral

print('O tempo em', cidade, 'está', tempo['weather'][0]['main'])
#é uma lista com [{ colchete e chave então coloca [0]
print('Temperatura máxima em', cidade, 'é', round(float(tempo['main']['temp_max']) -273.15, 2),'graus celsius')
print('Temperatura mínima em', cidade, 'é', round(float(tempo['main']['temp_min']) -273.15, 2),'graus celsius')
print('Temperatura agora em', cidade, 'é', round(float(tempo['main']['temp'])  -273.15, 2),'graus celsius')
#o tempo esta em kelvin, passar para celsius: float -273.15
#print('Temperatura agora em', cidade, 'é', float(tempo['main']['temp'])  -273.15,'graus celsius')
#modelo sem o round



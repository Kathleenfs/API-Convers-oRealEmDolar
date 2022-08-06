import requests as requests


url = 'https://api.exchangerate-api.com/v6/latest'

req = requests.get(url)

print(req.status_code)

dados = req.json()

valor_reais = float(input('Informe o valor em R$ a ser convertido\n'))
cotacao = dados['rates']['BRL']
print(f'R${valor_reais} em dolar valem US$ {(valor_reais/cotacao)}')
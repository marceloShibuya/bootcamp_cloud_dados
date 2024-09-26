from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from dotenv import load_dotenv
import json
import os
from pprint import pprint

load_dotenv()

url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'

session = Session()

# Parâmetros da requisição para obter a cotação do Bitcoin
parameters = {
    'symbol': 'BTC',  # Identificando o Bitcoin pelo símbolo
    'convert': 'BRL'  # Convertendo a cotação para BRL
}

# Headers com a chave da API obtida do arquivo .env
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': os.getenv('CMC_API_KEY'),  # Obtendo a chave do .env
}


# Criar uma sessão
session = Session()
session.headers.update(headers)


response = session.get(url=url, params=parameters)

data = json.loads(response.text)

#print(type(data)) # verifica o tipo do dado (no caso é um Dicionário)
# pprint(data) # print de forma identada o dicionário

bitcoin_data = data["data"]["BTC"][0]["quote"]["BRL"]

print(f"Útima cotação do Bitcoin: $ {bitcoin_data["price"]:.2f} BRL")
print(f"Volume 24h: $ {bitcoin_data["volume_24h"]:.2f} BRL")
print(f"Market Cap: $ {bitcoin_data["market_cap"]:.2f} BRL")
print(f"Última atualização: $ {bitcoin_data["last_updated"]}")


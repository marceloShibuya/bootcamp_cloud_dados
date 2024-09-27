from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from dotenv import load_dotenv
import json
import os
from pprint import pprint
import schedule
import time
import csv
import psycopg2
from psycopg2 import sql

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

def consultar_cotacao_bitcoin():
    try:
        response = session.get(url=url, params=parameters)
        data = json.loads(response.text)
        
        #print(type(data)) # verifica o tipo do dado (no caso é um Dicionário)
        # pprint(data) # print de forma identada o dicionário

        if "data" in data and "BTC" in data["data"]:
            bitcoin_data = data["data"]["BTC"]
            brl_quote = bitcoin_data[0]["quote"]["BRL"]

            print(f"Útima cotação do Bitcoin: $ {brl_quote["price"]:.2f} BRL")
            print(f"Volume 24h: $ {brl_quote["volume_24h"]:.2f} BRL")
            print(f"Market Cap: $ {brl_quote["market_cap"]:.2f} BRL")
            print(f"Última atualização: $ {brl_quote["last_updated"]}")
        else:
            print("Erro ao obter a cotação do Bitcoin:", data["status"].get("error_message", "Erro desconhecido"))

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(f"Erro na requisição> {e} ")


# Agendar a função para rodar a cada 15 segundos
schedule.every(15).seconds.do(consultar_cotacao_bitcoin)

# Loop principal para manter o agendamento ativo
if __name__ == "__main__":
    print("Iniciando o agendamento para consultar a API a cada 15 segundos...")
    while True:
        schedule.run_pending()
        time.sleep(1)

import requests
from bs4 import BeautifulSoup

def get_rate(args):
    desired_currencies = {i.upper(): None for i in args}

    url = r'https://myfin.by/crypto-rates'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    currencies_names = soup.find_all('tr', {'class': ['even', 'odd']})
    for currency_line in currencies_names:
        current_name = currency_line.find('div', class_='crypto_iname hidden-xs')
        text_current_name = current_name.text 
        if text_current_name in desired_currencies:
            price = currency_line.find_all('td', class_=None)[1]

            text_price = price.text
            text_price_splitted = text_price.split()
            text_price = f'{text_price_splitted[0]} ({text_price_splitted[1]})'

            desired_currencies[text_current_name] = text_price  # type: ignore
    
    return desired_currencies

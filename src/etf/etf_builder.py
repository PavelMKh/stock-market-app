from bs4 import BeautifulSoup
from etf_dto import EtfDto
from etf_client import load_page
from datetime import datetime


def load_etf(etf_ticker):
    html = load_page(input('Enter URL'))
    etf_structure = []
    soup = BeautifulSoup(html, 'html.parser')
    lines = soup.find('div', class_='bootstrap-table').find_all('td')
    i = 0
    data = []
    for line in lines:
        if i > 2:
            i = 0
            etf_key = f'{etf_ticker}{datetime.now().date()}{data[0]}'
            etf_structure.append(EtfDto(etf_ticker, datetime.now().date(), data[0], data[1], float(data[2][:-1])))
            data.clear()
        data.append(line.text.strip())
        i += 1
    return etf_structure

import requests


def get_daily_candles(ticker, api_key):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&outputsize=full&apikey={api_key}'
    r = requests.get(url)
    data = r.json()
    return data


def get_company_overview(ticker, api_key):
    url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={ticker}&apikey={api_key}'
    r = requests.get(url)
    data = r.json()
    return data


def get_income_statement(ticker, apikey):
    url = f'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={ticker}&apikey={apikey}'
    r = requests.get(url)
    data = r.json()
    return data


def get_balance_sheet(ticker, apikey):
    url = f'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={ticker}&apikey={apikey}'
    r = requests.get(url)
    data = r.json()
    return data


def get_cash_flow(ticker, apikey):
    url = f'https://www.alphavantage.co/query?function=CASH_FLOW&symbol={ticker}&apikey={apikey}'
    r = requests.get(url)
    data = r.json()
    return data

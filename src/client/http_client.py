import requests


def get_candles(ticker, api_key, candle_size, date_candles):
    if candle_size == 24:
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&outputsize=full&apikey={api_key}'
    else:
        month = date_candles.strftime("%Y-%m")
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval={candle_size}min&month={month}&outputsize=full&apikey={api_key}'
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

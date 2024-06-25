from data.repository import candles_save
from client.http_client import get_daily_candles
from model.candle_builder import candles_processing
from data.repository import create_db


def load_candles(tickers, api_key, candle_size, path):
    for ticker in tickers:
        data = get_daily_candles(ticker, api_key)
        print(data)
        candles = candles_processing(data, ticker, candle_size)
        candles_save(candles, path)


def create_db_service(path):
    create_db(path)

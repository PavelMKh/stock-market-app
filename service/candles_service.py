from data.repository import candles_save
from client.http_client import get_daily_candles
from model.candle_builder import candles_processing


def load_candles(ticker, api_key, candle_size, path):
    data = get_daily_candles(ticker, api_key)
    candles = candles_processing(data, ticker, candle_size)
    candles_save(candles, path)


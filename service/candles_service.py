from datetime import datetime

from data.repository import candles_save
from client.http_client import get_candles
from model.candle_builder import candles_processing


def load_candles(ticker, api_key, candle_size, start, end, path):
    candles_output = []
    if candle_size == 24:
        data = get_candles(ticker, api_key, candle_size, 0)
        candles = candles_processing(data, ticker, candle_size)
        candles_save(candles, path)
        candles_output.extend(candles)
    else:
        end_date = datetime.strptime(end, '%Y-%m').date()
        start_date = datetime.strptime(start, '%Y-%m').date()
        diff_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
        if diff_months > 24:
            raise ValueError("The difference between start and end should not exceed 24 months.")
        while start_date <= end_date:
            current_month = start_date
            data = get_candles(ticker, api_key, candle_size, current_month)
            candles = candles_processing(data, ticker, candle_size)
            candles_save(candles, path)
            candles_output.extend(candles)
            if start_date.month == 12:
                start_date = start_date.replace(year=start_date.year + 1, month=1)
            else:
                start_date = start_date.replace(month=start_date.month + 1)
    return candles_output

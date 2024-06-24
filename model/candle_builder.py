import datetime
from model.candle import Candle


def candles_processing(data, ticker, candle_size):
    candle_keys = [key for key in data['Time Series (Daily)']]
    candles = []
    source = 'global'
    for key in candle_keys:
        id = str(key) + str(ticker) + str(candle_size)
        candle = Candle(id,
                        datetime.datetime.strptime(key, '%Y-%m-%d'),
                        ticker,
                        candle_size,
                        source,
                        float(data['Time Series (Daily)'][key]['1. open']),
                        float(data['Time Series (Daily)'][key]['2. high']),
                        float(data['Time Series (Daily)'][key]['3. low']),
                        float(data['Time Series (Daily)'][key]['4. close']),
                        int(data['Time Series (Daily)'][key]['5. volume']))
        candles.append(candle)
    return candles

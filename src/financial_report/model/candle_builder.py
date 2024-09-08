import datetime
from model.candle import Candle


def candles_processing(data, ticker, candle_size):
    if candle_size == 24:
        time_series_key = 'Time Series (Daily)'
    else:
        time_series_key = f'Time Series ({candle_size}min)'
    candle_keys = [key for key in data[time_series_key]]
    candles = []
    source = 'global'
    for key in candle_keys:
        id = str(key) + str(ticker) + str(candle_size)
        if candle_size == 24:
            dtm = datetime.datetime.strptime(key, '%Y-%m-%d')
        else:
            dtm = datetime.datetime.strptime(key, '%Y-%m-%d %H:%M:%S')
        candle = Candle(id,
                        dtm,
                        ticker,
                        candle_size,
                        source,
                        float(data[time_series_key][key]['1. open']),
                        float(data[time_series_key][key]['2. high']),
                        float(data[time_series_key][key]['3. low']),
                        float(data[time_series_key][key]['4. close']),
                        int(data[time_series_key][key]['5. volume']))
        candles.append(candle)
    return candles

import datetime


class Candle:
    @property
    def id(self):
        pass

    @property
    def date_time(self):
        pass

    @property
    def ticker(self):
        pass

    @property
    def size(self):
        pass

    @property
    def source(self):
        pass

    @property
    def open(self):
        pass

    @property
    def max(self):
        pass

    @property
    def min(self):
        pass

    @property
    def close(self):
        pass

    @property
    def volume(self):
        pass

    def __init__(self, id: str, date_time: datetime.datetime, ticker: str, size: int,
                 source: str, open: float, max: float, min: float, close: float,
                 volume: int):
        self._id = id
        self._date_time = date_time
        self._ticker = ticker
        self._size = size
        self._source = source
        self._open = open
        self._max = max
        self._min = min
        self._close = close
        self._volume = volume

    def __str__(self) -> str:
        return (f"datetime: {self._date_time}, open: {self._open}, "
                f"high: {self._max}, low: {self._min}, close: {self._close}, volume: {self._volume}")

    def __repr__(self) -> str:
        return (f"datetime: {self._date_time}, open: {self._open}, high: {self._max}, "
                f"low: {self._min}, close: {self._close}, volume: {self._volume}")

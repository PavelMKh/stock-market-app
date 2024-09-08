from dataclasses import dataclass
from datetime import date

@dataclass
class EtfDto:
    etf_ticker: str
    report_date: date
    company_ticker: str
    company_name: str
    share: float

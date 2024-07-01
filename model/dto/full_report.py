from dataclasses import dataclass

from model.company import Company


@dataclass
class FullReport:
    candles: list
    company: Company
    pnl: list
    bs: list
    cf: list

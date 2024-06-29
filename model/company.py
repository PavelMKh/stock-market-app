from dataclasses import dataclass


@dataclass
class Company:
    symbol: str
    asset_type: str
    name: str
    description: str
    cik: int
    exchange: str
    currency: str
    country: str
    sector: str
    industry: str
    address: str
    fiscal_year_end: str

    @staticmethod
    def create_company_overview(json):
        company = Company(
            json["Symbol"],
            json["AssetType"],
            json["Name"],
            json["Description"],
            json["CIK"],
            json["Exchange"],
            json["Currency"],
            json["Country"],
            json["Sector"],
            json["Industry"],
            json["Address"],
            json["FiscalYearEnd"]
        )
        return company

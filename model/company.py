from dataclasses import dataclass


@dataclass
class Company:
    def __init__(self, symbol, asset_type, name, description, cik, exchange, currency, country, sector, industry,
                 address, fiscal_year_end):
        self.symbol = symbol
        self.asset_type = asset_type
        self.name = name
        self.description = description
        self.cik = cik
        self.exchange = exchange
        self.currency = currency
        self.country = country
        self.sector = sector
        self.industry = industry
        self.address = address
        self.fiscal_year_end = fiscal_year_end

    @classmethod
    def create_company_overview(json_data):
        company = Company(
            json_data["Symbol"],
            json_data["AssetType"],
            json_data["Name"],
            json_data["Description"],
            json_data["CIK"],
            json_data["Exchange"],
            json_data["Currency"],
            json_data["Country"],
            json_data["Sector"],
            json_data["Industry"],
            json_data["Address"],
            json_data["FiscalYearEnd"]
        )
        return company
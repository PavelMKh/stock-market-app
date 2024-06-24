class Company:
    def __init__(self, symbol, asset_type, name, description, cik, exchange, currency, country, sector, industry, address, fiscal_year_end):
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

    def __str__(self):
        return f"""
                    Company Name: {self.name}
                    Symbol: {self.symbol}
                    Asset Type: {self.asset_type}
                    Description: {self.description}
                    CIK: {self.cik}
                    Exchange: {self.exchange}
                    Currency: {self.currency}
                    Country: {self.country}
                    Sector: {self.sector}
                    Industry: {self.industry}
                    Address: {self.address}
                    Fiscal Year End: {self.fiscal_year_end}
                """

    def __repr__(self):
        return f"Company(symbol='{self.symbol}', asset_type='{self.asset_type}', name='{self.name}', description='{self.description}', cik={self.cik}, exchange='{self.exchange}', currency='{self.currency}', country='{self.country}', sector='{self.sector}', industry='{self.industry}', address='{self.address}', fiscal_year_end='{self.fiscal_year_end}')"
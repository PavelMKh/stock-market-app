from model.company import Company


def company_processing(json_data):
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
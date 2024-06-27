from data.repository import company_save
from client.http_client import get_company_overview
from model.company import Company


def load_company(ticker, apikey, path):
    company_json = get_company_overview(ticker, apikey)
    company = Company.create_company_overview(company_json)
    company_save(company, path)
    return company

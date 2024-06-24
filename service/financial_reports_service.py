from model.company_builder import company_processing
from data.repository import company_save
from client.http_client import get_company_overview


def load_company(ticker, apikey, path):
    company_json = get_company_overview(ticker, apikey)
    company = company_processing(company_json)
    company_save(company, path)
    return company

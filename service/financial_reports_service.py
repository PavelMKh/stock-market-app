from data.repository import company_save, save_income_statement
from client.http_client import get_company_overview, get_income_statement
from model.company import Company
from model.income_statement import IncomeStatement


def load_company(ticker, apikey, path):
    company_json = get_company_overview(ticker, apikey)
    company = Company.create_company_overview(company_json)
    company_save(company, path)
    return company


def load_pnl(ticker, apikey, path):
    pnl_json = get_income_statement(ticker, apikey)
    pnl = IncomeStatement.create_pnl(pnl_json)
    save_income_statement(pnl, path)
    return pnl

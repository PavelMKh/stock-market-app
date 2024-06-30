from data.repository import company_save, save_income_statement, save_balance_sheet
from client.http_client import get_company_overview, get_income_statement, get_balance_sheet
from model.balance_sheet import BalanceSheet
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


def load_bs(ticker, apikey, path):
    bs_json = get_balance_sheet(ticker, apikey)
    bs = BalanceSheet.create_from_json(bs_json)
    save_balance_sheet(bs, path)
    return bs

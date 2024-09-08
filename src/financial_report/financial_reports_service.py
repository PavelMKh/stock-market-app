from data.repository import company_save, save_income_statement, save_balance_sheet, save_cash_flow
from client.http_client import get_company_overview, get_income_statement, get_balance_sheet, get_cash_flow
from model.balance_sheet import BalanceSheet
from model.cash_flow import CashFlow
from model.company import Company
from model.dto.full_report import FullReport
from model.income_statement import IncomeStatement
from service.candles_service import load_candles


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


def load_cf(ticker, apikey, path):
    cf_json = get_cash_flow(ticker, apikey)
    cf = CashFlow.create_from_json(cf_json)
    save_cash_flow(cf, path)
    return cf


def load_full_data(tickers, apikey, path):
    full_data = []
    for ticker in tickers:
        company = load_company(ticker, apikey, path)
        pnl = load_pnl(ticker, apikey, path)
        bs = load_bs(ticker, apikey, path)
        cf = load_cf(ticker, apikey, path)
        candles = load_candles(ticker, apikey, 24, 0, 0, path)
        full_data.append(FullReport(candles, company, pnl, bs, cf))
    return full_data

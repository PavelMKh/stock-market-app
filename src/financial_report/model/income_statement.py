from dataclasses import dataclass
from datetime import date


@dataclass
class IncomeStatement:
    id: str
    ticker: str
    type: str
    fiscalDateEnding: date
    reportedCurrency: str
    grossProfit: float = None
    totalRevenue: float = None
    costOfRevenue: float = None
    costofGoodsAndServicesSold: float = None
    operatingIncome: float = None
    sellingGeneralAndAdministrative: float = None
    researchAndDevelopment: float = None
    operatingExpenses: float = None
    investmentIncomeNet: float = None
    netInterestIncome: float = None
    interestIncome: float = None
    interestExpense: float = None
    nonInterestIncome: float = None
    otherNonOperatingIncome: float = None
    depreciation: float = None
    depreciationAndAmortization: float = None
    incomeBeforeTax: float = None
    incomeTaxExpense: float = None
    interestAndDebtExpense: float = None
    netIncomeFromContinuingOperations: float = None
    comprehensiveIncomeNetOfTax: float = None
    ebit: float = None
    ebitda: float = None
    netIncome: float = None

    @staticmethod
    def create_pnl(json_data):
        reports = []
        for report_type, reports_data in [("annual", json_data["annualReports"]),
                                          ("quarterly", json_data["quarterlyReports"])]:
            for report_data in reports_data:
                report = IncomeStatement(
                    id=json_data["symbol"] + report_data["fiscalDateEnding"] + report_type,
                    ticker=json_data["symbol"],
                    type=report_type,
                    fiscalDateEnding=date.fromisoformat(report_data["fiscalDateEnding"]),
                    reportedCurrency=report_data["reportedCurrency"],
                    grossProfit=float(report_data["grossProfit"]) if report_data["grossProfit"] != "None" else None,
                    totalRevenue=float(report_data["totalRevenue"]) if report_data["totalRevenue"] != "None" else None,
                    costOfRevenue=float(report_data["costOfRevenue"]) if report_data[
                                                                             "costOfRevenue"] != "None" else None,
                    costofGoodsAndServicesSold=float(report_data["costofGoodsAndServicesSold"]) if report_data[
                                                                                                       "costofGoodsAndServicesSold"] != "None" else None,
                    operatingIncome=float(report_data["operatingIncome"]) if report_data[
                                                                                 "operatingIncome"] != "None" else None,
                    sellingGeneralAndAdministrative=float(report_data["sellingGeneralAndAdministrative"]) if
                    report_data["sellingGeneralAndAdministrative"] != "None" else None,
                    researchAndDevelopment=float(report_data["researchAndDevelopment"]) if report_data[
                                                                                               "researchAndDevelopment"] != "None" else None,
                    operatingExpenses=float(report_data["operatingExpenses"]) if report_data[
                                                                                     "operatingExpenses"] != "None" else None,
                    investmentIncomeNet=float(report_data["investmentIncomeNet"]) if report_data[
                                                                                         "investmentIncomeNet"] != "None" else None,
                    netInterestIncome=float(report_data["netInterestIncome"]) if report_data[
                                                                                     "netInterestIncome"] != "None" else None,
                    interestIncome=float(report_data["interestIncome"]) if report_data[
                                                                               "interestIncome"] != "None" else None,
                    interestExpense=float(report_data["interestExpense"]) if report_data[
                                                                                 "interestExpense"] != "None" else None,
                    nonInterestIncome=float(report_data["nonInterestIncome"]) if report_data[
                                                                                     "nonInterestIncome"] != "None" else None,
                    otherNonOperatingIncome=float(report_data["otherNonOperatingIncome"]) if report_data[
                                                                                                 "otherNonOperatingIncome"] != "None" else None,
                    depreciation=float(report_data["depreciation"]) if report_data["depreciation"] != "None" else None,
                    depreciationAndAmortization=float(report_data["depreciationAndAmortization"]) if report_data[
                                                                                                         "depreciationAndAmortization"] != "None" else None,
                    incomeBeforeTax=float(report_data["incomeBeforeTax"]) if report_data[
                                                                                 "incomeBeforeTax"] != "None" else None,
                    incomeTaxExpense=float(report_data["incomeTaxExpense"]) if report_data[
                                                                                   "incomeTaxExpense"] != "None" else None,
                    interestAndDebtExpense=float(report_data["interestAndDebtExpense"]) if report_data[
                                                                                               "interestAndDebtExpense"] != "None" else None,
                    netIncomeFromContinuingOperations=float(report_data["netIncomeFromContinuingOperations"]) if
                    report_data["netIncomeFromContinuingOperations"] != "None" else None,
                    comprehensiveIncomeNetOfTax=float(report_data["comprehensiveIncomeNetOfTax"]) if report_data[
                                                                                                         "comprehensiveIncomeNetOfTax"] != "None" else None,
                    ebit=float(report_data["ebit"]) if report_data["ebit"] != "None" else None,
                    ebitda=float(report_data["ebitda"]) if report_data["ebitda"] != "None" else None,
                    netIncome=float(report_data["netIncome"]) if report_data["netIncome"] != "None" else None
                )
                reports.append(report)

        return reports
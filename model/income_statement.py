from dataclasses import dataclass
from datetime import date


@dataclass
class IncomeStatement:
    id: int
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

    @classmethod
    def from_json(cls, json_data: dict):
        reports = []
        for report_type, reports_data in [("annual", json_data["annualReports"]), ("quarterly", json_data["quarterlyReports"])]:
            for report in reports_data:
                report = cls(
                    id=len(reports) + 1,
                    ticker=json_data["symbol"],
                    type=report_type,
                    fiscalDateEnding=date.fromisoformat(report["fiscalDateEnding"]),
                    reportedCurrency=report["reportedCurrency"],
                    **report
                )
                reports.append(report)

        return reports
from dataclasses import dataclass
from datetime import date


@dataclass
class CashFlow:
    id: str
    ticker: str
    type: str
    fiscalDateEnding: date
    reportedCurrency: str
    operatingCashflow: float = None
    paymentsForOperatingActivities: float = None
    proceedsFromOperatingActivities: float = None
    changeInOperatingLiabilities: float = None
    changeInOperatingAssets: float = None
    depreciationDepletionAndAmortization: float = None
    capitalExpenditures: float = None
    changeInReceivables: float = None
    changeInInventory: float = None
    profitLoss: float = None
    cashflowFromInvestment: float = None
    cashflowFromFinancing: float = None
    proceedsFromRepaymentsOfShortTermDebt: float = None
    paymentsForRepurchaseOfCommonStock: float = None
    paymentsForRepurchaseOfEquity: float = None
    paymentsForRepurchaseOfPreferredStock: float = None
    dividendPayout: float = None
    dividendPayoutCommonStock: float = None
    dividendPayoutPreferredStock: float = None
    proceedsFromIssuanceOfCommonStock: float = None
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet: float = None
    proceedsFromIssuanceOfPreferredStock: float = None
    proceedsFromRepurchaseOfEquity: float = None
    proceedsFromSaleOfTreasuryStock: float = None
    changeInCashAndCashEquivalents: float = None
    changeInExchangeRate: float = None
    netIncome: float = None

    @staticmethod
    def create_from_json(json_data):
        reports = []
        for report_type, reports_data in [("annual", json_data["annualReports"]),
                                          ("quarterly", json_data["quarterlyReports"])]:
            for report_data in reports_data:
                report = CashFlow(
                    id=json_data["symbol"] + report_data["fiscalDateEnding"] + report_type,
                    ticker=json_data["symbol"],
                    type=report_type,
                    fiscalDateEnding=date.fromisoformat(report_data["fiscalDateEnding"]),
                    reportedCurrency=report_data["reportedCurrency"],
                    operatingCashflow=float(report_data["operatingCashflow"]) if report_data[
                                                                                     "operatingCashflow"] != "None" else None,
                    paymentsForOperatingActivities=float(report_data["paymentsForOperatingActivities"]) if report_data[
                                                                                                               "paymentsForOperatingActivities"] != "None" else None,
                    proceedsFromOperatingActivities=float(report_data["proceedsFromOperatingActivities"]) if
                    report_data["proceedsFromOperatingActivities"] != "None" else None,
                    changeInOperatingLiabilities=float(report_data["changeInOperatingLiabilities"]) if report_data[
                                                                                                           "changeInOperatingLiabilities"] != "None" else None,
                    changeInOperatingAssets=float(report_data["changeInOperatingAssets"]) if report_data[
                                                                                                 "changeInOperatingAssets"] != "None" else None,
                    depreciationDepletionAndAmortization=float(report_data["depreciationDepletionAndAmortization"]) if
                    report_data["depreciationDepletionAndAmortization"] != "None" else None,
                    capitalExpenditures=float(report_data["capitalExpenditures"]) if report_data[
                                                                                         "capitalExpenditures"] != "None" else None,
                    changeInReceivables=float(report_data["changeInReceivables"]) if report_data[
                                                                                         "changeInReceivables"] != "None" else None,
                    changeInInventory=float(report_data["changeInInventory"]) if report_data[
                                                                                     "changeInInventory"] != "None" else None,
                    profitLoss=float(report_data["profitLoss"]) if report_data["profitLoss"] != "None" else None,
                    cashflowFromInvestment=float(report_data["cashflowFromInvestment"]) if report_data[
                                                                                               "cashflowFromInvestment"] != "None" else None,
                    cashflowFromFinancing=float(report_data["cashflowFromFinancing"]) if report_data[
                                                                                             "cashflowFromFinancing"] != "None" else None,
                    proceedsFromRepaymentsOfShortTermDebt=float(report_data["proceedsFromRepaymentsOfShortTermDebt"]) if
                    report_data["proceedsFromRepaymentsOfShortTermDebt"] != "None" else None,
                    paymentsForRepurchaseOfCommonStock=float(report_data["paymentsForRepurchaseOfCommonStock"]) if
                    report_data["paymentsForRepurchaseOfCommonStock"] != "None" else None,
                    paymentsForRepurchaseOfEquity=float(report_data["paymentsForRepurchaseOfEquity"]) if report_data[
                                                                                                             "paymentsForRepurchaseOfEquity"] != "None" else None,
                    paymentsForRepurchaseOfPreferredStock=float(report_data["paymentsForRepurchaseOfPreferredStock"]) if
                    report_data["paymentsForRepurchaseOfPreferredStock"] != "None" else None,
                    dividendPayout=float(report_data["dividendPayout"]) if report_data[
                                                                               "dividendPayout"] != "None" else None,
                    dividendPayoutCommonStock=float(report_data["dividendPayoutCommonStock"]) if report_data[
                                                                                                     "dividendPayoutCommonStock"] != "None" else None,
                    dividendPayoutPreferredStock=float(report_data["dividendPayoutPreferredStock"]) if report_data[
                                                                                                           "dividendPayoutPreferredStock"] != "None" else None,
                    proceedsFromIssuanceOfCommonStock=float(report_data["proceedsFromIssuanceOfCommonStock"]) if
                    report_data["proceedsFromIssuanceOfCommonStock"] != "None" else None,
                    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet=float(
                        report_data["proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet"]) if report_data[
                                                                                                         "proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet"] != "None" else None,
                    proceedsFromIssuanceOfPreferredStock=float(report_data["proceedsFromIssuanceOfPreferredStock"]) if
                    report_data["proceedsFromIssuanceOfPreferredStock"] != "None" else None,
                    proceedsFromRepurchaseOfEquity=float(report_data["proceedsFromRepurchaseOfEquity"]) if report_data[
                                                                                                               "proceedsFromRepurchaseOfEquity"] != "None" else None,
                    proceedsFromSaleOfTreasuryStock=float(report_data["proceedsFromSaleOfTreasuryStock"]) if
                    report_data["proceedsFromSaleOfTreasuryStock"] != "None" else None,
                    changeInCashAndCashEquivalents=float(report_data["changeInCashAndCashEquivalents"]) if report_data[
                                                                                                               "changeInCashAndCashEquivalents"] != "None" else None,
                    changeInExchangeRate=float(report_data["changeInExchangeRate"]) if report_data[
                                                                                           "changeInExchangeRate"] != "None" else None,
                    netIncome=float(report_data["netIncome"]) if report_data["netIncome"] != "None" else None
                )
                reports.append(report)

        return reports

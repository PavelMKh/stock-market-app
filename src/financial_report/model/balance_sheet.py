from dataclasses import dataclass
from datetime import date


@dataclass
class BalanceSheet:
    id: str
    ticker: str
    type: str
    fiscalDateEnding: date
    reportedCurrency: str
    totalAssets: float = None
    totalCurrentAssets: float = None
    cashAndCashEquivalentsAtCarryingValue: float = None
    cashAndShortTermInvestments: float = None
    inventory: float = None
    currentNetReceivables: float = None
    totalNonCurrentAssets: float = None
    propertyPlantEquipment: float = None
    accumulatedDepreciationAmortizationPPE: float = None
    intangibleAssets: float = None
    intangibleAssetsExcludingGoodwill: float = None
    goodwill: float = None
    investments: float = None
    longTermInvestments: float = None
    shortTermInvestments: float = None
    otherCurrentAssets: float = None
    otherNonCurrentAssets: float = None
    totalLiabilities: float = None
    totalCurrentLiabilities: float = None
    currentAccountsPayable: float = None
    deferredRevenue: float = None
    currentDebt: float = None
    shortTermDebt: float = None
    totalNonCurrentLiabilities: float = None
    capitalLeaseObligations: float = None
    longTermDebt: float = None
    currentLongTermDebt: float = None
    longTermDebtNoncurrent: float = None
    shortLongTermDebtTotal: float = None
    otherCurrentLiabilities: float = None
    otherNonCurrentLiabilities: float = None
    totalShareholderEquity: float = None
    treasuryStock: float = None
    retainedEarnings: float = None
    commonStock: float = None
    commonStockSharesOutstanding: float = None

    @staticmethod
    def create_from_json(json_data):
        reports = []
        for report_type, reports_data in [("annual", json_data["annualReports"]),
                                          ("quarterly", json_data["quarterlyReports"])]:
            for report_data in reports_data:
                report = BalanceSheet(
                    id=json_data["symbol"] + report_data["fiscalDateEnding"] + report_type,
                    ticker=json_data["symbol"],
                    type=report_type,
                    fiscalDateEnding=date.fromisoformat(report_data["fiscalDateEnding"]),
                    reportedCurrency=report_data["reportedCurrency"],
                    totalAssets=float(report_data["totalAssets"]) if report_data["totalAssets"] != "None" else None,
                    totalCurrentAssets=float(report_data["totalCurrentAssets"]) if report_data[
                                                                                       "totalCurrentAssets"] != "None" else None,
                    cashAndCashEquivalentsAtCarryingValue=float(report_data["cashAndCashEquivalentsAtCarryingValue"]) if
                    report_data["cashAndCashEquivalentsAtCarryingValue"] != "None" else None,
                    cashAndShortTermInvestments=float(report_data["cashAndShortTermInvestments"]) if report_data[
                                                                                                         "cashAndShortTermInvestments"] != "None" else None,
                    inventory=float(report_data["inventory"]) if report_data["inventory"] != "None" else None,
                    currentNetReceivables=float(report_data["currentNetReceivables"]) if report_data[
                                                                                             "currentNetReceivables"] != "None" else None,
                    totalNonCurrentAssets=float(report_data["totalNonCurrentAssets"]) if report_data[
                                                                                             "totalNonCurrentAssets"] != "None" else None,
                    propertyPlantEquipment=float(report_data["propertyPlantEquipment"]) if report_data[
                                                                                               "propertyPlantEquipment"] != "None" else None,
                    accumulatedDepreciationAmortizationPPE=float(
                        report_data["accumulatedDepreciationAmortizationPPE"]) if
                    report_data["accumulatedDepreciationAmortizationPPE"] != "None" else None,
                    intangibleAssets=float(report_data["intangibleAssets"]) if report_data[
                                                                                   "intangibleAssets"] != "None" else None,
                    intangibleAssetsExcludingGoodwill=float(report_data["intangibleAssetsExcludingGoodwill"]) if
                    report_data["intangibleAssetsExcludingGoodwill"] != "None" else None,
                    goodwill=float(report_data["goodwill"]) if report_data["goodwill"] != "None" else None,
                    investments=float(report_data["investments"]) if report_data["investments"] != "None" else None,
                    longTermInvestments=float(report_data["longTermInvestments"]) if report_data[
                                                                                         "longTermInvestments"] != "None" else None,
                    shortTermInvestments=float(report_data["shortTermInvestments"]) if report_data[
                                                                                           "shortTermInvestments"] != "None" else None,
                    otherCurrentAssets=float(report_data["otherCurrentAssets"]) if report_data[
                                                                                       "otherCurrentAssets"] != "None" else None,
                    otherNonCurrentAssets=float(report_data["otherNonCurrentAssets"]) if report_data[
                                                                                             "otherNonCurrentAssets"] != "None" else None,
                    totalLiabilities=float(report_data["totalLiabilities"]) if report_data[
                                                                                   "totalLiabilities"] != "None" else None,
                    totalCurrentLiabilities=float(report_data["totalCurrentLiabilities"]) if report_data[
                                                                                                 "totalCurrentLiabilities"] != "None" else None,
                    currentAccountsPayable=float(report_data["currentAccountsPayable"]) if report_data[
                                                                                               "currentAccountsPayable"] != "None" else None,
                    deferredRevenue=float(report_data["deferredRevenue"]) if report_data[
                                                                                 "deferredRevenue"] != "None" else None,
                    currentDebt=float(report_data["currentDebt"]) if report_data["currentDebt"] != "None" else None,
                    shortTermDebt=float(report_data["shortTermDebt"]) if report_data[
                                                                             "shortTermDebt"] != "None" else None,
                    totalNonCurrentLiabilities=float(report_data["totalNonCurrentLiabilities"]) if report_data[
                                                                                                       "totalNonCurrentLiabilities"] != "None" else None,
                    capitalLeaseObligations=float(report_data["capitalLeaseObligations"]) if report_data[
                                                                                                 "capitalLeaseObligations"] != "None" else None,
                    longTermDebt=float(report_data["longTermDebt"]) if report_data["longTermDebt"] != "None" else None,
                    currentLongTermDebt=float(report_data["currentLongTermDebt"]) if report_data[
                                                                                         "currentLongTermDebt"] != "None" else None,
                    longTermDebtNoncurrent=float(report_data["longTermDebtNoncurrent"]) if report_data[
                                                                                               "longTermDebtNoncurrent"] != "None" else None,
                    shortLongTermDebtTotal=float(report_data["shortLongTermDebtTotal"]) if report_data[
                                                                                               "shortLongTermDebtTotal"] != "None" else None,
                    otherCurrentLiabilities=float(report_data["otherCurrentLiabilities"]) if report_data[
                                                                                                 "otherCurrentLiabilities"] != "None" else None,
                    otherNonCurrentLiabilities=float(report_data["otherNonCurrentLiabilities"]) if report_data[
                                                                                                       "otherNonCurrentLiabilities"] != "None" else None,
                    totalShareholderEquity=float(report_data["totalShareholderEquity"]) if report_data[
                                                                                               "totalShareholderEquity"] != "None" else None,
                    treasuryStock=float(report_data["treasuryStock"]) if report_data[
                                                                             "treasuryStock"] != "None" else None,
                    retainedEarnings=float(report_data["retainedEarnings"]) if report_data[
                                                                                   "retainedEarnings"] != "None" else None,
                    commonStock=float(report_data["commonStock"]) if report_data["commonStock"] != "None" else None,
                    commonStockSharesOutstanding=float(report_data["commonStockSharesOutstanding"]) if report_data[
                                                                                                           "commonStockSharesOutstanding"] != "None" else None
                )
                reports.append(report)

        return reports

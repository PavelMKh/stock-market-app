CREATE TABLE IF NOT EXISTS company (
    Symbol VARCHAR(30) PRIMARY KEY NOT NULL,
    AssetType VARCHAR(50) NOT NULL,
    Name VARCHAR(50) NOT NULL,
    Description TEXT NOT NULL,
    CIK INT NOT NULL,
    Exchange VARCHAR(50) NOT NULL,
    Currency VARCHAR(10) NOT NULL,
    Country VARCHAR(50) NOT NULL,
    Sector VARCHAR(200) NOT NULL,
    Industry VARCHAR(200) NOT NULL,
    Address VARCHAR(200) NOT NULL,
    FiscalYearEnd VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS candles (
            id TEXT PRIMARY KEY,
            date_time DATETIME NOT NULL,
            ticker TEXT NOT NULL,
            size INTEGER NOT NULL,
            source TEXT NOT NULL,
            open REAL NOT NULL,
            max REAL NOT NULL,
            min REAL NOT NULL,
            close REAL NOT NULL,
            volume INTEGER NOT NULL
        )

CREATE TABLE IF NOT EXISTS pnl (
        id VARCHAR(30) PRIMARY KEY,
        ticker TEXT NOT NULL,
        type TEXT NOT NULL,
        fiscalDateEnding DATE NOT NULL,
        reportedCurrency TEXT NOT NULL,
        grossProfit REAL,
        totalRevenue REAL,
        costOfRevenue REAL,
        costofGoodsAndServicesSold REAL,
        operatingIncome REAL,
        sellingGeneralAndAdministrative REAL,
        researchAndDevelopment REAL,
        operatingExpenses REAL,
        investmentIncomeNet REAL,
        netInterestIncome REAL,
        interestIncome REAL,
        interestExpense REAL,
        nonInterestIncome REAL,
        otherNonOperatingIncome REAL,
        depreciation REAL,
        depreciationAndAmortization REAL,
        incomeBeforeTax REAL,
        incomeTaxExpense REAL,
        interestAndDebtExpense REAL,
        netIncomeFromContinuingOperations REAL,
        comprehensiveIncomeNetOfTax REAL,
        ebit REAL,
        ebitda REAL,
        netIncome REAL
    )

CREATE TABLE IF NOT EXISTS balance_sheet (
                    id VARCHAR(30) PRIMARY KEY,
                    ticker VARCHAR(30) NOT NULL,
                    type VARCHAR(30) NOT NULL,
                    fiscalDateEnding DATE NOT NULL,
                    reportedCurrency VARCHAR(30) NOT NULL,
                    totalAssets REAL,
                    totalCurrentAssets REAL,
                    cashAndCashEquivalentsAtCarryingValue REAL,
                    cashAndShortTermInvestments REAL,
                    inventory REAL,
                    currentNetReceivables REAL,
                    totalNonCurrentAssets REAL,
                    propertyPlantEquipment REAL,
                    accumulatedDepreciationAmortizationPPE REAL,
                    intangibleAssets REAL,
                    intangibleAssetsExcludingGoodwill REAL,
                    goodwill REAL,
                    investments REAL,
                    longTermInvestments REAL,
                    shortTermInvestments REAL,
                    otherCurrentAssets REAL,
                    otherNonCurrentAssets REAL,
                    totalLiabilities REAL,
                    totalCurrentLiabilities REAL,
                    currentAccountsPayable REAL,
                    deferredRevenue REAL,
                    currentDebt REAL,
                    shortTermDebt REAL,
                    totalNonCurrentLiabilities REAL,
                    capitalLeaseObligations REAL,
                    longTermDebt REAL,
                    currentLongTermDebt REAL,
                    longTermDebtNoncurrent REAL,
                    shortLongTermDebtTotal REAL,
                    otherCurrentLiabilities REAL,
                    otherNonCurrentLiabilities REAL,
                    totalShareholderEquity REAL,
                    treasuryStock REAL,
                    retainedEarnings REAL,
                    commonStock REAL,
                    commonStockSharesOutstanding REAL
                    );

CREATE TABLE IF NOT EXISTS cash_flow (
                    id VARCHAR(255) PRIMARY KEY,
                    ticker VARCHAR(30) NOT NULL,
                    type VARCHAR(30) NOT NULL,
                    fiscalDateEnding DATE NOT NULL,
                    reportedCurrency VARCHAR(30) NOT NULL,
                    operatingCashflow REAL,
                    paymentsForOperatingActivities REAL,
                    proceedsFromOperatingActivities REAL,
                    changeInOperatingLiabilities REAL,
                    changeInOperatingAssets REAL,
                    depreciationDepletionAndAmortization REAL,
                    capitalExpenditures REAL,
                    changeInReceivables REAL,
                    changeInInventory REAL,
                    profitLoss REAL,
                    cashflowFromInvestment REAL,
                    cashflowFromFinancing REAL,
                    proceedsFromRepaymentsOfShortTermDebt REAL,
                    paymentsForRepurchaseOfCommonStock REAL,
                    paymentsForRepurchaseOfEquity REAL,
                    paymentsForRepurchaseOfPreferredStock REAL,
                    dividendPayout REAL,
                    dividendPayoutCommonStock REAL,
                    dividendPayoutPreferredStock REAL,
                    proceedsFromIssuanceOfCommonStock REAL,
                    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet REAL,
                    proceedsFromIssuanceOfPreferredStock REAL,
                    proceedsFromRepurchaseOfEquity REAL,
                    proceedsFromSaleOfTreasuryStock REAL,
                    changeInCashAndCashEquivalents REAL,
                    changeInExchangeRate REAL,
                    netIncome REAL);

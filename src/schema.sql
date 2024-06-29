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

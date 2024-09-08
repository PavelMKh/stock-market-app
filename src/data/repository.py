import sqlite3
from dataclasses import asdict


def candles_save(candles, path):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    candles_to_insert = [(candle._id, candle._date_time, candle._ticker,
                          candle._size, candle._source, candle._open,
                          candle._max, candle._min, candle._close, candle._volume) for candle in candles]
    try:
        cursor.executemany('''
      INSERT OR IGNORE INTO candles (id, date_time, ticker, size, source, open, max, min, close, volume)
      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
      ''', candles_to_insert)
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        if conn:
            conn.rollback()
        print(f"Error: {e}")
    finally:
        conn.close()


def create_db(path):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    print('Create tables')
    try:
        cursor.execute("""
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
                )
            """)

        cursor.execute("""
                CREATE TABLE IF NOT EXISTS candles (
                    id VARCHAR(30) PRIMARY KEY,
                    date_time DATETIME NOT NULL,
                    ticker VARCHAR(30) NOT NULL,
                    size INTEGER NOT NULL,
                    source VARCHAR(30) NOT NULL,
                    open REAL NOT NULL,
                    max REAL NOT NULL,
                    min REAL NOT NULL,
                    close REAL NOT NULL,
                    volume INTEGER NOT NULL
                )
            """)

        cursor.execute("""
                CREATE TABLE IF NOT EXISTS pnl (
                    id VARCHAR(30) PRIMARY KEY,
                    ticker VARCHAR(30) NOT NULL,
                    type VARCHAR(30) NOT NULL,
                    fiscalDateEnding DATE NOT NULL,
                    reportedCurrency VARCHAR(30) NOT NULL,
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
            """)

        cursor.execute("""CREATE TABLE IF NOT EXISTS balance_sheet (
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
                """)

        cursor.execute("""CREATE TABLE IF NOT EXISTS cash_flow (
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
                """)

        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        if conn:
            conn.rollback()
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()


def company_save(company, path):
    conn = None
    try:
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        query = """
            INSERT OR IGNORE INTO company (Symbol, AssetType, Name, Description, CIK, Exchange, Currency, Country, Sector, Industry, Address, FiscalYearEnd)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(query, (
            company.symbol,
            company.asset_type,
            company.name,
            company.description,
            company.cik,
            company.exchange,
            company.currency,
            company.country,
            company.sector,
            company.industry,
            company.address,
            company.fiscal_year_end
        ))
        conn.commit()
        conn.close()

    except sqlite3.Error as e:
        if conn:
            conn.rollback()
        print(f"An error occurred: {e}")

    finally:
        if conn:
            conn.close()


def save_income_statement(pnl, path):
    conn = None
    try:
        conn = sqlite3.connect(path)
        c = conn.cursor()

        for statement in pnl:
            data = asdict(statement)
            data['fiscalDateEnding'] = data['fiscalDateEnding'].isoformat()
            placeholders = ', '.join('?' * len(data))
            columns = ', '.join(data.keys())
            query = f"INSERT OR IGNORE INTO pnl ({columns}) VALUES ({placeholders})"
            c.execute(query, tuple(data.values()))

        conn.commit()

    except sqlite3.Error as e:
        if conn:
            conn.rollback()
        print(f"An error occurred: {e}")

    finally:
        if conn:
            conn.close()


def save_balance_sheet(bs, path):
    conn = None
    try:
        conn = sqlite3.connect(path)
        c = conn.cursor()

        for statement in bs:
            data = asdict(statement)
            data['fiscalDateEnding'] = data['fiscalDateEnding'].isoformat()
            placeholders = ', '.join('?' * len(data))
            columns = ', '.join(data.keys())
            query = f"INSERT OR IGNORE INTO balance_sheet ({columns}) VALUES ({placeholders})"
            c.execute(query, tuple(data.values()))

        conn.commit()

    except sqlite3.Error as e:
        if conn:
            conn.rollback()
        print(f"An error occurred: {e}")

    finally:
        if conn:
            conn.close()


def save_cash_flow(cf, path):
    conn = None
    try:
        conn = sqlite3.connect(path)
        c = conn.cursor()

        for statement in cf:
            data = asdict(statement)
            data['fiscalDateEnding'] = data['fiscalDateEnding'].isoformat()
            placeholders = ', '.join('?' * len(data))
            columns = ', '.join(data.keys())
            query = f"INSERT OR IGNORE INTO cash_flow ({columns}) VALUES ({placeholders})"
            c.execute(query, tuple(data.values()))

        conn.commit()

    except sqlite3.Error as e:
        if conn:
            conn.rollback()
        print(f"An error occurred: {e}")

    finally:
        if conn:
            conn.close()

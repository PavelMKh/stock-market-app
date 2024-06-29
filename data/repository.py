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
        print(f"Error: {e}")
    finally:
        conn.close()


def create_db(path):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

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
            """)

        cursor.execute("""
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
            """)

        conn.commit()
        conn.close()
    except sqlite3.Error as e:
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
        print(f"An error occurred: {e}")

    finally:
        if conn:
            conn.close()
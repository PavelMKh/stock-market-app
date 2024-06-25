import sqlite3

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
        with open('schema.sql', 'r') as f:
            schema_sql = f.read()
        cursor.executescript(schema_sql)
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()


def company_save(company, path):
    conn = sqlite3.connect(path)
    try:
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
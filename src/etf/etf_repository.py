import sqlite3

def create_db_etf(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    print('Crate database for ETF data')
    try:
        cursor.execute("""
        CRATE TABLE IF NOT EXISTS etf_holdings (
                       etf_holding_key VARCHAR(30) PRIMERY KEY NOT KEY,
                       etf_ticker VARCHAR(20) NOT NULL,
                       report_date DATE NOT NULL,
                       company_ticker VARCHAR(20) NOT NULL,
                       company_name VARCHAR(160) NOT NULL,
                       share REAL NOT NULL)
        """)
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        if conn:
            conn.rollback
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()
CREATE TABLE IF NOT EXISTS company (
    Symbol VARCHAR(30) NOT NULL,
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
            date_time DATETIME,
            ticker TEXT,
            size INTEGER,
            source TEXT,
            open REAL,
            max REAL,
            min REAL,
            close REAL,
            volume INTEGER
        )


from service.candles_service import load_candles
from data.repository import create_db
from service.financial_reports_service import load_company, load_pnl, load_bs, load_cf, load_full_data
from config import DATABASE_PATH


def main():
    create_db(DATABASE_PATH)
    print("Welcome to stock market app!")
    while True:
        print('''Select menu item :
        1 - Load quote history into database
        2 - Get company overview
        3 - Get income statement
        4 - Get balance sheet
        5 - Get cash flow
        6 - Get full data (candles, reports)
        7 - Exit
        ''')
        menu = int(input('Input menu item >>> '))
        match menu:
            case 1:
                ticker = input("Enter stock ticker >>>")
                api_key = input("Enter API key >>>")
                candle_size = int(input("Enter candle size >>>"))
                load_candles(ticker, api_key, candle_size, DATABASE_PATH)
            case 2:
                ticker = input("Enter stock ticker >>>")
                api_key = input("Enter API key >>>")
                print(load_company(ticker, api_key, DATABASE_PATH))
            case 3:
                ticker = input("Enter stock ticker >>>")
                api_key = input("Enter API key >>>")
                print(load_pnl(ticker, api_key, DATABASE_PATH))
            case 4:
                ticker = input("Enter stock ticker >>>")
                api_key = input("Enter API key >>>")
                print(load_bs(ticker, api_key, DATABASE_PATH))
            case 5:
                ticker = input("Enter stock ticker >>>")
                api_key = input("Enter API key >>>")
                print(load_cf(ticker, api_key, DATABASE_PATH))
            case 6:
                tickers = list(map(str, input("Enter stock tickers >>>").split(',')))
                api_key = input("Enter API key >>>")
                print(load_full_data(tickers, api_key, DATABASE_PATH))
            case 7:
                print("Thank you for using our app!")
                break
            case _:
                print("Incorrect choice. Please try again.")


if __name__ == "__main__":
    main()

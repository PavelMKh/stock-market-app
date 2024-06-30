from service.candles_service import load_candles,  create_db_service
from service.financial_reports_service import load_company, load_pnl, load_bs
from config import DATABASE_PATH


def main():
    create_db_service(DATABASE_PATH)
    print("Welcome to stock market app!")
    while True:
        print('''Select menu item :
        1 - Load quote history into database")
        2 - Get company overview
        3 - Get income statement
        4 - Get balance sheet
        5 - Exit")
        ''')
        menu = int(input('Input menu item >>> '))
        if menu == 1:
            tickers = list(map(str, input("Enter stock tickers >>>").split(',')))
            api_key = input("Enter API key >>>")
            candle_size = int(input("Enter candle size >>>"))
            load_candles(tickers, api_key, candle_size, DATABASE_PATH)
        if menu == 2:
            ticker = input("Enter stock tickers >>>")
            api_key = input("Enter API key >>>")
            print(load_company(ticker, api_key, DATABASE_PATH))
        if menu == 3:
            ticker = input("Enter stock tickers >>>")
            api_key = input("Enter API key >>>")
            print(load_pnl(ticker, api_key, DATABASE_PATH))
        if menu == 4:
            ticker = input("Enter stock tickers >>>")
            api_key = input("Enter API key >>>")
            print(load_bs(ticker, api_key, DATABASE_PATH))
        if menu == 5:
            print("Thank you for using our app!")
            break


if __name__ == "__main__":
    main()

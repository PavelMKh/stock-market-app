from service.candles_service import load_candles
from service.financial_reports_service import load_company

db_path = 'candles_history.db'

def main():
    print("Welcome to stock market app!")
    while True:
        print('''Select menu item :
        1 - Load quote history into database")
        2 - Get company overview and save in Database
        3 - Exit")
        ''')
        menu = int(input('Input menu item >>> '))
        if menu == 1:
            tickers = list(map(str, input("Enter stock tickers >>>").split(',')))
            api_key = input("Enter API key >>>")
            candle_size = int(input("Enter candle size >>>"))
            load_candles(tickers, api_key, candle_size, db_path)
        if menu == 2:
            ticker = input("Enter stock tickers >>>")
            api_key = input("Enter API key >>>")
            print(load_company(ticker, api_key, db_path))
        if menu == 3:
            print("Thank you for using our app!")
            break


if __name__ == "__main__":
    main()

import yfinance as yf

if __name__ == '__main__':
    ticker_symbol = 'KKP.BK'

    #data = yf.download(ticker_symbol start="2020-01-01", end="2023-01-01")
    #print(data.head())


    stock = yf.Ticker(ticker_symbol)
    dividends = stock.dividends
    splits = stock.splits
    print(dividends)
    print(splits)

    apple = yf.Ticker("AAPL")
    dividends = apple.dividends
    splits = apple.splits
    print(dividends, splits)
        

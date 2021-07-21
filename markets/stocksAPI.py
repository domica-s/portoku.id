import yfinance as yf
import matplotlib.pyplot as plot
import seaborn

def getStockQuote(ticker):
    init_ticker = ticker # add upper()
    temp_ticker = init_ticker + ".JK"
    ticker = yf.Ticker(temp_ticker)
    hist = ticker.history(period="1h")
    closeDetails = hist['Close']
    # return format of closePrice --> Date 2021-07-21 30050.0 Name: Close, dtype: float64
    # closeDetails is of type series, take index 0 to get price value
    closePrice = closeDetails[0]

    temp_json = {
        'name' : init_ticker,
        'slug' : init_ticker,
        'price' : closePrice
    }

    return temp_json
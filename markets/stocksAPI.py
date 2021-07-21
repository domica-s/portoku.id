import yfinance as yf
import matplotlib.pyplot as plt
import io
import urllib, base64

def getStockQuote(ticker):
    init_ticker = ticker # add upper()
    temp_ticker = init_ticker + ".JK"
    ticker = yf.Ticker(temp_ticker)
    hist = ticker.history(period="1h")

    closeDetails = hist['Close']
    # return format of closePrice --> Date 2021-07-21 30050.0 Name: Close, dtype: float64
    # closeDetails is of type series, take index 0 to get price value
    closePrice = closeDetails[0]

    #dataframe for current 'daily' chart
    df = ticker.history(period="1d", interval="1m")
    plt.plot(df['Close'])
    fig = plt.gcf()

    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    temp_json = {
        'name' : init_ticker,
        'slug' : init_ticker,
        'price' : closePrice,
        'data' : uri,
    }

    return temp_json


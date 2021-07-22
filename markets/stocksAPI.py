import yfinance as yf
import matplotlib.pyplot as plt
import io
import urllib, base64

def getStockQuote(ticker):
    init_ticker = ticker # add upper()
    temp_ticker = init_ticker + ".JK"
    ticker = yf.Ticker(temp_ticker)
    info = ticker.info
    hist = ticker.history(period="1h")

    closeDetails = hist['Close']
    # return format of closePrice --> Date 2021-07-21 30050.0 Name: Close, dtype: float64
    # closeDetails is of type series, take index 0 to get price value
    closePrice = closeDetails[0]

    #dataframe for current 'daily' chart
    df = ticker.history(period="1d", interval="1m")
    plt.switch_backend('AGG') #with this script, no longer execute local python
    plt.tight_layout()
    plt.plot(df['Close'])
    # fig = plt.gcf()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    graph = base64.b64encode(buf.getvalue())
    graph = graph.decode('utf-8')
    buf.close()

    temp_json = {
        'name' : init_ticker,
        'fullname' : info['shortName'],
        'slug' : init_ticker,
        'price' : closePrice,
        'data' : graph,
    }

    return temp_json


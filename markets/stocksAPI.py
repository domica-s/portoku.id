import yfinance as yf
import matplotlib.pyplot as plt
import io
import urllib, base64

def getFullStockName(ticker):
    ticker = yf.Ticker(ticker)
    info = ticker.info

    return info['shortName']

def getStockSummary(ticker):
    ticker = yf.Ticker(ticker)
    info = ticker.info

    return info['longBusinessSummary']

def getStockGraph(ticker):
    ticker = yf.Ticker(ticker)
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

    return graph

def getStockSpotPrice(ticker):
    ticker = yf.Ticker(ticker)
    hist = ticker.history(period="1h")

    closeDetails = hist['Close']
    # return format of closePrice --> Date 2021-07-21 30050.0 Name: Close, dtype: float64
    # closeDetails is of type series, take index 0 to get price value
    closePrice = closeDetails[0]

    return closePrice



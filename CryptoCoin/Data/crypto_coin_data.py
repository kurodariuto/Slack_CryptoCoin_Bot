import requests
from matplotlib import pyplot as plt
from time import sleep

# Key generation
coin_name = {"btc_jpy", "etc_jpy", "mona_jpy"}
coin_ticker = {"bid", "ask"}
coin_data = []

# Hit the web API(rate)
def Coin_func():
    coin_rate = []
    btc = []
    etc = []
    mona = []
    for coin_names in coin_name:
        url = "https://coincheck.com/api/rate/" + coin_names
        coin_data.append(url)
        req = requests.get(url).json()
        coin_rate.append(req)
        print("rate確認")
        print(coin_rate)
    btc.append(coin_rate[0])
    etc.append(coin_rate[1])
    mona.append(coin_rate[2])
    print(btc)
    print(etc)
    print(mona)
    return btc, etc, mona

# Hit the web API(ticker)
def Ticker_func():
    url = "https://coincheck.com/api/ticker/"
    ticker_bid = []
    ticker_ask = []
    req = requests.get(url).json()
    ticker_bid.append(req["bid"])
    ticker_ask.append(req["ask"])
    print("GET_ticker")
    return ticker_bid, ticker_ask

# Graph creation
def Line_graph():
    bid = []
    ask = []
    for i in range(60):
        bid_ask = Ticker_func()
        print(bid_ask[0])
        print(bid_ask[1])
        bid.append(bid_ask[0])
        ask.append(bid_ask[1])
        sleep(60)
    plt.plot(bid, "-o", label="bid")
    plt.plot(ask, "-o", label="ask")
    plt.legend()
    plt.savefig('CryptoCoin_Lineraph.png')
    plt.close()
    plt.show()
    return bid[2], ask[2]
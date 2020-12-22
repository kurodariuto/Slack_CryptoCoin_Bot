import requests
import json
import schedule
import time
import sys
sys.path.append("../..")
from CryptoCoin.Data.crypto_coin_data import Coin_func, Ticker_func, Line_graph

# Specify Webhook URL
webhook_url = "Webhook url for your slack"

def job():
    
    # Graph and call coin_func
    all_rate = Coin_func()
    bid_ask = Line_graph()
    # Define the text to send
    bid_ask_text = "bid(現在の買い注文の最高価格)" \
                   "\nbit:" + str(bid_ask[0]) + \
                   "\n\nask(現在の売り注文の最安価格)" + \
                   "\nask:" + str(bid_ask[1])
    print(bid_ask_text)
    rate_text = "\nbtc_rate(ビットコインの値段)\n" + str(all_rate[0]).replace('{', '').replace('}', '').replace('"rate"',
                                                                                                       '').replace('[',
                                                                                                                   '').replace(
        ']', '').replace("'", "") + \
                "\n" + "\netc_rate(イーサリアムの値段)\n" + str(all_rate[1]).replace('{', '').replace('}', '').replace('"rate"',
                                                                                                              '').replace(
        '[', '').replace(']', '').replace("'", "") + \
                "\n" + "\nmona_rate(モナコインの値段)\n" + str(all_rate[2]).replace('{', '').replace('}', '').replace('"rate"',
                                                                                                              '').replace(
        '[', '').replace(']', '').replace("'", "").replace(' ', '')
    print(rate_text)

    # Send to Slack
    requests.post(webhook_url, data=json.dumps({
        "text": bid_ask_text
    }))
    requests.post(webhook_url, data=json.dumps({
        "text": rate_text
    }))

    # Send to imgges to Slack
    files = {'file': open("CryptoCoin_Lineraph.png", 'rb')}
    param = {
        'token': "xoxb-1448255571074-1595619608112-oO1vDwuDI6ggL3lXtV3TFMYM",
        'channels': "C01CRF5CB9D",
        'filename': "filename",
        'initial_comment': "image trnsmission",
        'title': "Line_graph"
    }
    requests.post(url="https://slack.com/api/files.upload", params=param, files=files)

# Set to run regularly at 11 AM every day
schedule.every().day.at("11:00").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
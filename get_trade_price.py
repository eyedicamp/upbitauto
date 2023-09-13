import requests
import json
import datetime


def get_trade_price(make_txt):

    time = datetime.datetime.utcnow()

    url = "https://api.upbit.com/v1/candles/days?market=KRW-BTC&count=200"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)

    data = json.loads(response.text)

    trade_price = []

    for i in range(200):
        trade_price.append(data[i]['trade_price'])

    while True:
        time = time - datetime.timedelta(days=200)

        url = "https://api.upbit.com/v1/candles/days?market=KRW-BTC&to=" + str(time)[:-16] + "%2008%3A44%3A58&count=200"
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
        
        data = json.loads(response.text)
        
        if len(data) < 200:
            for i in range(len(data)):
                trade_price.append(data[i]['trade_price'])
            break
        else:
            for i in range(200):
                trade_price.append(data[i]['trade_price'])

    trade_price.reverse()
    
    if make_txt:
        with open("trade_price.txt", 'w', encoding='UTF-8') as file:
            for price in trade_price:
                file.write(str(price) + '\n')
    
    return trade_price
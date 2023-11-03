import requests
import json
import datetime
import os

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
        
        if (len(data) < 200):
            try :
                if data[0]['name'] != 'too_many_requests':
                    for i in range(len(data)):
                        trade_price.append(data[i]['trade_price'])
                    break
            except:
                break

        else:
            for i in range(200):
                trade_price.append(data[i]['trade_price'])

    trade_price.reverse()

    for i in range(len(trade_price)):
        trade_price[i] = str(trade_price[i])
    
    if make_txt:
        file = open(r"C:\Users\신승윤\Documents\upbitauto\data\trade_price.txt", "w")
        # file.write("trade_price" + '\n')

        # data = file.read()
        # print("The file contents are:")
        # print (data)
        # print("출력 완료")

        file.write("hello")

        # for price in trade_price:
        #     file.write(str(price) + '\n')
        file.close()
    
    return trade_price

get_trade_price(True)
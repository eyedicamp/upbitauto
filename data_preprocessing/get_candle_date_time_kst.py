import requests
import json
import datetime

def get_candle_date_time_kst(make_txt):
    time = datetime.datetime.utcnow()

    url = "https://api.upbit.com/v1/candles/days?market=KRW-BTC&count=200"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)

    data = json.loads(response.text)

    candle_date_time_kst = []

    for i in range(200):
        candle_date_time_kst.append(data[i]['candle_date_time_kst'][:-9])

    while True:
        time = time - datetime.timedelta(days=200)

        url = "https://api.upbit.com/v1/candles/days?market=KRW-BTC&to=" + str(time)[:-16] + "%2008%3A44%3A58&count=200"
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
        
        data = json.loads(response.text)
        
        if len(data) < 200:
            for i in range(len(data)):
                candle_date_time_kst.append(data[i]['candle_date_time_kst'][:-9])
            break
        else:
            for i in range(200):
                candle_date_time_kst.append(data[i]['candle_date_time_kst'][:-9])

    candle_date_time_kst.reverse()

    # txt 파일로 저장
    if make_txt:
        with open("../data", 'w', encoding='UTF-8') as file:
            file.write("candle_date_time_kst" + '\n')
            for price in candle_date_time_kst:
                file.write(str(price) + '\n')

    return candle_date_time_kst
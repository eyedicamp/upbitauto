import requests
import json
import datetime

def get_change_rate():
    time = datetime.datetime.utcnow()

    url = "https://api.upbit.com/v1/candles/days?market=KRW-BTC&count=200"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)

    data = json.loads(response.text)

    change_rate = []

    for i in range(200):
        change_rate.append(data[i]['change_rate'])

    while True:
        time = time - datetime.timedelta(days=200)

        url = "https://api.upbit.com/v1/candles/days?market=KRW-BTC&to=" + str(time)[:-16] + "%2008%3A44%3A58&count=200"
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
        
        data = json.loads(response.text)
        
        if len(data) < 200:
            for i in range(len(data)):
                change_rate.append(data[i]['change_rate'])
            break
        else:
            for i in range(200):
                change_rate.append(data[i]['change_rate'])

    change_rate.reverse()

    # txt 파일로 저장
    with open("change_rate.txt", 'w', encoding='UTF-8') as file:
        for price in change_rate:
            file.write(str(price) + '\n')


    return change_rate
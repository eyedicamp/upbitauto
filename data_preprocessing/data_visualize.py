import pandas as pd
import matplotlib.pyplot as plt

def data_visulize(date):
    df = pd.read_excel("../data/raw_data.xlsx", engine="openpyxl")

    ax = plt.gca()

    df.plot(kind='line',x='candle_date_time_kst',y='trade_price',ax=ax)
    df.plot(kind='line',x='candle_date_time_kst',y='moving_average_5', ax=ax)
    df.plot(kind='line',x='candle_date_time_kst',y='moving_average_10', ax=ax)
    df.plot(kind='line',x='candle_date_time_kst',y='moving_average_20', ax=ax)
    
    for i in range(len(df['resistance_line'])):
        plt.axhline(df['resistance_line'][i], color='red', linestyle='--', linewidth=2) # 저항선
    for i in range(len(df['support_line'])):
        plt.axhline(df['support_line'][i], color='blue', linestyle='--', linewidth=2) # 지지선

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('BTC Price')
    plt.legend(['trade_price', 'moving_average_5', 'moving_average_10', 'moving_average_20'], loc='upper left')
    plt.grid(True)

    
    if date:
        date_num = len(df["candle_date_time_kst"]) - 1
        if date_num < date:
            print("ERROR : date is too big.")
        else:
            plt.xlim([date_num - date, date_num])      # X축의 범위: [xmin, xmax]
            # plt.ylim([30000000, 50000000])     # Y축의 범위: [ymin, ymax]     # min, max의 값을 구해서 범위의 1.5배정도 하면 보기 좋을듯
            plt.show()
    else:
        plt.show()

data_visulize(0)
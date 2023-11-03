import get_trade_price
import get_candle_date_time_kst
import get_change_rate
import get_moving_average
import get_support_resistance_line
import pandas as pd
import os


get_trade_price.get_trade_price(True)

get_candle_date_time_kst.get_candle_date_time_kst(True)

get_change_rate.get_change_rate(True)

get_moving_average.get_moving_average(5, True)

get_moving_average.get_moving_average(10, True)

get_moving_average.get_moving_average(20, True)

get_support_resistance_line.get_support_resistance_line(30, True, False)



df_trade_price = pd.read_csv('../data/trade_price.txt', sep = ' ')
df_candle_date_time_kst = pd.read_csv('../data/candle_date_time_kst.txt', sep = ' ')
df_change_rate = pd.read_csv('../data/change_rate.txt', sep = ' ')
df_moving_average_5 = pd.read_csv('../data/moving_average_5.txt', sep = ' ')
df_moving_average_10 = pd.read_csv('../data/moving_average_10.txt', sep = ' ')
df_moving_average_20 = pd.read_csv('../data/moving_average_20.txt', sep = ' ')
df_resistance_line = pd.read_csv('../data/resistance_line.txt', sep = ' ')
df_support_line = pd.read_csv('../data/support_line.txt', sep = ' ')

df = pd.concat([df_candle_date_time_kst, df_trade_price, df_change_rate, df_moving_average_5, df_moving_average_10, df_moving_average_20, df_resistance_line, df_support_line], axis=1)

print(df)

df.to_excel("../data/raw_data.xlsx", header=True, index=False)

df.to_csv("../data/raw_data.csv", header=True, index=False)
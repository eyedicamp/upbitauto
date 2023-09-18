import get_trade_price
import get_candle_date_time_kst
import get_change_rate
import get_moving_average
import pandas as pd
import os


# get_trade_price.get_trade_price(False)

# get_candle_date_time_kst.get_candle_date_time_kst(False)

# get_change_rate.get_change_rate(False)

# get_moving_average.get_moving_average(5, False)

# get_moving_average.get_moving_average(10, False)

# get_moving_average.get_moving_average(20, False)



df_trade_price = pd.read_csv('trade_price.txt', sep = ' ')
df_candle_date_time_kst = pd.read_csv('candle_date_time_kst.txt', sep = ' ')
df_change_rate = pd.read_csv('change_rate.txt', sep = ' ')
df_moving_average_5 = pd.read_csv('moving_average_5.txt', sep = ' ')
df_moving_average_10 = pd.read_csv('moving_average_10.txt', sep = ' ')
df_moving_average_20 = pd.read_csv('moving_average_20.txt', sep = ' ')

df = pd.concat([df_candle_date_time_kst, df_trade_price, df_change_rate, df_moving_average_5, df_moving_average_10, df_moving_average_20], axis=1)

print(df)

base_dir = "C:/upbitauto"
file_name = "raw_data.xlsx"
xlxs_dir = os.path.join(base_dir, file_name)
df.to_excel(file_name, header=True, index=False)
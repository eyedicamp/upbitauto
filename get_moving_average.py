import get_trade_price
import pandas as pd

def get_moving_average(days, make_txt):
    pd.set_option('display.float_format', lambda x: '%.1f' % x)

    df = pd.DataFrame(get_trade_price.get_trade_price(False), columns=['trade_price'])

    moving_average_df = df['trade_price'].rolling(days).mean()

    moving_average = moving_average_df.values.tolist()

    if make_txt:
        with open("moving_average_" + str(days) + ".txt", 'w', encoding='UTF-8') as file:
            for average in moving_average:
                file.write(str(average) + '\n')
    
    return moving_average
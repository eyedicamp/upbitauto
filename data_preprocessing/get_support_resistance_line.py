import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import hdbscan
from sklearn.preprocessing import RobustScaler

def get_support_resistance_line(cluster_size, make_txt, plot):
    df_trade_price = pd.read_csv('C:/Users/slsl9/Documents/upbitauto/data/trade_price.txt', sep = ' ')

    df_scale = pd.DataFrame(RobustScaler().fit_transform(df_trade_price), columns = df_trade_price.columns)

    clusterer = hdbscan.HDBSCAN(min_cluster_size=cluster_size)
    df_trade_price["dbscan_cluster"] = clusterer.fit_predict(np.array(df_scale).reshape(-1, 1))

    df_trade_price.plot(figsize=(12, 5))

    resist = []
    support = []

    for n in df_trade_price["dbscan_cluster"].unique():
        if n != -1:
            resist_line = df_trade_price[df_trade_price['dbscan_cluster']==n]["trade_price"].max()
            support_line = df_trade_price[df_trade_price['dbscan_cluster']==n]["trade_price"].min()
            
            resist.append(resist_line)
            support.append(support_line)
            if plot:
                plt.axhline(resist_line, color='red', linestyle='--', linewidth=2)
                plt.axhline(support_line, color='blue', linestyle='--', linewidth=2)

    if make_txt:
        with open("C:/Users/slsl9/Documents/upbitauto/data/resistance_line.txt", 'w', encoding='UTF-8') as file:
            file.write("resistance_line" + '\n')
            for rst in resist:
                file.write(str(rst) + '\n')
        with open("C:/Users/slsl9/Documents/upbitauto/data/support_line.txt", 'w', encoding='UTF-8') as file:
            file.write("support_line" + '\n')
            for spt in support:
                file.write(str(spt) + '\n')
    
    if plot:
        plt.show()
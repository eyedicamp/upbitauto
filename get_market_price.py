import ccxt
import pprint
import pandas as pd

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# binance = ccxt.binance()
# markets= binance.load_markets()

# print(markets.keys())
# print(len(markets))


# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# binance = ccxt.binance()
# btc = binance.fetch_ticker("BTC/USDT")
# pprint.pprint(btc)

# ask	    매도 1호가
# askVolume	매도 1호과 물량
# bid	    매수 1호가
# bidVolume	매수 1호과 물량
# datetime	현재시간
# timestamp	타임 스탬프
# open  	시가
# high  	고가
# low	    저가
# close 	종가
# symbol    심볼

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# 분봉 조회 (500개까지)

# binance = ccxt.binance()
# btc_ohlcv = binance.fetch_ohlcv("BTC/USDT")

# df = pd.DataFrame(btc_ohlcv, columns=['datetime', 'open', 'high', 'low', 'close', 'volume'])
# df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
# df.set_index('datetime', inplace=True)
# print(df)


# 일봉 조회 (500일치)

# binance = ccxt.binance()
# btc_ohlcv = binance.fetch_ohlcv("BTC/USDT", '1d')

# df = pd.DataFrame(btc_ohlcv, columns=['datetime', 'open', 'high', 'low', 'close', 'volume'])
# df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
# df.set_index('datetime', inplace=True)
# print(df)


# 원하는 개수만큼

# binance = ccxt.binance()
# btc_ohlcv = binance.fetch_ohlcv(symbol="BTC/USDT", timeframe='1d', limit=10)

# 데이터 프레임 변환
# df = pd.DataFrame(btc_ohlcv, columns=['datetime', 'open', 'high', 'low', 'close', 'volume'])
# df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
# df.set_index('datetime', inplace=True)
# print(df)


# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# 호가 조회

exchange = ccxt.binance()
orderbook = exchange.fetch_order_book('ETH/USDT')
print(orderbook['asks'])
print(orderbook['bids'])
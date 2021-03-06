from fetch_data import fetch_data
from store_OHLC import store_OHLC

import pandas as pd
import numpy as np

#fetch data
data = fetch_data()
print("data fetched")

# convert to dataframe
df = pd.DataFrame(data, columns = ['timestamp', 'price', 'volume'])
df['timestamp'] = df.timestamp/100000000
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
df = df.set_index('timestamp')
print("converted to dataframe")

#create tables, calculate then store ohlcv data for each case study
ohlcv = ['1Min', '5Min', '15Min', '30Min', '1H', '2H', '4H', '6H', '12H', 'D']
#ohlcv = ['D']

i, j = 0, len(ohlcv)
while(i < j):
	print("creating table and calculating ohlcv to then store it for every ", ohlcv[i])
	tmp = df.resample(ohlcv[i]).agg({'price': 'ohlc', 'volume': 'sum'})
	tmp['timeframe'] = tmp.index
	tmp.columns = tmp.columns.droplevel(0)
	tmp.rename(columns={'': 'date'}, inplace=True)
	tmp = tmp.replace(to_replace='None', value=np.nan).dropna()
	store_OHLC(ohlcv[i], tmp)
	i+=1
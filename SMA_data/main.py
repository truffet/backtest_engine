import mysql.connector
import pandas as pd
from fetch_data import fetch_data
from sma import sma
from store_SMA import store_SMA

#periods = ['1Min', '5Min', '15Min', '30Min', '1H', '2H', '4H', '6H', '12H', '24H']
periods = ['1H', '4H', '24H']
a, b = 0, len(periods)

while (a < b):
	print(periods[a])
	data = fetch_data(periods[a])
	i, j = 0, len(data)
	SMA = {10: [], 20: [], 50: [], 100: [], 200: []}
	sma_list = [10, 20, 50, 100, 200]
	y = len(sma_list)
	while(i < j):
		x = 0
		while (x < y):
			if (i > sma_list[x]):
				SMA[sma_list[x]].append((sma(sma_list[x], data, i)))
			else:
				SMA[sma_list[x]].append(0)
			x+=1
		i+=1

	df2 = pd.DataFrame.from_dict(SMA)
	store_SMA(('SMAs_' + periods[a]),df2)
	a+=1
import mysql.connector
import pandas as pd
from fetch_data import fetch_data
from sma import sma
from dsma import dsma
from store_SMA import store_SMA

periods = ['D', 'W']
a, b = 0, len(periods)

while (a < b):
	print(periods[a])
	data = fetch_data(periods[a])
	i, j = 0, len(data)
	SMA = {10: [], 20: [], 50: [], 100: [], 200: [], 'date': []}
	dSMA = {10: [], 20: [], 50: [], 100: [], 200: [], 'date': []}
	sma_list = [10, 20, 50, 100, 200]
	y = len(sma_list)
	while(i < j):
		x = 0
		while (x < y):
			if (i > sma_list[x]):
				tmp = sma(sma_list[x], data, i)
				SMA[sma_list[x]].append(tmp)
				dSMA[sma_list[x]].append(dsma(tmp, data, i))
			else:
				SMA[sma_list[x]].append(None)
				dSMA[sma_list[x]].append(None)
			x+=1
		SMA['date'].append(data[i][1])
		dSMA['date'].append(data[i][1])
		i+=1

	df1 = pd.DataFrame.from_dict(SMA)
	df2 = pd.DataFrame.from_dict(dSMA)
	store_SMA(('SMAs_' + periods[a]),df1)
	store_SMA(('dSMAs_' + periods[a]),df2)
	a+=1
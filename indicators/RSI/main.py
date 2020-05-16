import mysql.connector
import pandas as pd
from fetch_data import fetch_data
from store_RSI import store_RSI
from rsi_calculator import rsi_calculator

periods = ['D', 'W']
a, b = 0, len(periods)

while (a < b):
	print(periods[a])
	data = fetch_data(periods[a])
	i, j = 0, len(data)
	RSI = {14: [], 'date': []}
	rsi = rsi_calculator(14, data)
	while(i < j):
		RSI[14].append(rsi[i])
		RSI['date'].append(data[i][1])
		i+=1
	df = pd.DataFrame.from_dict(RSI)
	store_RSI(('RSI_' + periods[a]), df)
	a+=1
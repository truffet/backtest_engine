import mysql.connector
import pandas as pd
from fetch_data import fetch_data
from store_ATR import store_ATR
from atr_calculator import atr_calculator

periods = ['D', 'W']
a, b = 0, len(periods)

while (a < b):
	print(periods[a])
	data = fetch_data(periods[a])
	i, j = 0, len(data)
	ATR = {14: [], 'date': []}
	while (i < j):
		if (i < 13):
			ATR[14].append(None)
		else:
			ATR[14].append(atr_calculator(14, data, i))
		ATR['date'].append(data[i][3])
		i+=1

	df = pd.DataFrame.from_dict(ATR)
	store_ATR(('ATR_' + periods[a]), df)
	a+=1
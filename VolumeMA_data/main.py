import mysql.connector
import pandas as pd
from fetch_data import fetch_data
from store_VolumeMA import store_VolumeMA
from VolMA_calculator import VolMA_calculator

#periods = ['1Min', '5Min', '15Min', '30Min', '1H', '2H', '4H', '6H', '12H', '24H']
periods = ['1H', '4H', '24H']
a, b = 0, len(periods)

while (a < b):
	print(periods[a])
	data = fetch_data(periods[a])
	i, j = 0, len(data)
	VolMA = {20: [], 'date': []}
	while (i < j):
		if (i < 19):
			VolMA[20].append(0)
		else:
			VolMA[20].append(VolMA_calculator(20, data, i))
		VolMA['date'].append(data[i][1])
		i+=1

	df2 = pd.DataFrame.from_dict(VolMA)
	store_VolumeMA(('VolumeMA_' + periods[a]), df2)
	a+=1
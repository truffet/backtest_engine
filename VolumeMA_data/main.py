import mysql.connector
import pandas as pd
from fetch_data import fetch_data
from store_VolumeMA import store_VolumeMA

#periods = ['1Min', '5Min', '15Min', '30Min', '1H', '2H', '4H', '6H', '12H', '24H']
periods = ['24H']
a, b = 0, len(periods)

while (a < b):
	print(periods[a])
	data = fetch_data(periods[a])
	i, j = 0, len(data)
	print(data)
	store_VolumeMA(('VolumeMA_' + periods[a]))
	a+=1
from fetch_data import fetch_data
from store_data import store_data
from time import sleep
import sys
import pandas as pd

#timeframe = ['1Min', '5Min', '15Min', '30Min', '1H', '2H', '4H', '6H', '12H', 'D']
timeframe = ['D']
i, j = 0, len(timeframe)

while (i < j):
	
	#fetching required data
	PriceSMA = fetch_data('*', ('PSMA_' + timeframe[i]))
	delta = fetch_data('*', ('delta_' + timeframe[i]))
	ohlc = fetch_data('*', (timeframe[i]))

	#deleting data pre-2016
	while((ohlc[0][5].strftime("%Y/%m/%d, %H:%M:%S")).startswith('2016') != True):
		PriceSMA.pop(0)
		delta.pop(0)
		ohlc.pop(0)

	#create a copy before sorting
	sorted_delta = delta.copy()
	#sort from min to max
	sorted_delta.sort()

	#pairing up deltas for min and max test and returning profit/loss results for each
	size = len(delta)
	
	i+=1
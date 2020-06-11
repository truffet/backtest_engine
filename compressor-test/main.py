from fetch_data import fetch_data
from delta_strategy_backtest import delta_strategy_backtest
from store_data import store_data
from time import sleep
import itertools 
import sys
import pandas as pd

#timeframe = ['1Min', '5Min', '15Min', '30Min', '1H', '2H', '4H', '6H', '12H', 'D']
timeframe = ['4H']
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
		
	#deleting None data
	x, y = 0, len(delta)
	while(x < y):
		if (delta[x] == (None,)):
			PriceSMA.pop(x)
			delta.pop(x)
			ohlc.pop(x)
			y-=1
		else:
			x+=1

	#convert list of tuples to list
	delta = list(itertools.chain(*delta))
	#create a copy before sorting
	sorted_delta = delta.copy()
	#sort from min to max
	sorted_delta.sort()

	#pairing up deltas for min and max test and returning profit/loss results for each
	size = len(delta)
	x, y = 0, size-1
	all_star = []
	win, loss = 0, 0
	while (x < y):
		z = y
		while (z > x):
			result = delta_strategy_backtest(sorted_delta[x], sorted_delta[z], delta, PriceSMA, ohlc)
			if (result[0] > 100 and result[1] > 100):
				print("\nsummary:")
				print("min delta:", sorted_delta[x])
				print("max delta:", sorted_delta[z])
				print("cumul profit %:", result[0])
				print("number of trades:", result[1])
				print("\n")
				all_star.append((sorted_delta[x], sorted_delta[z], result[0], result[1]))
				#sys.exit()
				#sleep(2)
			z-=1
		x+=1
	#store all star results
	df = pd.DataFrame(all_star)
	store_data(('allstar_' + timeframe[i]), df)
	print("All star results stored for", timeframe[i])
	i+=1
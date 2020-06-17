from fetch_data import fetch_data
from store_data import store_data
from time import sleep
import sys
import pandas as pd
from decimal import *
from math import sqrt

def mean_delta(delta, size):
	x, total = 0, 0
	while(x < size):
		total = total + delta[x][0]
		x+=1
	return(Decimal(total)/size)

def variance_delta(mean, delta, size):
	x, total = 0, 0
	while(x < size):
		total = total + pow((Decimal(delta[x][0])-mean), 2)
		x+=1
	return(Decimal(total)/size)



timeframe = ['1Min', '5Min', '15Min', '30Min', '1H', '2H', '4H', '6H', '12H', 'D']
#timeframe = ['D']
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

	#avg delta
	size = len(delta)
	mean = mean_delta(delta, size)
	variance = variance_delta(mean, delta, size)
	std = sqrt(variance)

	print("timeframe:", timeframe[i])
	print("delta minimum:", sorted_delta[0][0])
	print("delta maximum:", sorted_delta[size-1][0])
	print("mean delta:", mean)
	print("variance:", variance)
	print("standard deviation:", std)
	print("\n")

	#pairing up deltas for min and max test and returning profit/loss results for each
	
	i+=1
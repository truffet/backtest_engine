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

def interest_count(mini, maxi, delta):
	i, j = 0, len(delta)
	pos, entry, exit = 0, 0, 0
	while(i < j):
		if (pos == 0 and delta[i][0] <= mini):
			entry+=1
			pos = 1
		elif (pos == 2 and delta[i][0] <= mini):
			entry+=1
			pos = 1
		elif (pos > 0 and delta[i][0] >= maxi and delta[i-1][0] <= maxi):
			exit+=1
			pos = 2
		i+=1
	if (pos == 1):
		entry-=1
	return(entry, exit)


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

	#avg delta
	size = len(delta)
	mean = mean_delta(delta, size)
	variance = variance_delta(mean, delta, size)
	std = Decimal(sqrt(variance))
	mini_delta = Decimal(sorted_delta[0][0])
	maxi_delta = Decimal(sorted_delta[size-1][0])

	mini_mean = mean - std
	maxi_mean = mean + std
	mini_step = Decimal(mini_mean - mini_delta)/Decimal(100)
	maxi_step = Decimal(maxi_delta - maxi_mean)/Decimal(100)
	
	x = mini_delta
	while (x < mini_mean):
		y = maxi_delta
		while (y > maxi_mean):
			entry, exit = interest_count(x, y, delta)
			print("dmin: " + str(x) + "; dmax: " + str(y) + "; entries: " + str(entry) + "; exits: " + str(exit))
			y-=maxi_step
		x+=mini_step

	print("timeframe:", timeframe[i])
	print("delta minimum:", mini_delta)
	print("delta maximum:", maxi_delta)
	print("mean delta:", mean)
	print("variance:", variance)
	print("standard deviation:", std)
	print("delta min search area between " + str(mini_delta) + " and " + str(mini_mean) + " with a step of " + str(mini_step))
	print("delta max search area between " + str(maxi_mean) + " and " + str(maxi_delta) + " with a step of " + str(maxi_step))

	i+=1
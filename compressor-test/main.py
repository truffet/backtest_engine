from fetch_data import fetch_data
from decimal import *

timeframe = ['4H','D']
i, j = 0, len(timeframe)

while (i < j):
	
	PSMA = fetch_data('*', ('PSMA_' + timeframe[i]))
	Price = fetch_data('*', (timeframe[i]))
	size = len(Price)
	open_price, high_price, low_price, close_price, volume, date = zip(*Price)
	data = list(zip(*PSMA))

	while((date[0].strftime("%Y/%m/%d, %H:%M:%S")).startswith('2016') != True):
		date.remove(1)
	print(date[0])
	print(Price[0])

	i+=1
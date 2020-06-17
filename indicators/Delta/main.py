from fetch_data import fetch_data
from store_data import store_data
from decimal import *
import pandas as pd

#timeframe = ['1Min', '5Min', '15Min', '30Min', '1H', '2H', '4H', '6H', '12H', 'D']
timeframe = ['D']

i, j = 0, len(timeframe)

while(i < j):

	#fetch relevant data
	print(timeframe[i])
	close_price = fetch_data('close', timeframe[i])
	print("price data fetched for", timeframe[i])
	PSMA = fetch_data('*', ('PSMA_' + timeframe[i]))
	print("SMA data fetched for", timeframe[i])

	#calculate delta
	delta = []
	x, y = 0, len(PSMA)
	while(x < y):

		tmp = list(PSMA[x])
		tmp.pop() #pop date out
		tmp.append(close_price[x][0]) #adding price close to delta calculation

		if (tmp.count(None) > 0):
			delta.append((None, None, None))
		else:
			mini = min(tmp)
			maxi = max(tmp)
			d = float(((Decimal(maxi)/Decimal(mini))-1)*100)
			#saving delta, minimum MA and maximum MA
			delta.append((d, mini, maxi))
		x+=1
	print("Delta calculated for", timeframe[i])

	#store delta
	df = pd.DataFrame(delta)
	store_data(('delta_' + timeframe[i]), df)
	print("Delta stored for", timeframe[i])

	i+=1
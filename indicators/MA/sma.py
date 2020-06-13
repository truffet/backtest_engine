from utils.storage_base import storage_base
from utils.store_data import store_data
from decimal import *
import pandas as pd

def sma_calculator(period, data, index):
	i, j = 0, period
	tmp = 0
	while(i < period):
		tmp = tmp + data[i][0]
		i+=1
	sma = float(Decimal(tmp)/Decimal(period))
	return(sma)

def sma(params):
	timeframe, periods, data, name = params[0], params[1], params[2], params[3]
	SMA = storage_base(periods)
	print("calculating sma for", timeframe)

	i, j = 0, len(data)
	y = len(periods)
	while(i < j):
		x = 0
		while (x < y):
			if (i > periods[x]):
				sma = sma_calculator(periods[x], data, i)
				SMA[periods[x]].append(sma)
			else:
				SMA[periods[x]].append(None)
			x+=1
		SMA['date'].append(data[i][1])
		i+=1
	df = pd.DataFrame.from_dict(SMA)

	print("sma calculated for", timeframe)

	store_data((name + 'SMA_' + timeframe),df)
	print("sma stored for", timeframe)
	
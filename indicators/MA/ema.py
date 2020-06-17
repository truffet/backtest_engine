from utils.storage_base import storage_base
from utils.store_data import store_data
from decimal import *
import pandas as pd

def sma_calculator(period, data, index):
	tmp = 0
	a = period-1
	while(a >= 0):
		tmp = tmp + data[index-a][0]
		a-=1
	sma = float(Decimal(tmp)/Decimal(period))
	return(sma)

def ema_calculator(data, index, prev, multiplier):
	ema = (Decimal(data[index][0] - prev) * multiplier) + Decimal(prev)
	return(float(ema))

def ema(params):
	timeframe, periods, data, name = params[0], params[1], params[2], params[3]
	EMA = storage_base(periods)
	print("calculating ema for", timeframe)

	i, j = 0, len(data)
	y = len(periods)
	while(i < j):
		x = 0
		while (x < y):
			multiplier = (2 / Decimal(periods[x] + 1))
			if (i == periods[x]):
				sma = sma_calculator(periods[x], data, i)
				EMA[periods[x]].append(sma)
				prev = sma
			elif (i > periods[x]):
				ema = ema_calculator(data, i, prev, multiplier)
				EMA[periods[x]].append(ema)
				prev = ema
			else:
				EMA[periods[x]].append(None)
			x+=1
		EMA['date'].append(data[i][1])
		i+=1
	df = pd.DataFrame.from_dict(EMA)

	print("ema calculated for", timeframe)

	store_data((name + 'EMA_' + timeframe),df)
	print("ema stored for", timeframe)
	
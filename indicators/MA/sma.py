from utils.storage_base import storage_base
from utils.store_data import store_data
from decimal import *
import pandas as pd

def dsma(sma, data, index):
	if (sma == None or data[index][0] == None):
		return(None)
	if (sma == 0 or data[index][0] == 0):
		return(None)
	d = Decimal(data[index][0])/Decimal(sma)
	result = (d - 1) * 100
	return(float(result))

def sma_calculator(period, data, index):
	i, j = 0, period
	tmp = 0

	#candle with no price action
	if(data[index][0] == 0 or data[index][0] == None):
		return(None)
	while(i < period):
		#current index out of bound
		if (index-i < 0):
			return(None)
		#period with no price action on candle and previous candle does not exist
		elif(data[index-i][0] == None and index-i == 0):
			return(None)
		#period with no price action on candle but previous candle exists
		elif (data[index-i][0] == None and index-i > 0):
			period+=1
		else:
			tmp = tmp + data[index-i][0]
		i+=1
	sma = Decimal(tmp)/Decimal(period)
	d = dsma(sma, data, index)
	return(d)

def sma(params):
	timeframe, periods, data, name = params[0], params[1], params[2], params[3]
	SMA = storage_base(periods)

	i, j = 0, len(data)
	y = len(periods)
	while(i < j):
		x = 0
		while (x < y):
			if (i > periods[x]):
				SMA[periods[x]].append(sma_calculator(periods[x], data, i))
			else:
				SMA[periods[x]].append(None)
			x+=1
		SMA['date'].append(data[i][1])
		i+=1
	df = pd.DataFrame.from_dict(SMA)
	store_data((name + 'SMA_' + timeframe),df)
	
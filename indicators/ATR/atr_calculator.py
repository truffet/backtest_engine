from decimal import *

def atr_calculator(period, data, index):
	i, j = 0, period
	tmp = 0

	#candle with no price action
	if(data[index][0] == 0 or data[index][0] == None):
		return(None)
	while(i < period):
		#no existing previous candle for tr calculation
		if (index-i == 0):
			return(None)
		#period with no price action on candle and previous 2 candles do not exist
		elif(data[index-i][1] == None and index-i == 1):
			return(None)
		#period with no price action on candle but previous candle exists
		elif (data[index-i][1] == None and index-i > 1):
			period+=1
		else:
			count = 1
			while((index-i-count >= 0) and data[index-i-count][1] == None):
				count+=1
			if (index-i-count < 0):
				return(None)
			tr = max((data[index-i][0]-data[index-i][1]),(data[index-i][0]-data[index-i-count][2]),(data[index-i][1]-data[index-i-count][2]))
			tmp = tmp + tr
		i+=1
	return(float(Decimal(tmp)/Decimal(period)))
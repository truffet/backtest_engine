from decimal import *

def VolMA_calculator(period, data, index):
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
	return(Decimal(tmp)/Decimal(period))
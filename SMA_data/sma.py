from decimal import *

def sma(period, data, index):
	i, j = (index-period+1), period
	tmp = 0
	while(i <= index):
		if(data[i][0] == None):
			return(0)
		tmp = tmp + data[i][0]
		i+=1
	return(float(Decimal(tmp)/Decimal(period)))
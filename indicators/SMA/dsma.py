from decimal import *

def dsma(sma, data, index):
	if (sma == 0):
		return(None)
	d = float(Decimal(data[index][0])/Decimal(sma))
	result = (d - 1) * 100
	return(result)
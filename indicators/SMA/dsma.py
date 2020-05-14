from decimal import *

def dsma(sma, data, index):
	if (sma == None or data[index][0] == None):
		return(None)
	if (sma == 0 or data[index][0] == 0):
		return(None)
	d = Decimal(data[index][0])/Decimal(sma)
	result = (d - 1) * 100
	return(float(result))
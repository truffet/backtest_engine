from decimal import *

def dVolMA_calculator(VolMA, data, index):
	if (VolMA == 0):
		return(None)
	d = float(Decimal(data[index][0])/Decimal(VolMA))
	result = (d - 1) * 100
	return(result)
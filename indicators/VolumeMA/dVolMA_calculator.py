from decimal import *

def dVolMA_calculator(VolMA, data, index):
	if (VolMA == None):
		return(None)
	d = float(Decimal(data[index][0])/Decimal(VolMA))
	result = (d - 1) * 100
	return(result)
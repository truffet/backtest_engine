from decimal import *

def dVolMA_calculator(VolMA, data, index):
	if (VolMA == None or data[index][0] == None):
		return(None)
	if (VolMA == 0 or data[index][0] == 0):
		return(None)
	d = float(Decimal(data[index][0])/Decimal(VolMA))
	result = (d - 1) * 100
	return(result)
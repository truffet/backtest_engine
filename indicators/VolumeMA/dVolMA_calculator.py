from decimal import *

def dVolMA_calculator(VolMA, data, index):
	if (VolMA == None):
		return(None)

	if (data[index][0] >= VolMA):
		d = float(Decimal(data[index][0])/Decimal(VolMA))
		result = (d - 1) * 100
	else:
		d = float(Decimal(VolMA)/Decimal(data[index][0]))
		result = (d - 1) * -100
	return(result)
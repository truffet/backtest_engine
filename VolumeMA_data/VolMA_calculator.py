from decimal import *

def VolMA_calculator(period, data, index):
	i, j = (index-period+1), period
	tmp = 0
	while(i <= index):
		tmp = tmp + data[i][3]
		i+=1
	return(float(Decimal(tmp)/Decimal(period)))
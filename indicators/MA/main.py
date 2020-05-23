from utils.fetch_data import fetch_data
from sma import sma
from ema import ema
from wma import wma

def period_calculator(step, maximum):
	i = step
	result = []
	while(i <= maximum):
		result.append(i)
		i+=step
	return(result)

#init params
timeframe = ['4H','D']

periods = period_calculator(5, 200)
print("Periods:", periods)

averages = {
	'PSMA': [sma, ema, wma],
	'VSMA': [sma, ema, wma]
}

def fire_all(func_list, params):
	for f in func_list:
		f(params)


i, j = 0, len(timeframe)
while(i < j):
	print(timeframe[i])
	price_data = fetch_data('close, date', timeframe[i])
	volume_data = fetch_data('volume, date', timeframe[i])
	for x in averages:
		if (x.startswith('P')):
			fire_all(averages[x],(timeframe[i], periods, price_data, 'P'))
		else:
			fire_all(averages[x],(timeframe[i], periods, volume_data, 'V'))
	i+=1
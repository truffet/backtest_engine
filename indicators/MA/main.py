from utils.fetch_data import fetch_data
from sma import sma
from ema import ema
from wma import wma

#init params
timeframe = ['D', 'W']
periods = [10, 20, 50, 100, 200]
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
			fire_all(averages[x],(timeframe[i], periods, volume_data, 'v'))
	i+=1

#		df = pd.DataFrame.from_dict(ATR)
#		store_ATR((name + '_' + periods[a]), df)
#test = Moving_Average(attributes)
#print(getattr(test, '10'))
#print(dir(test))
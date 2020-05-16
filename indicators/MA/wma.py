from utils.storage_base import storage_base

def wma(params):
	timeframe, periods, data, name = params[0], params[1], params[2], params[3]
	WMA = storage_base(periods)
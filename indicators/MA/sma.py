from utils.storage_base import storage_base

def sma(params):
	timeframe, periods, data, name = params[0], params[1], params[2], params[3]
	SMA = storage_base(periods)
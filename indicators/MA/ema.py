from utils.storage_base import storage_base

def ema(params):
	timeframe, periods, data, name = params[0], params[1], params[2], params[3]
	EMA = storage_base(periods)
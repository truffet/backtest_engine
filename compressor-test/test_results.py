from delta_strategy_backtest import delta_strategy_backtest
from fetch_data import fetch_data

#timeframe = ['1Min', '5Min', '15Min', '30Min', '1H', '2H', '4H', '6H', '12H', 'D']
timeframe = ['D', '12H']
i, j = 0, len(timeframe)

while (i < j):
	result = fetch_data('*', ('allstar_' + timeframe[i]))
	result_size = len(result)
	print("Number of cases with more than 10 trades and 100 percent cumul profit:", result_size)

	delta_min_list, delta_max_list, profit_list, nb_trades_list = zip(*result)

	x, y = 1, len(delta_min_list)
	max_spread, max_trades, max_profit = 0, 0, 0
	while (x < y):

		if (profit_list[x] > profit_list[max_profit]):
			max_profit = x
		
		if (nb_trades_list[x] > nb_trades_list[max_trades]):
			max_trades = x
		
		curr = delta_max_list[x] - delta_min_list[x]
		prev = delta_max_list[max_spread] - delta_min_list[max_spread]
		if (curr > prev):
			max_spread = x

		x+=1
	
	print("Max profit was made with:", result[max_profit])
	print("Max trades was made with:", result[max_trades])
	print("Max spread was made with:", result[max_spread])

	
	i+=1
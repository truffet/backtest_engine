from decimal import *

def delta_strategy_backtest(delta_min, delta_max, delta, moving_average, ohlc):
	
	#init parameters
	result = 0
	position = ["", 0]
	order = 0
	count = 0
	open_price, high_price, low_price, close_price, volume, date = zip(*ohlc)

	#calculating min and max ma for each delta (will need to implement this in delta calculation and storage later) #######
	i, j = 0, len(delta)
	ext = []
	while(i < j):
		tmp = list(moving_average[i])
		tmp.pop()
		tmp.append(close_price[i])
		ext.append((min(tmp), max(tmp)))
		i+=1

	x, y = 0, j
	while(x < y):
		# exit condition
		if (position[1] > 0 and delta[x] >= delta_max):
			tmp = Decimal(close_price[x] - position[1])/Decimal(position[1])
			if(position[0] == "short"):
				tmp = tmp * (-1)
			tmp = 100 * tmp
			result = result + tmp
			# reset params
			position, order = ["", 0], 0
			#print("closed position at " + str(close_price[x]) + " with percentage profit or loss of: " + str(tmp) + " ; date: " + str(date[x]))
			count+=1

		# order condition
		elif (order == 0 and delta[x] <= delta_min):
			#print("interest point spotted on the:", date[x])
			#print("delta:", delta[x])
			order = 1

		# expanding out of min delta
		elif (order == 1):
			
			# long entry
			if (close_price[x] == ext[x][1]):

				#flip position / stop loss
				if (position[0] == "short"):
					tmp = -100 * (Decimal(close_price[x] - position[1])/Decimal(position[1]))
					#print("short position stopped out at " + str(close_price[x]) + " with percentage loss of: " + str(tmp) + " ; date: " + str(date[x]))
					count+=1
					result = result + tmp
					position = ["long", close_price[x]]
					#print("long position opened at " + str(close_price[x]) + " ; date: " + str(date[x]))

				#no positions yet, time to long
				elif (position[1] == 0):
					position = ["long", close_price[x]]
					#print("long position opened at " + str(close_price[x]) + " ; date: " + str(date[x]))

			# short entry
			if (close_price[x] == ext[x][0]):

				#flip position / stop loss
				if (position[0] == "long"):
					tmp = 100 * (Decimal(close_price[x] - position[1])/Decimal(position[1]))
					#print("long position stopped out at " + str(close_price[x]) + " with percentage loss of: " + str(tmp) + " ; date: " + str(date[x]))
					count+=1
					result = result + tmp
					position = ["short", close_price[x]]
					#print("short position opened at " + str(close_price[x]) + " ; date: " + str(date[x]))

				#no positions yet, time to long
				elif (position[1] == 0):
					position = ["short", close_price[x]]
					#print("short position opened at " + str(close_price[x]) + " ; date: " + str(date[x]))
		x+=1
	return(float(result), count)
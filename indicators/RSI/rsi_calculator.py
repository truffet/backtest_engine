from decimal import *

#Calculating the Relative Strength Index
def relative_strength_index(RS):
	i, j = 0, len(RS)
	RSI = []
	while(i < j):
		if (RS[i] == None):
			RSI.append(None)
		else:
			RSI.append(float(100 - (100 / (1 + Decimal(RS[i])))))
		i+=1
	return(RSI)

#Calculating the Relative Strength
def relative_strength(avgUp, avgDown):
	i, j = 0, len(avgUp)
	RS = []
	while(i < j):
		if (avgUp[i] == None or avgDown[i] == 0):
			RS.append(None)
		else:
			RS.append(Decimal(avgUp[i])/Decimal(avgDown[i]))
		i+=1
	return(RS)

#Calculating the Period Average Gain
def average_gain(upMoves, downMoves, i, period):
	x, y = i, i-period+1#
	up, down = 0, 0
	while(x > y):
		if (upMoves[x] != None):
			up = up + upMoves[x]
			down = down + downMoves[x]
		else:
			if (y < 0):
				return(None, None)
			y-=1
		x-=1
	return(Decimal(up)/Decimal(period)), float((Decimal(down)/Decimal(period)))

#Averaging the Advances and Declines
def avgMove(period, upMoves, downMoves):
	i, j = 0, len(upMoves)
	avgUp = []
	avgDown = []
	while(i < j):
		if (upMoves[i] == None or i < (period-1)):#
			avgUp.append(None)
			avgDown.append(None)
		else:
			tmp = average_gain(upMoves, downMoves, i, period)
			avgUp.append(tmp[0])
			avgDown.append(tmp[1])
		i+=1
	return(avgUp, avgDown)

#Calculating Up Moves and Down Moves
def updown_calculator(data):
	i, j = 0, len(data)
	upMoves, downMoves = [], []
	up, down = 0, 0
	while(i<j):
		if (data[i][0] == None):
			upMoves.append(None)
			downMoves.append(None)
		else:	
			count = 1
			while(i-count > 0 and data[i-count][0] == None):
				count+=1
			if (i-count < 0):
				upMoves.append(None)
				downMoves.append(None)
			else:
				close = data[i][0]
				prev_close = data[i-count][0]
				if (close == prev_close):
					up = 0
					down = 0
				elif (close > prev_close):
					up = close - prev_close
					down = 0 
				else:
					up = 0 
					down = prev_close - close
				upMoves.append(up)
				downMoves.append(down)
		i+=1
	return(upMoves, downMoves)

#rsi calculator
def rsi_calculator(period, data):
	upMoves, downMoves = updown_calculator(data)
	avgUp, avgDown = avgMove(period, upMoves, downMoves)
	RS = relative_strength(avgUp, avgDown)
	RSI = relative_strength_index(RS)
	return(RSI)
from fetch_data import fetch_data
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from decimal import *

def add_drawing(fig, date, score, name, row, col):
	fig.add_trace(go.Scatter(x=date, y=score, mode='lines', name=name), row=row, col=col)
	fig.update_yaxes(type="log", row=row, col=col)

def add_drawing_nolog(fig, date, score, name, row, col):
	fig.add_trace(go.Scatter(x=date, y=score, mode='lines', name=name), row=row, col=col)

def range_value(value):
	result = 100 - (Decimal(100)/Decimal(1+value))
	return(result)

timeframe = ['D']
i, j = 0, len(timeframe)

while (i < j):
	
	ohlc = fetch_data('*', (timeframe[i]))
	Delta = fetch_data('*', ('delta_' + timeframe[i]))
	PSMA = fetch_data('*', ('PEMA_' + timeframe[i]))
	
	#deleting data pre-2016
	while((ohlc[0][5].strftime("%Y/%m/%d, %H:%M:%S")).startswith('2016') != True):
		Delta.pop(0)
		ohlc.pop(0)
		PSMA.pop(0)

	size = len(ohlc)
	open_price, high_price, low_price, close_price, volume, date = zip(*ohlc)

	#display test

	fig = make_subplots(rows=2, cols=1, shared_xaxes=True)

	#display ohlc
	#fig.add_trace(go.Ohlc(x=date, open=open_price, high=high_price, low=low_price, close=close_price), row=3, col=1)
	add_drawing_nolog(fig, date, close_price, 'price close', 1, 1)


	### DELTA ###
	delta, mini, maxi = zip(*Delta)
	add_drawing_nolog(fig, date, delta, 'delta', 2, 1)

	### PSMA ###
	sma20, sma40, sma60, sma80, sma100, sma120, sma140, sma160, sma180, sma200, date = zip(*PSMA)
	add_drawing_nolog(fig, date, sma200, 'sma200', 1, 1)

	#remove range slider for ohlc and show fig
	fig.update(layout_xaxis_rangeslider_visible=False)
	fig.show()

	i+=1

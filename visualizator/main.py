from fetch_data import fetch_data
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from decimal import *

def add_drawing(fig, date, score, name, row, col):
	fig.add_trace(go.Scatter(x=date, y=score, mode='lines', name=name), row=row, col=col)
	fig.update_yaxes(type="log", row=row, col=col)

def range_value(value):
	result = 100 - (Decimal(100)/Decimal(1+value))
	return(result)

timeframe = ['D']
i, j = 0, len(timeframe)

while (i < j):
	
	PSMA = fetch_data('*', ('PSMA_' + timeframe[i]))
	Price = fetch_data('*', (timeframe[i]))
	size = len(Price)
	open_price, high_price, low_price, close_price, volume, date = zip(*Price)
	
	#display test
	fig = make_subplots(rows=3, cols=1, shared_xaxes=True)
	fig2 = make_subplots(rows=1, cols=1, shared_xaxes=True) #########################
	#display ohlc
	#fig.add_trace(go.Ohlc(x=date, open=open_price, high=high_price, low=low_price, close=close_price), row=1, col=1)
	
	#display close price
	add_drawing(fig, date, close_price, 'close price', 1, 1)
	
	step = 5
	data = list(zip(*PSMA))
	x, y = 0, len(data)-1
	while(x < y):
		#display SMA
		add_drawing(fig, date, data[x], str((x+1)*step), 2, 1)
		add_drawing(fig2, date, data[x], str((x+1)*step), 1, 1) ##########################
		x+=1

	delta = []
	x, y = 0, len(PSMA)
	while(x < y):
		tmp = list(PSMA[x])
		tmp.pop()
		if (tmp.count(None) > 0):
			delta.append(None)
		else:
			#d = Decimal(min(tmp))/Decimal(max(tmp))
			d = 1 - (Decimal(min(tmp))/Decimal(max(tmp)))
			delta.append(float(d)*100)
		x+=1
	#display delta
	add_drawing(fig, date, delta, 'delta', 3, 1)

	#remove range slider for ohlc and add title
	fig.update(layout_xaxis_rangeslider_visible=False)
	fig.update_layout(title_text="Simple Moving Average")
	fig.show()
	fig2.show()#################

	i+=1

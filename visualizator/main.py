from fetch_data import fetch_data
import plotly.graph_objects as go
from decimal import *

def add_drawing(fig, date, score, name):
	fig.add_trace(go.Scatter(x=date, y=score,
                    mode='lines',
                    name=name))

periods = ['4H','D']
i, j = 0, len(periods)

while (i < j):
	
	PSMA = fetch_data('*', ('PSMA_' + periods[i]))
	VSMA = fetch_data('*',('VSMA_' + periods[i]))
	Price = fetch_data('*', (periods[i]))
	size = len(Price)
	PSMA10, PSMA20, PSMA50, PSMA100, PSMA200, date = zip(*PSMA)
	open_price, high_price, low_price, close_price, volume, date = zip(*Price)
	#display test
	fig = go.Figure(
		layout=go.Layout(
        	title=go.layout.Title(text=("Price Simple Moving Average"))
    	),
    	data=[go.Ohlc(x=date, open=open_price, high=high_price, low=low_price, close=close_price)]
   	)
	add_drawing(fig, date, PSMA10, 'PSMA10')
	add_drawing(fig, date, PSMA20, 'PSMA20')
	add_drawing(fig, date, PSMA50, 'PSMA50')
	add_drawing(fig, date, PSMA100, 'PSMA100')
	add_drawing(fig, date, PSMA200, 'PSMA200')
	fig.show()
	i+=1
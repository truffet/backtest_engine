from fetch_data import fetch_data
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from decimal import *

def range_value(value):
	result = 100 - (100/Decimal(1+value))
	return(result)

def add_drawing(fig, date, score, name, row, col):
	fig.add_trace(go.Scatter(x=date, y=score, mode='lines', name=name), row=row, col=col)
	fig.update_yaxes(type="log", row=row, col=col)

timeframe = ['D']
i, j = 0, len(timeframe)

while (i < j):
	
	PSMA = fetch_data('*', ('PdSMA_' + timeframe[i]))

	size = len(PSMA)
	#OHLCVD to compare (index)
	subject = size-1-1-61 #13/03/2020
	while(subject > 0 and PSMA[subject].count(None) > 0):
		subject-=1
	
	score = []
	smooth = []
	date = []
	x, y = 0, len(PSMA)
	
	#check if subject is valid
	if (subject <= 0):
		print("impossible to find suitable subject")
		y = 0

	while(x < subject):
		b = len(PSMA[x])-1
		if (PSMA[x].count(None) > 0):
			score.append(None)
			smooth.append(None)
		else:
			tmp, a = 0, 0
			while (a < b):
				tmp = tmp + max(PSMA[x][a],PSMA[subject][a]) - min(PSMA[x][a],PSMA[subject][a])
				a+=1
			tmp = float(Decimal(tmp)/Decimal(b))
			score.append(tmp)
			smooth.append(float(range_value(tmp)))
		date.append(PSMA[x][b])
		x+=1


	#display test
	fig = make_subplots(rows=2, cols=1, shared_xaxes=True)
	add_drawing(fig, date, score, 'score', 1, 1)
	add_drawing(fig, date, smooth, 'smooth', 2, 1)
	title = "Index Indicator for the " + PSMA[subject][len(PSMA[subject])-1].strftime("%m/%d/%Y")
	fig.update_layout(title_text=title)
	fig.show()
	i+=1
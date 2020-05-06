from fetch_data import fetch_data
import plotly.graph_objects as go
from decimal import *

def range_value(value):
	ranged_value = 100 - (100/Decimal(1+value))
	return(ranged_value)

def add_drawing(fig, date, score, name):
	fig.add_trace(go.Scatter(x=date, y=score,
                    mode='markers',
                    name=name))

#periods = ['1H', '4H', '24H']
periods = ['24H']
i, j = 0, len(periods)

while (i < j):
	
	dVolMA = fetch_data('*', ('dVolumeMA_' + periods[i]))
	dSMAs = fetch_data('*',('dSMAs_' + periods[i]))
	size = len(dVolMA)
	subject = size-1-52 #using last available period
	score_list = {
		'dVolMA_score': [],
		'dSMA10_score': [],
		'dSMA20_score': [],
		'dSMA50_score': [],
		'dSMA100_score': [],
		'dSMA200_score': [],
		'combined': [],
		'date': []
	}
	x = 0
	success, failure = 0, 0

	while (x < subject):
		if (dVolMA[x][0] == None or dSMAs[x][0] == None or dSMAs[x][1] == None or dSMAs[x][2] == None or dSMAs[x][3] == None or dSMAs[x][4] == None):
			failure+=1
			score_list['dVolMA_score'].append(None)
			score_list['dSMA10_score'].append(None)
			score_list['dSMA20_score'].append(None)
			score_list['dSMA50_score'].append(None)
			score_list['dSMA100_score'].append(None)
			score_list['dSMA200_score'].append(None)
			score_list['combined'].append(None)
		else:
			success+=1

			#100-(100/(1+positive diff)) and the postive diff = max - min , this is inspired of the RSI calculation method to keep values ranged between 0 and 100
			score_list['dVolMA_score'].append(range_value(max([dVolMA[x][0], dVolMA[subject][0]])-min([dVolMA[x][0], dVolMA[subject][0]])))
			score_list['dSMA10_score'].append(range_value(max([dSMAs[x][0], dSMAs[subject][0]])-min([dSMAs[x][0], dSMAs[subject][0]])))
			score_list['dSMA20_score'].append(range_value(max([dSMAs[x][1], dSMAs[subject][1]])-min([dSMAs[x][1], dSMAs[subject][1]])))
			score_list['dSMA50_score'].append(range_value(max([dSMAs[x][2], dSMAs[subject][2]])-min([dSMAs[x][2], dSMAs[subject][2]])))
			score_list['dSMA100_score'].append(range_value(max([dSMAs[x][3], dSMAs[subject][3]])-min([dSMAs[x][3], dSMAs[subject][3]])))
			score_list['dSMA200_score'].append(range_value(max([dSMAs[x][4], dSMAs[subject][4]])-min([dSMAs[x][4], dSMAs[subject][4]])))
			combined = (score_list['dVolMA_score'][x] + score_list['dSMA10_score'][x] + score_list['dSMA20_score'][x] + score_list['dSMA50_score'][x] + score_list['dSMA100_score'][x] + score_list['dSMA200_score'][x]) / 6
			score_list['combined'].append(combined)
		score_list['date'].append(dVolMA[x][1])
		x+=1

	print('Total:', (subject - 1))
	print('Miss:', failure)
	print('Success:', success)


	#display test
	fig = go.Figure(
		layout=go.Layout(
        	title=go.layout.Title(text=("Index Indicator for the " + dVolMA[subject][1].strftime("%m/%d/%Y")))
    	)
    )
	add_drawing(fig, score_list['date'], score_list['combined'], 'combined')
	add_drawing(fig, score_list['date'], score_list['dVolMA_score'], 'dVolMA_score')
	add_drawing(fig, score_list['date'], score_list['dSMA10_score'], 'dSMA10_score')
	add_drawing(fig, score_list['date'], score_list['dSMA20_score'], 'dSMA20_score')
	add_drawing(fig, score_list['date'], score_list['dSMA50_score'], 'dSMA50_score')
	add_drawing(fig, score_list['date'], score_list['dSMA100_score'], 'dSMA100_score')
	add_drawing(fig, score_list['date'], score_list['dSMA200_score'], 'dSMA200_score')
	fig.show()
	i+=1
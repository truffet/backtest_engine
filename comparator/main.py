from fetch_data import fetch_data
import plotly.graph_objects as go
from decimal import *

def range_value(value):
	result = 100 - (100/Decimal(1+value))
	return(result)

def add_drawing(fig, date, score, name):
	fig.add_trace(go.Scatter(x=date, y=score,
                    mode='markers',
                    name=name))

periods = ['4H','D']
i, j = 0, len(periods)

while (i < j):
	
	PSMA = fetch_data('*', ('PdSMA_' + periods[i]))
	VSMA = fetch_data('*',('VdSMA_' + periods[i]))

	size = len(PSMA)
	subject = size-1-1 #OHLCVD to compare (index)
	score_list = {
		'VSMA10_score': [],
		'VSMA20_score': [],
		'VSMA50_score': [],
		'VSMA100_score': [],
		'VSMA200_score': [],
		'PSMA10_score': [],
		'PSMA20_score': [],
		'PSMA50_score': [],
		'PSMA100_score': [],
		'PSMA200_score': [],
		'combined_simple': [],
		'combined_range': [],
		'date': []
	}
	x = 0
	success, failure = 0, 0

	if (VSMA[subject][0] == None or VSMA[subject][1] == None or VSMA[subject][2] == None or VSMA[subject][3] == None or VSMA[subject][4] == None or PSMA[subject][0] == None or PSMA[subject][1] == None or PSMA[subject][2] == None or PSMA[subject][3] == None or PSMA[subject][4] == None):
		print('Fatal Error, invalid subject. Please debug!')
	else:
		while (x < subject):
			if (VSMA[x][0] == None or VSMA[x][1] == None or VSMA[x][2] == None or VSMA[x][3] == None or VSMA[x][4] == None or PSMA[x][0] == None or PSMA[x][1] == None or PSMA[x][2] == None or PSMA[x][3] == None or PSMA[x][4] == None):
				failure+=1
				score_list['VSMA10_score'].append(None)
				score_list['VSMA20_score'].append(None)
				score_list['VSMA50_score'].append(None)
				score_list['VSMA100_score'].append(None)
				score_list['VSMA200_score'].append(None)
				score_list['PSMA10_score'].append(None)
				score_list['PSMA20_score'].append(None)
				score_list['PSMA50_score'].append(None)
				score_list['PSMA100_score'].append(None)
				score_list['PSMA200_score'].append(None)
				score_list['combined_simple'].append(None)
				score_list['combined_range'].append(None)
			else:
				success+=1
				score_list['VSMA10_score'].append((max([VSMA[x][0], VSMA[subject][0]])-min([VSMA[x][0], VSMA[subject][0]])))
				score_list['VSMA20_score'].append((max([VSMA[x][1], VSMA[subject][1]])-min([VSMA[x][1], VSMA[subject][1]])))
				score_list['VSMA50_score'].append((max([VSMA[x][2], VSMA[subject][2]])-min([VSMA[x][2], VSMA[subject][2]])))
				score_list['VSMA100_score'].append((max([VSMA[x][3], VSMA[subject][3]])-min([VSMA[x][3], VSMA[subject][3]])))
				score_list['VSMA200_score'].append((max([VSMA[x][4], VSMA[subject][4]])-min([VSMA[x][4], VSMA[subject][4]])))
				score_list['PSMA10_score'].append((max([PSMA[x][0], PSMA[subject][0]])-min([PSMA[x][0], PSMA[subject][0]])))
				score_list['PSMA20_score'].append((max([PSMA[x][1], PSMA[subject][1]])-min([PSMA[x][1], PSMA[subject][1]])))
				score_list['PSMA50_score'].append((max([PSMA[x][2], PSMA[subject][2]])-min([PSMA[x][2], PSMA[subject][2]])))
				score_list['PSMA100_score'].append((max([PSMA[x][3], PSMA[subject][3]])-min([PSMA[x][3], PSMA[subject][3]])))
				score_list['PSMA200_score'].append((max([PSMA[x][4], PSMA[subject][4]])-min([PSMA[x][4], PSMA[subject][4]])))

				combined_simple = Decimal(score_list['VSMA10_score'][x] + score_list['VSMA20_score'][x]*2 + score_list['VSMA50_score'][x]*5 + score_list['VSMA100_score'][x]*10 + score_list['VSMA200_score'][x]*20 + score_list['PSMA10_score'][x] + score_list['PSMA20_score'][x]*2 + score_list['PSMA50_score'][x]*5 + score_list['PSMA100_score'][x]*10 + score_list['PSMA200_score'][x]*20) / 76
				combined_range = range_value(combined_simple)
				score_list['combined_simple'].append(combined_simple)
				score_list['combined_range'].append(combined_range)

			score_list['date'].append(VSMA[x][5])
			x+=1

		print('Total:', (subject - 1))
		print('Miss:', failure)
		print('Success:', success)


		#display test
		fig = go.Figure(
			layout=go.Layout(
        		title=go.layout.Title(text=("Index Indicator for the " + VSMA[subject][5].strftime("%m/%d/%Y")))
    		)
    	)
		add_drawing(fig, score_list['date'], score_list['combined_simple'], 'combined_simple')
		add_drawing(fig, score_list['date'], score_list['combined_range'], 'combined_range')
		add_drawing(fig, score_list['date'], score_list['VSMA10_score'], 'VSMA10_score')
		add_drawing(fig, score_list['date'], score_list['VSMA20_score'], 'VSMA20_score')
		add_drawing(fig, score_list['date'], score_list['VSMA50_score'], 'VSMA50_score')
		add_drawing(fig, score_list['date'], score_list['VSMA100_score'], 'VSMA100_score')
		add_drawing(fig, score_list['date'], score_list['VSMA200_score'], 'VSMA200_score')

		add_drawing(fig, score_list['date'], score_list['PSMA10_score'], 'PSMA10_score')
		add_drawing(fig, score_list['date'], score_list['PSMA20_score'], 'PSMA20_score')
		add_drawing(fig, score_list['date'], score_list['PSMA50_score'], 'PSMA50_score')
		add_drawing(fig, score_list['date'], score_list['PSMA100_score'], 'PSMA100_score')
		add_drawing(fig, score_list['date'], score_list['PSMA200_score'], 'PSMA200_score')
		fig.show()
	i+=1
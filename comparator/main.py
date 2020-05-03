from fetch_data import fetch_data
import plotly.graph_objects as go


#periods = ['1H', '4H', '24H']
periods = ['24H']
i, j = 0, len(periods)

while (i < j):
	dVolMA = fetch_data('*', ('dVolumeMA_' + periods[i]))
	dSMAs = fetch_data('*',('dSMAs_' + periods[i]))
	size = len(dVolMA)
	subject = size-1-4 #just for test purposes to get bottom
	score_list = []
	x = 0
	count = 0
	while (x < subject):
		date = dVolMA[x][1]
		if dVolMA[x][0] != None:
			score = abs(dVolMA[subject][0] - dVolMA[x][0])
			if (dSMAs[x][0] != None and dSMAs[x][1] != None and dSMAs[x][2] != None and dSMAs[x][3] != None and dSMAs[x][4] != None):
				score = score + abs(dSMAs[subject][0] - dSMAs[x][0]) + abs(dSMAs[subject][1] - dSMAs[x][1]) + abs(dSMAs[subject][2] - dSMAs[x][2]) + abs(dSMAs[subject][3] - dSMAs[x][3]) + abs(dSMAs[subject][4] - dSMAs[x][4])
				score_list.append((score, dVolMA[x][1]))
			else:
				count+=1
		else:
			count+=1
		x+=1
	print('Total:', (subject - 1))
	print('Miss:', count)
	print('Success:', len(score_list))
	score, date = zip(*score_list)

	#display test
	fig = go.Figure(
    	data=[go.Scatter(x=date, y=score, mode="lines")],
    	layout=go.Layout(
        	title=go.layout.Title(text=("Index Indicator for the " + dVolMA[subject][1].strftime("%m/%d/%Y")))
    	)
	)
	fig.show()

	i+=1
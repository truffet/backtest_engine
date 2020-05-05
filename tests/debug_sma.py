import mysql.connector
import plotly.graph_objects as go

def fetch_data(what, where):
	#connect to database
	connection = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="bodyboard",
		database="kraken_spot_btcusd"
	)
	connection.autocommit = True
	mycursor = connection.cursor()
	query = "SELECT " + what + " FROM " + where
	mycursor.execute(query)
	#list of tuples
	myresult = mycursor.fetchall()
	return(myresult)


dSMA = fetch_data('*', 'dSMAs_24H')
SMA = fetch_data('*', 'SMAs_24H')
CD = fetch_data('close, date', '24H')
print("fetched data..")

i, j = 0, len(SMA)
sma_none, sma_zero, dsma_none, close_zero = 0, 0, 0, 0
while (i < j):
	if (SMA[i][0] == None or SMA[i][1] == None or SMA[i][2] == None or SMA[i][3] == None or SMA[i][4] == None):
		sma_none+=1
	if (SMA[i][0] == 0 or SMA[i][1] == 0 or SMA[i][2] == 0 or SMA[i][3] == 0 or SMA[i][4] == 0):
		sma_zero+=1
	if (dSMA[i][0] == None or dSMA[i][1] == None or dSMA[i][2] == None or dSMA[i][3] == None or dSMA[i][4] == None):
		dsma_none+=1
	if(CD[i][0] == None):
		close_zero+=1
	i+=1
print("SMA None:", sma_none)
print("SMA Zero:", sma_zero)
print("dSMA None:", dsma_none)
print("Close Zero:", close_zero)

i, j = 0, len(CD)
while(i < j):
	if(CD[i][0] == None):
		print("None close data:", CD[i])
	elif (CD[i][0] == 0):
		print("Houston we have a problem:", CD[i])
	i+=1

#display test
sma10, sma20, sma50, sma100, sma200, date = zip(*SMA)
close, date2 = zip(*CD) 

# Create traces
fig = go.Figure()
fig.add_trace(go.Scatter(x=date, y=sma10,
                    mode='lines',
                    name='sma10'))
fig.add_trace(go.Scatter(x=date, y=sma20,
                    mode='lines',
                    name='sma20'))
fig.add_trace(go.Scatter(x=date, y=sma50,
                    mode='lines', 
                    name='sma50'))
fig.add_trace(go.Scatter(x=date, y=sma100,
                    mode='lines', 
                    name='sma100'))
fig.add_trace(go.Scatter(x=date, y=sma200,
                    mode='lines', 
                    name='sma200'))
fig.add_trace(go.Scatter(x=date2, y=close,
                    mode='lines', 
                    name='close price'))

#fig.show()

dsma10, dsma20, dsma50, dsma100, dsma200, date = zip(*dSMA)
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=date, y=dsma10,
                    mode='lines',
                    name='dsma10'))
fig2.add_trace(go.Scatter(x=date, y=dsma20,
                    mode='lines',
                    name='dsma20'))
fig2.add_trace(go.Scatter(x=date, y=dsma50,
                    mode='lines', 
                    name='dsma50'))
fig2.add_trace(go.Scatter(x=date, y=dsma100,
                    mode='lines', 
                    name='dsma100'))
fig2.add_trace(go.Scatter(x=date, y=dsma200,
                    mode='lines', 
                    name='dsma200'))

fig2.show()
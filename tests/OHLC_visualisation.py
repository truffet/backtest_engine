import mysql.connector
import pandas as pd
import plotly.graph_objects as go

def fetch_data():
	#connect to database
	connection = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="bodyboard",
		database="kraken_spot_btcusd"
	)
	connection.autocommit = True
	mycursor = connection.cursor()
	mycursor.execute("SELECT * FROM 24H")
	#list of tuples
	myresult = mycursor.fetchall()
	return(myresult)

data = fetch_data()

df = pd.DataFrame(data, columns = ['open', 'high', 'low', 'close', 'volume', 'date'])
print(df)

# Obtain data from the data frame
fig = go.Figure(
	data=go.Ohlc(
		x=df['date'],
		open=df['open'],
		high=df['high'],
		low=df['low'],
		close=df['close']
	)
)

# Add title and annotations
fig.update_layout(
	title_text='Visualisation OHLC test',
	title={
		'y':1,
		'x':1,
		'xanchor': 'center',
		'yanchor': 'top'
	},
	xaxis_rangeslider_visible=True, 
	xaxis_title="Time", 
	yaxis_title="Price"
)


fig.show()
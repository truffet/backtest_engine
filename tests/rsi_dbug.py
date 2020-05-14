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


RSI = fetch_data('*', 'RSI_24H')
print("fetched data..")
#display test
rsi, date = zip(*RSI) 

# Create traces
fig = go.Figure()
fig.add_trace(go.Scatter(x=date, y=rsi,
                    mode='lines',
                    name='rsi14'))
fig.show()
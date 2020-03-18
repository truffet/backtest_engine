import mysql.connector

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
	mycursor.execute("SELECT unix_time, price, volume FROM tradesHistory limit 10000")
	#list of tuples
	myresult = mycursor.fetchall()
	output = []
	for row in myresult:
		output.append((row[0],float(row[1]), float(row[2])))
	return(output)

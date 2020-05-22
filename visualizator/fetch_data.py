import mysql.connector

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
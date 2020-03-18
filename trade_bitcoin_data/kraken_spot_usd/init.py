import mysql.connector

def connect_to_user():
	#connect to mysql root user session
	myuser = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="bodyboard"
	)
	myuser.autocommit = True
	#return
	return(myuser)

def connect_to_db():
	#connect to database
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="bodyboard",
		database="kraken_spot_btcusd"
	)
	mydb.autocommit = True
	#return
	return(mydb)


def create_database():
	#connect to mysql root user session
	m = connect_to_user()
	mycursor = m.cursor()
	#create database
	mycursor.execute("CREATE DATABASE IF NOT EXISTS kraken_spot_btcusd")
	#print databases
	mycursor.execute("SHOW DATABASES")


def create_tables():

	#connect to database
	m = connect_to_db()
	mycursor= m.cursor()
	#create tables
	mycursor.execute("CREATE TABLE IF NOT EXISTS tradesHistory (unix_time BIGINT(20) UNSIGNED, price DECIMAL(15,5) UNSIGNED, volume DECIMAL(16,8) UNSIGNED, side BOOLEAN, order_type BOOLEAN)")
	mycursor.execute("CREATE TABLE IF NOT EXISTS timeCursor (since BIGINT(20) UNSIGNED)")


def setup_env():
	print("\nSetting up env..")
	create_database()
	create_tables()


# Explaining data types:

# BOOLEAN: 0 False | 1 True
# side: 0 Buy | 1 Sell
# type: 0 Market | 1 Limit

# BIGINT
# unix_time: API result * 100 000 000 / example: 1559350785.29700000 
# since: timestamp in nanoseconds / example 1559350785297011117

# DECIMAL
# volume in bitcoin with 8 decimal point precision because satoshi is max limit
# price in dollars with 5 decimal point precision
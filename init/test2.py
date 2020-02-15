import mysql.connector

def setup_env():

	#connect to mysql root user session
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="bodyboard"
		)

	#create database
	mycursor = mydb.cursor()
	mycursor.execute("CREATE DATABASE IF NOT EXISTS bitmex_perps")

	#print databases
	mycursor.execute("SHOW DATABASES")
	for x in mycursor:
		print(x)

	#connect to database
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="bodyboard",
		database="bitmex_perps"
		)

	#create tables
	mycursor = mydb.cursor()
	#mycursor.execute("DROP TABLE tradesHistory")

	mycursor.execute("CREATE TABLE IF NOT EXISTS tradesHistory (tradeTime DATETIME(3), side VARCHAR(255), size BIGINT(255), price FLOAT(53), tickDirection VARCHAR(255), trdMatchID VARCHAR(255), grossValue FLOAT(53), homeNotional FLOAT(53), foreignNotional FLOAT(53))")
	mycursor.execute("CREATE TABLE IF NOT EXISTS timeCursor (tradeTime VARCHAR(255), trdMatchID VARCHAR(255))")

	#print tables
	mycursor.execute("SHOW TABLES")
	for x in mycursor:
		print(x)

setup_env()
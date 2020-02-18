import mysql.connector

def connect_to_user():
	#connect to mysql root user session
	myuser = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="bodyboard"
	)
	myuser.autocommit = True
	#print success
	print("\nConnected to root user")
	#return
	return(myuser)

def connect_to_db():
	#connect to database
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="bodyboard",
		database="bitmex_perps"
	)
	mydb.autocommit = True
	#print success
	print("\nConnected to database bitmex_perps")
	#return
	return(mydb)


def create_database():
	#connect to mysql root user session
	m = connect_to_user()
	mycursor = m.cursor()
	#create database
	mycursor.execute("CREATE DATABASE IF NOT EXISTS bitmex_perps")
	#print databases
	mycursor.execute("SHOW DATABASES")
	print("\nList of databases:")
	for x in mycursor:
		print(x)


def create_tables():

	#connect to database
	m = connect_to_db()
	mycursor= m.cursor()
	#create tables
	mycursor.execute("CREATE TABLE IF NOT EXISTS tradesHistory (tradeTime DATETIME(6), side VARCHAR(255), size BIGINT(255), price FLOAT(53), tickDirection VARCHAR(255), trdMatchID VARCHAR(255), grossValue FLOAT(53), homeNotional FLOAT(53), foreignNotional FLOAT(53))")
	mycursor.execute("CREATE TABLE IF NOT EXISTS timeCursor (tradeTime VARCHAR(255), trdMatchID VARCHAR(255))")
	#print tables
	print("\nList of tables:")
	mycursor.execute("SHOW TABLES")
	for x in mycursor:
		print(x)


def setup_env():
	print("\nSetting up env..")
	create_database()
	create_tables()
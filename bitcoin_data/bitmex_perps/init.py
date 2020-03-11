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
		database="bitmex_perps"
	)
	mydb.autocommit = True
	#return
	return(mydb)


def create_database():
	#connect to mysql root user session
	m = connect_to_user()
	mycursor = m.cursor()
	#create database
	mycursor.execute("CREATE DATABASE IF NOT EXISTS bitmex_perps")


def create_tables():

	#connect to database
	m = connect_to_db()
	mycursor= m.cursor()
	#create tables
	mycursor.execute("CREATE TABLE IF NOT EXISTS tradesHistory (tradeTime DATETIME(6), side VARCHAR(255), size BIGINT(255), price FLOAT(53), tickDirection VARCHAR(255), trdMatchID VARCHAR(255), grossValue FLOAT(53), homeNotional FLOAT(53), foreignNotional FLOAT(53))")
	mycursor.execute("CREATE TABLE IF NOT EXISTS timeCursor (tradeTime VARCHAR(255), trdMatchID VARCHAR(255))")


def setup_env():
	create_database()
	create_tables()
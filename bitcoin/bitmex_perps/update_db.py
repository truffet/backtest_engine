from get1000Trades import get1000Trades

import pyarrow as pa
import pandas as pd
import time
from init import connect_to_db

def is_empty_table(connection):
	mycursor = connection.cursor()

	mycursor.execute("INSERT INTO timeCursor (tradeTime, trdMatchID) VALUES ('test', 'test')")
	mycursor.execute("SELECT * FROM timeCursor")
	rowcount = len(mycursor.fetchall())
	if rowcount:
		print("timeCursor table is not empty")
		return(("",""))
	else:
		print("timeCursor table is empty")
		return(("",""))


def update():

	#connect to database and init cursor
	connection = connect_to_db()
	mycursor = connection.cursor()
	
	#fetch trades by blocks of 1000 in a loop 
	while (True):

		#test if we need to start from the beginning or last save, save result in tuple
		startingPoint = is_empty_table(connection)

		break;#to avoid infinite loop for test purposes
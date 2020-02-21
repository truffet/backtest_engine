from utils.get1000Trades import get1000Trades
from utils.add1000Trades import add1000Trades
from init import connect_to_db

import pyarrow as pa
import pandas as pd
from time import sleep


def last_save(connection):
	mycursor = connection.cursor()
	mycursor.execute("SELECT * FROM timeCursor")
	result_list = mycursor.fetchall()
	rowcount = len(result_list)
	if rowcount:
		return(result_list[0])
	else:
		return(("",""))


def update():

	#connect to database and init cursor
	connection = connect_to_db()
	mycursor = connection.cursor()

	#to prevent rare situation where there are 
	#more trades happening at the exact same moment than you can count (1000max) 
	start = 0

	#fetch trades by blocks of 1000 in a loop 
	while (True):

		#fetch last save or ("","") if empty
		startingPoint = last_save(connection)

		#fetch data from bitmex API
		response = get1000Trades(startingPoint[0], start)

		#handle responses:
		if (response[0] != 200):
			print("\nresponse: " + str(response))
			break
		else:
			size = len(response)
			#save data from bitmex api to database
			start = add1000Trades(response, connection, startingPoint, start)
			if (size < 1000):
				print("\nLess than a 1000 trades fetched, loading to database. Last response handled, end of update")
				break
		
		#wait 2 seconds to avoid api rate limit
		print("\n1000 trades batch fetched, loading to database...\nwaiting 2s before requesting more data...")
		sleep(2)

		#break;#to avoid infinite loop for test purposes
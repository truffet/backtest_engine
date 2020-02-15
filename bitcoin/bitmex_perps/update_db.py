from get1000Trades import get1000Trades
from init import setup_env

import pyarrow as pa
import pandas as pd
import time

def count_rows(con):
	cursor = con.cursor()
	count_rows = cursor.execute("SELECT COUNT(*) FROM timeCursor;")
	nb_of_rows = list(count_rows)[0][0]
	print("Number of rows in timeCursor: " + str(nb_of_rows))
	return (nb_of_rows)

def init_params(con):
	nb_of_rows = count_rows(con)
	if (nb_of_rows == 0):
		print("Table is empty, will start loading data from origin")
		return ("")
	else:
		print("Table is not empty, will start updating data from last saved point")
		query = "SELECT * FROM timeCursor;"
		df = con.select_ipc_gpu(query)
		print(df)
		return(str(df['tradeTime'][0]))

def add_row_to_table(row, con):
	print("Adding new row to tradesHistory")
	df = pd.DataFrame({"tradeTime": [row["timestamp"]], "symbol": [row["symbol"]], "side": [row["side"]], "size": [row["size"]], "price": [row["price"]], "tickDirection": [row["tickDirection"]], "trdMatchID": [row["trdMatchID"]], "grossValue": [row["grossValue"]], "homeNotional": [row["homeNotional"]], "foreignNotional": [row["foreignNotional"]]}, columns=['tradeTime', 'symbol', 'side', 'size', 'price', 'tickDirection', 'trdMatchID', 'grossValue', 'homeNotional', 'foreignNotional'])
	#print(df)
	con.load_table_columnar("tradesHistory", df, preserve_index=False)

def save_progress(row, con):
	print("Saving progress to timeCursor")
	#query = "DELETE FROM timeCursor"
	#cursor = con.cursor()
	#cursor.execute(query)

	df = pd.DataFrame({"tradeTime": str([row["timestamp"]]), "trdMatchID": str([row["trdMatchID"]])}, columns=['tradeTime', 'trdMatchID'])
	con.load_table_columnar("timeCursor", df, preserve_index=False)

def add_response_to_table(response, con):
	del response[0]
	size = len(response)
	i = 0
	while (i < size):
		add_row_to_table(response[i], con)
		i += 1
	save_progress(response[i-1], con)


#create user, database and tables for loading data. 
#then, assign connection in return of function
con = setup_env()


#fetch trades by blocks of 1000 or less 
while (True):

	#check if tables are empty or not and return start time
	startTime = init_params(con)
	
	#to avoid adding two times same entry (last previosu and first next)
	if startTime == "":
		startPoint = 0
	else:
		startPoint = 1

	#fetch data from bitmex API
	response = get1000Trades(startTime, startPoint)

	#handle responses:
	if (str(response).startswith("Error")):
		print(str(response))
		break
	elif (response[0] != 200):
		print(str(response))
		break
	else:
		add_response_to_table(response, con)
		#print(str(response))
		if (len(response) < 1000):
			print("Less than a 1000 trades fetched, loading to database. Last response handled, end of update")
			break
		print("1000 trades batch fetched, loading to database...\nwaiting 2s before requesting more data...")
		sleep(2)


#
# test code
#

#cursor = con.cursor()
#query = cursor.execute("SELECT * FROM timeCursor;")
#display = list(query)
#print("timeCursor table:\n" + str(display))
#print("timeCursor row count: " + str(cursor.rowcount))

#cursor = con.cursor()
#query = cursor.execute("SELECT * FROM tradesHistory;")
#display = list(query)
#print("tradesHistory table:\n" + str(display))
#print("tradesHistory row count: " + str(cursor.rowcount))
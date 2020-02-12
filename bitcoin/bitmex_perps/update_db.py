from get1000Trades import get1000Trades
from connect_to_db import connect_to_db
from init import setup_env

import pyarrow as pa
import pandas as pd

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
		query = "SELECT tradeTime FROM timeCursor"
		df = con.select_ipc_gpu(query)
		df.head()
		return("")

def add_row_to_table(row, con):
	print("Adding new row to tradesHistory")
	df = pd.DataFrame({"tradeTime": [row["timestamp"]], "symbol": [row["symbol"]], "side": [row["side"]], "size": [row["size"]], "price": [row["price"]], "tickDirection": [row["tickDirection"]], "trdMatchID": [row["trdMatchID"]], "grossValue": [row["grossValue"]], "homeNotional": [row["homeNotional"]], "foreignNotional": [row["foreignNotional"]]}, columns=['tradeTime', 'symbol', 'side', 'size', 'price', 'tickDirection', 'trdMatchID', 'grossValue', 'homeNotional', 'foreignNotional'])
	print(df)
	con.load_table_columnar("tradesHistory", df, preserve_index=False)

def save_progress(row, con):
	print("Saving progress to timeCursor")
	query = "DELETE FROM timeCursor;"
	con.execute(query)
	df = pd.DataFrame({"tradeTime": [row["timestamp"]], "trdMatchID": [row["trdMatchID"]]}, columns=['tradeTime', 'trdMatchID'])
	print(df)
	con.load_table_columnar("timeCursor", df, preserve_index=False)

def add_response_to_table(response, con):
	del response[0]
	size = len(response)
	while (size > 0):
		add_row_to_table(response[0], con)
		if (size == 1):
			save_progress(response[0], con)
		del response[0]
		size -=1


#create user, database and tables for loading data. 
#then, assign connection in return of function
con = setup_env()


#fetch trades by blocks of 1000 or less 
while (True):

	startTime = init_params(con)
	#fetch data from bitmex API
	response = get1000Trades(startTime)

	#handle responses:
	if (str(response).startswith("Error")):
		print(str(response))
		break
	elif (response[0] != 200):
		print(str(response))
		break
	else:
		#add_response_to_table(response, con)
		if (len(response) < 1000):
			print("Less than a 1000 trades fetched, loading to database. Last response handled, end of update")
			break
		print("1000 trades batch fetched, loading to database...")


#
# test code
#

cursor = con.cursor()
query = cursor.execute("SELECT * FROM timeCursor;")
display = list(query)
print("timeCursor table:\n" + str(display))

cursor = con.cursor()
query = cursor.execute("SELECT * FROM tradesHistory;")
display = list(query)
print("tradesHistory table:\n" + str(display))
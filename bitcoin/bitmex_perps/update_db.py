from get1000Trades import get1000Trades
from connect_to_db import connect_to_db
from init import setup_env


def count_rows(con):
	cursor = con.cursor()
	count_rows = cursor.execute("SELECT COUNT(*) FROM timeCursor;")
	nb_of_rows = list(count_rows)[0][0]
	print("Number of rows in timeCursor: " + str(nb_of_rows))
	return (nb_of_rows)


#connect to omnisci bitmex database
con = connect_to_db()

#create tables if they don't exist already
setup_env(con)

#calculate number of rows to see if fresh start or update needed
nb_of_rows = count_rows(con)

#init values for data fetching based on previous calculus
if (nb_of_rows == 0):
	print("Table is empty, will start loading data from origin")
	startTime = ""
	lastTradeID = ""
else:
	print("Table is not empty, will start updating data from last saved point")


#fetch trades by blocks of 1000 or less 
while (True):

	#fetch data from bitmex API
	response = get1000Trades(startTime, lastTradeID)
	print(str(response))

	#handle responses:
	if (str(response).startswith("Error")):
		print(str(response))
		break
	elif (len(response) < 1001):
		print("Less than a 1000 trades fetched, loading to database. Last response handled, end of update")
		break
	else:
		print("1000 trades batch fetched, loading to database...")
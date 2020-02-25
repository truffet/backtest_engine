from init import connect_to_db
from utils.getTrades import getTrades
from utils.addTrades import addTrades

from time import sleep
from ast import literal_eval
import signal


#signal handler to prevent interrupt in the middle of data saving
def signal_handler(signal, frame):
	global finish
	finish = True
#set var to determine if clean exit needed or not, by default False
finish = False
signal.signal(signal.SIGINT, signal_handler)


def last_save(connection):
	mycursor = connection.cursor()
	mycursor.execute("SELECT * FROM timeCursor")
	result_list = mycursor.fetchall()
	rowcount = len(result_list)
	if rowcount:
		return(result_list[0])
	else:
		return((0,))


def update():

	#connect to database and init cursor
	connection = connect_to_db()

	while (True):
		
		#clean interrupt
		if finish:
			print("\nupdate stopped cleanly :)")
			break

		#fetch saving point to pursue update
		since = last_save(connection)[0]
		print("\nfetched since from table: " + str(since))

		response = getTrades(since)

		#handle responses:
		if (response[0] != 200):
			print("\nresponse: " + str(response))
			break
		else:
			data = literal_eval(response[1])
			if (data['error']):
				print(data['error'])
				break
			else:
				#upload data from kraken to database
				addTrades(data, connection, since)
				#break

		#avoid API rate limit
		print("\nData fetched and stored.. waiting 3s before next call")	
		sleep(3)

	print("Finished uploading new data")
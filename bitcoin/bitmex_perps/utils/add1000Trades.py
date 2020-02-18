from datetime import datetime

def avoid_duplicates(response, startingPoint):
	i = 0
	j = len(response)
	#check if duplicates exists
	while i < j:
		if response[i]['trdMatchID'] == startingPoint[1]:
			break;
		else:
			i+=1
	#delete them
	if i != j:
		x = 0
		while x <= i:
			del response[0]
			x+=1		
	return(response)

def add_row(row, connection):
	mycursor = connection.cursor()
	query = "INSERT INTO tradesHistory (tradeTime, side, size, price, tickDirection, trdMatchID, grossValue, homeNotional, foreignNotional) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
	
	#add '000' to get microseconds format
	line = row['timestamp']
	index = line.find('Z')
	time = line[:index] + '000' + line[index:]

	values = (datetime.strptime(time, '%Y-%m-%dT%H:%M:%S.%fZ'), row['side'], row['size'], row['price'], row['tickDirection'], row['trdMatchID'], row['grossValue'], row['homeNotional'], row['foreignNotional'])
	mycursor.execute(query, values)


def upload_new_data(response, connection):
	i = 0
	j = len(response)
	#add data row by row
	while(i < j):
		add_row(response[i], connection)
		i+=1

	#return last row index
	return(j-1)

def save_progress(last, connection):
	mycursor = connection.cursor()

	#delete previous save point before inserting new one
	mycursor.execute("DELETE FROM timeCursor")

	#insert new save point
	query = "INSERT INTO timeCursor (tradeTime, trdMatchID) VALUES (%s, %s)"
	values = (last['timestamp'], last['trdMatchID'])
	mycursor.execute(query, values)


def add1000Trades(response, connection, startingPoint, start):
	#delete status code
	del response[0]
	#check for trades that are already saved in db (same datetime, different order issue)
	clean_response = avoid_duplicates(response, startingPoint)

	if (clean_response):
		#upload new data to tradesHistory db
		last = upload_new_data(clean_response, connection)
		#save progress to timeCursor db
		save_progress(clean_response[last], connection)
		return (0)
	else:
		return(start + 1)
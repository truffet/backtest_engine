def convert_data(unix_time, price, volume, side, order_type):
	new_unix_time = unix_time * 100000000
	new_price = float(price)
	new_volume = float(volume)
	if (side == "b"):
		new_side = 0
	else:
		new_side = 1
	if (order_type == "m"):
		new_order_type = 0
	else:
		new_order_type = 1
	return(new_unix_time, new_price, new_volume, new_side, new_order_type)

def add_row(row):
	return(convert_data(row[2], row[0], row[1], row[3], row[4]))


def upload_new_data(response, connection):
	data = response['result']
	i = 0
	j = len(data['XXBTZUSD'])
	values = []
	#add data row by row
	while(i < j):
		values.append(add_row(data['XXBTZUSD'][i]))
		i+=1

	#insert multiple rows into table
	mycursor = connection.cursor()
	query = "INSERT INTO tradesHistory (unix_time, price, volume, side, order_type) VALUES (%s, %s, %s, %s, %s)"
	mycursor.executemany(query, values)

	#return last for next update
	return(data['last'])

def save_progress(last, connection):
	mycursor = connection.cursor()

	#delete previous save point before inserting new one
	mycursor.execute("DELETE FROM timeCursor")

	#insert new save point
	query = "INSERT INTO timeCursor (since) VALUES (%s)"
	values = (last,)
	mycursor.execute(query, values)


def addTrades(response, connection, since):

	#upload new data
	last = upload_new_data(response, connection)
	#save progress to timeCursor db
	save_progress(last, connection)
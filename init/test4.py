import mysql.connector
import matplotlib.pyplot as plt

from datetime import datetime


def fetch_data():
	#connect to database
	connection = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="bodyboard",
		database="kraken_spot_btcusd"
	)
	connection.autocommit = True
	mycursor = connection.cursor()
	mycursor.execute("SELECT unix_time, price FROM tradesHistory limit 10000")
	#list of tuples
	myresult = mycursor.fetchall()
	output = []
	for row in myresult:
		output.append((row[0],float(row[1])))
	return(output)


def plot_scatter_data(output):

	size = len(output)
	i = 0
	x = []
	y = []

	while i < size:
		x.append(output[i][0])
		y.append(output[i][1])
		i+=1

	plt.plot(x, y, linewidth=0.2)
	#plt.scatter(x, y)

	plt.title('Data Visualization of BTCUSD Kraken spot')
	plt.ylabel('price')
	plt.xlabel('unix timestamp')
	plt.axis('tight')
	plt.show()


def main():
	output = fetch_data()
	plot_scatter_data(output)

main()
import mysql.connector

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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
	mycursor.execute("SELECT unix_time, price, volume, side FROM tradesHistory limit 1000")
	#list of tuples
	myresult = mycursor.fetchall()
	output = []
	for row in myresult:
		output.append((row[0],float(row[1]), float(row[2]), row[3]))
	return(output)


def price_time_volume_graph(output):
	size = len(output)
	i = 0
	x = []
	y = []
	z = []
	w = []

	while i < size:
		x.append(output[i][0])
		y.append(output[i][1])
		z.append(output[i][2])
		w.append(output[i][3])
		i+=1

	fig = plt.figure()
	ax = plt.axes(projection="3d")
	ax.set_title('Data Visualization of BTCUSD Kraken spot')
	ax.set_xlabel('nanosecond timestamp')
	ax.set_ylabel('price')
	ax.set_zlabel('volume')
	#ax.scatter(x, y, z, s=3, c='green', cmap='hsv')
	#ax.plot_trisurf(x, y, z, cmap='hsv')
	#ax.plot(x, y, z, zdir=z, color='green')
	for xx,yy,zz,ww in zip(x,y,z,w):
		if ww:
			color = '#F09C56'
		else:
			color = '#2AA2C7'
		ax.plot([xx,xx],[yy,yy],[0,zz], '-', color=color)
	plt.show()


def main():
	output = fetch_data()
	price_time_volume_graph(output)

main()

#highest volume ever recorded on XBTUSD for a single transaction is 400btc
#highest price ever recorded on XBTUSD is 19660$
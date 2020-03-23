import mysql.connector
from decimal import *
import pandas as pd

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
	mycursor.execute("SELECT * FROM 24H")
	#list of tuples
	myresult = mycursor.fetchall()
	return(myresult)

def sma(period, data, index):
	i, j = (index-period+1), period
	tmp = 0
	while(i <= index):
		if(data[i][3] == None):
			return(0)
		tmp = tmp + data[i][3]
		i+=1
	return(float(Decimal(tmp)/Decimal(period)))


data = fetch_data()

i, j = 0, len(data)
SMA = {10: [], 20: [], 50: [], 100: [], 200: [], "date": []}
sma_list = [10, 20, 50, 100, 200]
y = len(sma_list)
while(i < j):
	x = 0
	while (x < y):
		if (i > sma_list[x]):
			SMA[sma_list[x]].append((sma(sma_list[x], data, i)))
		else:
			SMA[sma_list[x]].append(0)
		x+=1
	SMA["date"].append(data[i][5])
	i+=1

df2 = pd.DataFrame.from_dict(SMA)
print(df2)
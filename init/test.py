import mysql.connector
from datetime import datetime


#connect to database
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="bodyboard",
	database="bitmex_perps"
)

#create tables
mycursor = mydb.cursor()

#
try:
	mycursor.execute("DROP TABLE test")
except:
	print("No table to delete")

mycursor.execute("CREATE TABLE IF NOT EXISTS test (tradeTime DATETIME(6))")

#print tables
mycursor.execute("SHOW TABLES")
for x in mycursor:
	print(x)



#2015-09-25T12:34:25.706Z
query = (
	"INSERT INTO test (tradeTime) "
	"VALUES (%s)"
)

value = '2015-09-25T12:34:25.706000Z'
a = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ')
print(a)
print(type(a))

mycursor.execute(query, (a,))

#print column from table
mycursor.execute("SELECT (tradeTime) FROM test")
for x in mycursor:
	print(x)
	print(x[0].strftime('%Y-%m-%dT%H:%M:%S.%fZ'))

###


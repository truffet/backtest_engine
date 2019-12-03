from get1000Trades import get1000Trades
from connect_to_db import connect_to_db
from init import setup_env


#connect to omnisci bitmex database
con = connect_to_db()

#create tables if they don't exist already
setup_env(con)

#nb of rows in table timeCursor
cursor = con.cursor()
count_rows = cursor.execute("SELECT COUNT(*) FROM timeCursor;")
nb_of_rows = list(count_rows)[0][0]
print("Number of rows in timeCursor: " + str(nb_of_rows))
if (nb_of_rows == 0):
	print("Table is empty, will start loading data from origin")
else:
	print("Table is not empty, will start updating data from last saved point")


#if timeCursor table is empty, no data has been uploaded to the table tradesHistory yet

#result = get1000Trades("","")
#print(result)

#if it exists already and needs update:
# while(True):

#if it exists already and up-to-date:

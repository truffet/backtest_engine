from pymapd import connect


def connect_to_db(db, user, password):
	uri = "mapd://" + user + ":" + password + "@localhost:6274/" + db + "?protocol=binary"
	con = connect(uri=uri)
	print("Connected to database " + db)
	return(con)

def create_superuser(con, name, password):
	try:
		request = "CREATE USER " + name + " (is_super='true', password='" + password + "');"
		con.execute(request)
		print("Created superuser " + name)
	except Exception as e:
		print("Error: " + str(e))

def create_db(con, name, owner):
	request = "CREATE DATABASE IF NOT EXISTS " + name + " (owner='" + owner + "');"
	con.execute(request)
	print("Created database " + name + " if it does not exist already, the owner is: " + owner)

def alter_user_default_db(con, name, default_db):
	request = "ALTER USER " + name + " (default_db = '" + default_db + "');"
	con.execute(request)
	print("Changed default db of " + name + " to " + default_db)

def create_bitmex_tables(con):
	con.execute("CREATE TABLE IF NOT EXISTS tradesHistory (tradeTime TEXT, symbol TEXT, side TEXT, size INTEGER, price FLOAT, tickDirection TEXT, trdMatchID TEXT, grossValue FLOAT, homeNotional FLOAT, foreignNotional FLOAT);")
	con.execute("CREATE TABLE IF NOT EXISTS timeCursor (tradeTime TEXT, trdMatchID TEXT);")
	print("Created tables tradesHistory and timeCursor if it does not already exist")


def setup_env():
	con = connect_to_db("omnisci", "admin", "HyperInteractive")
	create_superuser(con, "bitmex_superuser", "bitmex_pass")
	create_db(con, "bitmex_db", "bitmex_superuser")
	alter_user_default_db(con, "bitmex_superuser", "bitmex_db")
	con = connect_to_db("bitmex_db", "bitmex_superuser", "bitmex_pass")
	create_bitmex_tables(con)
	return(con)
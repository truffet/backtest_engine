def setup_env(con):
	con.execute("CREATE TABLE IF NOT EXISTS tradesHistory (tradeTime TIMESTAMP NOT NULL, symbol TEXT, side TEXT, size INTEGER, price FLOAT, tickDirection TEXT, trdMatchID TEXT, grossValue FLOAT, homeNotional FLOAT, foreignNotional FLOAT);")
	con.execute("CREATE TABLE IF NOT EXISTS timeCursor (tradeTime TIMESTAMP NOT NULL, trdMatchID TEXT);")
	print("Created table tradesHistory if it does not already exist")
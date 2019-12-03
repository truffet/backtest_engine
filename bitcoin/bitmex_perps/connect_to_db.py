from pymapd import connect


def connect_to_db():
	uri = "mapd://truffet:bodyboard@localhost:6274/bitmex?protocol=binary"
	con = connect(uri=uri)
	print("Connected to database bitmex")
	return(con)
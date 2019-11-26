from pymapd import connect

try:
	uri = "mapd://truffet:bodyboard@localhost:6274/test?protocol=binary"
	con = connect(uri=uri)
	print("connected")
except Exception as e:
	print(e)
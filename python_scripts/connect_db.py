from pymapd import connect

try:
	uri = "mapd://truffet:bodyboard@localhost:6274/teest?protocol=binary"
	con = connect(uri=uri)
except Exception as e:
	print(e)
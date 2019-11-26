import requests

def build_url(timestamp, baseUrl):
	if timestamp != "":
		return (baseUrl + "&startTime=" + timestamp)
	return (baseUrl)

def get_data(fullUrl):
	try:
		return (requests.get(fullUrl))
	except Exception as e:
		return ("Error: " + str(e))

def toJson(response):
	try:
		return(response.json())
	except Exception as e:
		return ("Error: " + str(e))

def get1000Trades(timestamp, lastTradeID):
	baseUrl = "https://www.bitmex.com/api/v1/trade?symbol=XBT%3Aperpetual&count=1"
	fullUrl = build_url(timestamp, baseUrl)
	response = get_data(fullUrl)
	data = toJson(response)

	if (str(response).startswith("Error")):
		print(1000)
		print(type([response]))
		print([response])
	elif (str(data).startswith("Error")):
		print(1001)
		print(type([data]))
		print([data])
	else:
		print(response)
		print(response.status_code)
		print(type(data))
		print(data)

#test
get1000Trades("","")
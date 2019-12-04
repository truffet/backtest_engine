import requests

def build_url(startTime, baseUrl):
	if startTime != "":
		return (baseUrl + "&startTime=" + str(startTime))
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

def handle_response(response, data):
	if (str(response).startswith("Error")):
		return([1000] + [data])
	elif (str(data).startswith("Error")):
		return([1001] + [data])
	else:
		return([response.status_code] + data)

def get1000Trades(startTime):
	baseUrl = "https://www.bitmex.com/api/v1/trade?symbol=XBT%3Aperpetual&count=2"
	response = get_data(build_url(startTime, baseUrl))
	result = handle_response(response, toJson(response))
	return result
import requests
from requests.exceptions import Timeout

def get_data(fullUrl):
	try:
		return (requests.get(fullUrl, timeout=(10,10)))
	except Exception as e:
		return ("Error: " + str(e))

def toJson(response):
	try:
		return(response.json())
	except Timeout:
		return ("Error: 'read or write timeout on get method'")
	except Exception as e:
		return ("Error: " + str(e))

def handle_response(response, data):
	if (str(response).startswith("Error")):
		return([1000] + [data])
	elif (str(data).startswith("Error")):
		return([1001] + [data])
	else:
		if(isinstance(data, dict)):
			return([response.status_code] + [str(data)])
		return([response.status_code] + [data])

def getTrades(since):
	rawUrl = "https://api.kraken.com/0/public/Trades?pair=xbtusd&since="
	baseUrl = rawUrl + str(since)
	response = get_data(baseUrl)
	result = handle_response(response, toJson(response))
	return result
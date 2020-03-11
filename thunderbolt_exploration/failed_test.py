from fetch_data import fetch_data


#init conditions for AB & CD minimum & maximum variation + step for exploration
wave_min_size = 0.1
print("Minimum % price variation: ", (wave_min_size*100))
wave_max_size = 0.5
step = 0.01

#init conditions for BC minimum & maximum variation
def retrace_size(a, b):
	return(b-((b-a)*0.382))

#init precision for a match between AB time + price and BC time + price
precision = 0.2
print("Precision: ", (precision*100))

#data to explore
data = fetch_data()

#init a, b, c, d
a, b, c, d = 0, 0, 0, 0

#init current price index & price list
p = 1

#calculate exploration size
end = len(data)
print("Number of transactions: ", end)

#list of results
result = []

#check if a=b=c=d=p
def is_reset(test, p):
	if(test.count(p) == 4): #4 is len(test)
		return(True)
	return(False)

while (p < end):

	#check A:
	#print("Checking A...")
	current_price = data[p][1]
	if (current_price == data[a][1]):
		p+=1
	elif (current_price < data[a][1]):
		a, b, c, d = p, p, p, p
		p+=1
	else:

		#check B:
		while(p < end):
			#print("Checking B...")
			current_price = data[p][1]
			if (is_reset([a, b, c, d], p)):
				break
			elif (current_price > data[b][1] and (current_price/data[a][1]) >= (wave_min_size+1)):
				b, c, d = p, p, p
				p+=1
			elif (current_price <= data[a][1]):
				a, b, c, d = p, p, p, p
				p+=1
				break
			elif (current_price < data[b][1]):

				#check C:
				while(p < end):
					#print("Checking C...")
					current_price = data[p][1]
					min_retrace_price = retrace_size(data[a][1], data[b][1])
					if (is_reset([a, b, c, d], p)):
						break
					elif (current_price <= data[a][1]):
						break
					elif (current_price < data[c][1] and (current_price < min_retrace_price)):
						c, d = p, p
						p+=1
					elif (current_price > data[b][1] and c == b):
						break
					elif (current_price > data[b][1] and data[c][1] < data[b][1]):

						#check d:
						time_ab = data[b][0]-data[a][0]
						price_ab = data[b][1]-data[a][1]
						while(p < end):
							#print("Checking D...")
							current_price = data[p][1]
							current_time = data[p][0]
							if (current_price < data[c][1] or (current_time-data[c][0]) > time_ab):
								a, b, c, d = c, c, c, c
								break
							elif ( ((((current_time-data[c][0])/time_ab) < (1+precision)) and (((current_time-data[c][0])/time_ab) > (1-precision))) and ((((current_price-data[c][1])/price_ab) < (1+precision)) and (((current_price-data[c][1])/price_ab) > (1-precision))) ):
								d = p
								#print(a, b, c, d)
								result.append((a,b,c,d))
								a, b, c, d = c, c, c, c
								break
							else:
								p+=1

					else:
						p+=1
			else:
				p+=1

#test purposes
import matplotlib.pyplot as plt
result_size = len(result)
print("Number of ABCD patterns in data: ", result_size)
if (result_size >= 1):
	i = 0
	while(i < result_size):
		print("\n")
		print("A: ", data[result[i][0]])
		print("B: ", data[result[i][1]])
		print("C: ", data[result[i][2]])
		print("D: ", data[result[i][3]])

		x = [data[result[i][0]][0], data[result[i][1]][0], data[result[i][2]][0], data[result[i][3]][0]]
		y = [data[result[i][0]][1], data[result[i][1]][1], data[result[i][2]][1], data[result[i][3]][1]]
		plt.plot(x, y)
		i+=1
	plt.show()
from fetch_data import fetch_data
from view_data import view_data

#minimum wave variation 
var_mini = 0.01
var_maxi = 0.15
step = 0.01
print("var_mini step: ", var_mini, step)
#precision of match AB=CD:
price_precision = 0.25
print("price_precision: ", price_precision)
time_precision = 0.25
print("time_precision: ", time_precision)


#data to explore
data = fetch_data()

size = len(data)

pattern_ABCD = []

while (var_mini <= var_maxi):

	data_points = []
	if size > 0:
		data_points.append(0)
	j = 0
	i = 1
	tmp = 0

	#explore mean reversion points
	while(i < size):
		#up variation detected
		if (data[i][1] > data[data_points[j]][1] and ((data[i][1]/data[data_points[j]][1])-1) > var_mini):
			tmp = i
			#looking for maximum
			while (i < size):
				if (data[i][1] > data[tmp][1]):
					tmp = i
				elif (data[i][1] < data[tmp][1] and (1-(data[i][1]/data[tmp][1])) > var_mini):
					data_points.append(tmp)
					j+=1
					break
				i+=1
			i = tmp
		#down variation detected
		elif (data[i][1] < data[data_points[j]][1] and (1-(data[i][1])/data[data_points[j]][1]) > var_mini):
			tmp = i
			#looking for minimum
			while(i < size):
				if (data[i][1] < data[tmp][1]):
					tmp = i
				elif (data[i][1] > data[tmp][1] and ((data[i][1]/data[tmp][1])-1) > var_mini):
					data_points.append(tmp)
					j+=1
					break
				i+=1
			i = tmp
		i+=1

	#explore AB=CD patterns:
	i, j = 3, len(data_points)
	while(i < j):
		a, b, c, d = data[data_points[i-3]], data[data_points[i-2]], data[data_points[i-1]], data[data_points[i]]
		price_test = ((b[1]-a[1])/(d[1]-c[1])) < (1 + price_precision) and ((b[1]-a[1])/(d[1]-c[1])) > (1 - price_precision)
		time_test = ((b[0]-a[0])/(d[0]-c[0])) < (1 + time_precision) and ((b[0]-a[0])/(d[0]-c[0])) > (1 - time_precision)
		c_condition = (c[1] > a[1] and c[1] < b[1]) or (c[1] < a[1] and c[1] > b[1])
		if (price_test and time_test and c_condition):
			if (pattern_ABCD.count((a, b, c, d)) == 0):
				pattern_ABCD.append((a, b, c, d))
		i+=1
	print(var_mini)
	var_mini+=step

nb_of_patterns = len(pattern_ABCD)
print("nb_of_patterns: ", nb_of_patterns)
view_data(pattern_ABCD, data, nb_of_patterns)
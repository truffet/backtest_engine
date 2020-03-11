from fetch_data import fetch_data
import matplotlib.pyplot as plt

#minimum wave variation 
var_mini = 0.2

#minimum correction/retracement variation
def retrace_down(a, b):
	return(b-((b-a)*0.382))
def retrace_up(a, b):
	return(b+((a-b)*0.382))

#precision for a match AB = CD
precision = 0.1

#data to explore
data = fetch_data()

size = len(data)

data_points = []
if size > 0:
	data_points.append(0)
j = 0
i = 1
tmp = 0


while(i < size):
	#up variation detected
	if ((data[i][1]/data[data_points[j]][1]) > (1+var_mini)):
		tmp = i
		#looking for maximum
		while (i < size):
			retrace_price = retrace_down(data[j][1], data[tmp][1])
			if (data[i][1] > data[tmp][1]):
				tmp = i
			elif (data[i][1] < data[tmp][1] and data[i][1] < retrace_price):
				data_points.append(tmp)
				j+=1
				break
			i+=1
	#down variation detected
	elif ((data[i][1]/data[data_points[j]][1]) < (1-var_mini)):
		tmp = i
		#looking for minimum
		while(i < size):
			retrace_price = retrace_up(data[j][1], data[tmp][1])
			if (data[i][1] < data[tmp][1]):
				tmp = i
			elif (data[i][1] > data[tmp][1] and data[i][1] > retrace_price):
				data_points.append(tmp)
				j+=1
				break
			i+=1
	i+=1

i, j = 0, len(data)
x, y = [], []
while (i < j):
	x.append(data[i][0])
	y.append(data[i][1])
	i+=1
plt.scatter(x, y, s=1, c=y)
i, j = 0, len(data_points)
x, y = [], []
while (i < j):
	x.append(data[data_points[i]][0])
	y.append(data[data_points[i]][1])
	i+=1
print(y)
plt.scatter(x, y, c='red', s=10)
plt.show()
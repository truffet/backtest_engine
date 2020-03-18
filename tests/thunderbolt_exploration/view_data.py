import matplotlib.pyplot as plt

def view_data(pattern_ABCD, data, nb_of_patterns):
	i = 0
	pat = pattern_ABCD
	x, y = [], []
	while (i < nb_of_patterns):
		x = [pat[i][0][0], pat[i][1][0], pat[i][2][0], pat[i][3][0]]
		y = [pat[i][0][1], pat[i][1][1], pat[i][2][1], pat[i][3][1]]
		plt.plot(x, y, lw=2)
		i+=1
	#plt.show()
	i, j = 0, len(data)
	x, y = [], []
	while (i < j):
		x.append(data[i][0])
		y.append(data[i][1])
		i+=1
	#plt.scatter(x, y, s=1, c=y)
	plt.plot(x, y, lw=0.2)

	plt.show()

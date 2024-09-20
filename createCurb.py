import matplotlib.pyplot as plt

def resolve(f, maximum):
	x = []
	y = []
	for a in range(0-maximum, maximum):
		x.append(a)
		y.append(f(a))

	plt.plot(x,y)
	plt.show()

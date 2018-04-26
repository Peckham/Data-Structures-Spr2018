import timeit
import matplotlib.pyplot as plt
import random

def timeFunction(f,n,repeat=1):
	return timeit.timeit(f.__name__+'('+str(n)+')',setup="from __main__ import "+f.__name__,number=repeat)/repeat

def prefix_average1(S):
    n = len(S)
    A = [0] * n
    for j in range(n):
        total = 0
        for i in range(j + 1):
            total += S[i]
        A[j] = total / (j + 1)
    return A

def prefix_average2(S):
    n = len(S)
    A = [0] * n
    for j in range(n):
        A[j] = sum(S[0 : j + 1]) / (j + 1)
    return A

def prefix_average3(S):
    n = len(S)
    A = [0] * n
    total = 0
    for j in range(n):
        total += S[j]
        A[j] = total / (j + 1)
    return A

def plot_data():
	x_values = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
	prefix1_y_values = []
	prefix2_y_values = []
	prefix3_y_values = []
	for i in x_values:
		data = []
		for j in range(i):
			data.append(random.randint(0,100))
		prefix1_y_values.append(timeFunction(prefix_average1, data))
		prefix2_y_values.append(timeFunction(prefix_average2, data))
		prefix3_y_values.append(timeFunction(prefix_average3, data))
	plt.plot(x_values, prefix1_y_values, label = "Prefix 1")
	plt.plot(x_values, prefix2_y_values, label = "Prefix 2")
	plt.plot(x_values, prefix3_y_values, label = "Prefix 3")
	plt.xlabel("Input Size")
	plt.ylabel("Runtime")
	plt.legend(handles = [line1, line2, line3])
	plt.show()




if __name__ == '__main__':
    plot_data()

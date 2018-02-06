#Downloaded from NYU Classes by Tavish Peckham on 1/30/18
import timeit
import random

def timeFunction(f,n,repeat=1):
	return timeit.timeit(f.__name__+'('+str(n)+')',setup="from __main__ import "+f.__name__,number=repeat)/repeat

def insertion_sort(dataList):
	for i in range(0, len(dataList)):
		for j in dataList[:i]:
			if dataList[j] < dataList[i]:
				for k in dataList[-1:j:-1]:
					dataList[k+1] = dataList[k]
				dataList[i] = dataList[j]
	print("DataList 1: " + str(dataList))
	return dataList


def python_sort(dataList):
	sortedData = dataList.sort()
	print("DataList 2: " + str(sortedData))
	return sortedData


if __name__ == '__main__':
    data1 = []
    data2 = []
    for i in range(100):
        value = random.randint(0,100)
        data1.append(value)
        data2.append(value)
    print("Insertion sort 10000 elements:",
          '{:.6f}'.format(timeFunction(insertion_sort, data1)), "seconds")
    print("Built in sort 10000 elements:",
          '{:.6f}'.format(timeFunction(python_sort, data2)), "seconds")

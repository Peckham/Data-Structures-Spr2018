# Created by Tavish Peckham on 2.4.18
import random
from functools import reduce

#Quicksort in-place the parameter toSort.
def partition(array, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot

def quickSort(array, begin, end):
    if begin >= end:
        return
    pivot = partition(array, begin, end)
    quickSort(array, begin, pivot-1)
    quickSort(array, pivot+1, end)

def question1(l1, l2):
	print("Question 1: Merge")

	output = []
	smaller = min(len(l1), len(l2))
	for i in range(smaller):
		output.append(l1[i])
		output.append(l2[i])
	output.extend(l1[smaller:])
	output.extend(l2[smaller:])
	return output

def question2(l1):
	print("Question 2: Largest Ten")

	if len(l1) <= 10: return l1
	quickSort(l1, 0 ,len(l1) - 1)
	return l1[len(l1) - 10:]

def question3(S):
	print("Question 3: Missing Number")
	print("Set with a missing number:", str(S))
	return (print("%d is the missing number." %(len(S) * (len(S) + 1) // 2 - sum(S))))

def question4(a, b , c):
	print("Question 4: Three-Way Set Disjointedness")

	return len(set(a) & set(b) & set(c)) == 0

def question6(S):
	print("Question 6: MinMax")

	mid = len(S) // 2
	firstHalf = S[0:mid]
	secondHalf = S[mid:]
	maxNum = S[0]
	minNum = S[-1]
	n = len(S)
	comparisons = 0
	swaps = 0
	for i in range(mid):
		comparisons += 3
		if firstHalf[i] > secondHalf[i]:
			if firstHalf[i] > maxNum:
				maxNum = firstHalf[i]
				swaps += 1
			if(secondHalf[i] < minNum):
				minNum = secondHalf[i]
				swaps += 1
		else:
			if secondHalf[i] > maxNum:
				maxNum = secondHalf[i]
				swaps += 1
			if firstHalf[i] < minNum:
				minNum = firstHalf[i]
				swaps += 1

	print("max: " + str(maxNum))
	print("min: " + str(minNum))
	print("n: " + str(n))
	print("comparisons: " + str(comparisons))
	print("swaps: " + str(swaps))

def main():
	randNums = [random.randint(0,100) for i in range(50)]
	l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	l2 = [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
	S = [0, 1, 2, 3, 4, 6, 7, 8]
	l3 = [0, 1, 2]
	l4 = [3, 4, 5]
	l5 = [6, 3, 8]

	print(question1(l1, l2))
	print(question2(randNums))
	print(question3(S))
	print(question4(l3, l4, l5))
	print(question4(S, l4, l5))
	question6(l1 + l2)

main()

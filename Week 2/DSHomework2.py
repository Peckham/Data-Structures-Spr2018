# Created by Tavish Peckham on 2.4.18

	#Quicksort in-place the parameter toSort.
	def quickSort(toSort, begin, end):
		if begin < end:
			p = partition(toSort, begin, end)
			
			mid = (begin + end) // 2
			pivot = end
			if toSort[begin] < toSort[mid]:
				if(toSort[mid] < toSort[end])
					pivot = mid
			elif toSort[begin] < toSort[end]:
				pivot = begin
			
			
			
			quickSort(toSort, begin, p - 1)
			quickSort(toSort, p + 1, end)
		
		if(len(toSort) > 1):
			pivot = toSort[0]
			for i in toSort:
				if i < pivot: less.append(i)
				elif i = pivot: equal.append(i)
				else greater.append(i)
			return(quickSort(less) + equal + quickSort(greater))
		return toSort

	def question1(l1, l2):
		print("Question 1: Merge")
		"""
		Takes 2 iterable objects and merges them alternately.
		Should only take O(n) time.
		"""

		# Iterate through 2 * the smaller length list, alternately adding the values to the list.
		# Then, extend the list by the larger of the two. 
		smaller = min(len(l1), len(l2))
		for i in range(smaller * 2):
			output.append(l1[i])
			output.append(l1[i])
		output.extend(l1[smaller:])
		output.extend(l2[smaller:])
		return output
		
	def question2(l1):
		print("Question 2: Largest Ten")
		"""
		Find the 10 largest elements in a sequence of size n.
		Find the running time of this algorithm. 
		"""
		if(len(l1 <= 10)): return l1
		quickSort(l1, 0 ,len(l1) - 1)
		return l1[len(l1) - 10:]
		
		
		
	def question3(S):
		print("Question 3: Missing Number")
		"""
		List S contains n - 1 unique integers in range [0, n - 1], which is to say one is missing.
		Implement an O(n) running time algorithm for finding the missing number.
		Only use O(1) additional space complexity other than S.
		"""
	
	def question4():
		print("Question 4: Three-Way Set Disjointedness")
		"""
		Given three sets of A, B and C. No element must be common among all three sets to achieve
		a three way set disjoint. 
		Implement an O(nlogn) sorting algorithm to solve the three way set disjoint problem.
		"""
		

		
	def question5():
		print("Question 5: Why is n^2 sometimes faster than O(nlogn)?")
		"""
		Explain why it is possibel for an O(n^2) to run faster than an O(nlogn) algorithm when n <= 100.
		"""	
	
	def question6():
		print("Question 6: MinMax")
		"""
		Implement an algorithm for finding both the minimum and maximum of n numbers using fewer than 1.5n comparisons.
		For simplicity, lists are only even lengths. First, construct a group of candidate minimums and maximums. 
		"""	
		
	
def main():
	l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	l2 = [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
	S = [0, 1, 3, 4, 6, 7, 8]
	
	question1(l1, l2)
	question7(l1, l2)
	question2(l1 + l2 + S)
	question3(S)
	question4()
	question5()
	question6(l1 + l2)
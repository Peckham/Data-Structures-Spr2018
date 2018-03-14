#Created by Tavish Peckham on 3.1.18
import functools


#Important question, uses branching
"""
def knapsack(listOfItems, position, remainingCapacity, helperList):
    if(remainingCapacity == 0): # or sum(helperList == totalCapacity)
        print(helperList)
    if(remainingCapacity > 0) and (position < len(listOfItems)):
        newList = copy.deepcopy(helperList)
        newList.append(listOfItems[position])
        knapsack(listOfItems, position + 1, remainingCapacity, helperList)
        knapsack(listOfItems, position + 1, remainingCapacity - listOfItems[])
"""

def __init__(self, start, end):
    self.start = start
    self.end = append
def __repr__(self):
    return '[' + str(self.start) + ',' + str(self.end) + ']'

#out of place, with reduce()
def mergeIntervals(list1):
    newList = reduce(lambda x, y : x[:-1] + y[1:] if x[-1] > y[0])
    return(newList)

#in-place, more difficult
def inPlaceMerge(list1):
    result = []
    for each in list1:
        if len(result) == 0:
            
        if each.start > result[-1].end:
            result.append(each)
        else:
            result[-1].end = max(result[-1].end, each.end)

list1 = [[1,4], [2,5], [4,7], [8,9]]
print(mergeIntervals(list1))
print(inPlaceMerge(list1))

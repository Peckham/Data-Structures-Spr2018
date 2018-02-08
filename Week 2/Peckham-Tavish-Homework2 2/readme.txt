Tavish Peckham
Professor Ratan Dey
Recitation Instructor Ruowen Tan
Data Structures
Homework assignment 2
Due 2.8.18

DSHomework2.py contains solutions to Questions 1-4 and 6.

Question 1
Takes 2 iterable objects and merges them alternately.
Should only take O(n) time.
Iterate through the range of the shorter list, appending elements to output from
both. Then, extend output by both lists from the last index of the smallest
list to the end, to append the remaining values of the longer list.

Question 2
Find the 10 largest elements in a sequence of size n.
Find the running time of this algorithm.

To find the 10 largest elements we first sort the sequence with the function
quickSort. Quicksort's worst runtime is O(n^2) but we will usually have O(nlogn)
-time

Question 3
List S contains n - 1 unique integers in range [0, n - 1], which is to say one is missing.
Implement an O(n) running time algorithm for finding the missing number.
Only use O(1) additional space complexity other than S.

We use the summation function n(n+1)/2 to find the sum of the integers in our
desired range, then simply subtract by the summation of the elements in the
argument S to find the element not summed by the first function.

Question 4
Given three sets of A, B and C. No element must be common among all three sets to achieve
a three way set disjoint.
Implement an O(nlogn) sorting algorithm to solve the three way set disjoint problem.

Taking A, B and C as sets, all we need to do for this question is check the length of the
list created by passing the bitwise AND operator through the sets to check if any value
is common between the three.

Question 5
If n < 100, the O(n^2)-time algorithm runs faster, and only when n ≥ 100, O(n log n)-time one runs faster.
Explain how this is possible.

This is possible because the big O notation for a function does not always accurately indicate how quickly
a function will run. For instance, if a function of O(nlogn)-time has a large enough coefficient, it will
take longer to compute than an an O(n^2)-time function without any coefficient. In the example situation given,
the coefficient of the O(nlogn)-time function no longer makes it slower than the O(n^2)-time function if
there are more than 100 elements.
Alternatively, there could potentially be a difference between two computer's code execution speed.
An O(nlogn)-time function may take a longer time to run on a slow computer than an O(n^2)-time function on
a fast computer. While the number of comparisons remains the same regardless of the compute speed, the
time it takes to run the algorithm can lead a function with more comparisons to be executed in less time.


Question 6
Implement an algorithm for finding both the minimum and maximum of n numbers using fewer than 1.5n comparisons.
For simplicity, lists are only even lengths. First, construct a group of candidate minimums and maximums.

First we separate list into two halves, then iterate through the halves comparing
the values of the two lists. If the first half's element is larger than the second's
element, then we check to see if the first's is the max and the second's is the minimum.
Otherwise, we check to see if the second's value is the max or the first's value is the
minimum. This way, we iterate through half the number of elements and make 3 comparisons
each iteration, meaning the function is O(3/2n)-time.

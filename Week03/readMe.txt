Tavish Peckham
Professor Dey
Recitation Instructor Ruowen Tan
Assignment # 3

1.
The runtime of this function is log base 2 of n.

2.
if n > 1, then recursively multiply by x stepping down by 1 each time.

3.
Calculates how many digits are in a number, or just -1 if the number is
negative.

4.
if we reach the end of the list without returning, then we know there are not
any doubles. For i in the list, look to see if i is in the remainder of the
list. If it is, return false.

5.
appends 1 to the sides of the sum of the pairs of the previous rows in order
to calculate a Pascal's Triangle of a certain length.

6. INCORRECT
If our cast is appearing in groups of 1, simply return the cast. Otherwise,
create an empty list to hold list of all possible stars. Then for i where is 1
through the number of cast members minus our number of stars plus 2, we append
to stars the first star and then iterate through the rest of the cast in groups
of numStars - 1 to append the other stars. Once we reach the end of the list,
we call _q6 again with the first element of cast1 removed. If our cast members
remaining == numStars, print our total collection of stars.

7. INCORRECT (second attempt at Question 6)
The first solution almost works, but does not work for all amounts of stars.
For each element in cast[:numStars], choose n more numbers after it in cast
until you reach the number of stars required. Then, begin iterating through
the entire cast adding elements to the list until it contains sublists for
every element from cast[numStars:], then do the same for the second to
last element until you end up with the last numStars elements of the list.
... But if you were actually programming this you would simply use
the builtin yield function as itertools does. Doing it with recursion
just makes it more confusing.

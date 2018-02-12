# Created by Tavish Peckham on 2.12.18
from math import factorial

def q2(x, n):
    if(n > 1): return x * q2(x, n - 1)
    else: return x

def q3(n):
    if(n < 0): return -1
    elif(n < 10): return 1
    total = 1
    while(n >= 10):
        total += 1
        n //= 10
    return total

def q4(l, i = 0):
    # if i == len(l) - 1: return True
    # elif l[i] in l[i+1:]: return False
    # else: return q4(l, i+1)
    if map(lambda x: x in l[i:], l): return False
    return True

# Alternative Base case: The summation of our rows is 2n.
# This would require:
# if reduce(lambda x, y : x + y, p[-1]) == 2n: return pasc
def q5(n):
    pasc = [[1], [1, 1]]
    if(n == 1): return pasc[0]
    elif(n == 2): return pasc[:]
    else: _q5(n)
    def _q5(n):
        if(n == 0): return pasc
        else:
            pasc.append([1] + [pasc[-1][i] + pasc[-1][i+1] for i in range(len(pasc[-1]) - 1)] + [1])
            return _q5(n - 1)

"""
Start by creating empty list to hold list of all possible stars.
We iterate through the cast with variable i. i then iterates through
the crew in groups of n where n is numStars-1, adding the group to stars.
We stop when no more stars can be added, so cast[i+numStars] > len(cast).
Then recurse, with cast[1:] and again stop when our number of star groups
equals the calculated amount.

Alternatively, we could terminate the recursion when len(cast) < numStars.
"""
def q6(cast, numStars):
    fac = math.factorial
    numChoices = fac(len(cast)) / fac(numStars) * fac(len(cast) - numStars)
    stars = []
    _q6(cast, numStars)
    def _q6(cast, numStars):
        for i in range(1, len(cast) - numStars):
            stars.append(list(cast[0]) + cast[i:i + numStars - 1])
        if(len(stars) == numChoices): return stars
        else: _q6(cast[1:], numStars)

def main():
    lis = [1, 2, 3, 4, 5, 6, 7, 8, 4]
    cast = ["Russell Crowe", "Johnny Depp", "Al Pacino",
            "Denzel Washington", "Brad Pitt", "Jim Carrey"]
    # print("Question 2: Recursive Power")
    # print(q2(5, 3))
    # print("Question 3: Write the function in iterative form")
    # print(q3(100))
    # print("Question 4: Element Uniqueness Problem")
    # print(q4(lis))
    print("Question 5: Pascal's Triangle")
    print(q5(5))
    print("Question 6: All Possible Combinations")
    print(q6(cast), 3)

main()

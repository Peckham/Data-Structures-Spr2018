# Created by Tavish Peckham on 2.12.18

def q2(x, n):
    if n > 1: return x * q2(x, n - 1)
    else: return x

def q3(n):
    if n < 0: return -1
    elif n < 10: return 1
    total = 1
    while n >= 10:
        total += 1
        n //= 10
    return total

# Fun one-line, iterative solution:
# return not any(map(lambda x: l[x] in l[x + 1:], list(range(len(l)))))
def q4(l, i = 0):
    if i == len(l) - 1: return True
    elif l[i] in l[i+1:]: return False
    else: return q4(l, i + 1)


# Alternative Base case: The summation of our rows is 2n.
# This would require:
# if reduce(lambda x, y : x + y, p[-1]) == 2n: return pasc
def q5(n):
    pasc = [[1], [1, 1]]
    def _q5(m):
        if(m == 1): return pasc
        else:
            pasc.append([1] + [pasc[-1][i] + pasc[-1][i + 1]
            for i in range(len(pasc[-1]) - 1)] + [1])
            return _q5(m - 1)
    if(n == 1): return pasc[0]
    elif(n == 2): return pasc[:]
    else: return _q5(n)

def q6(cast, numStars):
    if numStars == 1: return cast
    stars = []
    def _q6(cast1, numStars):
        for i in range(1, len(cast1) - numStars + 2):
            stars.append(list(cast1[:1] + (cast1[i:i + numStars - 1])))
        if(len(cast1) == numStars):
            for i in stars: print(str(i) + "\n")
        else: _q6(cast1[1:], numStars)
    return _q6(cast[:], numStars)


def q7(cast, numStars): # Second Attempt at Question 6
    if numStars == 1: return cast
    starList = []
    def _q7(cast, cList = [], cIndex = 0): # Current List and Index
        for i in range(len(cast[:numStars])):
            print(allPairs(cast[i],cast[i+1:]))
    _q7(cast)

def allPairs(n, lis): #returns a list of subslists of n appended to lis
    out = []
    for i in lis:
        out.append(n + [i])
    return out

def main():
    lis = [1, 2, 3, 4, 5, 6, 7, 8]
    lis1 = [1, 2, 3, 4, 5, 6, 7, 8, 5]
    cast = ["Russell Crowe", "Johnny Depp", "Al Pacino",
            "Denzel Washington", "Brad Pitt", "Jim Carrey", "Robert De Niro"]

    print("\nQuestion 2: Recursive Power")
    print(q2(5, 3))
    print("\nQuestion 3: Write the function in iterative form")
    print(q3(100))
    print("\nQuestion 4: Element Uniqueness Problem")
    print(q4(lis))
    print(q4(lis1))
    print("\nQuestion 5: Pascal's Triangle")
    print(*q5(7), sep = "\n")
    print("\nQuestion 6: All Possible Combinations")
    print("The entire cast: " + str(cast) + "\n")
    q6(cast, 3)
    q7(cast, 3)
main()

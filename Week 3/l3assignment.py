# Created by Tavish Peckham on 2.12.18


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
    if i == len(l) - 1: return True
    elif l[i] in l[i+1:]: return False
    else: return q4(l, i+1)

    map(2lambda x: filter(lambda y: ), l)
    # For each element, check everything after it in l for a dup.ww

def q5():
    return

def q6():
    return

def main():
    lis = [1, 2, 3, 4, 5, 6, 7, 8, 4]
    # print("Question 2: Recursive Power")
    # print(q2(5, 3))
    # print("Question 3: Write the function in iterative form")
    # print(q3(100))
    # print("Question 4: Element Uniqueness Problem")
    # print(q4(lis))
    # q5()
    # q6()

main()

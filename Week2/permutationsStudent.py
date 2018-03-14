#Tavish Peckham 1.31.18 Recitation Question 1
import timeit
import random

def permutation1(array):
    num = len(array)
    output = []
    for i in range(num):
        guess = random.randint(0, num - 1)
        while guess in output:
            guess = random.randint(0, num - 1)
        output.append(guess)
    return output

def permutation2(array):
    num = len(array)
    output = []
    ran = [False for x in range(num)]
    for x in range(num):
        while True:
            guess = random.randint(0, num - 1)
            if(not ran[x]):
                output.append(guess)
                ran[x] = True
                break
    return output

def permutation3(array):
    num = len(array)
    output = [x for x in range(num)]
    for i in range(num):
        j = random.randint(0, i)
        output[i], output[j] = output[j], output[i]
    return output

print(permutation1([0,1,2,3,4]))
print(permutation2([0,1,2,3,4]))
print(permutation3([0,1,2,3,4]))

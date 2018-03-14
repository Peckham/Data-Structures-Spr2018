#Tavish Peckham Data Structures Recitation
def q1():
    n = int(input("Enter an integer to get it reversed: "))
    print(str(n)[::-1])

def q2():
    arr = [1,1,1,1,2,3,4,5,1]
    numCount = {}
    for i in arr:
        if(i not in numCount.keys):
            numCount[i] = 1
        else: numCount[i] += 1

    for i in numCount.keys:
        if(i > arr.size()/2):
            print(i)
    print("Done checking for Majority Numbers")


def main():
    #q1()
    q2()
    #q3()
    #q4()
    #q5()
main()

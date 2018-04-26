#Tavish Peckham, January 30 2018 Homework 1
import math
def anagram(word1, word2):
    word1Letters = [x for x in word1 if x.isalpha()]
    word2Letters = [x for x in word2 if x.isalpha()]
    word1Letters.sort()
    word2Letters.sort()
    return word1Letters == word2Letters

def palindrome(word):
    letters = "".join([x for x in word if x.isalpha()])
    halfLength = len(letters) // 2
    for i in range(halfLength):
        if(letters[i] != letters[-i - 1]): return False
    return True

def GCD(bNum, sNum):
    if(bNum % sNum == 0): return sNum
    else: return GCD(sNum, bNum%sNum)

def addOne(numList):
    num = int("".join(map(str,numList)))+1
    return list(str(num))

class Shape:
    def __init__(self, name):
        self.name = name

    def compute_area(self):
        pass

    def compute_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

    def compute_area(self):
        return math.pi * self.radius^2

    def compute_perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, name, length, height):
        self.name = name
        self.length = length
        self.height = height

    def compute_area(self):
        return self.length * self.height

    def compute_perimeter(self):
        return 2 * self.length + 2 * self.height

def OOP():
    c = Circle("Moon", 15)
    print("Perimeter of a moon with size 15: " + str(c.compute_perimeter()))
    r = Rectangle("Block", 20, 10)
    print("Area of a rectangle with dimensions 20x10: " + str(r.compute_area()))


def main():
    print("Question 1: Anagram")
    print(anagram(input("Enter word 1: "), input("Enter word 2: ")))
    print("Questions 2: Palindrome")
    print(palindrome(input("Enter a palindrome: ")))
    print("Question 3: Greatest Common Divisor")
    print(GCD(int(input("Enter int1: ")), int(input("Enter int2: "))))
    print("Question 4: Add One")
    print(addOne(list(input("Enter a number: "))))
    print("Question 5: Object Oriented Programming")
    OOP()
main()

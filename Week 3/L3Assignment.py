#Created by Tavish Peckham on 2.5.18

def convertDecimalToBinary(n):
    if(n == 1):
        return "1"
    return convertDecimalToBinary(n // 2) + str(n % 2)

def main():
    print(convertDecimalToBinary(5))
    print(convertDecimalToBinary(10))
    print(convertDecimalToBinary(15))
main()

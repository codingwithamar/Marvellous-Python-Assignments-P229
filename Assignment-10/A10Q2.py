#Author : codingwithamar@gmail.com
#Description : '2. Write a program which accepts one number and prints sum of first N natural numbers.
#Input: 5
#Output: 15'

def SumNaturalNumber(Natural):
    total = 0
    for i in range(1, Natural + 1, 1):
        total += i
    print(total)
        
def main():
    print("Enter The number : ")
    NaturalNumber = int(input())
    SumNaturalNumber(NaturalNumber)

if __name__ == "__main__":
    main()
    
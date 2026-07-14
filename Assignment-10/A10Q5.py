# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A10Q4.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-10\A10Q4.py
# Subject : 5.Write a program which accepts one number and prints all odd numbers till that number.
# Description : Input: 10  Output: 1 3 5 7 9
# =============================================================================

def Odd(Value):
    i = 1
    while i <= Value:
        print(i)
        i += 2

def main():
    print("Enter the Number : ")
    Num = int(input())
    Odd(Num)

if __name__ == "__main__":
    main()
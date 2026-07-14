# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A10Q4.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-10\A10Q4.py
# Subject : 4. Write a program which accepts one number and prints all even numbers till that number.
# Description : Input: 10  Output: 2 4 6 8 10
# =============================================================================

def Even(Value):
    i = 2
    while i <= Value:
        print(i)
        i += 2

def main():
    print("Enter the Number : ")
    Num = int(input())
    Even(Num)

if __name__ == "__main__":
    main()
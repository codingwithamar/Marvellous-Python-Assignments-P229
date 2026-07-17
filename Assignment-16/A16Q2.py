# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A16Q2.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-16\A16Q2.py
# Subject : 2. Write a program which contains one function named as ChkNum() which accept 
# one parameter as number. If number is even then it should display “Even number” 
# otherwise display “Odd number” on console.
# Description : Input : 11 Output : Odd Number 
#               Input : 8 Output : Even Number
# =============================================================================

def ChkNum(iNum):
    if iNum%2==0:
        print("Even Number")
    else:
        print("Odd Number")

def main():
    print("Enter the Number :")
    Num = int(input())
    ChkNum(Num)

if __name__ == "__main__":
    main()
    
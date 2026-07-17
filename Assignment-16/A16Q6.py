# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A16Q6.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-16\A16Q6.py
# Subject : 6.Write a program which accept number from user and check whether that 
# number is positive or negative or zero.
# Description : Check Whether +, - or 0
# =============================================================================

def main():
    print("Enter the Number")
    Num = int(input())
    if Num >= 1:
        print("Positive")
    elif Num <= -1:
        print("Negative")
    else:
        print("Zero")

if __name__ == "__main__":
    main()
    
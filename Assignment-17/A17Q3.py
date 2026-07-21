# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A17Q3.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-17\A17Q3.py
# Subject : 3. Write a program which accept one number from user and return its factorial.
# Description : Input : 5 Output : 120
# =============================================================================

def main():

    fact = 1

    print("Enter the Number : ")
    Value = int(input())

    for i in range(1,Value+1):
        fact = fact * i

    print("Factorial is : ",fact)


if __name__ == "__main__":
    main()
    
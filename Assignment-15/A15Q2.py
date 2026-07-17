# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A15Q2.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-15\A15Q2.py
# Subject : 2. Write a lambda function using filter() which accepts a list of numbers and returns a list of even numbers.
# Description : Input : 1 2 3 4 5   Output : 2 4 
# =============================================================================

def main():
    print("Enter the list of Numbers : ")
    NumList = list(map(int, input().split()))
    print("You Entered List is : ", NumList)

    Even = filter(lambda iNumlist:iNumlist%2==0,NumList)
    print("Even Numbers : ",(Even))

if __name__ == "__main__":
    main()
    

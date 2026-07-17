# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A15Q3.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-15\A15Q3.py
# Subject : 3. Write a lambda function using filter() which accepts a list of numbers and returns a list of odd numbers.
# Description : Input : 1 2 3 4 5 6 7 8 9 10  OUTPUT : 2 4 6 8 10
# =============================================================================

def main():
    print("Enter the list of Numbers : ")
    NumList = list(map(int,input().split()))
    
    OddNumbers = filter(lambda iNumList : iNumList%2!=0,NumList)
    print("Odd Numbers : ",list(OddNumbers))

if __name__ == "__main__":
    main()
    
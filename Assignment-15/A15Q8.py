# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A15Q8.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-15\A15Q8.py
# Subject : 8. Write a lambda function using filter() which accepts a list of numbers 
# and returns a list of numbers divisible by both 3 and 5.
# Description : Return The List of Divisible by 3 and 5
# =============================================================================

Divisible = lambda iNumList : iNumList%3==0 and iNumList%5==0

def main():
    print("Enter the list of Numbers : ")
    NumList = list(map(int,input().split()))

    DivisibleList = list(filter(Divisible, NumList))
    print(DivisibleList)

if __name__ == "__main__":
    main()
    
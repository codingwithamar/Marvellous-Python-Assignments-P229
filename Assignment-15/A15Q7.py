# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A15Q7.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-15\A15Q7.py
# Subject : 7. Write a lambda function using filter() which accepts a list of strings and returns a list of 
# strings having length greater than 5.
# Description : Make List of Greater than 5 Digit
# =============================================================================

Digits = lambda iNumList : len(iNumList) > 5

def main():
    print("Enter the list of Numbers : ")
    NumList = list(map(str,input().split()))

    FilterList = list(filter(Digits, NumList))
    print(FilterList)

if __name__ == "__main__":
    main()
    
# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A15Q9.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-15\A15Q9.py
# Subject : 9. Write a lambda function using reduce() which accepts a list of numbers 
# and returns the product of all elements.
# Description : Product of elemends mean All numbers Multiplication 
# =============================================================================

from functools import reduce

def main():
    print("Enter the list of Numbers : ")
    NumList = list(map(int,input().split()))
    
    Products = reduce(lambda iNum1, iNum2 : iNum1 * iNum2, NumList)
    print("Product of all Elements : ", Products)

if __name__ == "__main__":
    main()
    
# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A15Q1.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-15\A15Q1.py
# Subject : 1. Write a lambda function using map() which accepts a list of numbers and returns a list of squares of each number.
# Description : Input : 1 2 3 4 5    OUTPUT : 1 4 9 16 25   
# =============================================================================                             

Square = lambda Nlist : (Nlist ** 2)

def main():
    print("Enter the list of Numbers : ")
    NumList = list(map(int,input().split()))
    
    Mdata = list(map(Square, NumList))
    print(Mdata)

if __name__ == "__main__":
    main()  
    
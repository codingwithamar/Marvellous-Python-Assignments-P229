# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A22Q1.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-22\A22Q1.py
# Subject/Question : 1. Write a program that accepts a list of integers and uses Pool.map()
#  to calculate the sum of squares from 1 to N for every element in the list.
# Description : Example Input
# [1,2,3,4]
# Expected Output:
# 1² + 2² + 3² + ... + N²
# =============================================================================

from multiprocessing import Pool

def square(x):
    Total = 0
    for i in range(1,x+1):
        Total = Total + (i * i)
    return Total

def main():
    numbers = [1000000,2000000,3000000,4000000]
    
    with Pool(4) as p:
        result = p.map(square, numbers)
        print(result)

if __name__ == "__main__":
    main()



# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A22Q4.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-22\A22Q4.py
# Subject/Question : 4. Write a program that calculates 1^5+2^5+3^5+…..+N^5 
# for multiple values of N simultaneously using Pool. 
# Description : 
# # Input
# [1000000,
# 2000000,
# 3000000,
# 4000000]
# Measure total execution time.
# =============================================================================

from multiprocessing import Pool
import time

def Power(iValues):
    Sum = 0
    for Value in range(1,iValues+1):
        Sum = Sum + (Value ** 5)
    return Sum
    

def main():
    StartTime = time.time()
    
    print("Enter the list of Numbers : ")
    Values = list(map(int,input().split()))
    print("You Entered list is :",Values)

    with Pool(4) as p:
        Result = p.map(Power,Values)

    for Value,PowerSum in zip(Values,Result):
        print(f"Value : {Value} - Sum of Power : {PowerSum} ")

    EndTime = time.time()

    print(f"Execution Time : {EndTime - StartTime}")

if __name__ == "__main__":
    main()
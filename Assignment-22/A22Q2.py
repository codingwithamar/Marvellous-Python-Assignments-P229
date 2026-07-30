# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A22Q2.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-22\A22Q2.py
# Subject/Question : 2. Write a program that calculates factorials of multiple 
# numbers simultaneously using Pool.map().
# Description : 
# Input
# [10,15,20,25] 
# Display
# • Process ID
# • Input Number
# • Factorial
# =============================================================================

from multiprocessing import current_process
from multiprocessing import Pool

def Factorial(Values):
    fact = 1
    for value in range(1,Values+1):
        fact = fact * value
    print("Process ID : ",current_process().pid)
    print("Input No : ",Values)
    print("Factorial is :",fact)
    print()
    return fact


def main():
    Values = [10,15,20,25]
    print("Values : ",Values)
    print()

    with Pool(4) as p:
        Result = p.map(Factorial,Values)
        print("Factorials of Number is : ",Result)
        print()

if __name__ == "__main__":
    main()

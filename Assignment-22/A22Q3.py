# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A22Q3.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-22\A22Q3.py
# Subject/Question : 3. For every number in the given list, count how many prime 
# numbers exist between 1 and N using multiprocessing Pool.
# Description : Input - 10000   OUTPUT - Display total prime count for each number.
# =============================================================================

from multiprocessing import Pool

def Prime(Value):
    PrimeCount = 0
    for Number in range(1,Value+1):
        Count = 0
        for i in range(1,Number+1):
            if Number%i==0:
                Count = Count + 1
        if Count == 2:
            PrimeCount = PrimeCount + 1
    return PrimeCount
    

def main():
    print("Enter the Numbers: ")
    Values = list(map(int,input().split()))
    print(f"You Entered {len(Values)} Values that is : {Values}")

    with Pool(4) as p:
        Result = p.map(Prime,Values)

    for Value,Count in zip(Values,Result):
        print(f"Total Prime numbers Count in between 1 to {Value} values is {Count}")
    print()

if __name__ == "__main__":
    main()  

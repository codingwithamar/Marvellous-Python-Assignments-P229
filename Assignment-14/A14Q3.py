# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A14Q3.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-14\A14Q3.py
# Subject : 3. Write a lambda function which accepts two numbers and returns maximum number.
# Description : input : 12 30   Output : 30
# =============================================================================

MinMax = lambda A, B : A if A > B else B

def main():
    iValue1 = int(input("Enter the Value 1 : "))
    iValue2 = int(input("Enter the Value 2 : "))
    Ret = MinMax(iValue1, iValue2)
    print("Maximum Number is : ",Ret)

if __name__ == "__main__":
    main()  
    
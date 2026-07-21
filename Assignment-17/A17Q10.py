# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A17Q10.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-17\A17Q10.py
# Subject : 10. Write a program which accept number from user and return addition of digits in that number
# Description : Input : 5187934 Output : 37
# =============================================================================
from functools import reduce

def Add(iValue1,iValue2):
    return iValue1+iValue2

def main():
    Values = []
    while True:
        data = input("Enter your numbers : ")

        if data == "":
            break

        Values.append(int(data))

    #if " " in data:
    #    Values = list(map(int,data.split()))
    #else:
    #    Values = list(map(int,data))

    Addition = reduce(Add,Values)
    print("Addition of all values : ",Addition)

if __name__ == "__main__":
    main()
    